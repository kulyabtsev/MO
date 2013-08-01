# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Unit(models.Model):
	SEX_CHOICES = (('M', 'Men'),('W', 'Woman'),)
	
	first_name = models.CharField(max_length=25)
	surname = models.CharField(max_length=25)
	second_name = models.CharField(max_length=25)
	birth_date = models.DateField()
	sex = models.CharField(max_length=10,
							choices=SEX_CHOICES)
	education = models.ForeignKey('Education', blank=True, null=True, on_delete=models.SET_NULL)
	organization = models.ForeignKey('organizations.Organization', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey('organizations.Branch', blank=True, null=True, on_delete=models.SET_NULL)
	hired = models.BooleanField(default=False)
	job_title = models.ForeignKey('Jobtitle', blank=True, null=True, on_delete=models.SET_NULL)
	
	def __unicode__(self):
		return self.surname + ' ' + self.first_name+ ' ' + self.second_name
	
	
class Jobtitle(models.Model):
	title = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title
	
class Education(models.Model):
	title = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title