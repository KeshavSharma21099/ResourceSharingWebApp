from django.db import models
from django.contrib.auth.models import User
from datetime import date
from Directory.models import Directory
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	mail = models.EmailField(blank=False)
	birth_date = models.DateField(null=False, blank=False, default=date.today)
	location = models.CharField(max_length=100, blank=True)
	MALE = 'M'
	FEMALE = 'F'
	OTHERS = 'O'
	GENDER_CHOICES = [
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(OTHERS, 'Others'),
	]
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
	root_directory = models.OneToOneField(Directory, on_delete=models.CASCADE, null=True)
