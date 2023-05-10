from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from games.views import WordAPI, LetterAPI


app_name = 'games'

router = SimpleRouter()

router.register('api/words', WordAPI)
router.register('api/letter', LetterAPI)

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('words/', views.words, name='words'),
]
urlpatterns += router.urls

