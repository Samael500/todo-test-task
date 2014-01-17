from django.conf.urls import patterns, url
from usersapp import views

urlpatterns = patterns('',

        url(r'^login/$', views.SignIn, name='signin'),
        url(r'^signup/$', views.SignUp, name ='signup'),
        url(r'^logout/$', views.SignOut, name='logout'),
)