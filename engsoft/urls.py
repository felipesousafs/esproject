from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^list$', views.list),
	url(r'^new$', views.new_project, name='new_project'),
]
