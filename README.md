python-restcountries
====================
------
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/SteinRobert/python-restcountries/badge.svg?branch=master)](https://coveralls.io/github/SteinRobert/python-restcountries?branch=master)
[![PyPI version](https://badge.fury.io/py/python-restcountries.svg)](https://badge.fury.io/py/python-restcountries)

This is a simple python wrapper for the API of [http://restcountries.eu](http://restcountries.eu).
If there are any issues, please use this repository to contact me about it.

Installation
------------
```shell
pip install python-restcountries
```


Usage
-----
Just import the API Wrapper and start using it!::
```python
# v1 from restcountries import RestCountryApi as rapi
from restcountries import RestCountryApiV2 as rapi

def foo(name):
    country_list = rapi.get_countries_by_name('France')
```



Response filtering
------------------
Pass filters as a keyword argument to any of RestCountryApiV2 or RestCountryApi methods,
this filters the response returned by the api. Thus the Country Object will only contain the attributes in the
filters list.
```python
# v1 from restcountries import RestCountryApi as rapi
from restcountries import RestCountryApiV2 as rapi

def foo(name):
    country_list = rapi.get_countries_by_name("France" ,filters=["name","currencies","capital"])
```


Attributes that can be passed in the filters list.
-------------------------------------------------
- topLevelDomain
- alpha2Code
- alpha3Code
- currencies
- capital
- callingCodes
- altSpellings
- relevance
- region
- subregion
- translations
- population
- latlng
- demonym
- area
- gini
- timezones
- borders
- nativeName
- name
- numericCode
- languages
- flag
- regionalBlocs
- cioc



The Country object
------------------
The API returns Country objects or a list of Country objects. Through the country objects one is able to
access following attributes.
```python
country = country_list[0]
print(country.name)
France
```
- top_level_domain
- alpha2_code
- alpha3_code
- currencies
- capital
- calling_codes
- alt_spellings
- relevance
- region
- subregion
- translations
- population
- latlng
- demonym
- area
- gini
- timezones
- borders
- native_name
- name
- numeric_code
- languages
- flag
- regional_blocs
- cioc
