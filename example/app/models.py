from django.db import models
from django_countries.fields import CountryField

GENDERS = (
	("female", "Female"),
	("male", "Male"),
	("other", "Other")
)

# Create your models here.
class Friend(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=100, choices=GENDERS)
	age = models.IntegerField()
	birthday = models.DateField()
	country = CountryField()
	check = models.BooleanField()
