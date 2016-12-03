from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
    # ex: /css_file/5/
	url(r'^(?P<cssfile_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /css_file/5/results/
    url(r'^(?P<cssfile_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /css_file/5/vote/
    url(r'^(?P<cssfile_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /css_app/search_results/
    url(r'^search_results/$', views.search_results, name="search_results"),
    
    url('^', include('django.contrib.auth.urls')),
]