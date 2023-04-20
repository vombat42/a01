from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from diary.views import EntryAPI

app_name = 'diary'

router = SimpleRouter()

router.register('api/entry', EntryAPI)

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('entry/', views.entry, name='entry'),
]
urlpatterns += router.urls
