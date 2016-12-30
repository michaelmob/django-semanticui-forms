from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt

from . import wrappers
from .utils import valid_padding, remove_blank_choice


def render_charfield(field, attrs):
	"""
	Render the generic CharField.
	"""
	return field


def render_nullbooleanfield(field, attrs):
	"""
	Render NullBooleanField as dropdown. ("Unknown", "Yes", "No")
	"""
	field.field.widget.attrs["class"] = "ui dropdown"
	return field


def render_booleanfield(field, attrs):
	"""
	Render BooleanField with label next to instead of above.
	"""
	attrs["_no_label"] = 1  # No normal label for booleanfields
	return wrappers.CHECKBOX_WRAPPER % {
		"style": valid_padding(attrs.get("_style", "")),
		"field": field,
		"label": format_html(
			wrappers.LABEL_TEMPLATE, field.html_name, mark_safe(field.label)
		)
	}


def render_choicefield(field, attrs, choices=None):
	"""
	Render ChoiceField as 'div' dropdown rather than select for more
	customization.
	"""
	# Allow custom choice list, but if no custom choice list then wrap all
	# choices into the `wrappers.CHOICE_TEMPLATE`
	if not choices:
		choices = format_html_join(
			"", wrappers.CHOICE_TEMPLATE,
			remove_blank_choice(field.field._choices)
		)

	field.field.widget.attrs["value"] = field.value() or attrs.get("value", "")

	return wrappers.DROPDOWN_WRAPPER % {
		"name": field.html_name,
		"attrs": valid_padding(flatatt(field.field.widget.attrs)),
		"placeholder": attrs.get("placeholder", "Select"),
		"style": valid_padding(attrs.get("_style", "")),
		"choices": choices
	}


def render_iconchoicefield(field, attrs):
	"""
	Render a ChoiceField with icon support; where the value is split by a pipe
	(|): first element being the value, last element is the icon.
	"""
	choices = ""

	# Loop over every choice to manipulate
	for choice in remove_blank_choice(field.field._choices):
		value = choice[1].split("|")  # Value|Icon

		# Each choice is formatted with the choice value being split with
		# the "|" as the delimeter. First element is the value, the second
		# is the icon to be used.
		choices += format_html(
			wrappers.ICON_CHOICE_TEMPLATE,
			choice[0],  # Key
			mark_safe(wrappers.ICON_TEMPLATE.format(value[-1])),  # Icon
			value[0]  # Value
		)

	# Render a dropdown field
	return render_choicefield(field, attrs, choices)


def render_countryfield(field, attrs):
	"""
	Render a custom ChoiceField specific for CountryFields.
	"""
	choices = ((k, k.lower(), v)
		for k, v in remove_blank_choice(field.field._choices))

	# Render a `ChoiceField` with all countries
	return render_choicefield(
		field, attrs, format_html_join("", wrappers.COUNTRY_TEMPLATE, choices)
	)


def render_multiplechoicefield(field, attrs):
	"""
	MultipleChoiceField only requires the multiple class to be added.
	"""
	field.field.widget.attrs["class"] = "ui multiple dropdown"
	return field


def render_datefield(field, attrs, style="date"):
	"""
	DateField that uses wrappers.CALENDAR_WRAPPER.
	"""
	return wrappers.CALENDAR_WRAPPER % {
		"field": field,
		"style": valid_padding(style),
		"align": valid_padding(attrs.get("_align", "")),
		"icon": format_html(wrappers.ICON_TEMPLATE, attrs.get("_icon")),
	}


def render_timefield(field, attrs):
	"""
	DateField with 'time' style.
	"""
	return render_datefield(field, attrs, "time")


def render_datetimefield(field, attrs):
	"""
	DateField with 'datetime' style.
	"""
	return render_datefield(field, attrs, "datetime")


FIELDS = {
	# Choice Fields
	"ChoiceField": render_choicefield,
	"TypedChoiceField": render_choicefield,
	"LazyTypedChoiceField": render_choicefield,
	"FilePathField": render_choicefield,

	# Multi-choice Fields
	"MultipleChoiceField": render_multiplechoicefield,
	"TypedMultipleChoiceField": render_multiplechoicefield,

	# Custom-choice fields
	"CountryField": render_countryfield,
	"IconChoiceField": render_iconchoicefield,

	# Boolean Fields
	"NullBooleanField": render_nullbooleanfield,
	"BooleanField": render_booleanfield,

	# Date/time pickers
	"DateField": render_datefield,
	"TimeField": render_timefield,
	"DateTimeField": render_datetimefield,

	# Default
	"_": render_charfield
}
