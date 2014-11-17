from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jobtracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'jobtracker.views.index'),
    url(r'^dashboard/', 'jobtracker.views.dashboard'),
    url(r'^auth/', 'jobtracker.views.auth'),
    url(r'^logout/', 'jobtracker.views.userLogout'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^jobs/', include('jobs.urls', namespace='jobs')),
    url(r'^connections/', include('connections.urls', namespace='connections')),
)
