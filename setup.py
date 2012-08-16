from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='ga_log_importer',
      version=version,
      description="Import Varnish logs to Google analytics as page views.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Upfront Systems',
      author_email='rijk@upfrontsystems.co.za',
      url='',
      license='',
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
