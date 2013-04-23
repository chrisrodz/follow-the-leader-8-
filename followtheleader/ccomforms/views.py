from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from ccomforms.models import T02
from t02 import t02

def createpdf(request, document_root):
	data = serializers.serialize('json',T02.objects.filter(id=1))
	generator = t02()
	generator.buildPDF(data, document_root)
	return HttpResponseRedirect('/')