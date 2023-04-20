from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from diary.serializers import *
from diary.models import *


app_name = 'diary'

def index(request):
	return render (request, "diary/index.html")

def about(request):
	return render (request, "diary/about.html")

class EntryAPI(ModelViewSet):
	queryset = Entry.objects.all()
	serializer_class = EntrySerializer

def entry(request):
	return render (request, "diary/entry.html")
