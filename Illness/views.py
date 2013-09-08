from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Illness.models import Illness, Symptom, IllnessSymptom, Recommendation, IllnessRecommendation
from django import forms
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
import json

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

#this class should be deleted later, it was only a visual aid
def symptoms_clues_view(request):
	args = {}
	args['symptoms'] = Symptom.objects.filter( illness = Illness.objects.get(id = 2))
	return render_to_response('clues.html', args)

# below are all the forms -----------------------------------------------------------------------------------
class IllnessForm(ModelForm):
	class Meta:
		model = Illness
def add_illness_form(request):
	if request.method == "POST":
		posted_form = IllnessForm(request.POST)
		if posted_form.is_valid():
			posted_form.save()
			return HttpResponseRedirect('/list')
	args = {}
	args.update(csrf(request))
	args['illness_form'] = IllnessForm()
	return render_to_response('Illness/add_illness_form.html',args)


# builds form for entering in new symptoms
class SymptomForm (ModelForm):
	class Meta:
		model = Symptom
class RecommendationForm(ModelForm):
	class Meta: 
		model = Recommendation
def illness_form (request, illnessID = '0'):
	illness = Illness.objects.get(id = illnessID)
	if request.method == "POST":
		print request.POST
		# if you are submitting an existing symptom, simple add a mapping for illness and symptom to IllnessSymptom table
		if 'submit_old' in request.POST:
			symptoms = request.POST.getlist('old_symptom')
			print symptoms
			for symp in symptoms:
				try:
					symptom = Symptom.objects.get(description = symp)
					# create new mappingping between that symptom and the illness
					new_mapping = IllnessSymptom(illness = illness, symptom = symptom)
					new_mapping.save()
				except:
					print 'duplicate mappings'
					# TODO: dont even show duplicate mappings
		else:
			posted_form = SymptomForm(request.POST)
			if posted_form.is_valid():
				posted_form.save()
				# also make a new mapping between the symptom and the current illness
				new_mapping = IllnessSymptom(illness = illness, symptom = posted_form.instance)
				new_mapping.save()
				return HttpResponseRedirect('/illness_form/'+illnessID)
	args = {}
	args['all_symptoms'] = Symptom.objects.all()
	args['symptom_form'] = SymptomForm()
	args['recommendation_form'] = RecommendationForm()
	args['symptoms'] = getSymptoms(Illness.objects.get(id = illnessID))
	args['illness'] = illness
	# args['symptom_types'] = Symptom.objects.values_list('symptom_type', flat = True).distinct()
	args.update(csrf(request))
	return render_to_response('Illness/illness_form.html', args)

# will always be a get request, filters out all but symptoms with the keyword in their descriptions
def filter_symptom_view(request):
	bad_symptoms = []
	keyword = request.GET.get('filter_term')
	for symptom in Symptom.objects.all():
		if keyword not in symptom.description:
			bad_symptoms.append(symptom.description)
	print keyword
	print bad_symptoms
	args = {}
	args['bad_symptoms'] = bad_symptoms
	return HttpResponse(json.dumps(args), mimetype='application/json')
#returns a list of symptoms associated with the input parameter illness
def getSymptoms(illness):
	symptoms = []
	symp_maps = IllnessSymptom.objects.filter(illness = illness)
	for mapping in symp_maps:
		symptoms.append(mapping.symptom)
	return symptoms