from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^list$', views.list, name="list"),
	url(r'^new$', views.new_project, name='new_project'),
]
