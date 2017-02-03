from django.db import models
from django.utils import timezone

class Introducao(models.Model):
	nome_produto = models.CharField(max_length=200)
	logo_url = models.TextField() #1 imagem
	escopo = models.TextField() 
	limites = models.TextField() #2+ itens

class Definicao_dos_Requisitos(models.Model):
	requisitos_funcionais = models.TextField() #2+ itens
	requisios_naofuncionais = models.TextField() #2+ itens

class Detalhamento_dos_Requisitos(models.Model):
	diagrama_de_contexto_url_list = models.TextField() #2+ imagens
	atores = models.TextField() #2+ itens
	casos_de_uso_url_list = models.TextField() #2+ itens

class Analise_de_Dados(models.Model):
	diagramas_de_classe_url_list = models.TextField() #2+ imagens
	diagramas_de_sequencia_url_list = models.TextField() #2+ imagens
	plano_de_iteracoes = models.TextField() #2+ itens

class Prototipos(models.Model):
	prototipo_baixa_fidelidade_url_list = models.TextField() #2+ imagens
	prototipo_ma_fidelidade_url_list = models.TextField() #2+ imagens
