#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'requests>=2.19.1',
    'Pillow>=5.3.0',
    'tqdm>=4.26.0'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="German Bourdin",
    author_email='german.bourdin@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Downloads documents from turecibo.com as PDF",
    entry_points={
        'console_scripts': [
            'turecibo_downloader=turecibo_downloader.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='turecibo_downloader',
    name='turecibo_downloader',
    packages=find_packages(include=['turecibo_downloader']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gbourdin/turecibo_downloader',
    version='0.1.0',
    zip_safe=False,
)
