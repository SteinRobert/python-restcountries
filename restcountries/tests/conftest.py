import pytest

from restcountries.base import Country
from restcountries.tests.countries_data import RSA, NGR, EGY, KEN

BASE_URI = "https://restcountries.com/v2"


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
    url = BASE_URI + "/all"
    requests_mock.get(url, json=[RSA, NGR, EGY, KEN])


@pytest.fixture(name="mock_get_all_countries_with_filters")
def fixture_mock_get_all_countries_with_filter(requests_mock):
    """
    Mock requests for getting all countries and filters the response.
    """
    url = BASE_URI + "/all?fields=name;capital"
    requests_mock.get(url, json=[RSA, NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_name")
def fixture_mock_get_countries_by_name(requests_mock):
    """
    Mock requests for getting countries by name.
    """
    sa_url = BASE_URI + "/name/south%20africa"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/name/nigeria"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/name/egypt"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/name/kenya"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_name_with_filter")
def fixture_mock_get_countries_by_name_with_filter(requests_mock):
    """
    Mock requests for getting countries by name and filters the response.
    """
    sa_url = BASE_URI + "/name/south%20africa?fields=name;currencies"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/name/nigeria?fields=name;currencies"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/name/egypt?fields=name;currencies"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/name/kenya?fields=name;currencies"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_country_by_country_code")
def fixture_mock_get_country_by_country_code(requests_mock):
    """
    Mock requests for getting a country by its country code.
    """
    za_url = BASE_URI + "/alpha/za"
    requests_mock.get(za_url, json=RSA)
    zaf_url = BASE_URI + "/alpha/zaf"
    requests_mock.get(zaf_url, json=RSA)
    ng_url = BASE_URI + "/alpha/ng"
    requests_mock.get(ng_url, json=NGR)
    ngr_url = BASE_URI + "/alpha/ngr"
    requests_mock.get(ngr_url, json=NGR)


@pytest.fixture(name="mock_get_country_by_country_code_with_filter")
def fixture_mock_get_country_by_country_code_with_filter(requests_mock):
    """
    Mock requests for getting a country by its country code and filters the response.
    """
    za_url = BASE_URI + "/alpha/za?fields=name;capital"
    requests_mock.get(za_url, json=RSA)
    zaf_url = BASE_URI + "/alpha/zaf?fields=name;capital"
    requests_mock.get(zaf_url, json=RSA)
    ng_url = BASE_URI + "/alpha/ng?fields=name;capital"
    requests_mock.get(ng_url, json=NGR)
    ngr_url = BASE_URI + "/alpha/ngr?fields=name;capital"
    requests_mock.get(ngr_url, json=NGR)


@pytest.fixture(name="mock_get_countries_by_country_codes")
def fixture_mock_get_countries_by_country_codes(requests_mock):
    """
    Mock requests for getting a list of countries by a list of country codes.
    """
    url = BASE_URI + "/alpha?codes=ng;eg;ken"
    requests_mock.get(url, json=[NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_country_codes_with_filter")
def fixture_mock_get_countries_by_country_codes_with_filter(requests_mock):
    """
    Mock requests for getting a list of countries by a list of country codes with response filtering.
    """
    url = BASE_URI + "/alpha?codes=ng;eg;ken&fields=name;currencies"
    requests_mock.get(url, json=[NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_currency")
def fixture_mock_get_countries_by_currency(requests_mock):
    """
    Mock requests for getting countries by currency.
    """
    sa_url = BASE_URI + "/currency/zar"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/currency/ngn"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/currency/egp"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/currency/kes"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_currency_with_filter")
def fixture_mock_get_countries_by_currency_with_filter(requests_mock):
    """
    Mock requests for getting countries by currency and filters the response.
    """
    sa_url = BASE_URI + "/currency/zar?fields=name"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/currency/ngn?fields=name"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/currency/egp?fields=name"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/currency/kes?fields=name"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_language")
def fixture_mock_get_countries_by_language(requests_mock):
    """
    Mock request for getting countries by language.
    """
    url = BASE_URI + "/lang/en"
    requests_mock.get(url, json=[RSA, NGR, KEN])


@pytest.fixture(name="mock_get_countries_by_language_with_filter")
def fixture_mock_get_countries_by_language_with_filter(requests_mock):
    """
    Mock request for getting countries by language and filters the response.
    """
    url = BASE_URI + "/lang/en?fields=name;flag"
    requests_mock.get(url, json=[RSA, NGR, KEN])


@pytest.fixture(name="mock_get_countries_by_capital")
def fixture_mock_get_countries_by_capital(requests_mock):
    """
    Mock requests for getting countries by capital city.
    """
    sa_url = BASE_URI + "/capital/pretoria"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/capital/abuja"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/capital/cairo"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/capital/nairobi"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_capital_with_filter")
def fixture_mock_get_countries_by_capital_with_capital(requests_mock):
    """
    Mock requests for getting countries by capital city and filters the response.
    """
    sa_url = BASE_URI + "/capital/pretoria?fields=name;demonym"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/capital/abuja?fields=name;demonym"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/capital/cairo?fields=name;demonym"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/capital/nairobi?fields=name;demonym"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_calling_code")
