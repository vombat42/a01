from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
#from words.serializers import *
#from words.models import *
from django_filters.rest_framework import DjangoFilterBackend


app_name = 'words'

def index(request):
	return render (request, "games/index.html")

def about(request):
	return render (request, "games/about.html")

#class WordsAPI(ModelViewSet):
	#queryset = Entry.objects.all()
	#serializer_class = EntrySerializer
	#filter_backends = [DjangoFilterBackend]
	#filterset_fields = ['chapter__name', 'user__username', 'grade']

def words(request):
	return render (request, "games/words.html")
