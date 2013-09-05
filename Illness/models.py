from django.db import models

# Create your models here.
class Illness(models.Model):
	name = models.CharField(max_length=300)
	description = models.TextField(blank = True)
	def __str__(self):
		return '%s' % (self.name)

symptom_type_choices = (('head','head'),('ears','ears'),('eyes','eyes'),
	('nose/mouth','nose and mouth'),('neck/throat','neck and throat'),('history', 'history'), ('time' ,'time'))

class Symptom(models.Model):
	symptom_type = models.CharField(max_length=300, choices = symptom_type_choices)
	description = models.TextField()
	# illness = models.ForeignKey(Illness)
	def __str__(self):
		return '%s ' % self.description
	class Meta:
		unique_together = ("symptom_type", "description")

class IllnessSymptom(models.Model):
	illness = models.ForeignKey(Illness)
	symptom = models.ForeignKey(Symptom)
	def __str__(self):
		return '%s %s' % (self.illness, self.symptom)
	class Meta:
		unique_together = ('illness', 'symptom')