def fixture_mock_get_countries_by_calling_code(requests_mock):
    """
    Mock requests for getting countries by calling code.
    """
    sa_url = BASE_URI + "/callingcode/27"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/callingcode/234"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/callingcode/20"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/callingcode/254"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_calling_code_with_filter")
def fixture_mock_get_countries_by_calling_code_with_filter(requests_mock):
    """
    Mock requests for getting countries by calling code and filters the response.
    """
    sa_url = BASE_URI + "/callingcode/27?fields=name"
    requests_mock.get(sa_url, json=[RSA])
    ng_url = BASE_URI + "/callingcode/234?fields=name"
    requests_mock.get(ng_url, json=[NGR])
    eg_url = BASE_URI + "/callingcode/20?fields=name"
    requests_mock.get(eg_url, json=[EGY])
    ke_url = BASE_URI + "/callingcode/254?fields=name"
    requests_mock.get(ke_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_region")
def fixture_mock_get_countries_by_region(requests_mock):
    """
    Mock requests for getting countries by region.
    """
    eu_url = BASE_URI + "/region/europe"
    requests_mock.get(eu_url, json=[])
    af_url = BASE_URI + "/region/africa"
    requests_mock.get(af_url, json=[RSA, NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_region_with_filter")
def fixture_mock_get_countries_by_region_with_filter(requests_mock):
    """
    Mock requests for getting countries by region and filters the response.
    """
    eu_url = BASE_URI + "/region/europe?fields=name"
    requests_mock.get(eu_url, json=[])
    af_url = BASE_URI + "/region/africa?fields=name"
    requests_mock.get(af_url, json=[RSA, NGR, EGY, KEN])


@pytest.fixture(name="mock_get_countries_by_subregion")
def fixture_mock_get_countries_by_subregion(requests_mock):
    """
    Mock requests for getting countries by subregion.
    """
    sa_url = BASE_URI + "/subregion/southern%20africa"
    requests_mock.get(sa_url, json=[RSA])
    wa_url = BASE_URI + "/subregion/western%20africa"
    requests_mock.get(wa_url, json=[NGR])
    na_url = BASE_URI + "/subregion/northern%20africa"
    requests_mock.get(na_url, json=[EGY])
    ea_url = BASE_URI + "/subregion/eastern%20africa"
    requests_mock.get(ea_url, json=[KEN])


@pytest.fixture(name="mock_get_countries_by_subregion_with_filter")
def fixture_mock_get_countries_by_subregion_with_filter(requests_mock):
    """
    Mock requests for getting countries by subregion and filters the response.
    """
    sa_url = BASE_URI + "/subregion/southern%20africa?fields=name"
    requests_mock.get(sa_url, json=[RSA])
    wa_url = BASE_URI + "/subregion/western%20africa?fields=name"
    requests_mock.get(wa_url, json=[NGR])
    na_url = BASE_URI + "/subregion/northern%20africa?fields=name"
    requests_mock.get(na_url, json=[EGY])
    ea_url = BASE_URI + "/subregion/eastern%20africa?fields=name"
    requests_mock.get(ea_url, json=[KEN])
