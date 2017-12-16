#!/usr/bin/python3
"""
sudo apt install python3-pip
sudo pip3 install twine

python3 setup.py sdist
twine upload dist/django-semanticui-forms-1.6.5.tar.gz
"""
from setuptools import setup, find_packages

setup(
	name="django-semanticui-forms",
	version=str("1.6.5"),
	description="Effortlessly style all of your Django forms and form fields with Semantic UI wrappers.",
	author="Michael",
	author_email="thetarkus@users.noreply.github.com",
	url="https://github.com/thetarkus/django-semanticui-forms",
	install_requires=["django>=1.8"],
	packages=find_packages()
)
