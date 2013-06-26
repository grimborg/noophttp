#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

curdir = os.path.dirname(os.path.abspath(__file__))

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name = 'noophttp',
    description = 'Serve an empty response on HTTP, for example to block adds',
    long_description = read('README.rst'),
    license = 'http://www.gnu.org/licenses/gpl-2.0.html',
    version = '1.0',
    author = 'Òscar Vilaplana',
    author_email = 'dev@oscarvilaplana.cat',
    url = 'https://github.com/grimborg/noophttp',
    install_requires = ['opster', 'tornado'],
    py_modules = ['noophttp'],
    entry_points = {'console_scripts': ['noophttp=noophttp:start.command', ]},
    )
