from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
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


# def post(request):
#   if request.method == 'POST':
#     form = PostForm(request.POST)
#     new_post = form.save(commit=False)
#     new_post.user = request.user
#     new_post.pub_date = timezone.now()
#     new_post.save()
#     return home(request)
#   else:
#     form = PostForm
#   return render(request, 'micro/post.html', {'form' : form})

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
	queried_files = 0
	queried_file = 0
	if spec == 'popular':
		queried_files = (CSSFile.objects.filter(host_hash=host)).order_by('-vote_count')
	if spec == 'recent':
		queried_files = (CSSFile.objects.filter(host_hash=host)).order_by('-created_at')
	if queried_files:
		queried_file = queried_files[0]
	if spec == 'id':
		queried_file = (CSSFile.objects.get(pk=host))

	if queried_file:
		return JsonResponse({'css': queried_file.css_text})
	return JsonResponse({'error': 'no file saved for this host'})
