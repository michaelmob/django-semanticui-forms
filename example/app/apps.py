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
			Friend.objects.get_or_create(first_name="Michael", last_name="1", age=22)
			Friend.objects.get_or_create(first_name="Joe", last_name="2", age=21)
			Friend.objects.get_or_create(first_name="Bill", last_name="3", age=20)
		except:
			pass