from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Illness.models import *
from django import forms
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
from db_methods import *
import json
import quopri

def home_view(request):
	args = {}
	args['illnesses'] = Illness.objects.all()
	args['illness_types'] = IllnessType.objects.all()
	return render_to_response('Illness/home_view.html', args)
def illness_detail_view(request, illnessID = '0'):
	illness = Illness.objects.get(id = illnessID)
	args = {}
	args['illness'] = illness
	args['symptoms'] = getSymptoms(illness)
	return render_to_response('Illness/detail.html', args)
def illness_list_view (request):
	illness_list = Illness.objects.all()
	illnesses = []
	for illness in illness_list:
		# symptom_list = Symptom.objects.filter(illness = illness)
		symptom_list = IllnessSymptom.objects.filter(illness = illness)
		entry = {'illness': illness , 'symptoms': symptom_list}
		illnesses.append(entry)
	args = {}
	args['entries'] = illnesses
	return render_to_response('Illness/illness_list.html', args)

# below are all the forms -----------------------------------------------------------------------------------

