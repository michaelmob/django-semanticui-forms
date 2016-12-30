from django import forms
from django.test import TestCase
from .templatetags.semanticui import render_field, render_form



class CharFieldTestCase(TestCase):
	"""
	CharField is a generic field meaning that anything that passes on this
	field would also pass on any other field
	"""

	def setUp(self):
		"""
		Set up testing environment.
		"""
		class Form(forms.Form):
			charfield1 = forms.CharField()
			charfield2 = forms.CharField(widget=forms.TextInput(attrs={
				"value": "Testing",
				"_no_label": True
			}))

		self.form = Form()


	def test_renders(self):
		"""
		Test that HTML component is rendered.
		"""
		html = render_field(self.form["charfield1"])

		self.assertTrue("required field" in html)
		self.assertTrue("label" in html)
		self.assertTrue("charfield" in html)


	def test_overrides(self):
		"""
		Test that widget attrs override arguments.
		"""
		html = render_field(self.form["charfield2"], value="Bad!")

		# Widget's attribute should prioritize over argument in render_field
		self.assertTrue("Testing" in html)
		self.assertFalse("Bad!" in html)


	def test_attributes(self):
		"""
		Test that custom and private attributes are set.
		"""
		html = render_field(
			self.form["charfield2"],
			value="Bad!", placeholder="I am the placeholder!"
		)

		# No label should be present, because "_no_label" attribute
		self.assertFalse("label" in html)

		# Placeholder should be present in form
		self.assertTrue("I am the placeholder!" in html)


	def test_icon(self):
		"""
		Test that icon is added to field.
		"""
		html = render_field(
			self.form["charfield1"], _icon="star", _align="left"
		)

		# Should contain star and left, for a star icon that is left aligned
		# to the field
		self.assertTrue("star" in html)
		self.assertTrue("left" in html)



class ChoiceFieldTestCase(TestCase):
	"""
	ChoiceField is different than a CharField and must be tested.
	"""

	def setUp(self):
		"""
		Set up testing environment.
		"""
		class Form(forms.Form):
			choicefield1 = forms.ChoiceField(choices=(
				("male", "Male"),
				("female", "Female"),
				("other", "Other")
			))
			choicefield2 = forms.ChoiceField(initial="female", choices=(
				("male", "Male|man"),
				("female", "Female|woman"),
				("other", "Other|genderless")
			))
			choicefield3 = forms.ChoiceField(choices=(
				("Yes", "Yes"),
				("No", "No"),
			))

		self.form = Form()


	def test_initial(self):
		"""
		Test that an initial value is set.
		"""
		# From widget attributes, "female" should be set as initial
		html = render_field(self.form["choicefield2"])
		self.assertTrue(" value=\"female\"" in html)

		# From custom arguments, "other" should be set as initial
		html = render_field(self.form["choicefield1"], value="other")
		self.assertTrue(" value=\"other\"" in html)

		# No initial value, value should be an empty string
		html = render_field(self.form["choicefield3"],)
		self.assertTrue(" value=\"\"" in html)


	def test_icon_dropdown(self):
		"""
		Test that icons are next to values in dropdown.
		"""
		html = render_field(
			self.form["choicefield2"], _override="IconChoiceField")
		self.assertTrue(" class=\"woman icon\"" in html)
