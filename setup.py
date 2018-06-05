#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from django_article import settings

import os

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.rst'))
long_description = f.read().strip()
f.close()

setup(
    name='django-article',
    version=settings.VERSION,
    author='Noah Wang',
    author_email='234082230@qq.com',
    url='http://github.com/noahzaozao/django-article',
    description='Django aritcle app!',
    packages=find_packages(),
    long_description=long_description,
    keywords='django',
    zip_safe=False,
    install_requires=[
        'six',
        'Django>=1.10.0'
    ],
    test_suite='django_common.tests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
