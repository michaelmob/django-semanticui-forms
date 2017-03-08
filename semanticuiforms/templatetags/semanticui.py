from django import template
from django.utils.html import format_html, escape
from django.utils.safestring import mark_safe

from ..wrappers import *
from ..utils import valid_padding
from ..fields import FIELDS

register = template.Library()


@register.simple_tag
def render_field(field, **kwargs):
	"""Render field in a Semantic UI wrapper

	Args:
		field (BoundField): Form field
		**kwargs (dict): Keyword arguments to add onto field

	Returns:
		string: HTML code for field
	"""
	try:  # Make sure field is valid
		field.field
	except:
		return

	# Save old dict in variable before recreating a new one, deepcopy not needed
	field_widget_attrs = field.field.widget.attrs

	# Override kwargs (attrs) with widget's attrs
	kwargs.update(field.field.widget.attrs)

	# Recreate widget attrs to include the ones from the template
	# Note: Widget attrs defined in the form class have priority
	field.field.widget.attrs = {
		k: v for k, v in kwargs.items() if k[:1] != "_"
	}

	# Values for field wrapper
	input_ = kwargs.get("_override", field.field.widget.__class__.__name__)
	values = {
		"class": "",
		"label": "",
		"errors": "",
		"help": "",
		"field": str(FIELDS.get(input_, FIELDS["_"])(field, kwargs))
	}

	# Return form field without wrapper
	if kwargs.get("_no_wrapper"):
		return values["field"]

	# Label tag
	if field.label and not kwargs.get("_no_label"):
		values["label"] += format_html(
			LABEL_TEMPLATE, field.html_name, mark_safe(field.label)
		)

	# Custom field classes on field wrapper
	if kwargs.get("_field_class"):
		values["class"] += escape(str(kwargs.get("_field_class"))) + " "

	# Inline class on field wrapper
	if kwargs.get("_inline"):
		values["class"] += "inline "

	# Required class on field wrapper
	if field.field.required and not kwargs.get("_no_required"):
		values["class"] += "required "

	# Error class on field wrapper
	if field.errors and not kwargs.get("_no_errors"):
		values["class"] += "error "

		# Add field errors to `error` element in `values`
		for error in field.errors:
			values["errors"] += ERROR_WRAPPER % {"message": error}

	# Add help_text to field's html
	if field.help_text and kwargs.get("_help"):
		values["help"] = HELP_TEMPLATE.format(field.help_text)

	# Wrap field wrapper with input wrapper; unofficial calendar has quirks
	if kwargs.get("_icon") and (not "Date" in field.field.__class__.__name__):
		values["field"] = INPUT_WRAPPER % {
			"field": values["field"],
			"help": values["help"], 
			"style": "%sicon " % escape(valid_padding(kwargs.get("_align", ""))),
			"icon": format_html(ICON_TEMPLATE, kwargs.get("_icon")),
		}

	# Restore widget attributes to widget
	field.field.widget.attrs = field_widget_attrs

	return mark_safe(FIELD_WRAPPER % values)


@register.simple_tag()
def render_form(formset, exclude=None, **kwargs):
	"""Render an entire form with Semantic UI wrappers for each field
	
	Args:
	    formset (formset): Django Form
	    exclude (string): exclude fields by name, separated by commas
	    kwargs (dict): other attributes will be passed to fields
	
	Returns:
	    string: HTML of Django Form fields with Semantic UI wrappers
	"""
	if exclude:
		exclude = exclude.split(",")
		for field in exclude:
			formset.fields.pop(field)

	return mark_safe("".join([
		render_field(field, **kwargs) for field in formset
	]))
