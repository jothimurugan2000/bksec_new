# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bksec/__init__.py
from bksec import __version__ as version

setup(
	name='bksec',
	version=version,
	description='Custom DocTypes as required for BKSEC',
	author='B & K Securities',
	author_email='naveen.prabhu@bksec.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
