# -*- coding: utf-8 -*-
""" django-datatables setup.py script """

# django-datatables

# system
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from os.path import join, dirname


setup(
    name="django-datatables",
    version='0.1.0',
    description='django-datatables',
    author='royendgel',
    author_email='royendgel@gmail.com',
    packages=['django-datatables','django-datatables.test'],
    url='https://github.com/royendgel/django-datatables',
    long_description=open('README.txt').read(),
    install_requires=[''],
    test_suite='django-datatables.test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
      ],
)
