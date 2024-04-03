#! /bin/env python

'''
Unicon Plugin Setup File
------------------------

setup.py is a standard Python packaging mechanism. For more information on how
to write this file, please refer to:
    setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html
    distutils: https://docs.python.org/3/distutils/setupscript.html

'''


import os
from setuptools import setup, find_packages


def read(fname):
    'convenience function to read a file into text'
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(

    # name of your plugin, this will become the package name
    name='unicon-plugin-adva',

    # package version string
    version='1.0',

    # descriptions
    description='Unicon Plugin for ADVA',

    # use README.md as long description
    long_description=read('README.md'),

    # the project's main homepage.
    url='https://developer.cisco.com/site/pyats/',

    # author details
    author="Oli I'Anson",
    author_email='oianson@cisco.com',

    # project licensing
    license='Apache 2.0',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # project keywords
    keywords='pyats unicon plugin connection',

    # project packages
    packages=find_packages(where='src'),

    # project directory
    package_dir={
        '': 'src',
    },

    # additional package data files that goes into the package itself
    package_data={},

    # console entry point
    entry_points={'unicon.plugins': ['adva = unicon_plugin_adva']},

    # package dependencies
    install_requires=['setuptools', 'unicon'],

    # any additional groups of dependencies.
    # install using: $ pip install -e .[dev]
    extras_require={},

    # any data files placed outside this package.
    data_files=[],

    # custom commands for setup.py
    cmdclass={},

    # non zip-safe (never tested it)
    zip_safe=False,
)