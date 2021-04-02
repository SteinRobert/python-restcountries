import requests
import json


class RestCountryApi:
    BASE_URI = "https://restcountries.eu/rest/v1"
    QUERY_SEPARATOR = ","

    @classmethod
    def _get_country_list(cls, resource, term="", filters=None):
        """Takes a resource and a search term and return a list of countries or a country.

        :param resource - resource to create the URL
        :param term - search term provided by the user of this package
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns - either a Country object or a list of Countries
        """
        # create the filter string
        filters_uri_string = ""
        if filters:
            filter_string = cls.QUERY_SEPARATOR.join(filters)
            filters_uri_string = "fields={}".format(filter_string)

        # build uri
        if term and not resource.endswith("="):
            # add the forward slash only when there is a term
            # and it is not specifying the value part of a query string
            term = "/{}".format(term)

        uri = "{}{}{}".format(cls.BASE_URI, resource, term)
        if filters:
            prefix = "?"
            if "?" in uri:
                prefix = "&"
            uri += "{}{}".format(prefix, filters_uri_string)

        response = requests.get(uri)
        if response.status_code == 200:
            result_list = []
            data = json.loads(response.text)  # parse json to dict
            if type(data) == list:
                for (
                    country_data
                ) in (
                    data
                ):  # in case it is a list create python list with country instances
                    country = Country(country_data)
                    result_list.append(country)
            else:
                return Country(data)
            return result_list
        elif response.status_code == 404:
            raise requests.exceptions.InvalidURL
        else:
            raise requests.exceptions.RequestException

    @classmethod
    def get_all(cls, filters=None):
        """Returns all countries provided by  restcountries.eu.

            :param filters - a list of fields to filter the output of the request to include only the specified fields.
        """
        resource = "/all"
        return cls._get_country_list(resource, filters=filters)

    @classmethod
    def get_countries_by_name(cls, name, filters=None):
        """Returns a list of countries.

        :param name - Name string of a country. E.g. 'France'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/name"
        return cls._get_country_list(resource, name, filters=filters)

    @classmethod
    def get_countries_by_language(cls, language, filters=None):
        """Returns a list of countries.

        :param language - Language string of a country. E.g. 'en'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/lang"
        return cls._get_country_list(resource, language, filters=filters)

    @classmethod
    def get_countries_by_calling_code(cls, calling_code, filters=None):
        """Returns a list of countries.

        :param calling_code - Calling code string of a country. E.g. '1'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/callingcode"
        return cls._get_country_list(resource, calling_code, filters=filters)

    @classmethod
    def get_country_by_country_code(cls, alpha, filters=None):
        """Returns a `Country` object by alpha code.

        :param alpha - Alpha code string of a country. E.g. 'de'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: a Country object
        You can look those up at wikipedia: https://en.wikipedia.org/wiki/ISO_3166-1
        """
        resource = "/alpha"
        return cls._get_country_list(resource, alpha, filters=filters)

    @classmethod
    def get_countries_by_country_codes(cls, codes, filters=None):
        """Returns a list of countries.

        :param codes - List of strings which represent the codes of countries. E.g. ['us', 'ke']
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        You can look those up at wikipedia: https://en.wikipedia.org/wiki/ISO_3166-1
        :returns: list of Country objects
        """
        resource = "/alpha?codes="
        codes = cls.QUERY_SEPARATOR.join(codes)
        return cls._get_country_list(resource, codes, filters=filters)

    @classmethod
    def get_countries_by_currency(cls, currency, filters=None):
        """Returns a list of countries.

        :param currency - Currency string of a country. E.g. 'EUR'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/currency"
        return cls._get_country_list(resource, currency, filters=filters)

    @classmethod
    def get_countries_by_region(cls, region, filters=None):
        """Returns a list of countries.

        :param region - Region string of a country. E.g. 'Europe'.
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/region"
        return cls._get_country_list(resource, region, filters=filters)

    @classmethod
    def get_countries_by_subregion(cls, subregion, filters=None):
        """Returns a list of countries.

        :param subregion - Subregion string of a country. E.g. 'Western Europe'
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/subregion"
        return cls._get_country_list(resource, subregion, filters=filters)

    @classmethod
    def get_countries_by_capital(cls, capital, filters=None):
        """Returns a list of countries.

        :param capital - Capital string of a country. E.g. 'London'
        :param filters - a list of fields to filter the output of the request to include only the specified fields.
        :returns: list of Country objects
        """
        resource = "/capital"
        return cls._get_country_list(resource, capital, filters=filters)


class RestCountryApiV2(RestCountryApi):
    BASE_URI = "https://restcountries.eu/rest/v2"
    QUERY_SEPARATOR = ";"


class Country:
    def __str__(self):
        return "{}".format(self.name)

    def __init__(self, country_data):
        self.top_level_domain = country_data.get("topLevelDomain")
        self.alpha2_code = country_data.get("alpha2Code")
        self.alpha3_code = country_data.get("alpha3Code")
        self.currencies = country_data.get("currencies")
        self.capital = country_data.get("capital")
        self.calling_codes = country_data.get("callingCodes")
        self.alt_spellings = country_data.get("altSpellings")
        self.relevance = country_data.get("relevance")
        self.region = country_data.get("region")
        self.subregion = country_data.get("subregion")
        self.translations = country_data.get("translations")
        self.population = country_data.get("population")
        self.latlng = country_data.get("latlng")
        self.demonym = country_data.get("demonym")
        self.area = country_data.get("area")
        self.gini = country_data.get("gini")
        self.timezones = country_data.get("timezones")
        self.borders = country_data.get("borders")
        self.native_name = country_data.get("nativeName")
        self.name = country_data.get("name")
        self.numeric_code = country_data.get("numericCode")
        self.languages = country_data.get("languages")
        self.flag = country_data.get("flag")
        self.regional_blocs = country_data.get("regionalBlocs")
        self.cioc = country_data.get("cioc")

    def __eq__(self, other):
        assert isinstance(other, Country)
        return self.numeric_code == other.numeric_code

    def __lt__(self, other):
        assert isinstance(other, Country)
        return self.numeric_code < other.numeric_code

    def __hash__(self):
        return int(self.numeric_code)

    def __str__(self):
        return "<{} | {}>".format(self.name, self.alpha3_code)

    def __repr__(self):
        return "<{} | {}>".format(self.name, self.alpha3_code)


# s = RestCountryApiV2()

# s.get_countries_by_country_codes(["ke", "ug"],filters=["name","capital","currencies"])
