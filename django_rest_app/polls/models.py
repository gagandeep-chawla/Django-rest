from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	title = models.TextField(null=False,blank=False)
	status = models.CharField(default='inactive',max_length=55)
	created_by = models.ForeignKey(User,null=True,blank=True,on_delete = models.CASCADE)
	start_date = models.DateTimeField(null = True,blank= True)
	end_date = models.DateTimeField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class PracticeModel(models.Model):

	STATUS_CODE = (('ACTIVE','active'),
		('INACTIVE','inactive'))

	title = models.TextField(unique=True)
	status = models.CharField(default='active',choices=STATUS_CODE,max_length= 255)
	owner = models.ForeignKey(User, null = True,blank=True,on_delete = models.CASCADE)
	question = models.ManyToManyField(Question)

	# def __str__(self):
	# 	return self.title
