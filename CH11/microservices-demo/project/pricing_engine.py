import itertools
import json
import math
import decimal

from multiprocessing import Pool

import threading

import requests

from collections import defaultdict

from buyAndSellApi import DBConnect

MY_STORE = 'MY_STORE'

def floorNDigits(value, decimals):
    with decimal.localcontext() as ctx:
        d = decimal.Decimal(value)
        ctx.rounding = decimal.ROUND_DOWN
        return float(round(d, decimals))

def get_expected_values(stores, msrp = 10):
    profits = defaultdict(int)

    if (len(stores) == 1):
        return { stores[0][0]: 999999999 }

    permutations = itertools.permutations(stores, min([3, len(stores)]))

    count = 0

    for permutation in permutations:
        count += 1
        smallest = min(permutation, key=lambda x: x[1])
        winners = [store for store in permutation if store[1] == smallest[1]]
        for winner in winners:
            profits[winner[0]] += (winner[1] - msrp) / len(winners)

    return {  name: floorNDigits(profits[name] / count, 2) for name, _ in stores }

def process(args):
    other_stores, my_price = args
    return (my_price, get_expected_values([*other_stores, (MY_STORE, my_price)]))

def get_optimal_price(other_stores, msrp = 10):
    if (not len(other_stores)): return 9999999

    my_prices = [(other_stores, max([msrp, floorNDigits(store[1], 2) - 0.01])) for store in other_stores]

    pool = Pool(5)

    results = pool.map(process, my_prices)

    highest_ev = 0
    best_price = msrp
    best_expected_values = None

    for my_price, expected_values in results:
        if expected_values[MY_STORE] >= highest_ev:
            highest_ev = expected_values[MY_STORE]
            best_price = my_price
            best_expected_values = expected_values

    print('Current prices:')
    print({name: f'{price}$' for name, price in other_stores})
    print(f'optimal price is: {best_price}$ with an EV of {highest_ev}$')
    print('Current Expected Values:')
    print({name: f'{price}$' for name, price in best_expected_values.items()})
    print('\n==================\n')

    return best_price

addresses = [
    '172.16.17.108',
    '172.16.17.151',
    '172.16.17.106',
    '172.16.17.169',
    '172.16.17.203',
    '172.16.17.133',
    '172.16.17.166'
]

import aiohttp
import asyncio

async def fetch(name, session):
    headers = {'User-Agent': '$BOSS$'}
    try:
        async with session.get(
            f'http://{name}:8000/product/Colourful',
            headers=headers,
            ssl=False,
            timeout=aiohttp.ClientTimeout(
                total=None,
                sock_connect=0.1,
                sock_read=0.1
            )
        ) as response:
            return (name, await response.json())
    except Exception:
        return None

# async def main():
#     connection = DBConnect('Colourful')

#     async with aiohttp.ClientSession() as session:
#         print('==================\n')
#         tasks = [
#             asyncio.ensure_future(fetch(url, session))
#             for url in addresses
#         ]

#         responses = await asyncio.gather(*tasks)

#         stores = [
#             (response[0], response[1]['price'])
#             for response in responses
#             if response is not None
#         ]

#         new_price = get_optimal_price(stores)
#         print(f'setting price to {new_price}')
#         connection.setProductPrice(new_price)
#         print('\n')

#     return stores

################# V2 #################

def update_prices(name, stores, connection):
    try:
        result = requests.get(
            f'http://{name}:8000/product/Colourful',
            timeout=100
        ).json()
    except Exception:
        return

    store_name = name
    store_price = result['price']

    if store_name not in stores or stores[store_name] != store_price:
        stores[store_name] = store_price
        update_to_optimal_price(stores.copy(), connection)

def update_to_optimal_price(stores, connection):
    new_price = get_optimal_price(list(stores.items()))
    print(f'setting price to {new_price}$')
    connection.setProductPrice(new_price)
    print('\n')

def mainV2():
    connection = DBConnect('Colourful')
    stores = {}

    def update_prices_for(name):
        while True:
            update_prices(name, stores, connection)

    tasks = [
        threading.Thread(target=update_prices_for, args=(url,))
        for url in addresses
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

# asyncio.run(main())
mainV2()