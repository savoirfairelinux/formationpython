import falcon
import msgpack
import requests
from lxml import html
import json
from falcon_cors import CORS

def json_serializer(req, resp, exception):
    representation = None

    preferred = req.client_prefers(('application/x-yaml',
                                    'application/json'))

    if exception.has_representation and preferred is not None:
        if preferred == 'application/json':
            representation = exception.to_json()
        else:
            representation = yaml.dump(exception.to_dict(),
                                       encoding=None)
        resp.body = representation
        resp.content_type = preferred

    resp.append_header('Vary', 'Accept')

class ssenseProductClass:

    def validate_req_type(req, resp, resource, params, allowed_types):
        if req.content_type not in allowed_types:
            msg = 'Request content type not allowed'
            raise falcon.HTTPBadRequest('Bad request', msg)

    def validate_req_type(req, resp, resource, params, allowed_types):
        if req.content_type not in allowed_types:
            msg = 'Request content type not allowed'
            raise falcon.HTTPBadRequest('Bad request', msg)

    @falcon.before(validate_req_type, ['application/json'])
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


cors = CORS(allow_all_origins=True)
api = application = falcon.API()
api.add_route('/getProducts', ssenseProductClass())
api.set_error_serializer(json_serializer);