from Illness.models import *

for sym in Symptom.objects.all():
	sym.description = sym.description.replace('\r\n','')
	sym.save()