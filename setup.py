#! /usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup
import os.path

setup(name='startup_asgard_app',
      version='0.1.0',
      description='startup_asgard_app',
      author='Nicolas Vanhoren',
      author_email='nicolas.vanhoren@unknown.com',
      url='http://nowhere.com',
      py_modules = [],
      packages=[],
      scripts=[],
      long_description="",
      keywords="",
      license="none",
      classifiers=[
          ],
      install_requires=[
        'argparse',
        'gevent',
        'asgard',
        ],
     )

