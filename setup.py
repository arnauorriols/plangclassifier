#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(name='plangclassifier',
      version="1.0.0",
      keywords=('detect', 'programming', 'language', 'classifier', 'Bayesian'),
      description='Programming language Classifier',
      long_description='Detect probability of programming language of a string snippet',
      license='New BSD',

      url='https://github.com/arnauorriols/plangclassifier',
      author='orriols',
      packages=['plangclassifier'],
      package_data={
          'plangclassifier': ['samples.json']
      },
      platforms='any',
      install_requires=['scanner==0.0.5'],
      classifiers=[])
