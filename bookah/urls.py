from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings.development import MEDIA_ROOT

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'', include('entertainer.urls')),
     url(r'', include('accounts.urls')),
     url(r'^pages/', include('django.contrib.flatpages.urls')),
     url(r'', include('contactapp.urls')),
     url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
