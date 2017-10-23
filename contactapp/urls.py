from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact/$', views.email, name='email'),
    url(r'^thank-you/$', views.success, name='success'),
]