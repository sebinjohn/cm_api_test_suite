from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cm_api_test_suite',
    version='0.1',
    description='A test suit of cm api',
    long_description=long_description,
    url='https://github.com/sebinjohn/cm_api_test_suite',
    author='Sebin John',
    author_email='sebin.john.sebin@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='cloudera cm_api test suit',
    packages=['mock_cm_api']
)
