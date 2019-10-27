import falcon
import msgpack
#import json


class ssenseProductClass:
    def on_get(self, req, resp):
        """This is our listenner"""
        content = {
            'name': 'Black Ruben Coat',
            'brand': 'Nudie Jeans',
            'price': '650',
            'currency': 'CAD',
            'code': '192078M176001',
            'image': 'https://img.ssensemedia.com/images//192078M176001_1/nudie-jeans-black-ruben-coat.jpg'
        }
        #resp.body = json.dumps(content)
        resp.data = msgpack.packb(content, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200

api = falcon.API()
api.add_route('/getProduct', ssenseProductClass())
