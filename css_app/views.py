from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import CSSFile

# Create your views here.

@login_required
def index(request):
	latest_css_file_list = CSSFile.objects.order_by('-created_at')[:5]
	context = {'latest_css_file_list': latest_css_file_list}
	if(request.method == 'POST'):
		# DO THE POST STUFF
		title = request.POST['title']
		host = request.POST['host']
		css_text = request.POST['css_text']
		new_css_file = CSSFile(title=title, host=host, css_text=css_text, user=request.user)
		new_css_file.save()
	return render(request, 'css_app/index.html', context)

def detail(request, cssfile_id):
    css_file = get_object_or_404(CSSFile, pk=cssfile_id)
    return render(request, 'css_app/detail.html', {'css_file': css_file})


def results(request, cssfile_id):
	response = "You are looking at the results of cssfile %s."
	return HttpResponse(results % cssfile_id)

def vote(request, cssfile_id):
	return HttpResponse("You're voting on cssfile %s" % cssfile_id)
