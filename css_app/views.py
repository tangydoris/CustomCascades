from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.cache import cache
from .models import CSSFile
from hashlib import md5

# Create your views here.

@login_required
def index(request):
	latest_css_file_list = CSSFile.objects.filter(user=request.user).order_by('-created_at')
	trending_css_file_list = CSSFile.objects.exclude(user=request.user).order_by('-vote_count')[:5]
	context = {'latest_css_file_list': latest_css_file_list, 'trending_css_file_list':trending_css_file_list}

	if(request.method == 'POST'):
		# DO THE POST STUFF
		title = request.POST['title']
		host = request.POST['host']
		host_hash = (md5(host.encode())).hexdigest()[:16]
		css_text = request.POST['css_text']

		# cache logic, we put stuff in the cache when we create the css file
		mem_cache_key_recent = host_hash + "recent"
		mem_cache_key_popular = host_hash + "popular"
		cache.set(mem_cache_key_recent, css_text)
		if cache.get(mem_cache_key_popular) is None:
			cache.set(mem_cache_key_popular, css_text)

		description = request.POST['description']
		new_css_file = CSSFile(title=title, host=host, host_hash=host_hash, css_text=css_text, user=request.user, description=description)
		new_css_file.save()
	return render(request, 'css_app/index.html', context)



@login_required
def search(request):
	print(request)
	if ('q' in request.GET):
		query_string = request.GET['q']
		query_set = CSSFile.objects.filter(host__icontains=query_string)

		# if filter is requested
		if ('filter_by' in request.GET):
			filt = request.GET['filter_by']
			if (filt == "trending"):
				query_set = query_set.order_by('-vote_count')

		results_list = list(query_set)
		context = {'results_list': results_list, 'query': query_string}
		return render(request, 'css_app/search.html', context)

	return render(request, 'css_app/search.html')

def detail(request, cssfile_id):
    css_file = get_object_or_404(CSSFile, pk=cssfile_id)
    return render(request, 'css_app/detail.html', {'css_file': css_file})

def results(request, cssfile_id):
	response = "You are looking at the results of cssfile %s."
	return HttpResponse(results % cssfile_id)

def upvote(request, cssfile_id):
	css_file = CSSFile.objects.get(pk=cssfile_id)
	css_file.vote_count += 1
	css_file.save()

	most_upvoted = CSSFile.objects.filter(host=css_file.host).order_by('-vote_count')[:1].get()

	host = most_upvoted.host_hash
	cache_string = host + "popular"
	cache.set(cache_string, css_file.css_text)

	return redirect('/css_app')

def remove(request, cssfile_id):
	css_file = CSSFile.objects.filter(id=cssfile_id).delete()
	return redirect('/css_app')

def save(request, cssfile_id):
	css_file = CSSFile.objects.get(pk=cssfile_id)
	u = request.user
	u.cssfile_set.add(css_file)
	print u
	return redirect('/css_app')

def api_detail(request, host, spec):
	cache_string = host + spec
	queried_file = cache.get(cache_string)

	if queried_file:
		print("The cache successfully returned a file")
		return JsonResponse({'css': queried_file.css_text})
	print("The cache did not find the file")
	return JsonResponse({'error': 'no file saved for this host'})
