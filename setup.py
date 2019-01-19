try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Cucumber for Data (cuke4data)',
  'author': 'Iñigo Gonzalez',
  'url': 'https://github.com/igponce/cuke4data',
  'download_url': 'https://github.com/igponce/cuke4data',
  'author_email': 'inigo@syntetic.us',
  'install_requires': [ ],
  'packages': ['cuke4data'],
  'scripts': [],
  'name': 'cuke4data'
}

setup (**config)

