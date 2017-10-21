import importlib
import json
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
	"""
	Basic SemanticUI validation generator for Django forms.
	"""
	help = "Output SemanticUI validation for a form"

	beginning_wrap = "$(\".ui.%s.form\").form({\n\tfields:"
	ending_wrap = "});"


	def add_arguments(self, parser):
		parser.add_argument("form", nargs="+", type=str, help="Absolute path of form class")
		parser.add_argument("--shorthand", action="store_true", help="Use shorthand version")


	def handle(self, *args, **options):
		path = str("".join(options["form"])).split(".")
		klass = getattr(importlib.import_module(".".join(path[:-1])), path[-1])

		form = klass()
		fields = {}
		
		# Loop over each field and create a base and then add rules to it
		for key, field in form.fields.items():
			fields[key] = {
				"identifier": key,
				"rules": []
			}

			# Required
			if field.required:
				fields[key]["rules"].append({
					"type": "checked" if type(field).__name__ == "BooleanField" else "empty",
					"prompt": str(field.error_messages["required"]),
				})

			# Max Length
			if field.error_messages.get("max_length") and getattr(field, "max_length"):
				fields[key]["rules"].append({
					"type": "maxLength[%s]" % getattr(field, "max_length"),
					"prompt": str(field.error_messages["max_length"]),
				})

			# Min Length
			if field.error_messages.get("min_length") and getattr(field, "min_length"):
				fields[key]["rules"].append({
					"type": "minLength[%s]" % getattr(field, "min_length"),
					"prompt": str(field.error_messages["min_length"]),
				})

		# Create shorthand field
		if options.get("shorthand"):
			shorthand_fields = {}

			for key, value in fields.items():
				for rule in value["rules"]:
					if not shorthand_fields.get(key):
						shorthand_fields[key] = []
					shorthand_fields[key].append(rule["type"])

				# 
				if len(shorthand_fields[key]) < 2:
					shorthand_fields[key] = shorthand_fields[key][0]

			fields = shorthand_fields

		# Data
		data = json.dumps(fields, sort_keys=True, indent="\t", separators=(',', ': '))

		# Output
		self.stdout.write(self.beginning_wrap % form.__class__.__name__.lower())
		for line in data.splitlines():
			self.stdout.write("\t" + line);
		self.stdout.write(self.ending_wrap)