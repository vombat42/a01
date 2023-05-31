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
		# fields = ['name']


class WordSerializer(ModelSerializer):
	letters = LetterSerializer(read_only=True, many=True)
	class Meta:
		model = Word
		fields = ['chapter','name','voice','letters']
