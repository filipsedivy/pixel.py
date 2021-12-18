#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pixel.py',
    version='1.0',
    packages=['pixel'],
    url='https://github.com/filipsedivy/pixel.py',
    license='Apache-2.0 License',
    author='Filip Sedivy',
    author_email='mail@filipsedivy.cz',
    description='Image Data Preprocessing Toolkit',
    long_description=readme,
    long_description_content_type='text/markdown',
    requires=['pillow', 'filetype']
)
