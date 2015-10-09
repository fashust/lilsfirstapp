from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<simpletab_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<simpletab_id>\d+)/result/$', views.result, name='result'),
    url(r'^(?P<simpletab_id>\d+)/vote/$', views.vote, name='vote'),
)