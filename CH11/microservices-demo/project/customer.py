import requests
import random

class Customer:
    
    def __init__(self, stores=['localhost'], visits=1):
        self._budget = 100
        self._expected_buying_price = 0
        self.stores = stores
        self.waiting_time = 0
        self.visits = visits

    def find_cheapest(self, stores):
        #TODO: Multithreaded
        cheapest = (100, None)
        for store in stores:
            price = get_store_price(store)
            if price < cheapest:
                cheapest = (price, store)
        return cheapest

    def get_store_price(self, store):
        #TODO: Get Store 
        price = 0
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
