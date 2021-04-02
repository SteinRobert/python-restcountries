from setuptools import setup, find_packages

from restcountries import __version__

setup(
    name="python-restcountries",
    version=__version__,
    author="Robert Stein",
    author_email="robert@blueshoe.de",
    url="https://github.com/SteinRobert/python-restcountries",
    download_url="https://github.com/SteinRobert/python-restcountries/tarball/{}".format(
        __version__
    ),
    packages=find_packages(),
    dependencies=["future", "requests"],
    description="Python API Wrapper for restcountries.eu",
    license="Unlicense",
    keywords=["api", "wrapper", "country", "countries"],
    install_requires=["requests"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
)
