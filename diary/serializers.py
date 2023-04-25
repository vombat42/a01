from rest_framework.serializers import ModelSerializer
from diary.models import Entry, Chapter, Link
from rest_framework import serializers


#class ChapterSerializer(ModelSerializer):
#	class Meta:
#		model = Chapter
#		fields = ['name']


class LinkSerializer(ModelSerializer):
	class Meta:
		model = Link
		#fields = '__all__'
		fields = ['link']


class EntrySerializer(ModelSerializer):
	chapter_name = serializers.CharField(source='chapter.name')
	user_name = serializers.CharField(source='user.username')
	links = LinkSerializer(read_only=True, many=True)
	date_start = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
	date_end = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

	class Meta:
		model = Entry
		fields = ['id','chapter_name', 'date_start', 'date_end','text', 'user_name', 'links', 'grade']
		#fields = [*]

