# coding: utf-8
from dados.maps import get_city_geojson, get_city_info
from dados import dbdata
from dados import models as M
from dados.episem import episem
from dbf.models import DBF
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, View
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from time import mktime
from collections import defaultdict, OrderedDict

import random
import json
import os
import datetime
import numpy as np
import locale
import geojson

locale.setlocale(locale.LC_TIME, locale="pt_BR.UTF-8")

dados_alerta = dbdata.get_alerta_mrj()
dados_alerta_chik = dbdata.get_alerta_mrj_chik()

with open(os.path.join(settings.STATICFILES_DIRS[0], 'rio_aps.geojson')) as f:
    polygons = geojson.load(f)


class AlertaMainView(TemplateView):
    template_name = 'main.html'

    _state_names = ['Rio de Janeiro', 'Paraná', 'Espírito Santo']
    _state_initials = {
        'Rio de Janeiro': 'RJ',
        'Paraná': 'PR',
        'Espírito Santo': 'ES'
    }

    def get_context_data(self, **kwargs):
        context = super(AlertaMainView, self).get_context_data(**kwargs)

        diseases = ('dengue', 'chikungunya')

        # today
        last_se = {}
        penultimate_se = {}

        today = datetime.datetime.today()
        se2 = episem(today, sep='')
        # 7 days ago
        last_week = today - datetime.timedelta(days=0, weeks=1)
        se1 = episem(last_week, sep='')

        case_series = defaultdict(dict)
        case_series_state = defaultdict(dict)

        count_cities = defaultdict(dict)
        current_week = defaultdict(dict)
        estimated_cases_next_week = defaultdict(dict)
        variation_to_current_week = defaultdict(dict)
        variation_4_weeks = defaultdict(dict)
        v1_week_fixed = defaultdict(dict)
        v1_4week_fixed = defaultdict(dict)

        notif_resume = dbdata.NotificationResume

        for d in diseases:
            # mundict = dict(dbdata.get_all_active_cities())
            # municipios, geocodigos = list(mundict.values()), list(mundict.keys())
            # results[d] = dbdata.load_serie_cities(geocodigos, d)
            case_series[d] = dbdata.get_series_by_UF(d)


            for s in self._state_names:
                df = case_series[d]  # alias
                cases = df[df.uf == s].casos_s.values
                # cases estimation
                cases_est = df[df.uf == s].casos_est_s.values

                case_series_state[d][s] = cases[:-52]

                count_cities[d][s] = notif_resume.count_cities_by_uf(s, d)
                current_week[d][s] = {
                    'casos': cases[-1] if cases.size else 0,
                    'casos_est': cases_est[-1] if cases_est.size else 0
                }
                estimated_cases_next_week[d][s] = 'Em breve'
                v1 = cases[-2] if cases.size else 0
                v2 = cases[-1] if cases_est.size else 0

                v1_week_fixed[d][s] = v1 == 0 and v2 != 0

                variation_to_current_week[d][s] = round(
                    0 if v1 == v2 == 0 else
                    ((v2 - v1) / 1) * 100 if v1 == 0 else
                    ((v2-v1)/v1)*100, 2
                )

                if cases.size < 55:
                    variation_4_weeks[d][s] = 0
                else:
                    v1 = cases[-4:-1].sum()
                    v2 = cases[-55:-52].sum()

                    v1_4week_fixed[d][s] = v1 == 0 and v2 != 0

                    variation_4_weeks[d][s] = round(
                        0 if v1 == v2 == 0 else
                        ((v2 - v1) / 1) * 100 if v1 == 0 else
                        ((v2-v1)/v1)*100, 2
                    )
        '''
        for st_name in self._state_names:
            print(case_series)
            # Municípios participantes
            count_cities[st_name] = notif_resume.count_cities_by_uf(st_name)
            # Total de casos notificado e estimados na semana
            current_week[st_name] = notif_resume.count_cases_by_uf(
                st_name, se2
            ).iloc[0].to_dict()
            # Previsão de casos para as próximas semanas
            estimated_cases_next_week[st_name] = current_week[st_name]['casos']
            # Variação em relação à semana anterior
            # ((v2-v1)/v1)*100
            variation_to_current_week[st_name] = (
                notif_resume.count_cases_week_variation_by_uf(
                    st_name, se1, se2
                )
            ).loc[0, 'casos']
            variation_4_weeks[st_name] = int((
                notif_resume.get_4_weeks_variation(st_name, today)
            ).loc[0, 'casos'])
            
        '''

        context.update({
            # 'mundict': json.dumps(mundict),
            # 'num_mun': len(mundict),
            # 'municipios': municipios,
            # 'geocodigos': geocodigos,
            # 'alerta': json.dumps(alerta),
            'diseases': diseases,
            'case_series': case_series,
            #'total': json.dumps(total.tolist()),
            'states': self._state_names,
            'count_cities': count_cities,
            'current_week': current_week,
            'estimated_cases_next_week': estimated_cases_next_week,
            'variation_to_current_week': variation_to_current_week,
            'variation_4_weeks': variation_4_weeks,
            'state_initials': self._state_initials

        })

        return context


