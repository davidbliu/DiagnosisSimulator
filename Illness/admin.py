from django.contrib import admin
from Illness.models import Illness, Symptom, IllnessSymptom

admin.site.register(Illness)
admin.site.register(Symptom)
admin.site.register(IllnessSymptom)