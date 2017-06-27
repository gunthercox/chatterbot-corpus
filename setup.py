#!/usr/bin/env python
"""
Setup file for chatterbot-corpus.
"""
from setuptools import setup


# Dynamically retrieve the version information from the chatterbot module
CORPUS = __import__('chatterbot_corpus')
VERSION = CORPUS.__version__
AUTHOR = CORPUS.__author__
AUTHOR_EMAIL = CORPUS.__email__
URL = CORPUS.__url__
DESCRIPTION = CORPUS.__doc__

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='chatterbot-corpus',
    version=VERSION,
    url=URL,
    download_url='{}/tarball/{}'.format(URL, VERSION),
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='readme.md',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=[
        'chatterbot_corpus',
    ],
    install_requires=REQUIREMENTS,
    package_dir={'chatterbot_corpus': 'chatterbot_corpus'},
    include_package_data=True,
    license='BSD',
    zip_safe=False,
    platforms=['any'],
    keywords=['chatterbot', 'dialog', 'language', 'corpus'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
