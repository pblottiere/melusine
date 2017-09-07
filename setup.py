#!/usr/bin/env python

PROJECT = 'melusine'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Melusine',
    long_description=long_description,

    author='Paul blottiere',
    author_email='paul.blottiere@gmail.com',

    url='https://github.com/pblottiere/melusine',
    download_url='https://github.com/pblottiere/melusine/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=[''],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'melusine = melusine.main:main'
        ],
        'melusine': [
            'simple = melusine.simple:Simple',
        ],
    },

    zip_safe=False,
)
