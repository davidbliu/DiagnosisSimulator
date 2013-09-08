from django.db import models

# Create your models here.
class Illness(models.Model):
	name = models.CharField(max_length=300, unique = True)
	description = models.TextField(blank = True)
	def __str__(self):
		return '%s' % (self.name)

# symptom_type_choices = (('head','head'),('ears','ears'),('eyes','eyes'),
# 	('nose/mouth','nose and mouth'),('neck/throat','neck and throat'),('history', 'history'), ('time' ,'time'))

# body_parts = ('head', 'neck', 'chest', 'abdomen', 'pelvis', 'legs', 'arms', 'back')

class BodyArea(models.Model):
	name = models.CharField(max_length = 300, unique = True)
	def __str__(self):
		return '%s ' % self.name

class SymptomType(models.Model):
	name = models.CharField(max_length = 300)
	body_area = models.ForeignKey(BodyArea, blank = True)
	def __str__(self):
		return '%s ' % self.name
	class Meta:
		unique_together = ("name", "body_area")

class Symptom(models.Model):
	symptom_type = models.ForeignKey(SymptomType)
	description = models.TextField()
	def __str__(self):
		return '%s ' % self.description
	class Meta:
		unique_together = ("symptom_type", "description")

class Recommendation(models.Model):
	recommendation = models.TextField(unique = True)
	# recommendation_type = models.CharField(max_length = 300, blank = True)
	def __str__(self):
		return '%s ' % self.recommendation

class IllnessRecommendation(models.Model):
	illness = models.ForeignKey(Illness)
	recommendation = models.ForeignKey(Recommendation)
	def __str__(self):
		return '%s %s' % (self.illness, self.recommendation)
	class Meta:
		unique_together = ('illness', 'recommendation')

class IllnessSymptom(models.Model):
	illness = models.ForeignKey(Illness)
	symptom = models.ForeignKey(Symptom)
	def __str__(self):
		return '%s %s' % (self.illness, self.symptom)
	class Meta:
		unique_together = ('illness', 'symptom')
