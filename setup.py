from setuptools import setup, find_packages

long_description="Endpoint json: http://hostip:8080/api/info \
  Endpoint to get service status: http://hostip:8080/  (Online if OK) \
  Author: Erik Lonroth erik.lonroth@gmail.com"

setup(name='microsample',
      version='0.1',
      py_modules=['server'],
      )
