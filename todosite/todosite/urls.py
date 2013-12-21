from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include('todoapp.adminurls')),

    url(r'^admin/', include(admin.site.urls)),
       # ex: /todoapp/5/
    url(r'^todoapp/', include('todoapp.urls')),

)
