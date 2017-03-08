#!/usr/bin/python3
# python setup.py sdist upload -r pypi
from setuptools import setup, find_packages

setup(
	name="django-semanticui-forms",
	version=str("1.5.2"),
	description="Effortlessly style all of your Django forms and form fields with Semantic UI wrappers.",
	author="Michael",
	author_email="thetarkus@users.noreply.github.com",
	url="https://github.com/thetarkus/django-semanticui-forms",
	install_requires=["django>=1.8"],
	packages=find_packages()
)
