=====================
Python Rest Countries
=====================

This is a simple python wrapper for the API of `http://restcountries.eu <http://restcountries.eu>`.
If there are any issues, please use this repository to contact me about it.

Installation
------------

    pip install python-restcountries



Usage
-----
Just import the API Wrapper and start using it!::

    # v1 from restcountries import RestCountryApi as rapi
    from restcountries import RestCountryApiV2 as rapi

    def foo(name):
        country_list = rapi.get_countries_by_name('France')
  

The Country object
------------------
The API returns Country objects or a list of Country objects. Through the country objects one is able to
access following attributes.::

    country = country_list[0]
    print(country.name)
    France

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
