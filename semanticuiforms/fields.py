from django.utils.html import format_html, format_html_join, escape
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt

from . import wrappers
from .utils import pad, get_choices, get_placeholder_text


def render_charfield(field, attrs):
	"""
	Render the generic CharField.
	"""
	return field


def render_hiddenfield(field, attrs):
	"""
	Return input as a hidden field.
	"""
	if not "_no_wrapper" in attrs:
		attrs["_no_wrapper"] = 1
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
	attrs.setdefault("_no_label", True)  # No normal label for booleanfields
	attrs.setdefault("_inline", True)  # Checkbox should be inline
	field.field.widget.attrs["style"] = "display:hidden"  # Hidden field

	return wrappers.CHECKBOX_WRAPPER % {
		"style": pad(attrs.get("_style", "")),
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
		choices = format_html_join("", wrappers.CHOICE_TEMPLATE, get_choices(field))

	# Accessing the widget attrs directly saves them for a new use after
	# a POST request
	field.field.widget.attrs["value"] = field.value() or attrs.get("value", "")

	return wrappers.DROPDOWN_WRAPPER % {
		"name": field.html_name,
		"attrs": pad(flatatt(field.field.widget.attrs)),
		"placeholder": attrs.get("placeholder") or get_placeholder_text(),
		"style": pad(attrs.get("_style", "")),
		"icon": format_html(wrappers.ICON_TEMPLATE, attrs.get("_dropdown_icon") or "dropdown"),
		"choices": choices
	}


def render_iconchoicefield(field, attrs):
	"""
	Render a ChoiceField with icon support; where the value is split by a pipe
	(|): first element being the value, last element is the icon.
	"""
	choices = ""

	# Loop over every choice to manipulate
	for choice in field.field._choices:
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
		for k, v in field.field._choices[1:])

	# Render a `ChoiceField` with all countries
	return render_choicefield(
		field, attrs, format_html_join("", wrappers.COUNTRY_TEMPLATE, choices)
	)


def render_multiplechoicefield(field, attrs, choices=None):
	"""
	MultipleChoiceField uses its own field, but also uses a queryset.
	"""
	choices = format_html_join("", wrappers.CHOICE_TEMPLATE, get_choices(field))
	return wrappers.MULTIPLE_DROPDOWN_WRAPPER % {
		"name": field.html_name,
		"field": field,
		"choices": choices,
		"placeholder": attrs.get("placeholder") or get_placeholder_text(),
		"style": pad(attrs.get("_style", "")),
		"icon": format_html(wrappers.ICON_TEMPLATE, attrs.get("_dropdown_icon") or "dropdown"),
	}


def render_datefield(field, attrs, style="date"):
	"""
	DateField that uses wrappers.CALENDAR_WRAPPER.
	"""
	return wrappers.CALENDAR_WRAPPER % {
		"field": field,
		"style": pad(style),
		"align": pad(attrs.get("_align", "")),
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


def render_filefield(field, attrs):
	"""
	Render a typical File Field.
	"""
	field.field.widget.attrs["style"] = "display:none"

	if not "_no_label" in attrs:
		attrs["_no_label"] = True

	return wrappers.FILE_WRAPPER % {
		"field": field,
		"id": "id_" + field.name,
		"style": pad(attrs.get("_style", "")),
		"text": escape(attrs.get("_text", "Select File")),
		"icon": format_html(wrappers.ICON_TEMPLATE, attrs.get("_icon", "file outline"))
	}


FIELDS = {
	# Generic Fields
	None: render_charfield,

	# Character Fields
	"TextInput": render_charfield,

	# Hidden Fields
	"HiddenInput": render_hiddenfield,
	"MultipleHiddenInput": render_hiddenfield, 

	# Boolean Fields
	"CheckboxInput": render_booleanfield,
	"NullBooleanSelect": render_nullbooleanfield,

	# Choice Fields
	"Select": render_choicefield,
	"IconSelect": render_iconchoicefield,
	"SelectMultiple": render_multiplechoicefield,
	"CountrySelect": render_countryfield,

	# Date/Time Fields
	"TimeInput": render_timefield,
	"DateInput": render_datefield,
	"DateTimeInput": render_datetimefield,

	# File Fields
	"FileInput": render_filefield,
}