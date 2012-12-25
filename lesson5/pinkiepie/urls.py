from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from .views import pie_list

urlpatterns = patterns('',
    url(r'^$', pie_list, name='home'),
    # url(r'^pinkiepie/', include('pinkiepie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls))
)
