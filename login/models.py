from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=200,primary_key=True)
	password = models.CharField(max_length=50)
	auth12 = models.CharField(max_length=20)
	name = models.CharField(max_length=200)
	