def get_municipio(request):
    q = request.GET['q']
    muns = dbdata.get_city(q)
    data = json.dumps([
        {'geocodigo': g, 'nome': n, 'uf': u} for g, n, u in muns
    ])
    return HttpResponse(data, content_type='application/json')


class AlertaPageView(TemplateView):
    template_name = 'alerta.html'

    def get_context_data(self, **kwargs):
        context = super(AlertaPageView, self).get_context_data(**kwargs)

        disease_code = context['disease']

        disease_label = (
            'Dengue' if disease_code == 'dengue' else
            'Chikungunya' if disease_code == 'chikungunya' else
            None
        )

        bairros_mrj = {
            1.0: 'AP 1: Centro e adjacências',
            2.1: 'AP 2.1: Zona Sul',
            2.2: 'AP 2.2: Tijuca e adjacências',
            3.1: 'AP 3.1: Bonsucesso e adjacências',
            3.2: 'AP 3.2: Meier e adjacências',
            3.3: 'AP 3.3: Madureira e adjacências',
            4.0: 'AP 4: Barra, Recreio e Jacarepaguá',
            5.1: 'AP 5.1: Bangu e adjacências',
            5.2: 'AP 5.2: Campo Grande e adjacências',
            5.3: 'AP 5.3: Santa Cruz e adjacências'
        }

        alert, current, case_series, last_year, observed_cases, min_max_est = \
            get_alert(disease_code)

        if alert:
            casos_ap = {
                float(ap.split('AP')[-1]):
                    int(current[current.aps == ap]['casos_est'])
                for ap in alert.keys()
            }
            alerta = {
                float(k.split('AP')[-1]): int(v) - 1
                for k, v in alert.items()
            }
            semana = str(current.se.iat[-1])[-2:]
            segunda = current.data.iat[-1]
            city_info = get_city_info("3304557")
            total_series = sum(
                np.array(list(case_series.values())), np.zeros(12, int)
            )
            total_observed_series = sum(
                np.array(list(observed_cases.values())), np.zeros(12, int)
            )
        else:
            casos_ap = {}
            alerta = {}
            semana = 0
            segunda = datetime.datetime.now() - datetime.timedelta(7)
            city_info = get_city_info("3304557")
            total_series = [0]
            total_observed_series = [0]

        context.update({
            'geocodigo': "3304557",
            'nome': "Rio de Janeiro",
            'populacao': city_info['populacao'],
            'incidencia': (
                total_observed_series[-1] / city_info['populacao']
            ) * 100000,  # casos/100000
            'casos_por_ap': json.dumps(casos_ap),
            'alerta': alerta,
            'novos_casos': sum(casos_ap.values()),
            'bairros': bairros_mrj,
            'min_est': sum(i[0] for i in min_max_est.values()),
            'max_est': sum(i[1] for i in min_max_est.values()),
            'series_casos': case_series,
            'SE': int(semana),
            'data1': segunda.strftime("%d de %B de %Y"),
            'data2': (
                segunda + datetime.timedelta(6)
            ).strftime("%d de %B de %Y"),
            'last_year': last_year,
            'look_back': len(total_series),
            'total_series': ', '.join(map(str, total_series)),
            'total_observed': total_observed_series[-1],
            'total_observed_series': ', '.join(
                map(str, total_observed_series)),
            'disease_label': disease_label,
            'disease_code': disease_code
        })
        return context


