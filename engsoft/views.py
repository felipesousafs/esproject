from django.shortcuts import render
from .models import Projeto
from .forms import ProjectForm,Formulario
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your views here.
def list(request):
	projeto = Projeto.objects.filter()
	for pro in projeto:
		pro.limites = pro.limites.split(";")
	return render(request,'engsoft/list.html',{'projeto':projeto})
def index(request):
	return render(request,'engsoft/index.html',{})


def new_project(request):
	if request.method == "POST":
		#Saving file
		nome_produto = request.POST['nome_produto']
		escopo = request.POST['escopo']
		limites = request.POST['limites']
		requisitos_funcionais = request.POST['requisitos_funcionais']
		casos_de_uso_url_list = request.POST['casos_de_uso_url_list']
		if request.FILES['logo_url']:
			f = request.FILES['logo_url']
			fs = FileSystemStorage()
			filename = fs.save(f.name, f)
			uploaded_file_url = fs.url(filename)
			#Saving file
			form = ProjectForm({'nome_produto':nome_produto,'escopo':escopo,'limites':limites,
			'requisitos_funcionais':requisitos_funcionais,'casos_de_uso_url_list':casos_de_uso_url_list,
			'logo_url':uploaded_file_url})
		if form.is_valid():
			projeto = form.save(commit=False)
			projeto.save()
			#return redirect('engsoft.views.list')
			return render(request, 'engsoft/list.html', {
            'uploaded_file_url': uploaded_file_url
        	})
		else:
			return render(request,'engsoft/project_form.html',{'form':form, 'logo_url':form.logo_url})
	else:
		form = ProjectForm()
	return render(request,'engsoft/project_form.html',{'form':form})

