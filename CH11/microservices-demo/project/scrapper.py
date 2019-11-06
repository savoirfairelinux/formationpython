import requests
import ipdb
import json
from multiprocessing.pool import ThreadPool
import time


ips = [
 '172.16.17.91',
 '172.16.17.30',
 '172.16.17.51',
 '172.16.17.85',
 '172.16.17.132',
 '172.16.17.143',
]

def get_socks(url):
 try:
  response = requests.get('http://' + url + '/catalogue');
  socks = json.loads(response.content)
  return socks
 except ConnectionError:
  print('error with ip: ' + url)
  return 10000

def get_all_prices():
 results = []

 pool = ThreadPool(len(ips))

 for ip in ips:
  results.append(pool.apply_async(get_socks, (ip,)))  # tuple of args for foo)

 results = [r.get() for r in results]

 pool.close()
 pool.join()

 return results

def get_price(catalogue, product_name):
 for product in catalogue:
  if product['name'] == product_name:
   return product['price']

def get_min_price(catalogues, product_name):
 price = 1000000
 for catalogue in catalogues:
  new_price = get_price(catalogue, product_name)
  if new_price < price:
   price = new_price

 return price

def update_price(product_name, price):
 data = {
  'price': price
 }
 requests.put('http://localhost:8000/product/' + product_name, data=json.dumps(data));


def magic():
 prices = get_all_prices()
 product = 'Colourful'
 min_price = get_min_price(prices, product)
 # new_price = max(10, float(min_price) - 0.1);
 new_price = float(min_price) - 0.1
 # if new_price == 10:
 #  new_price = float(10.001)
 update_price(product, new_price)
 print('Up ' + str(new_price))

while True:
 magic()
 time.sleep(1)