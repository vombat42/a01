from rest_framework.serializers import ModelSerializer
from diary.models import Entry, Chapter, Link
from rest_framework import serializers

class ChapterSerializer(ModelSerializer):
	class Meta:
		model = Chapter
		fields = ['name']


class EntrySerializer(ModelSerializer):
	chapter_name = serializers.CharField(source='chapter.name')
	user_name = serializers.CharField(source='user.username')
	class Meta:
		model = Entry
		fields = ['chapter_name', 'date_start', 'date_end','text', 'user_name']
		#fields = [*]

