from Illness.models import Illness, Symptom, SymptomType, BodyArea

body_area_list = []
body_area_list.append('head')
body_area_list.append('chest')
body_area_list.append('arms')
body_area_list.append('groin')
body_area_list.append('legs')
body_area_list.append('back')

head_symptom_types = []
head_symptom_types.append('eyes')
head_symptom_types.append('nose')
head_symptom_types.append('mouth')
head_symptom_types.append('neck')
head_symptom_types.append('ears')
head_symptom_types.append('hair')
head_symptom_types.append('face')

illness_list = []
illness_list.append('flu')
illness_list.append('cold')
illness_list.append('tapeworm infection')
illness_list.append('malaria')
illness_list.append('bacterial pneumonia')
illness_list.append('intestinal parasites')
illness_list.append('severe dehydration')
illness_list.append('strep throat')
illness_list.append('cholera')


for area in body_area_list:
	body_area = BodyArea(name = area)
	body_area.save()

for htype in head_symptom_types:
	symptom_type = SymptomType( body_area = BodyArea.objects.get(name = 'head'), name = htype)
	symptom_type.save()

for illness in illness_list:
	ill = Illness(name = illness)
	ill.save()