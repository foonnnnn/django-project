from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'', include('web.urls')),
)