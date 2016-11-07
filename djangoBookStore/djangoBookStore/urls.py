"""
Definition of urls for djangoBookStore.
"""

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
from store import urls

urlpatterns = [      
      url(r'^store/', include('store.urls'), name='store'),
      url(r'^accounts/', include('registration.backends.default.urls')), 
      url(r'^admin/', include(admin.site.urls)), 
      ]

    