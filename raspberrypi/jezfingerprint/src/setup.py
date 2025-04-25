#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import sys
sys.path.insert(0, './files/')

import pyfingerprint

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name            = 'pyfingerprint',
    version         = pyfingerprint.__version__,
    author          = 'Bastian Raschke',
    author_email    = 'bastian.raschke@posteo.de',
    maintainer      = 'Philipp Meisberger',
    maintainer_email= 'team@pm-codeworks.de',
    description     = 'Python written library for using ZhianTec fingerprint sensors.',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url             = 'https://github.com/bastianraschke/pyfingerprint',
    license         = 'D-FSL',
    package_dir     = {'': 'files'},
    packages        = ['pyfingerprint'],
    install_requires= [
        'pyserial',
        'Pillow'
    ],
    classifiers     = [
        'Development Status :: 5 - Production/Stable'
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Terminals :: Serial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
