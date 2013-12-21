from django.conf.urls import patterns, url

from todoapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /todoapp/5/
    url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
    # ex: /todoapp/5/results/
    url(r'^(?P<task_id>\d+)/results/$', views.results, name='results'),

 )