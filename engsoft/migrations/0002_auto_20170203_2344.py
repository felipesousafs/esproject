# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engsoft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome_produto', models.CharField(max_length=200)),
                ('logo_url', models.TextField()),
                ('escopo', models.TextField()),
                ('limites', models.TextField()),
                ('requisitos_funcionais', models.TextField()),
                ('requisios_naofuncionais', models.TextField()),
                ('diagrama_de_contexto_url_list', models.TextField()),
                ('atores', models.TextField()),
                ('casos_de_uso_url_list', models.TextField()),
                ('diagramas_de_classe_url_list', models.TextField()),
                ('diagramas_de_sequencia_url_list', models.TextField()),
                ('plano_de_iteracoes', models.TextField()),
                ('prototipo_baixa_fidelidade_url_list', models.TextField()),
                ('prototipo_ma_fidelidade_url_list', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Analise_de_Dados',
        ),
        migrations.DeleteModel(
            name='Definicao_dos_Requisitos',
        ),
        migrations.DeleteModel(
            name='Detalhamento_dos_Requisitos',
        ),
        migrations.DeleteModel(
            name='Introducao',
        ),
        migrations.DeleteModel(
            name='Prototipos',
        ),
    ]
