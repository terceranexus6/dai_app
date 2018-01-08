from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^nuevo_personaje/$', views.nuevo_personaje, name = 'nuevo_personaje'),
]
