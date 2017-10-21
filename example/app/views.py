from django.shortcuts import render
from .forms import *
from .models import Friend


# Create your views here.
def example_form(request, template="form.html"):
	form = ExampleForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "form.html", {
		"form": form
	})


def example_modelform(request):
	obj = Friend.objects.filter(first_name="Jane").last()

	form = ExampleModelForm(request.POST or None, instance=obj)

	if obj:
		print(type(obj.gender))
		print(obj.gender)

	if request.POST and form.is_valid():
		value = form.save()
	else:
		print(form.errors.as_data())

	return render(request, "modelform.html", {
		"form": form
	})


def example_manyfieldsform(request):
	form = ManyFieldsExampleForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "manyfieldsform.html", {
		"form": form
	})


def example_choicefieldsform(request):
	form = ExampleChoiceForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "choicefieldsform.html", {
		"form": form
	})


def example_layoutform(request):
	form = ExampleLayoutForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "layoutform.html", {
		"form": form
	})