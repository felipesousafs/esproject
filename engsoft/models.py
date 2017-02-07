from django.db import models

class Projeto(models.Model):
	nome_produto = models.CharField(max_length=200)
	logo_url = models.TextField() #1 imagem
	escopo = models.TextField() 
	limites = models.TextField() #2+ itens
	requisitos_funcionais = models.TextField() #2+ itens
	requisios_naofuncionais = models.TextField() #2+ itens
	diagrama_de_contexto_url_list = models.TextField() #2+ imagens
	atores = models.TextField() #2+ itens
	casos_de_uso_url_list = models.TextField() #2+ itens
	diagramas_de_classe_url_list = models.TextField() #2+ imagens
	diagramas_de_sequencia_url_list = models.TextField() #2+ imagens
	plano_de_iteracoes = models.TextField() #2+ itens
	prototipo_baixa_fidelidade_url_list = models.TextField() #2+ imagens
	prototipo_ma_fidelidade_url_list = models.TextField() #2+ imagens
