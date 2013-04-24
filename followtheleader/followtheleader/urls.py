from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^createpdf/$','ccomforms.views.createpdf', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^pdfform/$','ccomforms.views.pdfform'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
