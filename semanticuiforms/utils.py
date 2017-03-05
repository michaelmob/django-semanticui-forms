from django.db.models.fields import BLANK_CHOICE_DASH


def remove_blank_choice(choices):
	"""
	Remove blank choice from choices for a ChoiceField.

	Args:
		choices (tuple): Tuple of choices; ex: (("key", "value"),)
		lower_key (bool, optional): Set key to lowercase

	Returns:
		tuple: Return tuple of choices with blank choice removed if present
	"""
	if choices and choices[0][1] == BLANK_CHOICE_DASH[0][1]:
		return choices[1:]
	else:
		return choices


def valid_padding(value):
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
	Find choices of a field, whether it's has choices or has a queryset.

	Args:
		field (BoundField): Django form boundfield

	Returns:
		list: List of choices
	"""
	choices = ()
	# Data is the choices
	if hasattr(field.field, "_choices"):
		choices = remove_blank_choice(field.field._choices)

	# Data is a queryset
	elif hasattr(field.field, "_queryset"):
		queryset = field.field._queryset
		field_name = getattr(field.field, "to_field_name") or "pk"
		choices = ((getattr(obj, field_name), str(obj)) for obj in queryset)

	return choices