import falcon
import msgpack
import requests
from lxml import html
import json
from falcon_cors import CORS



class ssenseProductClass:
    """ 
    This Class is implemented to return products scrapped from the
    SSENS Store 
    """
    def data_type(req, resp, resource):
        if req.content_type != falcon.MEDIA_JSON:
            msg = {'Error': 'Wrong data type ! Use Content-Type=application/json'}
            raise falcon.HTTPBadRequest('Bad request', msg)
    
    @falcon.after(data_type)
    def on_get(self, req, resp):
        """"
        Eg:
        {
            'url' : 'https://www.ssense.com/en-ca/men/clothing?page=2'
        }
        """
        try:
            #import ipdb; ipdb.set_trace()
            url = 'https://www.ssense.com/en-ca/men/clothing?page=3'
            #import ipdb; ipdb.set_trace()
            #url = json.loads(req.stream.read())['url']
            page = requests.get(url)
            tree = html.fromstring(page.content)
            
            # based on our analysis of the web page structure we can suppose
            # that products names are located in the xpath
            # //p[@itemprop="name"]
            # /text()
            brands = tree.xpath(
                '//figcaption/p[@class="product-name-plp"]/text()')
            buyers = tree.xpath('//figcaption/p[@class="bold"]/text()')
            prices = tree.xpath('//span[@class="price"]/text()')
            pictures = tree.xpath('//picture/img/@*[1]')
            links = tree.xpath(
                '//figure[@class="browsing-product-item"]/a/@href')
            resp.body = json.dumps(
                dict(zip(buyers, zip(brands, prices, pictures,
                                     links))))
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_200

        except falcon.HTTPInvalidHeader as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_404
        except json.decoder.JSONDecodeError as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_500


cors = CORS(allow_all_origins=True)
api = application = falcon.API()
api.add_route('/getProducts', ssenseProductClass())
