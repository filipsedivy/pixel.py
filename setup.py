from setuptools import setup

setup(
    name='pixel.py',
    version='1.0',
    packages=['pixel'],
    url='https://github.com/filipsedivy/pixel.py',
    license='Apache-2.0 License',
    author='Filip Sedivy',
    author_email='mail@filipsedivy.cz',
    description='Image Data Preprocessing Toolkit',
    requires=['pillow', 'filetype']
)
