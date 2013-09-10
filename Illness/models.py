from django.db import models

class IllnessType(models.Model):
	name = models.CharField(max_length = 300, unique = True)
	image = models.URLField(blank = True)
	def __str__(self):
		return '%s ' % self.name
# Create your models here.
class Illness(models.Model):
	name = models.CharField(max_length=300, unique = True)
	description = models.TextField(blank = True)
	illness_type = models.ForeignKey(IllnessType, blank = True, null = True)
	def __str__(self):
		return '%s' % (self.name)

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
	image = models.URLField(blank= True)
	def __str__(self):
		return '%s ' % self.description
	class Meta:
		unique_together = ("symptom_type", "description")

class Recommendation(models.Model):
	recommendation = models.TextField(unique = True)
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

class Link(models.Model):
	link = models.URLField()
	description = models.TextField()