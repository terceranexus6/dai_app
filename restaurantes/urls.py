from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^test_template/$',views.test_template, name='test_template'),
    url(r'^nuevo_restaurante/$',views.test_template, name='nuevo_restaurante'),
]
