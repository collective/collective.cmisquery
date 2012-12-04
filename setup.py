# Copyright (c) 2012 Vlaamse Overheid. All rights reserved.
# See also LICENSE.txt

import os, sys
from setuptools import setup, find_packages

version = '1.0dev'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('docs/HISTORY.txt')
    )
requires = [
    "setuptools",
    "Products.ATReferenceBrowserWidget",
    "collective.cmisbrowser"
    ]

tests_requires = [
    "Products.PloneTestCase"
    ]

setup(name='collective.cmisquery',
      version=version,
      description="CMIS repository query for Plone",
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        ],
      keywords='CMIS connection query browser plone',
      author='Sylvain Viollon',
      author_email='sylvain@infrae.com',
      url='http://pypi.python.org/pypi/collective.cmisquery',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require = tests_requires,
      extras_require = {'test': tests_requires},
      )
