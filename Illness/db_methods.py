from Illness.models import *

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
