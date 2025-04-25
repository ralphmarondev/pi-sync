#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__name__), '../src/files/'))

import pyfingerprint

project = u'PyFingerprint'
master_doc = 'index'
author = 'Bastian Raschke <bastian.raschke@posteo.de>'
copyright = '2014-{}, {}'.format(datetime.date.today().year, author)
version = pyfingerprint.__version__
release = version
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]
extensions = [
    'sphinx.ext.napoleon',
]
autoclass_content = "both"
autodoc_mock_imports = ["serial"]
html_theme = "sphinx_rtd_theme"
