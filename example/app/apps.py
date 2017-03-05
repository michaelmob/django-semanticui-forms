from django.apps import AppConfig



class ExampleAppConfig(AppConfig):
	"""
	App config for the Example App.
	"""
	name = "app"


	def ready(self):
		"""
		Create test friends for displaying.
		"""
		from .models import Friend

		# Requires migrations, not necessary
		try:
			Friend.objects.get_or_create(first_name="A", age=18)
			Friend.objects.get_or_create(first_name="B", age=18)
			Friend.objects.get_or_create(first_name="C", age=18)
		except:
			pass