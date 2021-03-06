from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='peters',
      version=version,
      install_requires=[
      "untangle",
      "requests",
      "dateutil",
      "numpy",
      "pandas"
      ],
      scripts = ['scripts/getting_data.py','scripts/check_repo.py'],
      description="Python Course 2013",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christoph Peters',
      author_email='christoph.peters@scilifelab.se',
      url='https://github.com/pythonkurs/peters',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
