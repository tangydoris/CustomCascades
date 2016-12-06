from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
    # ex: /css_file/5/
	url(r'^(?P<cssfile_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /css_file/5/results/
  url(r'^(?P<cssfile_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /css_app/search/
  url(r'^search/$', views.search, name="search"),
 	url(r'^upvote/(?P<cssfile_id>[0-9]+)/$', views.upvote, name='upvote'),
 	url(r'^remove/(?P<cssfile_id>[0-9]+)/$', views.remove, name='remove'),
 	url(r'^save/(?P<cssfile_id>[0-9]+)/$', views.save, name='save'),
  url('^', include('django.contrib.auth.urls')),
]