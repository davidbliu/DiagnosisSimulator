from django.contrib import admin
from Illness.models import *
from django.db.models import get_models

admin.site.register(Illness)
admin.site.register(Symptom)
admin.site.register(IllnessSymptom)
admin.site.register(Recommendation)
admin.site.register(IllnessRecommendation)
admin.site.register(SymptomType)
admin.site.register(BodyArea)
admin.site.register(IllnessType)

