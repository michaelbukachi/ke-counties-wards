from flask.testing import FlaskClient


def test_getting_all_counties(client: FlaskClient):
    res = client.get('data/counties')
    assert res.ok
    assert res.json


def test_getting_counties_wards(client: FlaskClient):
    res = client.get('data/counties/busia/wards')
    assert res.ok
    assert res.json


def test_getting_counties_wards__bad_county(client: FlaskClient):
    res = client.get('data/counties/xyz/wards')
    assert res.ok
    assert not res.json


def test_get_county_from_ward(client: FlaskClient):
    res = client.get('data/wards/abogeta east/county')
    assert res.ok
    assert res.json


def test_get_county_from_ward__not_found(client: FlaskClient):
    res = client.get('data/wards/sdfasdf/county')
    assert res.not_found
