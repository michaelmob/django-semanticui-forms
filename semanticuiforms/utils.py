from django.db.models.fields import BLANK_CHOICE_DASH


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
	Find choices of a field, whether it has choices or has a queryset.

	Args:
		field (BoundField): Django form boundfield

	Returns:
		list: List of choices
	"""
	empty_label = getattr(field.field, "empty_label", None)
	if empty_label and empty_label != BLANK_CHOICE_DASH[0][1]:
		choices = [("", field.field.empty_label)]
	else:
		choices = []

	# Data is the choices
	if hasattr(field.field, "_choices"):
		choices += field.field._choices

	# Data is a queryset
	elif hasattr(field.field, "_queryset"):
		queryset = field.field._queryset
		field_name = getattr(field.field, "to_field_name") or "pk"
		choices += ((getattr(obj, field_name), str(obj)) for obj in queryset)

	return choices