class AlertaPageViewMunicipio(TemplateView):
    template_name = 'alerta_municipio.html'

    def dispatch(self, request, *args, **kwargs):
        super(AlertaPageViewMunicipio, self) \
            .get_context_data(**kwargs)
        municipio_gc = kwargs['geocodigo']

        if int(municipio_gc) == 3304557:  # Rio de Janeiro
            return redirect('mrj', disease='dengue', permanent=True)

        return super(AlertaPageViewMunicipio, self) \
            .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AlertaPageViewMunicipio, self) \
            .get_context_data(**kwargs)

        disease_code = context['disease']

        disease_label = (
            'Dengue' if disease_code == 'dengue' else
            'Chikungunya' if disease_code == 'chikungunya' else
            None
        )

        municipio_gc = context['geocodigo']

        city_info = get_city_info(municipio_gc)

        (
            alert, SE, case_series, last_year,
            observed_cases, min_max_est, dia, prt1
        ) = dbdata.get_city_alert(municipio_gc, disease_code)

        for x in dbdata.get_city_alert(municipio_gc, disease_code):
            print(x)

        if alert is not None:
            casos_ap = {municipio_gc: int(case_series[-1])}
            bairros = {municipio_gc: city_info['nome']}
            total_series = case_series[-12:]
            total_observed_series = observed_cases[-12:]
        else:
            casos_ap = {}
            bairros = {}
            total_series = [0]
            total_observed_series = [0]

        context.update({
            'nome': city_info['nome'],
            'populacao': city_info['populacao'],
            'incidencia': (
                case_series[-1] / city_info['populacao']
            ) * 100000,  # casos/100000
            'casos_por_ap': json.dumps(casos_ap),
            'alerta': {municipio_gc: alert},
            'prt1': prt1 * 100,
            'novos_casos': case_series[-1],
            'bairros': bairros,
            'min_est': min_max_est[0],
            'max_est': min_max_est[1],
            'series_casos': {municipio_gc: case_series[-12:]},
            'SE': SE,
            'data1': dia.strftime("%d de %B de %Y"),
            'data2': (dia + datetime.timedelta(6)).strftime("%d de %B de %Y"),
            'last_year': last_year,
            'look_back': len(total_series),
            'total_series': ', '.join(map(str, total_series)),
            'total_observed': total_observed_series[-1],
            'total_observed_series': ', '.join(
                map(str, total_observed_series)),
            'geocodigo': municipio_gc,
            'disease_label': disease_label,
            'disease_code': disease_code
        })
        return context


class AlertaGeoJSONView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(geojson.dumps(polygons))


class CityMapView(View):
    def get(self, request, geocodigo):
        return geojson.dumps(get_city_geojson(int(geocodigo)))


class DetailsPageView(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailsPageView, self).get_context_data(**kwargs)
        # messages.info(
        #   self.request,
        #   'O site do projeto Alerta Dengue está em construção.')
        series = load_series()
        aps = list(series.keys())
        aps.sort()
        ga = {}
        ya = {}
        oa = {}
        ra = {}
        for k, v in series.items():
            ga[k] = [1 if a == 0 else None for a in v['alerta']]
            ya[k] = [1 if a == 1 else None for a in v['alerta']]
            oa[k] = [1 if a == 2 else None for a in v['alerta']]
            ra[k] = [1 if a == 3 else None for a in v['alerta']]

        context.update({
            'APS': aps,
            'green_alert': json.dumps(ga),
            'yellow_alert': json.dumps(ya),
            'casos': json.dumps(series),
            'red_alert': json.dumps(ra),
            'orange_alert': json.dumps(oa),
            'xvalues': series['AP1']['dia'],
        })
        return context


class MapaDengueView(TemplateView):
    template_name = 'mapadengue.html'

    def get_context_data(self, **kwargs):
        context = super(MapaDengueView, self).get_context_data(**kwargs)
        return context


class MapaMosquitoView(TemplateView):
    template_name = 'mapamosquito.html'

    def get_context_data(self, **kwargs):
        context = super(MapaMosquitoView, self).get_context_data(**kwargs)
        return context


class HistoricoView(TemplateView):
    template_name = 'historico.html'

    def get_context_data(self, **kwargs):
        context = super(HistoricoView, self).get_context_data(**kwargs)
        series = load_series()
        aps = list(series.keys())
        aps.sort()
        context.update({
            'APS': aps,
            'xvalues': series['AP1']['dia'],
            'dados': json.dumps(series)
        })
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        # messages.info(
        #   self.request,
        #   'O site do projeto Alerta Dengue está em construção.')
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        # messages.info(
        #   self.request,
        #   'O site do projeto Alerta Dengue está em construção.')
        return context


