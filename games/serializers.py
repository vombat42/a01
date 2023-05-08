from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from games.models import Letter, Chapter, Word


class ChapterSerializer(ModelSerializer):
	class Meta:
		model = Chapter
		fields = '__all__'


class LetterSerializer(ModelSerializer):
	class Meta:
		model = Letter
		fields = '__all__'


class WordSerializer(ModelSerializer):
	class Meta:
		model = Word
		fields = '__all__'

