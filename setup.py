#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='pixel.py',
    version='1.0.1',
    packages=['pixel'],
    url='https://github.com/filipsedivy/pixel.py',
    license='Apache-2.0 License',
    author='Filip Sedivy',
    author_email='mail@filipsedivy.cz',
    description='Image Data Preprocessing Toolkit',
    long_description=readme,
    requires=['pillow', 'filetype'],
    python_requires='>=3',
)
