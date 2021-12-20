#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='pixel.py',
    version='1.0.2',
    packages=['pixel'],
    url='https://github.com/filipsedivy/pixel.py',
    download_url='https://github.com/filipsedivy/pixel.py/tarball/master',
    license='Apache-2.0 License',
    licesne_file='LICENSE',
    author='Filip Sedivy',
    author_email='mail@filipsedivy.cz',
    description='Image Data Preprocessing Toolkit',
    long_description=readme,
    requires=['pillow', 'filetype'],
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'
    ],
    platforms=['any'],
    zip_safe=True
)
