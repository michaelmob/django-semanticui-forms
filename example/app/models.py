from django.db import models
from django_countries.fields import CountryField


GENDERS = (
	("female", "Female"),
	("male", "Male"),
	("other", "Other")
)


CHOICES_1 = (
	(0, "Zero"),
	(1, "One"),
	(2, "Two"),
	(3, "Three"),
	(4, "Four"), 
	(5, "Five"),
)


CHOICES_2 = (
	("", "Empty"),
	(0, "Zero"),
	(1, "One"),
	(2, "Two"),
	(3, "Three"),
	(4, "Four"),
	(5, "Five"),
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



class Choice(models.Model):
	# choices_1_* has no item with "" as a value, therefore an HTML placeholder
	# will be shown unless an `empty_label` is specified  // check out forms.py
	choices_1_1 = models.IntegerField(choices=CHOICES_1)
	choices_1_2 = models.IntegerField(choices=CHOICES_1, null=True, blank=True)
	
	# choices_2_* contain an item with "" as the value, therefore Django selects
	# this one as the active item
	choices_2_1 = models.IntegerField(choices=CHOICES_2)
	choices_2_2 = models.IntegerField(choices=CHOICES_2, null=True, blank=True)