from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='my_bug_test_2',
    version=version,
    description="None",
    long_description="""\
	""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['the_p'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
)
