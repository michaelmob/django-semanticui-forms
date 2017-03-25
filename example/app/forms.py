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
	hiddeninput = forms.CharField(widget=forms.HiddenInput())
	multiplehiddeninput = forms.MultipleChoiceField(widget=forms.MultipleHiddenInput, choices=CONTINENTS)
	modelchoicefield = forms.ModelChoiceField(queryset=Friend.objects.all(), empty_label="Empty Space", to_field_name="first_name")
	modelmultiplechoicefield = forms.ModelMultipleChoiceField(queryset=Friend.objects.all())
	booleanfield = forms.BooleanField(label="BooleanField")
	charfield = forms.CharField(label="CharField")
	choicefield = forms.ChoiceField(label="ChoiceField", choices=CONTINENTS)
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
	first_name = forms.CharField(max_length=100, help_text="Your first name (form).")
	last_name = forms.CharField(max_length=100)
	billing_address = forms.CharField(max_length=100)
	continent = forms.ChoiceField(choices=CONTINENTS)
	file = forms.FileField(label="Upload Your File", widget=forms.FileInput)
	agree = forms.BooleanField(label="Agree to do whatever")
	gender = forms.ChoiceField(choices=ICON_GENDERS,
		widget=forms.Select(attrs={"_override": "IconSelect"})
	)


	def clean(self):
		self.add_error("agree", "Error!")
		self.add_error("first_name", "Houston, we've had a problem.")



class ExampleModelForm(forms.ModelForm):
	class Meta:
		model = Friend
		fields = ["first_name", "last_name", "gender", "age", "birthday", "country", "check", "friends"]


	def __init__(self, *args, **kwargs):
		super(__class__, self).__init__(*args, **kwargs)
		self.fields["gender"].empty_label = "Who Knows?"