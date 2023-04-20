
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from knowhow.serializers import ArticleSerializer
from knowhow.models import Article
#from .forms import fNameAge, fUpFile
#from .functions import handle_uploaded_file


app_name = 'knowhow'

def index(request):
	return render (request, "knowhow/index.html")

def about(request):
	return render (request, "knowhow/about.html")

def articles(request):
	return render (request, "knowhow/articles.html")

def addarticles(request):
	data={"bdir":123}
	return render (request, "knowhow/addarticles.html", context=data)

class ArticlesView(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

def apiarticles(request):
	return render (request, "knowhow/api_articles.html")
