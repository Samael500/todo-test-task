from django.conf.urls import patterns, url

from todoapp import views

urlpatterns = patterns('',
    url(r'^auth/user/(?P<user_id>\d+)/tasklists$', views.usertasklists),

)