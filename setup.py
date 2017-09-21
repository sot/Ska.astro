# Licensed under a 3-clause BSD style license - see LICENSE.rst
from setuptools import setup
setup(name='Ska.astro',
      author = 'Tom Aldcroft',
      description='Astronomy utilities',
      author_email = 'aldcroft@head.cfa.harvard.edu',
      py_modules = ['Ska.astro'],
      version='3.2.1',
      zip_safe=False,
      packages=['Ska'],
      package_dir={'Ska' : 'Ska'},
      package_data={}
      )
