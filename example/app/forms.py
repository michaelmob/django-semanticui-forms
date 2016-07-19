from django import forms
from .models import Friend

CONTINENTS = (
	("af", "Africa"),
	("as", "Asia"),
	("au", "Australia"),
	("eu", "Europe"),
	("na", "North America"),
	("sa", "South America")
)

ICON_GENDERS = (
	("m", "Male|woman"),
	("f", "Female|man"),
	("o", "Other|genderless"),
)

class ManyFieldsExampleForm(forms.Form):
	 booleanfield = forms.BooleanField(label="BooleanField")
	 charfield = forms.CharField(label="CharField")
	 choicefield = forms.ChoiceField(label="ChoiceField")
	 typedchoicefield = forms.TypedChoiceField(label="TypedChoiceField")
	 datefield = forms.DateField(label="DateField")
	 datetimefield = forms.DateTimeField(label="DateTimeField")
	 decimalfield = forms.DecimalField(label="DecimalField")
	 durationfield = forms.DurationField(label="DurationField")
	 emailfield = forms.EmailField(label="EmailField")
	 filefield = forms.FileField(label="FileField")
	 filepathfield = forms.FilePathField(label="FilePathField", path="/")
	 floatfield = forms.FloatField(label="FloatField")
	 imagefield = forms.ImageField(label="ImageField")
	 integerfield = forms.IntegerField(label="IntegerField")
	 genericipaddressfield = forms.GenericIPAddressField(label="GenericIPAddressField")
	 multiplechoicefield = forms.MultipleChoiceField(label="MultipleChoiceField", choices=CONTINENTS)
	 typedmultiplechoicefield = forms.TypedMultipleChoiceField(label="TypedMultipleChoiceField", choices=CONTINENTS)
	 nullbooleanfield = forms.NullBooleanField(label="NullBooleanField")
	 slugfield = forms.SlugField(label="SlugField")
	 timefield = forms.TimeField(label="TimeField")
	 urlfield = forms.URLField(label="URLField")
	 uuidfield = forms.UUIDField(label="UUIDField")



class ExampleForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	billing_address = forms.CharField(max_length=100)
	continent = forms.ChoiceField(choices=CONTINENTS)
	agree = forms.BooleanField(label="Agree to do whatever")
	gender = forms.ChoiceField(choices=ICON_GENDERS,
		widget=forms.Select(attrs={ "_override": "IconChoiceField" })
	)


class ExampleModelForm(forms.ModelForm):
	class Meta:
		model = Friend
		fields = ["first_name", "last_name", "gender", "age", "birthday", "country", "check"]
