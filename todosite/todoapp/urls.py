from django.conf.urls import patterns, url
from todoapp import views

urlpatterns = patterns('',

        url(r'^index/$', views.index, name='index'),
        
        url(r'^detail/(?P<tasklist_id>\d+)/$', views.detail, name ='detail'),
        url(r'^detail/$', views.detail, name ='detail'),
        
        url(r'^addtl/$', views.addtl, name ='addtl'),
        url(r'^addtask/(?P<tasklist_id>\d+)/$', views.addtask, name ='addtask'),
        
        url(r'^deltl/(?P<tasklist_id>\d+)/$', views.deltl, name ='deltl'),
        url(r'^deltask/(?P<task_id>\d+)/$', views.deltask, name ='deltask'),
        
        url(r'^change/(?P<task_id>\d+)/$', views.change, name ='change'),
        url(r'^changetl/(?P<tasklist_id>\d+)/$', views.changetl, name ='changetl'),
        url(r'^changetask/(?P<task_id>\d+)/$', views.changetask, name ='changetask'),
#        url(r'^logout/$', views.SignOut, name='logout'),
)