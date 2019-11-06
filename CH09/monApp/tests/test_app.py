import json

import falcon
from falcon import testing
#import msgpack
import json
import pytest
from unittest.mock import patch
from ..monApp.app import ssenseProductClass

from ..monApp.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
#@patch(ssenseProductClass, 'on_get') # This decorator can be used to mock the function
def test_list_images(client):
    content = {'description': 
               {'Error': 'Wrong data type ! Use Content-Type=application/json'
               },
               'title': 'Bad request',
              }
    
    # Exercice 1 : There is an error in the following call for simulate_get, fixe it
    response = client.simulate_get('/getProducts', headers={'Content-Type': 'application/json1'})
    #result_doc = msgpack.unpackb(response.content, raw=False)
    result_doc = json.loads(response.content)

    assert result_doc == content
    #assert response.status == falcon.HTTP_OK
    assert response.status == falcon.HTTP_400
