from django.shortcuts import render
from .forms import *


# Create your views here.
def example_form(request, template="form.html"):
	form = ExampleForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "form.html", {
		"form": form
	})


def example_modelform(request):
	form = ExampleModelForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

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