#!/usr/bin/env python
from distutils.core import setup

setup(
    name='BooksMe',
    version='1.0',
    description='Book system recommendation that depending on the purchases we recommend the best products for you on oru system.',
    author='Jorge Ferreiro',
    author_email='me@jgferreiro.com',
    url='http://www.jgferreiro.com',
    packages=[''],
    requires = (
            'algorithms'
    )
    #packages=['algorithms.sorting'],
)
