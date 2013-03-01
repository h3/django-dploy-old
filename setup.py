#!/usr/bin/env python
"""
django-dploy
"""

VERSION = __import__('django_dploy').VERSION

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
   #'simplejson',
   #'GitPython',
   #'PyYAML',
]

setup(
    name='django_dploy',
    version=VERSION,
    author='Maxime Haineault',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-dploy',
    description = 'Django dploy',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    license='BSD',
    install_requires=install_requires,
    dependency_links=[],
   #test_suite='nose.collector',
   #tests_require=['nose', 'nose-cov', 'coverage', 'setuptools', 'distribute'], #'pep8'
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'dploy = django_dploy.client:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
