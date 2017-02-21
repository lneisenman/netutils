#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def get_install_requirements(path):
    ''' This function based on code in pyscaffold '''
    with open(path) as requirements:
        content = requirements.read()

    return [req for req in content.splitlines() if req != '']


test_requirements = [
    'pytest', 'pytest-cov', 'coverage'
]

setup(
    name='netutils',
    version='0.1.0',
    description="Python utilities for NEURON network models",
    long_description=readme + '\n\n' + history,
    author="Larry Eisenman",
    author_email='leisenman@wustl.edu',
    url='https://github.com/lneisenman/netutils',
    packages=[
        'netutils',
    ],
    package_dir={'netutils':
                 'netutils'},
    include_package_data=True,
    install_requires=get_install_requirements('requirements.txt'),
    license="BSD license",
    zip_safe=False,
    keywords='netutils',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
