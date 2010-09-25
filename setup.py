#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name = 'django-clean',
      version = 1.0,
      description = 'Clean out .pyc files in a django app.',
      author = 'Ash Christopher',
      author_email = 'ash.christopher@gmail.com',
      url = 'http://github.com/ashchristopher/django-clean',
      py_modules = ['clean'],
      keywords = "django clean pyc",
      classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: Linux/Unix',
        'Programming Language :: Python',
        'Topic :: Software Development',
      ]
    )