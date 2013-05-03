from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from ccomforms.models import T02, T02Form, A125, A125Form, Profile, ProfileForm
from t02 import t02
from a125 import a125
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def createt02(request, document_root, obj):
	data = serializers.serialize('json',T02.objects.filter(id=obj))
	generator = t02()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/media/t02-gen.pdf')

def createa125(request, document_root, obj):
	data = serializers.serialize('json',A125.objects.filter(id=obj))
	generator = a125()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/media/a125-gen.pdf')

@login_required
def pdfform(request):
	me = T02.objects.get(id=1)
	if request.method != 'POST':
		p = T02Form(instance=me)
		p.fix_instance()
		return render_to_response('pdfform.html', {'form': p}, context_instance=RequestContext(request))
	else:
		form = T02Form(request.POST, instance=me)
		if form.is_valid():
			pdf = form.save()
			return HttpResponseRedirect('/')

@login_required
def profile(request):
	t02s = T02.objects.filter(professor=request.user)
	a125s = A125.objects.filter(professor=request.user)
	return render_to_response('profile.html', {'t02s': t02s, 'a125s': a125s})

@login_required
def editprofile(request):
	current = Profile.objects.get(professor=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=current)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
		else:
			return render_to_response('editprofile.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = ProfileForm(instance=current)
		return render_to_response('editprofile.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def newT02(request):
	if request.method == 'POST':
		form = T02Form(request.POST)
		if form.is_valid():
			form.save()
			return profile(request)
		else:
			return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = T02Form()
		return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def newA125(request):
	if request.method == 'POST':
		form = A125Form(request.POST)
		if form.is_valid():
			pdf = form.save()
			return profile(request)
		else:
			return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = A125Form()
		return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))