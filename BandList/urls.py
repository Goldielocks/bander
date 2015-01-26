from django.conf.urls import patterns, url
from BandList import views

urlpatterns = patterns('',
	(r'^$', views.base),
	(r'^shows/$', views.shows),
	(r'^bands/$', views.bands),
	(r'^register/$', views.register),
	url(r'home/$', views.home, name='home'),
    (r'^accounts/login/$', views.user_login),
	(r'^add/$', views.add),
	(r'^remove/$', views.remove),
)