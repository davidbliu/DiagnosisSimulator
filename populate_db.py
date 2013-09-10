from Illness.models import *

colors = []
colors.append("http://3.bp.blogspot.com/-P18UUkOikck/UZr0DkLnnHI/AAAAAAAAA7o/mefS9IeGJnU/s400/blue.jpg")
colors.append("http://graybeardtrail.files.wordpress.com/2011/05/orange.jpg")
colors.append("http://3.bp.blogspot.com/-05zSm1UBNRk/Ta9Fzw_-LSI/AAAAAAAABAw/s3atkFcDvMo/s320/yello.JPG")

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

arm_symptom_types = []
arm_symptom_types.append('forearm')
arm_symptom_types.append('hand')
arm_symptom_types.append('elbow')
arm_symptom_types.append('upper arm')

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

illness_types = []
illness_types.append('infectious diseases')
illness_types.append('contagious diseases')
illness_types.append('foodborne illness')
illness_types.append('communicable diseases')
illness_types.append('non-communicable diseases')
illness_types.append('airborne diseases')
illness_types.append('lifesyle diseases')
illness_types.append('mental disorders')
illness_types.append('organic disease')

try: 
	for area in body_area_list:
		body_area = BodyArea(name = area)
		body_area.save()

	for htype in head_symptom_types:
		symptom_type = SymptomType( body_area = BodyArea.objects.get(name = 'head'), name = htype)
		symptom_type.save()

	for atype in arm_symptom_types:
		symptom_type = SymptomType( body_area = BodyArea.objects.get(name = 'arms'), name = atype) 
		symptom_type.save()

	for illness in illness_list:
		ill = Illness(name = illness)
		ill.save()

	
except: 
	print 'you have made a mistake somewhere'
# try:
print 'adding itypes'
for dtype in illness_types:
	import random
	randi = int(random.random() * len(colors))
	typ = IllnessType(name = dtype, image = colors[randi])
	typ.save()
	print str(randi)
	print dtype
# except:
	# print 'itypes failed'