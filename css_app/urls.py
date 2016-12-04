from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
    # ex: /css_file/5/
	url(r'^(?P<cssfile_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /css_file/5/results/
    url(r'^(?P<cssfile_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /css_app/search_results/
    url(r'^search_results/$', views.search_results, name="search_results"),
   	url(r'^upvote/(?P<cssfile_id>[0-9]+)/$', views.upvote, name='upvote'),
    url('^', include('django.contrib.auth.urls')),
]