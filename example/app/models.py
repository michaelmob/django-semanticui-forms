from django.db import models
from django_countries.fields import CountryField


GENDERS = (
	("female", "Female"),
	("male", "Male"),
	("other", "Other")
)



# Create your models here.
class Friend(models.Model):
	first_name = models.CharField(max_length=100, help_text="Your first name (model).")
	last_name = models.CharField(max_length=100, null=True)
	gender = models.CharField(max_length=100, choices=GENDERS, null=True)
	age = models.IntegerField(null=True)
	birthday = models.DateField(null=True)
	country = CountryField(null=True)
	check = models.BooleanField(default=False)
	friends = models.ManyToManyField("Friend")


	def __str__(self):
		return self.first_name