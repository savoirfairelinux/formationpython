import falcon
from falcon import testing
import msgpack
import pytest
from unittest.mock import patch
from ..monApp.app import ssenseProductClass
from ..monApp.app import api
import json
import pdb

@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
# @patch(ssenseProductClass, 'on_get')
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


    #     assert response.content == "{"title: "Bad request",
    # description: "Request content type not allowed"
    # }"

    # result_doc = msgpack.unpackb(response.content, raw=False)
    #
    # assert result_doc == content
    # assert response.status == falcon.HTTP_OK

# pytest will inject the object returned by the "client" function
# as an additional parameter.
# @patch(ssenseProductClass, 'on_get')
# def test_content_type(client):
#     content = {
#         'name': 'Black Ruben Coat',
#         'brand': 'Nudie Jeans',
#         'price': '650',
#         'currency': 'CAD',
#         'code': '192078M176001',
#         'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
#     }
#
#     response = client.simulate_get('/getProduct')
#     result_doc = msgpack.unpackb(response.content, raw=False)
#
#     assert result_doc == content
#     assert response.status == falcon.HTTP_OK