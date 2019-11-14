import itertools
import json
import math
import decimal
import requests
import threading

from multiprocessing import Pool
from collections import defaultdict

from buyAndSellApi import DBConnect

MY_STORE = 'MY_STORE'

PRODUCT_NAME = 'Colourful'

STORE_URLS = [
    '192.168.0.141'
]

should_update_price = False

def floor(value):
   return math.floor(value * 100) / 100

def get_expected_values(stores, cost = 10):
    profits = defaultdict(int)
    number_of_stores = len(stores)

    if (number_of_stores == 1):
        return { stores[0][0]: stores[0][1] - cost}

    # this will only work if the numbers of stores is at a maneagable level
    # for 20 stores this would be 6840 permutations whereas for 100 stores this
    # would be 970200 permutations.
    number_of_stores_selected_by_customers = min([3, number_of_stores])
    permutations = itertools.permutations(stores, )

    count_of_permutations = math.factorial(number_of_stores) / math.factorial(
        number_of_stores - number_of_stores_selected_by_customers
    ) if 0 < number_of_stores and number_of_stores <= number_of_stores_selected_by_customers else 0

    for permutation in permutations:
        smallest = min(permutation, key=lambda x: x[1])
        winners = [store for store in permutation if store[1] == smallest[1]]

        for winner in winners:
            # we divide our profit by the number of winners since in the case of
            # a tie the sale will be awarded randomly to one of them.
            profits[winner[0]] += (winner[1] - cost) / len(winners)

    return {  name: profits[name] / count_of_permutations for name, _ in stores }

def _run_get_expected_values(args):
    other_stores, my_price = args

    return (
        my_price,
        get_expected_values([*other_stores, (MY_STORE, my_price)])
    )

def get_optimal_price(other_stores, cost = 10):
    # if we are the only store we want to set our price as high as possible
    if (not len(other_stores)): return 9999999999

    # we will use different prices to get the EV (expected value) of each price
    # we will try to price it at 1 cent less than everyone else
    # and also we will try to price it the same as everyone else
    # we then select the price that gives us the highest expected return
    # it is important to also try the prices that others stores have already
    # selected because they can sometimes have a higher EV than pricing it
    # at 1 cent less.
    # this could for sure be optimized, there are high guesses that we know
    # for sure can never be profitable
    my_prices = list(set(itertools.chain.from_iterable(
        (max([cost, floor(store[1])]), max([cost, floor(store[1]) - 0.01]))
        for store in other_stores
    )))

    pool = Pool(5)

    results = pool.map(
        _run_get_expected_values,
        [(other_stores, price) for price in my_prices]
    )

    highest_ev = 0
    best_price = cost
    best_expected_values = None

    for my_price, expected_values in results:
        if expected_values[MY_STORE] >= highest_ev:
            highest_ev = expected_values[MY_STORE]
            best_price = my_price
            best_expected_values = expected_values

    print('Current prices:')
    print({name: f'{price}$' for name, price in other_stores})
    print(f'optimal price is: {best_price}$ with an EV of {highest_ev}$')

    if best_expected_values is not None:
        print('Current Expected Values:')
        print({name: f'{price}$' for name, price in best_expected_values.items()})

    print('\n==================\n')

    return best_price

def fetch_prices(name, stores):
    try:
        result = requests.get(
            f'http://{name}:8000/product/{PRODUCT_NAME}',
            timeout=100
        ).json()
    except Exception:
        return
    on_price_update(stores, name, result['price'])

def on_price_update(stores, store_name, store_price):
    global should_update_price

    if store_name not in stores or stores[store_name] != store_price:
        stores[store_name] = store_price
        should_update_price = True

def run_price_updater(stores, connection):
    global should_update_price
    while True:
        if (not should_update_price): continue
        should_update_price = False
        # we copy the prices here
        # so that anothre thread doesn't overwrite them while
        # we are processing them
        stores = stores.copy()
        new_price = get_optimal_price(list(stores.items()))
        print(f'setting price to {new_price}$')
        connection.setProductPrice(new_price)
        print('\n')

def run_price_poller_for(name, stores):
    while True: fetch_prices(name, stores)

def main():
    connection = DBConnect('Colourful')
    stores = {}

    threads = [
        threading.Thread(target=run_price_poller_for, args=(url, stores))
        for url in STORE_URLS
    ] + [threading.Thread(target=run_price_updater, args=(stores, connection))]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# print(get_optimal_price((('a', 10.05), ('b', 10.05), ('c', 10.05), ('d', 10.05), ('e', 10.04), ('f', 10.8), ('g', 10.07))))
# print(get_expected_values((('a', 100), ('b', 100), ('c', 11.25), ('d', 10.05), ('e', 10.04), ('f', 10.8), ('g', 10.07))))
# print(get_optimal_price((('a', 100), ('b', 100), ('c', 11.25), ('d', 10.05), ('e', 10.04), ('f', 10.8), ('g', 10.07))))
# print(get_expected_values((('a', 10.70), ('b', 10.42), ('c', 10.29), ('d', 10.17), ('e', 10.23), ('f', 10.25), ('g', 10.69), ('MY_STORE', 10.16))))

main()