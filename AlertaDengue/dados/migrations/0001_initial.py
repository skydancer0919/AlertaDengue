# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-14 18:02
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dengue_2010',
            fields=[
                ('pk_uid', models.IntegerField(db_column='PK_UID', primary_key=True, serialize=False)),
                ('nu_notif', models.CharField(max_length=7, null=True)),
                ('x', models.CharField(max_length=20, null=True)),
                ('y', models.CharField(max_length=20, null=True)),
                ('tp_not', models.CharField(max_length=1, null=True)),
                ('id_agravo', models.CharField(max_length=4, null=True)),
                ('dt_notific', models.DateField(null=True)),
                ('sem_not', models.CharField(max_length=6, null=True)),
                ('nu_ano', models.CharField(max_length=4, null=True)),
                ('sg_uf_not', models.CharField(max_length=2, null=True)),
                ('id_unidade', models.CharField(max_length=7, null=True)),
                ('dt_sin_pri', models.DateField(null=True)),
                ('sem_pri', models.CharField(max_length=6, null=True)),
                ('cs_raca', models.CharField(max_length=1, null=True)),
                ('cs_escol_n', models.CharField(max_length=2, null=True)),
                ('id_cns_sus', models.CharField(max_length=15, null=True)),
                ('sg_uf', models.CharField(max_length=2, null=True)),
                ('nduplic_n', models.CharField(max_length=1, null=True)),
                ('dt_digita', models.DateField(null=True)),
                ('dt_transus', models.DateField(null=True)),
                ('dt_transdm', models.DateField(null=True)),
                ('dt_transsm', models.DateField(null=True)),
                ('dt_transrm', models.DateField(null=True)),
                ('dt_transrs', models.DateField(null=True)),
                ('dt_transse', models.DateField(null=True)),
                ('nu_lote_v', models.CharField(max_length=7, null=True)),
                ('nu_lote_h', models.CharField(max_length=7, null=True)),
                ('cs_flxret', models.CharField(max_length=1, null=True)),
                ('flxrecebi', models.CharField(max_length=1, null=True)),
                ('ident_micr', models.CharField(max_length=50, null=True)),
                ('migrado_w', models.CharField(max_length=1, null=True)),
                ('dt_invest', models.DateField(null=True)),
                ('id_ocupa_n', models.CharField(max_length=6, null=True)),
                ('dt_soro', models.DateField(null=True)),
                ('resul_soro', models.CharField(max_length=1, null=True)),
                ('dt_ns1', models.DateField(null=True)),
                ('resul_ns1', models.CharField(max_length=1, null=True)),
                ('dt_viral', models.DateField(null=True)),
                ('resul_vi_n', models.CharField(max_length=1, null=True)),
                ('dt_pcr', models.DateField(null=True)),
                ('resul_pcr_field', models.CharField(max_length=1, null=True)),
                ('sorotipo', models.CharField(max_length=1, null=True)),
                ('histopa_n', models.CharField(max_length=1, null=True)),
                ('imunoh_n', models.CharField(max_length=1, null=True)),
                ('coufinf', models.CharField(max_length=2, null=True)),
                ('copaisinf', models.CharField(max_length=4, null=True)),
                ('comuninf', models.CharField(max_length=6, null=True)),
                ('codisinf', models.CharField(max_length=4, null=True)),
                ('doenca_tra', models.CharField(max_length=1, null=True)),
                ('epistaxe', models.CharField(max_length=1, null=True)),
                ('gengivo', models.CharField(max_length=1, null=True)),
                ('metro', models.CharField(max_length=1, null=True)),
                ('petequias', models.CharField(max_length=1, null=True)),
                ('hematura', models.CharField(max_length=1, null=True)),
                ('sangram', models.CharField(max_length=1, null=True)),
                ('laco_n', models.CharField(max_length=1, null=True)),
                ('plasmatico', models.CharField(max_length=1, null=True)),
                ('evidencia', models.CharField(max_length=1, null=True)),
                ('plaq_menor', models.FloatField(null=True)),
                ('tp_sistema', models.CharField(max_length=1, null=True)),
                ('fid_field', models.IntegerField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=-1)),
            ],
            options={
                'managed': True,
                'db_table': 'Dengue_2010',
            },
        ),
        migrations.CreateModel(
            name='Dengue_2011',
            fields=[
                ('pk_uid', models.IntegerField(db_column='PK_UID', primary_key=True, serialize=False)),
                ('nu_notif', models.CharField(max_length=7, null=True)),
                ('tp_not', models.CharField(max_length=1, null=True)),
                ('id_agravo', models.CharField(max_length=4, null=True)),
                ('dt_notific', models.DateField(null=True)),
                ('sem_not', models.CharField(max_length=6, null=True)),
                ('nu_ano', models.CharField(max_length=4, null=True)),
                ('sg_uf_not', models.CharField(max_length=2, null=True)),
                ('id_unidade', models.CharField(max_length=7, null=True)),
                ('dt_sin_pri', models.DateField(null=True)),
                ('sem_pri', models.CharField(max_length=6, null=True)),
                ('cs_raca', models.CharField(max_length=1, null=True)),
                ('cs_escol_n', models.CharField(max_length=2, null=True)),
                ('id_cns_sus', models.CharField(max_length=15, null=True)),
                ('sg_uf', models.CharField(max_length=2, null=True)),
                ('nduplic_n', models.CharField(max_length=1, null=True)),
                ('dt_digita', models.DateField(null=True)),
                ('dt_transus', models.DateField(null=True)),
                ('dt_transdm', models.DateField(null=True)),
                ('dt_transsm', models.DateField(null=True)),
                ('dt_transrm', models.DateField(null=True)),
                ('dt_transrs', models.DateField(null=True)),
                ('dt_transse', models.DateField(null=True)),
                ('nu_lote_v', models.CharField(max_length=7, null=True)),
                ('nu_lote_h', models.CharField(max_length=7, null=True)),
                ('cs_flxret', models.CharField(max_length=1, null=True)),
                ('flxrecebi', models.CharField(max_length=1, null=True)),
                ('ident_micr', models.CharField(max_length=50, null=True)),
                ('migrado_w', models.CharField(max_length=1, null=True)),
                ('dt_invest', models.DateField(null=True)),
                ('id_ocupa_n', models.CharField(max_length=6, null=True)),
                ('dt_soro', models.DateField(null=True)),
                ('resul_soro', models.CharField(max_length=1, null=True)),
                ('dt_ns1', models.DateField(null=True)),
                ('resul_ns1', models.CharField(max_length=1, null=True)),
                ('dt_viral', models.DateField(null=True)),
                ('resul_vi_n', models.CharField(max_length=1, null=True)),
                ('dt_pcr', models.DateField(null=True)),
                ('resul_pcr_field', models.CharField(max_length=1, null=True)),
                ('sorotipo', models.CharField(max_length=1, null=True)),
                ('histopa_n', models.CharField(max_length=1, null=True)),
                ('imunoh_n', models.CharField(max_length=1, null=True)),
                ('coufinf', models.CharField(max_length=2, null=True)),
                ('copaisinf', models.CharField(max_length=4, null=True)),
                ('comuninf', models.CharField(max_length=6, null=True)),
                ('codisinf', models.CharField(max_length=4, null=True)),
                ('co_bainf', models.CharField(max_length=8, null=True)),
                ('nobaiinf', models.CharField(max_length=60, null=True)),
                ('doenca_tra', models.CharField(max_length=1, null=True)),
                ('epistaxe', models.CharField(max_length=1, null=True)),
                ('gengivo', models.CharField(max_length=1, null=True)),
                ('metro', models.CharField(max_length=1, null=True)),
                ('petequias', models.CharField(max_length=1, null=True)),
                ('hematura', models.CharField(max_length=1, null=True)),
                ('sangram', models.CharField(max_length=1, null=True)),
                ('laco_n', models.CharField(max_length=1, null=True)),
                ('plasmatico', models.CharField(max_length=1, null=True)),
                ('evidencia', models.CharField(max_length=1, null=True)),
                ('plaq_menor', models.FloatField(null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('municipio', models.CharField(max_length=6, null=True)),
                ('nu_lote_i', models.CharField(max_length=7, null=True)),
                ('tp_sistema', models.CharField(max_length=1, null=True)),
                ('x', models.CharField(max_length=20, null=True)),
                ('y', models.CharField(max_length=20, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=-1)),
            ],
            options={
                'managed': True,
                'db_table': 'Dengue_2011',
            },
        ),
        migrations.CreateModel(
            name='Dengue_2012',
            fields=[
                ('pk_uid', models.IntegerField(db_column='PK_UID', primary_key=True, serialize=False)),
                ('nu_notific', models.CharField(max_length=7, null=True)),
                ('status_r', models.CharField(max_length=14, null=True)),
                ('coord_x', models.FloatField(null=True)),
                ('coord_y', models.FloatField(null=True)),
                ('tp_not', models.CharField(max_length=1, null=True)),
                ('id_agravo', models.CharField(max_length=4, null=True)),
                ('dt_notific', models.DateField(null=True)),
                ('sem_not', models.CharField(max_length=6, null=True)),
                ('nu_ano', models.CharField(max_length=4, null=True)),
                ('sg_uf_not', models.CharField(max_length=2, null=True)),
                ('id_unidade', models.CharField(max_length=7, null=True)),
                ('dt_sin_pri', models.DateField(null=True)),
                ('sem_pri', models.CharField(max_length=6, null=True)),
                ('cs_raca', models.CharField(max_length=1, null=True)),
                ('cs_escol_n', models.CharField(max_length=2, null=True)),
                ('id_cns_sus', models.CharField(max_length=15, null=True)),
                ('sg_uf', models.CharField(max_length=2, null=True)),
                ('nduplic_n', models.CharField(max_length=1, null=True)),
                ('dt_digita', models.DateField(null=True)),
                ('dt_transus', models.DateField(null=True)),
                ('dt_transdm', models.DateField(null=True)),
                ('dt_transsm', models.DateField(null=True)),
                ('dt_transrm', models.DateField(null=True)),
                ('dt_transrs', models.DateField(null=True)),
                ('dt_transse', models.DateField(null=True)),
                ('nu_lote_v', models.CharField(max_length=7, null=True)),
                ('nu_lote_h', models.CharField(max_length=7, null=True)),
                ('cs_flxret', models.CharField(max_length=1, null=True)),
                ('flxrecebi', models.CharField(max_length=7, null=True)),
                ('ident_micr', models.CharField(max_length=50, null=True)),
                ('migrado_w', models.CharField(max_length=1, null=True)),
                ('dt_invest', models.DateField(null=True)),
                ('id_ocupa_n', models.CharField(max_length=6, null=True)),
                ('dt_soro', models.DateField(null=True)),
                ('resul_soro', models.CharField(max_length=1, null=True)),
                ('histopa_n', models.CharField(max_length=1, null=True)),
                ('dt_viral', models.DateField(null=True)),
                ('resul_vi_n', models.CharField(max_length=1, null=True)),
                ('sorotipo', models.CharField(max_length=1, null=True)),
                ('imunoh_n', models.CharField(max_length=1, null=True)),
                ('dt_pcr', models.DateField(null=True)),
                ('resul_pcr_field', models.CharField(max_length=1, null=True)),
                ('dt_ns1', models.DateField(null=True)),
                ('resul_ns1', models.CharField(max_length=1, null=True)),
                ('coufinf', models.CharField(max_length=2, null=True)),
                ('copaisinf', models.CharField(max_length=4, null=True)),
                ('doenca_tra', models.CharField(max_length=1, null=True)),
                ('epistaxe', models.CharField(max_length=1, null=True)),
                ('gengivo', models.CharField(max_length=1, null=True)),
                ('metro', models.CharField(max_length=1, null=True)),
                ('petequias', models.CharField(max_length=1, null=True)),
                ('hematura', models.CharField(max_length=1, null=True)),
                ('sangram', models.CharField(max_length=1, null=True)),
                ('laco_n', models.CharField(max_length=1, null=True)),
                ('plasmatico', models.CharField(max_length=1, null=True)),
                ('plaq_menor', models.FloatField(null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('municipio', models.CharField(max_length=6, null=True)),
                ('nu_lote_i', models.CharField(max_length=9, null=True)),
                ('tp_sistema', models.CharField(max_length=1, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=-1)),
            ],
            options={
                'managed': True,
                'db_table': 'Dengue_2012',
            },
        ),
        migrations.CreateModel(
            name='Dengue_2013',
            fields=[
                ('pk_uid', models.IntegerField(db_column='PK_UID', primary_key=True, serialize=False)),
                ('nu_notific', models.CharField(max_length=7, null=True)),
                ('coord_x', models.FloatField(null=True)),
                ('coord_y', models.FloatField(null=True)),
                ('tp_not', models.CharField(max_length=1, null=True)),
                ('id_agravo', models.CharField(max_length=4, null=True)),
                ('dt_notific', models.DateField(null=True)),
                ('sem_not', models.CharField(max_length=6, null=True)),
                ('nu_ano', models.CharField(max_length=4, null=True)),
                ('sg_uf_not', models.CharField(max_length=2, null=True)),
                ('dt_sin_pri', models.DateField(null=True)),
                ('sem_pri', models.CharField(max_length=6, null=True)),
                ('cs_raca', models.CharField(max_length=1, null=True)),
                ('cs_escol_n', models.CharField(max_length=2, null=True)),
                ('id_cns_sus', models.CharField(max_length=15, null=True)),
                ('nduplic_n', models.CharField(max_length=1, null=True)),
                ('dt_digita', models.DateField(null=True)),
                ('dt_transus', models.DateField(null=True)),
                ('dt_transdm', models.DateField(null=True)),
                ('dt_transsm', models.DateField(null=True)),
                ('dt_transrm', models.DateField(null=True)),
                ('dt_transrs', models.DateField(null=True)),
                ('dt_transse', models.DateField(null=True)),
                ('nu_lote_v', models.CharField(max_length=7, null=True)),
                ('nu_lote_h', models.CharField(max_length=7, null=True)),
                ('cs_flxret', models.CharField(max_length=1, null=True)),
                ('flxrecebi', models.CharField(max_length=7, null=True)),
                ('ident_micr', models.CharField(max_length=50, null=True)),
                ('migrado_w', models.CharField(max_length=1, null=True)),
                ('dt_invest', models.DateField(null=True)),
                ('id_ocupa_n', models.CharField(max_length=6, null=True)),
                ('dt_soro', models.DateField(null=True)),
                ('resul_soro', models.CharField(max_length=1, null=True)),
                ('histopa_n', models.CharField(max_length=1, null=True)),
                ('dt_viral', models.DateField(null=True)),
                ('resul_vi_n', models.CharField(max_length=1, null=True)),
                ('sorotipo', models.CharField(max_length=1, null=True)),
                ('imunoh_n', models.CharField(max_length=1, null=True)),
                ('dt_pcr', models.DateField(null=True)),
                ('resul_pcr_field', models.CharField(max_length=1, null=True)),
                ('dt_ns1', models.DateField(null=True)),
                ('resul_ns1', models.CharField(max_length=1, null=True)),
                ('doenca_tra', models.CharField(max_length=1, null=True)),
                ('epistaxe', models.CharField(max_length=1, null=True)),
                ('gengivo', models.CharField(max_length=1, null=True)),
                ('metro', models.CharField(max_length=1, null=True)),
                ('petequias', models.CharField(max_length=1, null=True)),
                ('hematura', models.CharField(max_length=1, null=True)),
                ('sangram', models.CharField(max_length=1, null=True)),
                ('laco_n', models.CharField(max_length=1, null=True)),
                ('plasmatico', models.CharField(max_length=1, null=True)),
                ('evidencia', models.CharField(max_length=1, null=True)),
                ('plaq_menor', models.FloatField(null=True)),
                ('nu_lote_i', models.CharField(max_length=9, null=True)),
                ('tp_sistema', models.CharField(max_length=1, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=-1)),
            ],
            options={
                'managed': True,
                'db_table': 'Dengue_2013',
            },
        ),
        migrations.CreateModel(
            name='DengueConfirmados_2013',
            fields=[
                ('pk_uid', models.IntegerField(db_column='PK_UID', primary_key=True, serialize=False)),
                ('nu_notific', models.CharField(max_length=7, null=True)),
                ('coord_x', models.FloatField(null=True)),
                ('coord_y', models.FloatField(null=True)),
                ('tp_not', models.CharField(max_length=1, null=True)),
                ('id_agravo', models.CharField(max_length=4, null=True)),
                ('dt_notific', models.DateField(null=True)),
                ('sem_not', models.CharField(max_length=6, null=True)),
                ('nu_ano', models.CharField(max_length=4, null=True)),
                ('id_unidade', models.CharField(max_length=7, null=True)),
                ('dt_sin_pri', models.DateField(null=True)),
                ('sem_pri', models.CharField(max_length=6, null=True)),
                ('cs_raca', models.CharField(max_length=1, null=True)),
                ('cs_escol_n', models.CharField(max_length=2, null=True)),
                ('id_cns_sus', models.CharField(max_length=15, null=True)),
                ('id_distrit', models.CharField(max_length=9, null=True)),
                ('nduplic_n', models.CharField(max_length=1, null=True)),
                ('dt_digita', models.DateField(null=True)),
                ('dt_transus', models.DateField(null=True)),
                ('dt_transdm', models.DateField(null=True)),
                ('dt_transsm', models.DateField(null=True)),
                ('dt_transrm', models.DateField(null=True)),
                ('dt_transrs', models.DateField(null=True)),
                ('dt_transse', models.DateField(null=True)),
                ('nu_lote_v', models.CharField(max_length=7, null=True)),
                ('nu_lote_h', models.CharField(max_length=7, null=True)),
                ('cs_flxret', models.CharField(max_length=1, null=True)),
                ('flxrecebi', models.CharField(max_length=7, null=True)),
                ('ident_micr', models.CharField(max_length=50, null=True)),
                ('migrado_w', models.CharField(max_length=1, null=True)),
                ('dt_invest', models.DateField(null=True)),
                ('id_ocupa_n', models.CharField(max_length=6, null=True)),
                ('dt_soro', models.DateField(null=True)),
                ('resul_soro', models.CharField(max_length=1, null=True)),
                ('histopa_n', models.CharField(max_length=1, null=True)),
                ('dt_viral', models.DateField(null=True)),
                ('resul_vi_n', models.CharField(max_length=1, null=True)),
                ('sorotipo', models.CharField(max_length=1, null=True)),
                ('imunoh_n', models.CharField(max_length=1, null=True)),
                ('dt_pcr', models.DateField(null=True)),
                ('resul_pcr_field', models.CharField(max_length=1, null=True)),
                ('dt_ns1', models.DateField(null=True)),
                ('resul_ns1', models.CharField(max_length=1, null=True)),
                ('coufinf', models.CharField(max_length=2, null=True)),
                ('copaisinf', models.CharField(max_length=4, null=True)),
                ('comuninf', models.CharField(max_length=6, null=True)),
                ('codisinf', models.CharField(max_length=4, null=True)),
                ('co_bainf', models.CharField(max_length=8, null=True)),
                ('nobaiinf', models.CharField(max_length=60, null=True)),
                ('doenca_tra', models.CharField(max_length=1, null=True)),
                ('epistaxe', models.CharField(max_length=1, null=True)),
                ('gengivo', models.CharField(max_length=1, null=True)),
                ('metro', models.CharField(max_length=1, null=True)),
                ('petequias', models.CharField(max_length=1, null=True)),
                ('hematura', models.CharField(max_length=1, null=True)),
                ('sangram', models.CharField(max_length=1, null=True)),
                ('laco_n', models.CharField(max_length=1, null=True)),
                ('plasmatico', models.CharField(max_length=1, null=True)),
                ('evidencia', models.CharField(max_length=1, null=True)),
                ('plaq_menor', models.FloatField(null=True)),
                ('nu_lote_i', models.CharField(max_length=9, null=True)),
                ('tp_sistema', models.CharField(max_length=1, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=-1)),
            ],
            options={
                'managed': True,
                'db_table': 'DengueConfirmados_2013',
            },
        ),
    ]
