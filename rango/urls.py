from django.conf.urls imoprt patterns, url
from rango import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
