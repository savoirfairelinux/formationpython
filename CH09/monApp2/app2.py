import json, falcon
import requests


class ssenseProductClass:
    def on_get(self, req, resp):
        """This is our listenner"""
        print(req.body())
        data = {}

        content = {
            'name': 'Black Ruben Coat',
            'brand': 'Nudie Jeans',
            'price': '650',
            'currency': 'CAD',
            'code': '192078M176001',
            'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
        }
        #output = {}
        #if data['method'] == 'get-price':
        #    output['value'] = content['name']
        #resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/getProduct', ssenseProductClass())
