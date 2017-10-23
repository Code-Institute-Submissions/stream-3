from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.entertainer_index, name='enterainer_index'),
	url(r'^entertainer/new/$', views.entertainer_new, name='entertainer_new'),
    url(r'^entertainers/$', views.entertainer_list, name='enterainer_list'),
    url(r'^entertainer/(?P<pk>\d+)/$', views.entertainer_detail, name='entertainer_detail'),
]