from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from knowhow.views import ArticlesView

app_name = 'knowhow'

router = SimpleRouter()

router.register('api/articles', ArticlesView)

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('articles/', views.articles, name='articles'),
	path('apiarticles/', views.apiarticles, name='apiarticles'),
	path('addarticles/', views.addarticles, name='addarticles'),
]

urlpatterns += router.urls
