from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
                       #Tracks
                       (r'^', include('tracks.urls')),    
                       
    # Examples:
    # url(r'^$', 'Server.views.home', name='home'),
    # url(r'^Server/', include('Server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       #Admin
                       url(r'^admin/', include(admin.site.urls)),
)
