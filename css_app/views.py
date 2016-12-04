from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import CSSFile

# Create your views here.

@login_required
def index(request):
	latest_css_file_list = CSSFile.objects.filter(user=request.user).order_by('-created_at')
	trending_css_file_list = CSSFile.objects.order_by('-vote_count')[:5]
	context = {'latest_css_file_list': latest_css_file_list, 'trending_css_file_list':trending_css_file_list}
	if(request.method == 'POST'):
		# DO THE POST STUFF
		title = request.POST['title']
		host = request.POST['host']
		css_text = request.POST['css_text']
		description = request.POST['description']
		new_css_file = CSSFile(title=title, host=host, css_text=css_text, user=request.user, description=description)
		new_css_file.save()
	return render(request, 'css_app/index.html', context)

# @login_required
def search_results(request):
	if (request.method == 'POST'):
		queriedTitle = request.POST['title']
		# print("******")
		print(queriedTitle)
		# print("*****")
		hits_list = CSSFile.objects.filter(title=queriedTitle)
		# print(hits_list)
		# print("******")
		context = {'hits_list': hits_list}
		# return render(request, 'css_app/search_results.html', context)
		return render(request, 'css_app/search_results.html')
	else:
		return render(request, 'css_app/search_results.html')

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

