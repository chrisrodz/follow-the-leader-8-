from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from ccomforms.models import T02, T02Form
from t02 import t02
from django.template import RequestContext

def createpdf(request, document_root):
	data = serializers.serialize('json',T02.objects.filter(id=1))
	generator = t02()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/')

def pdfform(request):
	me = T02.objects.get(id=1)
	if request.method != 'POST':
		p = T02Form(instance=me)
		p.initial['f10'] = ",".join([str(x) for x in p.initial['f10']])
		p.initial['f11'] = ",".join([str(x) for x in p.initial['f11']])
		p.initial['f12'] = ",".join([str(x) for x in p.initial['f12']])
		p.initial['f13'] = ",".join([str(x) for x in p.initial['f13']])
		p.initial['f14'] = ",".join([str(x) for x in p.initial['f14']])
		p.initial['f15'] = ",".join([str(x) for x in p.initial['f15']])
		p.initial['f16'] = ",".join([str(x) for x in p.initial['f16']])
		p.initial['f17'] = ",".join([str(x) for x in p.initial['f17']])
		p.initial['f18'] = ",".join([str(x) for x in p.initial['f18']])
		p.initial['f19'] = ",".join([str(x) for x in p.initial['f19']])
		p.initial['f20'] = ",".join([str(x) for x in p.initial['f20']])
		p.initial['f21'] = ",".join([str(x) for x in p.initial['f21']])
		p.initial['f23'] = ",".join([str(x) for x in p.initial['f23']])
		p.initial['f27'] = ",".join([str(x) for x in p.initial['f27']])
		return render_to_response('pdfform.html', {'form': p}, context_instance=RequestContext(request))
	else:
		form = T02Form(request.POST, instance=me)
		if form.is_valid():
			pdf = form.save()
			return HttpResponseRedirect('/')