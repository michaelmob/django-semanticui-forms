from django import forms
from .models import Friend, Choice


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
	modelchoicefield2 = forms.ModelChoiceField(queryset=Friend.objects.all(), to_field_name="first_name")
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



class ExampleLayoutForm(forms.Form):
	class Meta:
		layout = [
			("Text", "<h4 class=\"ui dividing header\">Personal Details</h4>"),
			("Three Fields",
				("Field", "first_name"),
				("Field", "middle_initial"),
				("Field", "last_name"),
			),

			("Text", "<h4 class=\"ui dividing header\">More Details</h4>"),
			("Inline Fields",
				("Field", "website"),
				("Field", "email"),
			),

			("Text", "<h4 class=\"ui dividing header\">Complicated Details</h4>"),
			("Four Fields",
				("Field", "first_name"),
				("Field", "middle_initial"),
				("Field", "last_name"),
				("Two Fields",
					("Field", "username"),
					("Field", "email"),
				),
			)
		]


	def __init__(self, *args, **kwargs):
		super(__class__, self).__init__(*args, **kwargs)

		placeholders = {
			"first_name": "John",
			"middle_initial": "C",
			"last_name": "Smith",
		}
		
		for key, value in placeholders.items():
			self.fields[key].widget.attrs["placeholder"] = value


	username = forms.CharField()
	first_name = forms.CharField()
	middle_initial = forms.CharField()
	last_name = forms.CharField()
	website = forms.CharField()
	email = forms.EmailField()
	phone_number = forms.CharField()
	helpful = forms.BooleanField()



class ExampleModelForm(forms.ModelForm):
	class Meta:
		model = Friend
		fields = ["first_name", "last_name", "gender", "age", "birthday", "country", "check", "friends"]


	def __init__(self, *args, **kwargs):
		super(__class__, self).__init__(*args, **kwargs)
		self.fields["gender"].empty_label = "Who Knows?"



class ExampleChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		exclude = []


	def __init__(self, *args, **kwargs):
		super(__class__, self).__init__(*args, **kwargs)
		# `empty_label` instead of placeholder
		self.fields["choices_1_2"].empty_label = "Who Knows?"

		# changing the placeholder with no `empty_label`
		self.fields["choices_1_1"].widget.attrs["placeholder"] = "Choose One"

		# `empty_label` when there is an empty ("") choice
		# this will not be set because there is already an empty choice
		self.fields["choices_2_1"].empty_label = "Who Knows?"