from django.conf.urls.defaults import *
from moxitems.views import TestFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mOxItems/', include('mOxItems.foo.urls')),
    (r'^mOxItems/feed/(?P<slug>[\w/]+)$', TestFeed() )

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
