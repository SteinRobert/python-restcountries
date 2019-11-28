import pytest

from restcountries import RestCountryApiV2 as rapi


@pytest.mark.usefixtures("mock_get_all_countries")
def test_get_all(countries_map):
    """
    Test that a list of all countries can be retrieved.
    """
    countries = rapi.get_all()
    assert sorted(countries) == sorted(countries_map.values())


@pytest.mark.usefixtures("mock_get_countries_by_name")
@pytest.mark.parametrize("country_name", ["south_africa", "nigeria", "egypt", "kenya"])
def test_get_countries_by_name(countries_map, country_name):
    """
    Test that countries can be retrieved by name.
    """
    sanitized_country_name = country_name.replace("_", " ")
    countries = rapi.get_countries_by_name(sanitized_country_name)
    assert countries == [countries_map[country_name]]


@pytest.mark.usefixtures("mock_get_country_by_country_code")
@pytest.mark.parametrize(
    "country_code, country_name",
    [
        ("za", "south_africa"),
        ("zaf", "south_africa"),
        ("ng", "nigeria"),
        ("ngr", "nigeria"),
    ],
)
def test_get_country_by_country_code(countries_map, country_code, country_name):
    """
    Test that a single country can be retrieved by its country code.
    """
    country = rapi.get_country_by_country_code(country_code)
    assert country == countries_map[country_name]


@pytest.mark.usefixtures("mock_get_countries_by_country_codes")
def test_get_countries_by_country_codes(nigeria, egypt, kenya):
    """
    Test that multiple countries can be retrieved by multiple country codes.
    """
    countries = rapi.get_countries_by_country_codes(["ng", "eg", "ken"])
    assert sorted(countries) == sorted([nigeria, egypt, kenya])


@pytest.mark.usefixtures("mock_get_countries_by_currency")
@pytest.mark.parametrize(
    "currency, country_name",
    [("ZAR", "south_africa"), ("NGN", "nigeria"), ("EGP", "egypt"), ("KES", "kenya")],
)
def test_get_countries_by_currency(countries_map, currency, country_name):
    """
    Test that countries can be retrieved by currency.
    """
    countries = rapi.get_countries_by_currency(currency)
    assert countries == [countries_map[country_name]]


@pytest.mark.usefixtures("mock_get_countries_by_language")
def test_get_countries_by_language(south_africa, nigeria, kenya):
    """
    Test that countries can be retrieved by language.
    """
    countries = rapi.get_countries_by_language("en")
    assert countries == [south_africa, nigeria, kenya]


@pytest.mark.usefixtures("mock_get_countries_by_capital")
@pytest.mark.parametrize(
    "capital, country_name",
    [
        ("Pretoria", "south_africa"),
        ("Abuja", "nigeria"),
        ("Cairo", "egypt"),
        ("Nairobi", "kenya"),
    ],
)
def test_get_countries_by_capital(countries_map, capital, country_name):
    """
    Test that countries can be retrieved by capital city.
    """
    countries = rapi.get_countries_by_capital(capital)
    assert countries == [countries_map[country_name]]


@pytest.mark.usefixtures("mock_get_countries_by_calling_code")
@pytest.mark.parametrize(
    "calling_code, country_name",
    [("27", "south_africa"), ("234", "nigeria"), ("20", "egypt"), ("254", "kenya")],
)
def test_get_countries_by_calling_code(countries_map, calling_code, country_name):
    """
    Test that countries can be retrieved by calling code.
    """
    countries = rapi.get_countries_by_calling_code(calling_code)
    assert countries == [countries_map[country_name]]


@pytest.mark.usefixtures("mock_get_countries_by_region")
def test_get_countries_by_region(countries_map):
    """
    Test that countries can be retrieved by region.
    """
    countries = rapi.get_countries_by_region("africa")
    assert sorted(countries) == sorted(countries_map.values())

    countries = rapi.get_countries_by_region("europe")
    assert countries == []


@pytest.mark.usefixtures("mock_get_countries_by_subregion")
@pytest.mark.parametrize(
    "subregion, country_name",
    [
        ("southern africa", "south_africa"),
        ("western africa", "nigeria"),
        ("northern africa", "egypt"),
        ("eastern africa", "kenya"),
    ],
)
def test_get_countries_by_subregion(countries_map, subregion, country_name):
    """
    Test that countries can be retrieved by subregion.
    """
    countries = rapi.get_countries_by_subregion(subregion)
    assert countries == [countries_map[country_name]]
