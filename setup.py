from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='peters',
      version=version,
      description="Test package",
      long_description="""\
blablabla""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='test',
      author='Test',
      author_email='Test',
      url='test',
      license='test',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
