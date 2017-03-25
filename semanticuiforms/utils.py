from django.db.models.fields import BLANK_CHOICE_DASH


def pad(value):
	"""
	Add one space padding around value if value is valid.

	Args:
		value (string): Value

	Returns:
		string: Value with padding if value was valid else one space
	"""
	return " %s " % value if value else " "


def get_choices(field):
	"""
	Find choices of a field, whether it has choices or has a queryset.

	Args:
		field (BoundField): Django form boundfield

	Returns:
		list: List of choices
	"""
	empty_label = getattr(field.field, "empty_label", False)
	choices = []

	# Data is the choices
	if hasattr(field.field, "_choices"):
		choices = field.field._choices

	# Data is a queryset
	elif hasattr(field.field, "_queryset"):
		queryset = field.field._queryset
		field_name = getattr(field.field, "to_field_name") or "pk"
		choices += ((getattr(obj, field_name), str(obj)) for obj in queryset)

	# Remove empty value when
	# field is required and first choice's value is "---------"
	if field.field.required and choices and choices[0][1] == BLANK_CHOICE_DASH[0][1]:
		del choices[0]

	# Add empty value when
	# has empty_label or (the fields not required and has a non-blank first choice)
	if empty_label or (not field.field.required and choices and choices[0][0]):
		choices.insert(0, ("", empty_label or BLANK_CHOICE_DASH[0][1]))

	return choices