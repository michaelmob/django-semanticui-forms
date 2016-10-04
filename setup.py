#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
	name="django-semanticui-forms",
	version=str("1.2"),
	description="django-semanticui-forms",
	author="Michael Tark",
	author_email="theTarkus@users.noreply.github.com",
	url="https://github.com/theTarkus/django-semantic-ui-forms",
	install_requires=["django>=1.8"],
	packages=find_packages()
)
