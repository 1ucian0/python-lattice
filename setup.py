# -*- coding:utf-8 -*-
from distutils.core import setup

setup(
    name = 'python-lattice',
    version = '0.0.1',
    author = 'Luciano Bello',
    author_email = 'luciano (a) debian (*) org',
    py_modules = ['lattice'],
    url = 'https://code.google.com/p/python-lattice/',
    license = 'LICENSE.txt',
    description = 'Python library to operate elements of a finite lattice',
    long_description = open('README').read(),
)
