#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is included so that you can cythonise the data helper functions
# manually, if installation through pip fails and/or you're doing a 
# non-standard installation. If this is you, run this file using the following
# command in a terminal or command prompt. Note that you may have to change 
# `python3` to the alias for python on your system (e.g. `python` or `py`).
#
# python3 setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(name='data_helper_functions', \
    ext_modules=cythonize("data_helper_functions.pyx"))

