import sys

import falcon
from falcon import testing
import msgpack
import pytest
from unittest.mock import patch

from ..monApp.app import ssenseProductClass

from ..monApp.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
# @patch(ssenseProductClass, 'on_get')
def test_list_images(client):
    content = {
        'name': 'Black Ruben Coat',
        'brand': 'Nudie Jeans',
        'price': '650',
        'currency': 'CAD',
        'code': '192078M176001',
        'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
    }

    response = client.simulate_get('/getProducts')
    print(response.content)
    result_doc =  response.content
        # msgpack.unpackb(response.content, raw=False)

    # assert result_doc == content
    assert response.status == falcon.HTTP_OK
