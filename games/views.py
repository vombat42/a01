from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from games.serializers import *
from games.models import *


app_name = 'words'


def index(request):
	return render (request, "games/index.html")


def about(request):
	return render (request, "games/about.html")


def words(request):
	return render (request, "games/words.html")


class WordAPI(ModelViewSet):
	queryset = Word.objects.all()
	serializer_class = WordSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['chapter__name', 'name']


class LetterAPI(ModelViewSet):
	queryset = Letter.objects.all()
	serializer_class = LetterSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['name']