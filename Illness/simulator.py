from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Illness.models import Illness, Symptom, IllnessSymptom, symptom_type_choices
from django import forms
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf

def get_clues_view(request):
	symptoms = []
	if request.method == 'GET':
		symptom_type = request.GET['symptom_type']
		illness = Illness.objects.get(name = request.GET['illness'])
		mappings = IllnessSymptom.objects.filter(illness = illness)
		for mapping in mappings:
			if mapping.symptom.symptom_type == symptom_type:
				symptoms.append(mapping.symptom)
	args = {}
	args['symptoms'] = symptoms
	return render_to_response('Illness/clues.html', args)

def simulator_view(request, illnessID = "0"):
	illness = Illness.objects.get(id = illnessID)
	mappings = IllnessSymptom.objects.filter(illness = illness)
	symptoms = []
	for mapping in mappings:
		symptoms.append(mapping.symptom)
	args = {}
	args['illness'] = illness
	args['symptoms'] = symptoms
	args['symptom_types'] = []
	for choice in symptom_type_choices:
		args['symptom_types'].append(choice[1])
	return render_to_response('Illness/simulator.html', args)