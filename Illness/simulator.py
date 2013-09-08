from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Illness.models import *
from django import forms
from django.forms import ModelForm
from django.template import RequestContext
from django.core.context_processors import csrf
import json

# used in ajax call to return the patient's response when user checks for symptoms
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

def get_symptoms_view(request):
	# always going to be a get request so dont worry about other cases
	args = {}
	illness = Illness.objects.get(name = request.GET['illness'])
	symptom_type = SymptomType.objects.get(name = request.GET['symptom_type'])
	mappings = IllnessSymptom.objects.filter(illness = illness)
	symptom_list = []
	for mapping in mappings:
		sym = mapping.symptom
		if sym.symptom_type == symptom_type:
			symptom_list.append(sym.description)
	print symptom_list
	args['symptom_list'] = symptom_list
	# return HttpResponse('hi there')
	return HttpResponse(json.dumps(args), mimetype='application/json')

def simulator_view(request, illnessID = "0"):
	args = {} # is the dictionary of values passed into the template
	illness = Illness.objects.get(id = illnessID)
	mappings = IllnessSymptom.objects.filter(illness = illness)
	symptoms = []
	for mapping in mappings:
		symptoms.append(mapping.symptom)

	if request.method == "POST":
		try: 
			answered_illness = Illness.objects.get(name = request.POST.get('answer_input'))
			if answered_illness == illness:
				args['message'] = 'you got it right! the illness was '+request.POST.get('answer_input')
			else:
				# guessed the answer wrong so display the differences in symptoms
				args['message'] = 'not quite...your guess was '+request.POST.get('answer_input')
				args['right_symptoms'] = []
				args['wrong_symptoms'] = []
				args['missing_symptoms'] = []
				ans_symptoms = []
				ans_mappings = IllnessSymptom.objects.filter(illness = answered_illness)
				for mapping in ans_mappings:
					ans_symptoms.append(mapping.symptom)
				for symptom in ans_symptoms:
					if symptom in symptoms:
						args['right_symptoms'].append(symptom)
					else:
						args['wrong_symptoms'].append(symptom)
				for symptom in symptoms:
					if symptom not in ans_symptoms:
						args['missing_symptoms'].append(symptom)
		except: 
			print 'your entered an invalid illness'
			args['message'] = 'sorry that is an invalid illness'
		# handle the recommendations
		print 'these were the recommendations'
		args['user_recommendations'] = request.POST.get('recommendation_input').split('\n')
		for rec in args['user_recommendations']:
			temp = check_recommendation(rec, illness, 3)
		# args['recommendations'] = 
	
	args['illness'] = illness
	args['symptoms'] = symptoms
	args['symptom_types'] = SymptomType.objects.all()
	args['body_parts'] = get_body_parts()
	print(args['body_parts'])
	# for choice in symptom_type_choices:
		# args['symptom_types'].append(choice[1])
	args.update(csrf(request))
	return render_to_response('Illness/simulator.html', args)

# used to check if recommendations are correct. input string recommendation text that
# user inputted and checks to see if matches any of the recommendations in db
# returns correct, wrong, or unknown
def check_recommendation(user_recommendation, illness, thresh):
	recommendations = IllnessRecommendation.objects.filter(illness = illness)
	user_recommendation_words = user_recommendation.split(' ')
	for rec in recommendations:
		matches = 0
		for word in user_recommendation_words:
			if word in rec.recommendation.recommendation:
				matches += 1
		print 'there were '+str(matches)+'for the recommendation '+user_recommendation
		if matches > thresh:
			print 'im returning correct for recommendation ' + user_recommendation
			return 'correct'
	return 'unknown'

def get_body_parts():
	body_parts = []
	for general_area in BodyArea.objects.all():
		# body_dict[general_area] = SymptomType.objects.filter(body_area = general_area)
		entry = {'general_area' : general_area, 'symptom_types':SymptomType.objects.filter(body_area = general_area)}
		body_parts.append(entry)
	print body_parts
	return body_parts