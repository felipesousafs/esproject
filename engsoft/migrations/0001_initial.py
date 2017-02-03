# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analise_de_Dados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('diagramas_de_classe_url_list', models.TextField()),
                ('diagramas_de_sequencia_url_list', models.TextField()),
                ('plano_de_iteracoes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Definicao_dos_Requisitos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('requisitos_funcionais', models.TextField()),
                ('requisios_naofuncionais', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalhamento_dos_Requisitos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('diagrama_de_contexto_url_list', models.TextField()),
                ('atores', models.TextField()),
                ('casos_de_uso_url_list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Introducao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome_produto', models.CharField(max_length=200)),
                ('logo_url', models.TextField()),
                ('escopo', models.TextField()),
                ('limites', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prototipos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('prototipo_baixa_fidelidade_url_list', models.TextField()),
                ('prototipo_ma_fidelidade_url_list', models.TextField()),
            ],
        ),
    ]
