import requests
import random
import json


class Customer:
    
    def __init__(self, stores=['172.16.17.132'], visits=1):
        self._budget = 100
        self._expected_buying_price = 0
        self.stores = stores
        self.waiting_time = 0
        self.visits = visits

    def find_cheapest(self, stores):
        #TODO: Multithreaded
        cheapest = (100, None)
        for store in stores:
            price = self.get_store_price(store)
            if price < cheapest[0]:
                cheapest = (price, store)
        self._expected_buying_price = cheapest[0]
        return cheapest

    def get_store_price(self, store_address, product_name='Colourful'):
        req=requests.get('http://' + store_address + ':8000/product/' + product_name)
        price = json.loads(req.text)['price']
        return price
    
    def get_stores(self, size=None, visits=None):
        """Method that returns #(visits) random stores
        of a given number (size) of stores"""

        if visits:
            self.visits = visits
        if not size:
            if len(self.stores) < 1:
                return None
            size = len(self.stores)
        indexes = random.sample(range(0,size),self.visits)
        i_will_look_at_stores = []
        for index in indexes:
            i_will_look_at_stores.append(self.stores[index])
        return i_will_look_at_stores

    def buy_sock_from_store(self, store_address, product_name='Colourful'):
        return requests.put( 
            'http://' + store_address + ':8000/buy/' + product_name)

    def go_shopping_for_socks(self):
        self.shopping_stores = self.get_stores()
        cheapest = self.find_cheapest(self.shopping_stores)
        if not cheapest[1]:
            return
        self.new_product = self.buy_sock_from_store(str(cheapest[1]))
        print("Bought from:"+ str(cheapest[1] + " at " + str(cheapest[0])))
