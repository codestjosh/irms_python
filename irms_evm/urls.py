from django.conf.urls import url, patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('core.urls'), name="core"),
                       url(r'admin/', include(admin.site.urls)),
)
