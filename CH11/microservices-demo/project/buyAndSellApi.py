import pymysql
import falcon
import json
import requests
from lxml import html
import ipdb

class DBConnect:
    def __init__(self, product_name):
        try:
            with open('config.json', 'r') as myfile:
                data=myfile.read()
            obj = json.loads(data)
            self.product_name = product_name
            self.dbServerName = obj["dbServerName"]
            self.dbUser = obj["dbUser"]
            self.dbName = obj["dbName"]
            self.charSet = obj["charSet"]
            self.dbPort = obj["dbPort"]

        except IOError as e:
            raise

    def connect(self):
        return pymysql.connect(db=self.dbName, 
                               user=self.dbUser, 
                               host=self.dbServerName, 
                               port=self.dbPort
                              ) 

    def buyProduct(self):
        connection = self.connect()
        if connection:
            try:
                cr = connection.cursor()
                sql_query = 'SELECT count from sock where name="' + str(self.product_name) + '"'
                cr.execute(sql_query)
                quantity = cr.fetchall()[0][0]
                if quantity > 0:
                    sql_query = 'UPDATE sock SET count="' + str(quantity-1) + '" where name="' + str(self.product_name) + '"'
                    cr.execute(sql_query)
                    print(sql_query)
                    connection.commit()
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
            finally:
                connection.close()
        else:
            raise falcon.HTTPInternalServerError
    
    def productInformation(self):
        connection = self.connect()
        if connection:
            try:
                cr = connection.cursor()
                sql_query = 'SELECT name, count, price from sock where name="' + str(self.product_name) + '"'
                cr.execute(sql_query)
                data = cr.fetchall()[0]
                return {'name': data[0], 'count': data[1], 'price': data[2]}
            except Exception as e:
                print(e)
            finally:
                connection.close()
        else:
            return False

    def updatePrice(self, price):
        connection = self.connect()
        if connection:
            try:
                cr = connection.cursor()
                sql_query = 'UPDATE sock SET price="' + str(price) + '" where name="' + str(self.product_name) + '"'
                cr.execute(sql_query)
                print(sql_query)
                connection.commit()
                return {'done': True}
            except Exception as e:
                print(e)
            finally:
                connection.close()
        else:
            return False

class buyProduct:
    """ 
    This Class is implemented to Buy a Product
    """
    def on_put(self, req, resp, id):
        try:
            connect = DBConnect(id)
            if connect.buyProduct():
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_200
            else:
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_404

        except falcon.HTTPInvalidHeader as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_400

class productInformation:
    """ 
    This Class is implemented to return product information
    """
    def on_get(self, req, resp, id):
        try:
            connect = DBConnect(id)
            content = connect.productInformation()
            if content:
                resp.body = json.dumps(content)
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_200
            else:
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_400

        except falcon.HTTPInvalidHeader as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_404

    def on_put(self, req, resp, id):
        try:
            connect = DBConnect(id)
            req_body_str = req.stream.read()
            req_body = json.loads(req_body_str)
            content = connect.updatePrice(req_body['price'])
            if content:
                resp.body = json.dumps(content)
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_200
            else:
                resp.content_type = falcon.MEDIA_JSON
                resp.status = falcon.HTTP_400
        except falcon.HTTPInvalidHeader as e:
            resp.body = str(e)
            resp.status = falcon.HTTP_404


api = application = falcon.API()
api.add_route('/buy/{id}', buyProduct())
api.add_route('/product/{id}', productInformation())
