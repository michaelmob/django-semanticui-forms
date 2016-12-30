from django import template
from django.utils.html import format_html, escape
from django.utils.safestring import mark_safe

from ..wrappers import (
	FIELD_WRAPPER, ERROR_WRAPPER, INPUT_WRAPPER, LABEL_TEMPLATE, ICON_TEMPLATE
)
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

	# Override kwargs (attrs) with widget's attrs
	kwargs.update(field.field.widget.attrs)

	# Recreate widget attrs to include the ones from the template
	# Note: Widget attrs defined in the form class have priority
	field.field.widget.attrs = {
		k: v for k, v in kwargs.items() if k[:1] != "_"
	}

	# Values for field wrapper
	values = {
		"class": "",
		"label": "",
		"errors": "",
		"field": FIELDS.get(
			kwargs.get("_override", field.field.__class__.__name__), FIELDS["_"]
		)(field, kwargs)
	}

	# Label tag
	if field.label and not kwargs.get("_no_label"):
		values["label"] += format_html(
			LABEL_TEMPLATE, field.html_name, mark_safe(field.label)
		)

	# Required class on field wrapper
	if field.field.required and not kwargs.get("_no_required"):
		values["class"] += "required "

	# Error class on field wrapper
	if field.errors and not kwargs.get("_no_errors"):
		values["class"] += "error "

		# Add field errors to `error` element in `values`
		for error in field.errors:
			values["errors"] += ERROR_WRAPPER % {"message": error}

	# Wrap field wrapper with input wrapper; unofficial calendar has quirks
	if kwargs.get("_icon") and (not "Date" in field.field.__class__.__name__):
		values["field"] = INPUT_WRAPPER % {
			"field": values["field"],
			"style": "%sicon " % escape(valid_padding(kwargs.get("_align", ""))),
			"icon": format_html(ICON_TEMPLATE, kwargs.get("_icon")),
		}

	return mark_safe(FIELD_WRAPPER % values)


@register.simple_tag()
def render_form(formset):
	"""Render an entire form with Semantic UI wrappers for each field
	
	Args:
	    formset (formset): Django Form
	
	Returns:
	    string: HTML of Django Form fields with Semantic UI wrappers
	"""
	return mark_safe("".join([
		render_field(field) for field in formset
	]))
