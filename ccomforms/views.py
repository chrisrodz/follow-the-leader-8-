from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from ccomforms.models import T02, A125, Profile
from ccomforms.forms import T02Form, A125Form, ProfileForm
from t02 import t02
from a125 import a125
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# View for creating the T02 PDF
def createt02(request, document_root, obj):
	data = serializers.serialize('json',T02.objects.filter(id=obj))
	generator = t02()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/media/t02-gen.pdf')

# View for creating the A125 PDF
def createa125(request, document_root, obj):
	data = serializers.serialize('json',A125.objects.filter(id=obj))
	generator = a125()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/media/a125-gen.pdf')

# TEST VIEW, NOT USED IN PROJECT
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

# View for rendering the professor's profile
@login_required
def profile(request):
	t02s = T02.objects.filter(professor=request.user)
	a125s = A125.objects.filter(professor=request.user)
	return render_to_response('profile.html', {'t02s': t02s, 'a125s': a125s})

# View for rendering the professor's history
@login_required
def history(request):
	t02s = T02.objects.filter(professor=request.user)
	a125s = A125.objects.filter(professor=request.user)
	return render_to_response('history.html', {'t02s': t02s, 'a125s': a125s})

# View for editing professor's profile information
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

# View for creating a new T02 form and saving it into the database
@login_required
def newT02(request, formid=None):
	if request.method == 'POST':
		form = T02Form(request.POST)
		if form.is_valid():
			form.save()
			return profile(request)
		else:
			return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))
	else:
		if formid:
			old = T02.objects.get(id=formid)
			form = T02Form(initial={'professor': old.professor, 'Num_Referencia': old.Num_Referencia, 'Transaccion': old.Transaccion, 'f1': old.f1, 'f2': old.f2, 'f3': old.f3, 'f5': old.f5, 'f6': old.f6, 'f7': old.f7, 'f8': old.f8, 'f9': old.f9, 'f10': old.f10, 'f11': old.f11, 'f12': old.f12, 'f13': old.f13, 'f14': old.f14, 'f15': old.f15, 'f16': old.f16, 'f17': old.f17, 'f18': old.f18, 'f19': old.f19, 'f20': old.f20, 'f21': old.f21, 'f22': old.f22, 'f23': old.f23, 'f24': old.f24, 'f25': old.f25, 'f26': old.f26, 'f27': old.f27, 'f30': old.f30})
			form.fix_instance()
		else:
			form = T02Form()	
		return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))

# View for creating a new A125 form and saving it into the database
@login_required
def newA125(request, formid=None):
	if request.method == 'POST':
		form = A125Form(request.POST)
		if form.is_valid():
			pdf = form.save()
			return profile(request)
		else:
			return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))
	else:
		if formid:
			old = A125.objects.get(id=formid)
			form = A125Form(initial={'professor': old.professor, 'name': old.name, 'ssn': old.ssn, 'title': old.title, 'base_salary': old.base_salary, 'period': old.period, 'period_year': old.period_year, 'effective_date': old.effective_date, 'multi_campus': old.multi_campus, 'sponsored_accounts': old.sponsored_accounts, 'cost_sharing': old.cost_sharing, 'university_funds': old.university_funds, 'total_compensation': old.total_compensation, 'payments_paid': old.payments_paid, 'comments': old.comments})
			form.fix_instance()
		else:
			form = A125Form()	
		return render_to_response('newform.html', {'form': form}, context_instance=RequestContext(request))

