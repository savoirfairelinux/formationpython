import json
import threading

import pymysql
import requests

HOSTS = ['172.16.17.91',  # simone
         '172.16.17.81',  # jp
         '172.16.17.51',  # yassine
         '172.16.17.85',  # marc
         '172.16.17.132',  # bilal
         '172.16.17.143',  # mikhail
         ]

DB_CONFIG = {
    "dbServerName": "127.0.0.1",
    "dbUser": "root",
    "dbName": "socksdb",
    "charSet": "utf8mb4",
    "dbPort": 5432
}

RESULTS = {}


def do_it_all():
    _scrape_pages()

    hosts_colourfuls = {}
    for host, catalogue in RESULTS.items():
        hosts_colourfuls[host] = _get_colourful_price(catalogue)

    lowest_price = _get_lowest(hosts_colourfuls.values())
    new_price = lowest_price * 0.95
    if new_price >= 10:
        _set_price(_db_connect(), new_price)


def _set_price(connection, price):
    try:
        cr = connection.cursor()
        sql_query = f'UPDATE sock SET price={price} WHERE name="Colourful"'
        cr.execute(sql_query)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()


def _db_connect():
    return pymysql.connect(db=DB_CONFIG['dbName'],
                           user=DB_CONFIG['dbUser'],
                           host=DB_CONFIG['dbServerName'],
                           port=DB_CONFIG['dbPort']
                           )


def _get_lowest(lst):
    return min(lst)


def _scrape_pages():
    threads = []
    for host in HOSTS:
        t = threading.Thread(target=_scrape, args=[host])

        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def _scrape(url):
    try:
        page_url = f"http://{url}/catalogue"
        print(f"scraping {page_url}...")
        response = requests.get(page_url, timeout=2)
        if response is not None:
            RESULTS['host'] = json.loads(response.content)
    except Exception as e:
        pass


def _get_colourful_price(products):
    for product in products:
        if product is not None:
            if product['name'] == 'Colourful':
                return product['price']


if __name__ == '__main__':
    while True:
        do_it_all()