class JoininPageView(TemplateView):
    template_name = 'joinin.html'

    def get_context_data(self, **kwargs):
        context = super(JoininPageView, self).get_context_data(**kwargs)
        # messages.info(
        #   self.request,
        #   'O site do projeto Alerta Dengue está em construção.')
        return context


class SinanCasesView(View):
    def get(self, request, year, sample):
        sample = int(sample)
        try:
            assert int(year) in [2010, 2011, 2012, 2013]
        except AssertionError:
            messages.error(
                self.request,
                'O projeto conté dados apenas dos anos 2010 a 2013.'
            )

        sample = 1 if sample == 0 else sample / 100.
        cases = "{\"type\":\"FeatureCollection\", \"features\":["
        if int(year) == 2010:
            dados = M.Dengue_2010.objects.geojson()
        elif int(year) == 2011:
            dados = M.Dengue_2011.objects.geojson()
        elif int(year) == 2012:
            dados = M.Dengue_2012.objects.geojson()
        elif int(year) == 2013:
            dados = M.Dengue_2013.objects.geojson()
        else:
            dados = []

        if len(dados) < 5500:
            sample = 1
        for c in random.sample(list(dados), int(len(dados) * sample)):
            cases += (
                "{\"type\":\"Feature\",\"geometry\":" + c.geojson +
                ", \"properties\":{\"data\":\"" + c.dt_notific.isoformat() +
                "\"}},"
            )
        cases = cases[:-1] + "]}"
        # json.loads(cases)
        return HttpResponse(cases, content_type="application/json")


def get_alert(disease='dengue'):
    """
    Read the data and return the alert status of all APs.
    returns a tuple with the following elements:
    - alert: dictionary with the alert status per AP
    - current: tuple with all variables from the last SE
    - case_series: dictionary with 12-weeks case series per AP
    - last_year: integer representing the total number of cases 52 weeks ago.
    :rtype : tuple
    """
    # dados_alerta and dados_alert_chick are global variables
    df = (
        dados_alerta if disease == 'dengue' else
        dados_alerta_chik if disease == 'chikungunya' else
        None
    )

    if df is None:
        raise Exception('Doença não cadastrada.')

    df.fillna(0, inplace=True)
    last_SE = df.se.max()  # Last epidemiological week
    # year = datetime.date.today().year  # Current year
    # current epidemiological week
    # SE = int(str(last_SE).split(str(year))[-1])
    current = df[df['se'] == last_SE]  # Current status
    G = df.groupby("aps")
    group_names = G.groups.keys()
    alert = defaultdict(lambda: 0)
    case_series = {}
    obs_case_series = {}
    min_max_est = {}
    last_year = None

    for ap in group_names:
        adf = G.get_group(ap)  # .tail()  # only calculates on the series tail
        case_series[str(float(ap.split('AP')[-1]))] = [
            int(v) for v in adf.casos_est.iloc[-12:].values
        ]
        obs_case_series[str(float(ap.split('AP')[-1]))] = [
            int(v) for v in adf.casos.iloc[-12:].values
        ]
        alert[ap] = adf.nivel.iloc[-1]
        last_year = int(adf.casos.iloc[-52])
        min_max_est[ap] = (
            adf.casos_estmin.iloc[-1],
            adf.casos_estmax.iloc[-1]
        )
    return alert, current, case_series, last_year, obs_case_series, min_max_est


def load_series():
    """
    Monta as séries para visualização no site
    """
    series = defaultdict(lambda: defaultdict(lambda: []))
    G = dados_alerta.groupby("aps")
    for ap in G.groups.keys():
        series[ap]['dia'] = [
            int(mktime(datetime.datetime.strptime(d, "%Y-%m-%d").timetuple()))
            if isinstance(d, str) else None
            for d in G.get_group(ap).data
        ]
        series[ap]['tweets'] = [
            float(i) if not np.isnan(i) else None
            for i in G.get_group(ap).tweets
        ]
        series[ap]['tmin'] = [
            float(i) if not np.isnan(i) else None
            for i in G.get_group(ap).tmin
        ]
        series[ap]['casos_est'] = [
            float(i) if not np.isnan(i) else None
            for i in G.get_group(ap).casos_est
        ]
        series[ap]['casos'] = [
            float(i) if not np.isnan(i) else None
            for i in G.get_group(ap).casos
        ]
        series[ap]['alerta'] = [
            c - 1 if not np.isnan(c) else None
            for c in G.get_group(ap).cor
        ]
    return series


