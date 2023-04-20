from rest_framework.serializers import ModelSerializer
from knowhow.models import Article


class ArticleSerializer(ModelSerializer):
	class Meta:
		model = Article
		fields = ['name', 'date', 'text']
