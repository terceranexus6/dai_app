from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^test_t/$', views.test_t, name = 'test_t'),
]
