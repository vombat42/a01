from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contacts/', views.contacts, name='contacts'),
	path('textanalysis/', views.textanalysis, name='textanalysis'),
]