class AlertaStateView(TemplateView):
    template_name = 'state_cities.html'

    _state_name = {
        'RJ': 'Rio de Janeiro',
        'PR': 'Paraná',
        'ES': 'Espírito Santo'}
    _map_center = {
        'RJ': [-22.187, -43.176],
        'PR': [-25.006, -51.833],
        'ES': [-20.015, -40.803]}
    _map_zoom = {
        'RJ': 6,
        'PR': 6,
        'ES': 6}

    def get_context_data(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        context = super(AlertaStateView, self).get_context_data(**kwargs)

        cities_alert = dbdata.NotificationResume.get_cities_alert_by_state(
            self._state_name[context['state']], context['disease']
        )

        mun_dict = dict(cities_alert[['municipio_geocodigo', 'nome']].values)

        mun_dict_ordered = OrderedDict(
            sorted(
                cities_alert[['municipio_geocodigo', 'nome']].values,
                key=lambda d: d[1]
            )
        )

        geo_ids = list(mun_dict.keys())

        alerts = dict(
            cities_alert[['municipio_geocodigo', 'level_alert']].values
        )

        dbf = DBF.objects.filter(
            state_abbreviation=context['state']
        ).order_by('export_date').last()

        if dbf is None:
            last_update = 'desconhecida'
        else:
            last_update = dbf.export_date

        if len(geo_ids) > 0:
            cases_series_last_12 = (
                dbdata.NotificationResume.tail_estimated_cases(
                    geo_ids, 12
                )
            )
        else:
            cases_series_last_12 = []

        context.update({
            'state_abv': context['state'],
            'state': self._state_name[context['state']],
            'map_center': self._map_center[context['state']],
            'map_zoom': self._map_zoom[context['state']],
            'mun_dict': mun_dict,
            'mun_dict_ordered': mun_dict_ordered,
            'geo_ids': geo_ids,
            'alerts_level': alerts,
            # estimated cases is used to show a chart of the last 12 events
            'case_series': cases_series_last_12,
            'disease_label': context['disease'].title(),
            'last_update': last_update
        })
        return context


class NotificationReducedCSV_View(View):
    _state_name = {
        'RJ': 'Rio de Janeiro',
        'PR': 'Paraná',
        'ES': 'Espírito Santo'}

    request = None

    def _get(self, param, default=None):
        """

        :param param:
        :param default:
        :return:
        """
        result = (
            self.request.GET[param]
            if param in self.request.GET else
            default
        )

        return result if result else default

    def get(self, request):
        """

        :param kwargs:
        :return:
        """
        self.request = request

        uf = self._state_name[self._get('state_abv')]

        chart_type = self._get('chart_type')

        notifQuery = dbdata.NotificationQueries(
            uf=uf,
            disease_values=self._get('diseases'),
            age_values=self._get('ages'),
            gender_values=self._get('genders'),
            city_values=self._get('cities'),
            initial_date=self._get('initial_date'),
            final_date=self._get('final_date')
        )

        if chart_type == 'disease':
            result = notifQuery.get_disease_dist().to_csv()
        elif chart_type == 'age':
            result = notifQuery.get_age_dist().to_csv()
        elif chart_type == 'age_gender':
            result = notifQuery.get_age_gender_dist().to_csv()
        elif chart_type == 'age_male':
            result = notifQuery.get_age_male_dist().to_csv()
        elif chart_type == 'age_female':
            result = notifQuery.get_age_female_dist().to_csv()
        elif chart_type == 'gender':
            result = notifQuery.get_gender_dist().to_csv()
        elif chart_type == 'period':
            result = notifQuery.get_period_dist().to_csv(
                date_format='%Y-%m-%d'
            )
        elif chart_type == 'epiyears':
            # just filter by one disease
            result = notifQuery.get_epiyears(uf, self._get('disease')).to_csv()
        elif chart_type == 'total_cases':
            result = notifQuery.get_total_rows().to_csv()
        elif chart_type == 'selected_cases':
            result = notifQuery.get_selected_rows().to_csv()

        return HttpResponse(result, content_type="text/plain")


class PartnersPageView(TemplateView):
    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersPageView, self).get_context_data(**kwargs)
        return context
