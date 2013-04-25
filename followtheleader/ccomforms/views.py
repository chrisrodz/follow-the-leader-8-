from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from ccomforms.models import T02, T02Form
from t02 import t02
from django.template import RequestContext

def createpdf(request, document_root):
	data = serializers.serialize('json',T02.objects.filter(id=1))
	generator = t02()
	return generator.buildPDF(data, document_root)
	# return HttpResponseRedirect('/')

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