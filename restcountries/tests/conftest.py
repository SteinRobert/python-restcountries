import pytest

from restcountries.base import Country
from restcountries.tests.countries_data import RSA, NGR, EGY, KEN


@pytest.fixture(name="south_africa")
def fixture_south_africa():
    return Country(RSA)


@pytest.fixture(name="nigeria")
def fixture_nigeria():
    return Country(NGR)


@pytest.fixture(name="egypt")
def fixture_egypt():
    return Country(EGY)


@pytest.fixture(name="kenya")
def fixture_kenya():
    return Country(KEN)


@pytest.fixture(name="countries_map")
def fixture_all_countries(south_africa, nigeria, egypt, kenya):
    """
    Returns a map of all country objects.
    """
    return {
        "south_africa": south_africa,
        "nigeria": nigeria,
        "egypt": egypt,
        "kenya": kenya,
    }


@pytest.fixture(name="mock_get_all_countries")
def fixture_mock_get_all_countries(requests_mock):
    """
    Mock requests for getting all countries.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/all", json=[RSA, NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_name")
def fixture_mock_get_countries_by_name(requests_mock):
    """
    Mock requests for getting countries by name.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/name/south%20africa", json=[RSA]
    )
    requests_mock.get("https://restcountries.eu/rest/v2/name/nigeria", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/name/egypt", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/name/kenya", json=[KEN])


@pytest.fixture(name="mock_get_country_by_country_code")
def fixture_mock_get_country_by_country_code(requests_mock):
    """
    Mock requests for getting a country by its country code.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/za", json=RSA)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/zaf", json=RSA)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/ng", json=NGR)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/ngr", json=NGR)


@pytest.fixture(name="mock_get_countries_by_country_codes")
def fixture_mock_get_countries_by_country_codes(requests_mock):
    """
    Mock requests for getting a list of countries by a list of country codes.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha?codes=ng;eg;ken", json=[NGR, EGY, KEN]
    )


@pytest.fixture(name="mock_get_countries_by_currency")
def fixture_mock_get_countries_by_currency(requests_mock):
    """
    Mock requests for getting countries by currency.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/currency/zar", json=[RSA])
    requests_mock.get("https://restcountries.eu/rest/v2/currency/ngn", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/currency/egp", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/currency/kes", json=[KEN])


@pytest.fixture(name="mock_get_countries_by_language")
def fixture_mock_get_countries_by_language(requests_mock):
    """
    Mock request for getting countries by language.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/lang/en", json=[RSA, NGR, KEN])


@pytest.fixture(name="mock_get_countries_by_capital")
def fixture_mock_get_countries_by_capital(requests_mock):
    """
    Mock requests for getting countries by capital city.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/capital/pretoria", json=[RSA])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/abuja", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/cairo", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/nairobi", json=[KEN])


@pytest.fixture(name="mock_get_countries_by_calling_code")
def fixture_mock_get_countries_by_calling_code(requests_mock):
    """
    Mock requests for getting countries by calling code.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/27", json=[RSA])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/234", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/20", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/254", json=[KEN])


@pytest.fixture(name="mock_get_countries_by_region")
def fixture_mock_get_countries_by_region(requests_mock):
    """
    Mock requests for getting countries by region.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/region/europe", json=[])
    requests_mock.get(
        "https://restcountries.eu/rest/v2/region/africa", json=[RSA, NGR, EGY, KEN]
    )


@pytest.fixture(name="mock_get_countries_by_subregion")
def fixture_mock_get_countries_by_subregion(requests_mock):
    """
    Mock requests for getting countries by subregion.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/southern%20africa", json=[RSA]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/western%20africa", json=[NGR]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/northern%20africa", json=[EGY]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/eastern%20africa", json=[KEN]
    )
