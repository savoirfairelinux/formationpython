import json

import falcon
from falcon import testing
import msgpack
import pytest

from ..monApp.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.

def test_list_images(client):
    content = {
        'name': 'Black Ruben Coat',
        'brand': 'Nudie Jeans',
        'price': '650',
        'currency': 'CAD',
        'code': '192078M176001',
        'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
    }

    response = client.simulate_get('/getProducts', headers={'content-type': 'application/json'})
    result_doc = json.loads(response.content)
    assert len(result_doc.keys()) == 13
    assert response.status == falcon.HTTP_OK


def test_list_bad_content_type(client):
    content = {
        'name': 'Black Ruben Coat',
        'brand': 'Nudie Jeans',
        'price': '650',
        'currency': 'CAD',
        'code': '192078M176001',
        'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
    }

    response = client.simulate_get('/getProducts')
    result_doc = json.loads(response.content)
    print(result_doc)
    assert result_doc == {'title': 'bad request', 'description': 'not application/json'}
    assert response.status == falcon.HTTP_400
