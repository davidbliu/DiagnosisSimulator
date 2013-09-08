from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Illness.models import Illness, Symptom, IllnessSymptom, Recommendation, IllnessRecommendation
from django import forms
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
import json
import quopri

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
		if 'submit_old_symptom' in request.POST:
			symptoms = request.POST.getlist('old_symptom')
			for symp in symptoms:
				symptom = Symptom.objects.get(description = symp)
				createISMapping(illness, symptom)
		elif 'submit_symptom' in request.POST:
			posted_form = SymptomForm(request.POST)
			if posted_form.is_valid():
				posted_form.save()
				createISMapping(illness, posted_form.instance)
		elif 'submit_old_rec' in request.POST:
			recs = request.POST.getlist('old_recommendation')
			for rec in recs:
				recommendation = Recommendation.objects.get(recommendation = rec)
				createIRMapping(illness, recommendation)
		elif 'submit_rec' in request.POST:
			posted_form = RecommendationForm(request.POST)
			if posted_form.is_valid():
				posted_form.save()
				createIRMapping(illness, posted_form.instance)
		return HttpResponseRedirect('/illness_form/'+illnessID)
	args = {}
	args['all_symptoms'] = Symptom.objects.all()
	args['all_recommendations'] = Recommendation.objects.all()
	args['symptom_form'] = SymptomForm()
	args['recommendation_form'] = RecommendationForm()
	args['symptoms'] = getSymptoms(Illness.objects.get(id = illnessID))
	args['recommendations'] = getRecommendations(Illness.objects.get(id = illnessID))
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
#returns a list of recommendations for the input illness
def getRecommendations(illness):
	recommendations = []
	maps = IllnessRecommendation.objects.filter(illness = illness)
	for mapping in maps:
		recommendations.append(mapping.recommendation)
	return recommendations

def createISMapping(illness, symptom):
	try:
		is_map = IllnessSymptom(illness = illness, symptom = symptom)
		is_map.save()
	except:
		print 'you have a duplicate mapping'
		#means there is a duplicate mapping
def createIRMapping(illness, recommendation):
	try:
		ir_map = IllnessRecommendation(illness = illness, recommendation = recommendation)
		ir_map.save()
	except:
		print 'you have a duplicate mapping'
		#means there is a duplicate mapping