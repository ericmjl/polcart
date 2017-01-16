#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as req_file:
    requirements = req_file.read()

with open('test_requirements.txt') as testreq_file:
    test_requirements = testreq_file.read()

setup(
    name='polcart',
    version='2017.01.16.14.45',
    description="A small utility for converting between polar\
and cartesian units.",
    long_description=readme,
    author="Eric J. Ma",
    author_email='ericmajinglong@gmail.com',
    url='https://github.com/ericmjl/polcart',
    packages=[
        'polcart',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='geometry, math, polar coordinates, cartesian coordinates',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
