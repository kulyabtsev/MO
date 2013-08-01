from django.db import models

# Create your models here.
class Branch(models.Model):
	title = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.title
		
class Organization(models.Model):
	title = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.title