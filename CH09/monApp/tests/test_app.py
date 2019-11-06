from falcon import testing
import pytest
import json
from ..monApp.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_400(client):
    content = {
        'name': 'Black Ruben Coat',
        'brand': 'Nudie Jeans',
        'price': '650',
        'currency': 'CAD',
        'code': '192078M176001',
        'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
    }

    response = client.simulate_get('/getProducts')

    parsed_response = json.loads(response.content)

    assert parsed_response == {
        'title': "Bad request",
        'description': "Request content type not allowed"
    }

def test_OK(client):
    content = {
        'name': 'Black Ruben Coat',
        'brand': 'Nudie Jeans',
        'price': '650',
        'currency': 'CAD',
        'code': '192078M176001',
        'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
    }

    response = client.simulate_get('/getProducts', headers={
        'content-type': 'application/json'
    })

    parsed_response = json.loads(response.content)

    assert len(parsed_response.keys()) == 13

