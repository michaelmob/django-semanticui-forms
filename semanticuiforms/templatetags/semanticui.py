from django import template
from django.utils.html import format_html, escape
from django.utils.safestring import mark_safe

from ..wrappers import *
from ..utils import pad
from ..fields import FIELDS

register = template.Library()



class Field():
	"""
	Semantic UI Form Field.
	"""
	def __init__(self, field, **kwargs):
		"""Initializer for Field class.
		
		Args:
			field (BoundField): Form field
			**kwargs (dict): Field attributes
		"""
		# Kwargs will always be additional attributes
		self.attrs = kwargs
		self.attrs.update(field.field.widget.attrs)

		# Field
		self.field = field
		self.widget = field.field.widget

		# Defaults
		self.values = {"class": [], "label": "", "help": "", "errors": ""}


	def set_input(self):
		"""Returns form input field of Field.
		"""
		name = self.attrs.get("_override", self.widget.__class__.__name__)
		self.values["field"] = str(FIELDS.get(name, FIELDS.get(None))(self.field, self.attrs))


	def set_label(self):
		"""Set label markup.
		"""
		if not self.field.label or self.attrs.get("_no_label"):
			return

		self.values["label"] = format_html(
			LABEL_TEMPLATE, self.field.html_name, mark_safe(self.field.label)
		)


	def set_help(self):
		"""Set help text markup.
		"""
		if not (self.field.help_text and self.attrs.get("_help")):
			return

		self.values["help"] = HELP_TEMPLATE.format(self.field.help_text)


	def set_errors(self):
		"""Set errors markup.
		"""
		if not self.field.errors or self.attrs.get("_no_errors"):
			return
		
		self.values["class"].append("error")

		for error in self.field.errors:
			self.values["errors"] += ERROR_WRAPPER % {"message": error}


	def set_icon(self):
		"""Wrap current field with icon wrapper.
		This setter must be the last setter called.
		"""
		if not self.attrs.get("_icon"):
			return

		if "Date" in self.field.field.__class__.__name__:
			return

		self.values["field"] = INPUT_WRAPPER % {
			"field": self.values["field"],
			"help": self.values["help"], 
			"style": "%sicon " % escape(pad(self.attrs.get("_align", ""))),
			"icon": format_html(ICON_TEMPLATE, self.attrs.get("_icon")),
		}


	def set_classes(self):
		"""Set field properties and custom classes.
		"""
		# Custom field classes on field wrapper
		if self.attrs.get("_field_class"):
			self.values["class"].append(escape(self.attrs.get("_field_class")))

		# Inline class
		if self.attrs.get("_inline"):
			self.values["class"].append("inline")

		# Disabled class
		if self.field.field.disabled:
			self.values["class"].append("disabled")

		# Required class
		if self.field.field.required and not self.attrs.get("_no_required"):
			self.values["class"].append("required")


	def render(self):
		"""Render field as HTML.
		"""
		self.widget.attrs = {
			k: v for k, v in self.attrs.items() if k[0] != "_"
		}
		self.set_input()

		if not self.attrs.get("_no_wrapper"):
			self.set_label()
			self.set_help()
			self.set_errors()
			self.set_classes()
			self.set_icon()  # Must be the bottom-most setter

		self.values["class"] = pad(" ".join(self.values["class"])).lstrip()
		result = mark_safe(FIELD_WRAPPER % self.values)
		self.widget.attrs = self.attrs  # Re-assign variables
		return result



@register.simple_tag
def render_field(field, **kwargs):
	"""Render field in a Semantic UI wrapper

	Args:
		field (BoundField): Form field
		**kwargs (dict): Keyword arguments to add onto field

	Returns:
		string: HTML code for field
	"""
	if field:
		return Field(field, **kwargs).render()


@register.simple_tag()
def render_form(form, exclude=None, **kwargs):
	"""Render an entire form with Semantic UI wrappers for each field
	
	Args:
		form (form): Django Form
		exclude (string): exclude fields by name, separated by commas
		kwargs (dict): other attributes will be passed to fields
	
	Returns:
		string: HTML of Django Form fields with Semantic UI wrappers
	"""
	if hasattr(form, "Meta") and hasattr(form.Meta, "layout"):
		return render_layout_form(form, getattr(form.Meta, "layout"), **kwargs)

	if exclude:
		exclude = exclude.split(",")
		for field in exclude:
			form.fields.pop(field)

	return mark_safe("".join([
		render_field(field, **kwargs) for field in form
	]))


@register.simple_tag()
def render_layout_form(form, layout=None, **kwargs):
	"""Render an entire form with Semantic UI wrappers for each field with
	a layout provided in the template or in the form class
	
	Args:
		form (form): Django Form
		layout (tuple): layout design
		kwargs (dict): other attributes will be passed to fields
	
	Returns:
		string: HTML of Django Form fields with Semantic UI wrappers
	"""
	def make_component(type_, *args):
		"""Loop through tuples to make field wrappers for fields.
		"""
		if type_ == "Text":
			return "".join(args)

		elif type_ == "Field":
			result = ""
			for c in args:
				if isinstance(c, tuple):
					result += make_component(*c)
				elif isinstance(c, str):
					result += render_field(form.__getitem__(c), **kwargs)
			return result
		else:
			if len(args) < 2:
				return ""

			result = "".join([make_component(*c) for c in args])
			if type_:
				return "<div class=\"%s\">%s</div>" % (type_.lower(), result)
			else:
				return result 

	return mark_safe("".join([make_component(*component) for component in layout]))
