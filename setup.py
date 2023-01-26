from setuptools import setup, find_packages

long_description="Endpoint json: http://hostip:8080/api/info \
  Endpoint to get service status: http://hostip:8080/  (Online if OK) \
  Author: Erik Lonroth erik.lonroth@gmail.com"


version = "0.2"

setup(name='microsample',
      version=version,
      py_modules=['server'],
       entry_points={
        'console_scripts': ['start-server=server:main']
    }
      )
