from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rudp',
    packages=find_packages(),

    version='1.0.3',

    license='MIT',

    install_requires=[],

    author='reeve0930',
    author_email='reeve0930@gmail.com',

    url='https://github.com/reeve0930/rudp',

    description='Send and receive message simply by UDP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='rudp RUDP UDP socket', 

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)