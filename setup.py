#!/usr/bin/env python
from distutils.core import setup

with open('requirements.txt') as f:
        required = f.read().splitlines()

setup(
    name='ldap_paged_search',
    version='0.1',
    packages=['ldap_paged_search',],
    license='LGPLv2.1',
    long_description=open('README.rst').read(),
    )
