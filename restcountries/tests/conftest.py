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


@pytest.fixture(name="mock_get_all_countries_with_filters")
def fixture_mock_get_all_countries_with_filter(requests_mock):
    """
    Mock requests for getting all countries and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/all?fields=name;capital",
        json=[RSA, NGR, EGY, KEN],
    )


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


@pytest.fixture(name="mock_get_countries_by_name_with_filter")
def fixture_mock_get_countries_by_name_with_filter(requests_mock):
    """
    Mock requests for getting countries by name and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/name/south%20africa?fields=name;currencies",
        json=[RSA],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/name/nigeria?fields=name;currencies",
        json=[NGR],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/name/egypt?fields=name;currencies", json=[EGY]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/name/kenya?fields=name;currencies", json=[KEN]
    )


@pytest.fixture(name="mock_get_country_by_country_code")
def fixture_mock_get_country_by_country_code(requests_mock):
    """
    Mock requests for getting a country by its country code.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/za", json=RSA)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/zaf", json=RSA)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/ng", json=NGR)
    requests_mock.get("https://restcountries.eu/rest/v2/alpha/ngr", json=NGR)


@pytest.fixture(name="mock_get_country_by_country_code_with_filter")
def fixture_mock_get_country_by_country_code_with_filter(requests_mock):
    """
    Mock requests for getting a country by its country code and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha/za?fields=name;capital", json=RSA
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha/zaf?fields=name;capital", json=RSA
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha/ng?fields=name;capital", json=NGR
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha/ngr?fields=name;capital", json=NGR
    )


@pytest.fixture(name="mock_get_countries_by_country_codes")
def fixture_mock_get_countries_by_country_codes(requests_mock):
    """
    Mock requests for getting a list of countries by a list of country codes.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha?codes=ng;eg;ken", json=[NGR, EGY, KEN]
    )


@pytest.fixture(name="mock_get_countries_by_country_codes_with_filter")
def fixture_mock_get_countries_by_country_codes_with_filter(requests_mock):
    """
    Mock requests for getting a list of countries by a list of country codes with response filtering.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/alpha?codes=ng;eg;ken&fields=name;currencies",
        json=[NGR, EGY, KEN],
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


@pytest.fixture(name="mock_get_countries_by_currency_with_filter")
def fixture_mock_get_countries_by_currency_with_filter(requests_mock):
    """
    Mock requests for getting countries by currency and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/currency/zar?fields=name", json=[RSA]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/currency/ngn?fields=name", json=[NGR]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/currency/egp?fields=name", json=[EGY]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/currency/kes?fields=name", json=[KEN]
    )


@pytest.fixture(name="mock_get_countries_by_language")
def fixture_mock_get_countries_by_language(requests_mock):
    """
    Mock request for getting countries by language.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/lang/en", json=[RSA, NGR, KEN])


@pytest.fixture(name="mock_get_countries_by_language_with_filter")
def fixture_mock_get_countries_by_language_with_filter(requests_mock):
    """
    Mock request for getting countries by language and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/lang/en?fields=name;flag",
        json=[RSA, NGR, KEN],
    )


@pytest.fixture(name="mock_get_countries_by_capital")
def fixture_mock_get_countries_by_capital(requests_mock):
    """
    Mock requests for getting countries by capital city.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/capital/pretoria", json=[RSA])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/abuja", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/cairo", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/capital/nairobi", json=[KEN])


@pytest.fixture(name="mock_get_countries_by_capital_with_filter")
def fixture_mock_get_countries_by_capital_with_capital(requests_mock):
    """
    Mock requests for getting countries by capital city and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/capital/pretoria?fields=name;demonym",
        json=[RSA],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/capital/abuja?fields=name;demonym", json=[NGR]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/capital/cairo?fields=name;demonym", json=[EGY]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/capital/nairobi?fields=name;demonym",
        json=[KEN],
    )


@pytest.fixture(name="mock_get_countries_by_calling_code")
def fixture_mock_get_countries_by_calling_code(requests_mock):
    """
    Mock requests for getting countries by calling code.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/27", json=[RSA])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/234", json=[NGR])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/20", json=[EGY])
    requests_mock.get("https://restcountries.eu/rest/v2/callingcode/254", json=[KEN])


@pytest.fixture(name="mock_get_countries_by_calling_code_with_filter")
def fixture_mock_get_countries_by_calling_code_with_filter(requests_mock):
    """
    Mock requests for getting countries by calling code and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/callingcode/27?fields=name", json=[RSA]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/callingcode/234?fields=name", json=[NGR]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/callingcode/20?fields=name", json=[EGY]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/callingcode/254?fields=name", json=[KEN]
    )


@pytest.fixture(name="mock_get_countries_by_region")
def fixture_mock_get_countries_by_region(requests_mock):
    """
    Mock requests for getting countries by region.
    """
    requests_mock.get("https://restcountries.eu/rest/v2/region/europe", json=[])
    requests_mock.get(
        "https://restcountries.eu/rest/v2/region/africa", json=[RSA, NGR, EGY, KEN]
    )


@pytest.fixture(name="mock_get_countries_by_region_with_filter")
def fixture_mock_get_countries_by_region_with_filter(requests_mock):
    """
    Mock requests for getting countries by region and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/region/europe?fields=name", json=[]
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/region/africa?fields=name",
        json=[RSA, NGR, EGY, KEN],
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


@pytest.fixture(name="mock_get_countries_by_subregion_with_filter")
def fixture_mock_get_countries_by_subregion_with_filter(requests_mock):
    """
    Mock requests for getting countries by subregion and filters the response.
    """
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/southern%20africa?fields=name",
        json=[RSA],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/western%20africa?fields=name",
        json=[NGR],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/northern%20africa?fields=name",
        json=[EGY],
    )
    requests_mock.get(
        "https://restcountries.eu/rest/v2/subregion/eastern%20africa?fields=name",
        json=[KEN],
    )
