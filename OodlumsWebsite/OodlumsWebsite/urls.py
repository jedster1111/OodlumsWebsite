"""
Definition of urls for OodlumsWebsite.
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
admin.autodiscover()

from . import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin


urlpatterns = [
    path('', views.home, name = "home"),
    path('videos/', include('videos.urls')),
    path('contact/', views.contact, name ="contact"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


    # Examples:
    # url(r'^$', OodlumsWebsite.views.home, name='home'),
    # url(r'^OodlumsWebsite/', include('OodlumsWebsite.OodlumsWebsite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
