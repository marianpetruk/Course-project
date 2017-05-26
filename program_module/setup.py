# setup.py
from distutils.core import setup


setup(name = "project",
      version = "1.0",
      py_modules = ['adt'],
      packages = ['ADT', 'examples', 'docs'],
      scripts = ['main.py'],
      )
