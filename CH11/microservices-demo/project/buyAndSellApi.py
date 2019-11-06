import pymysql
import falcon
import json
import requests
from lxml import html


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
                # Check availaiblity
                #import ipdb; ipdb.set_trace()
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
        

class buyProduct:
    """ 
    This Class is implemented to Buy a Product
    """
#    def data_type(req, resp, resource):
#        if req.content_type != falcon.MEDIA_JSON:
#            msg = {'Error': 'Wrong data type ! Use Content-Type=application/json'}
#            raise falcon.HTTPBadRequest('Bad request', msg)
#    
#    @falcon.after(data_type)
    def on_put(self, req, resp, id):
        try:
            #url = json.loads(req.stream.read())['url']
            #resp.body = json.dumps({'id': id})
            connect = DBConnect(id)
            if connect.buyProduct():
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
#api.add_route('/product/{id}', productInformation())
