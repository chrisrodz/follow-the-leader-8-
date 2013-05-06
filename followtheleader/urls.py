from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^createt02/(?P<obj>\d*)$','ccomforms.views.createt02', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^createa125/(?P<obj>\d*)$','ccomforms.views.createa125', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^pdfform/$','ccomforms.views.pdfform'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^profile/$','ccomforms.views.profile'),
    url(r'^newT02/$','ccomforms.views.newT02'),
    url(r'^newA125/$','ccomforms.views.newA125'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^editprofile/$','ccomforms.views.editprofile'),

)
