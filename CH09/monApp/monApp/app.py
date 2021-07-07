import falcon
import msgpack
import requests
from lxml import html
import json
from falcon_cors import CORS
import sqlite3


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
            'buyer' : 'abc'
        }
        """
        try:
            buyer = json.loads(req.stream.read())['buyer']
            conn = sqlite3.connect('mydb')

            c = conn.cursor()
            c.execute(f"SELECT * FROM stocks2 WHERE buyer = '{buyer}'")

            resp.body = json.dumps(c.fetchall())
            resp.content_type = falcon.MEDIA_JSON
            resp.status = falcon.HTTP_200

        except falcon.HTTPInvalidHeader as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_404
        except json.decoder.JSONDecodeError as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_500

    @falcon.after(data_type)
    def on_put(self, req, resp):
        """"
        Eg:
        {
            'url' : 'https://www.ssense.com/en-ca/men/clothing?page=2'
        }
        """
        try:
            url = json.loads(req.stream.read())['url']

            page = requests.get(url)
            tree = html.fromstring(page.content)

            brands = tree.xpath(
                '//figcaption/p[@class="product-name-plp"]/text()')
            buyers = tree.xpath('//figcaption/p[@class="bold"]/text()')
            prices = tree.xpath('//span[@class="price"]/text()')
            pictures = tree.xpath('//picture/img/@*[1]')
            links = tree.xpath(
                '//figure[@class="browsing-product-item"]/a/@href')

            products = dict(zip(buyers, zip(brands, prices, pictures,
                                            links)))

            conn = sqlite3.connect('mydb')
            c = conn.cursor()

            def getProductFields(buyer):
                return ','.join([f'"{val}"' for val in products[buyer]])

            values = ','.join([
                f'("{buyer}",{getProductFields(buyer)})'
                for buyer in products
            ])

            print(values)
            c.execute(f'INSERT INTO stocks2 VALUES {values}')

            conn.commit()

            resp.body = json.dumps(products)
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
conn = sqlite3.connect('mydb')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocks2
             (buyer text, brand text, price text, picture text, link text)''')
conn.close()
