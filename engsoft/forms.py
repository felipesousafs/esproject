from django import forms
from .models import Projeto
from projectmanager import settings

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Projeto
		fields = (
			'nome_produto','escopo','limites',
			'requisitos_funcionais','requisios_naofuncionais',
			'logo_url',
			)
class Formulario(forms.Form):
	nome_produto = forms.CharField(max_length=100)
	logo_url = forms.ImageField()