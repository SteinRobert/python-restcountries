from distutils.core import setup

from setuptools import find_packages

from restcountries import __version__

setup(
    name='python-restcountries',
    version=__version__,
    author='Robert Stein',
    author_email='robert@blueshoe.de',
    url='https://github.com/SteinRobert/python-restcountries',
    download_url='https://github.com/SteinRobert/python-restcountries/tarball/{}'.format(__version__),
    packages=find_packages(),
    dependencies=['future', 'requests'],
    description='Python API Wrapper for restcountries.eu',
    license='Unlicense',
    keywords=['api', 'wrapper', 'country', 'countries'],
    install_requires=[
        'requests',
        'future'
    ],
    long_description=open('README.rst').read()
)