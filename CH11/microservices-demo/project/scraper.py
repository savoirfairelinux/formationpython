import json
import urllib
import requests
import concurrent.futures

addresses = [
             'http://172.16.17.91:8000/product/Colourful',
             'http://172.16.17.81:8000/product/Colourful',
             'http://172.16.17.30:8000/product/Colourful',
             'http://172.16.17.51:8000/product/Colourful',
             'http://172.16.17.85:8000/product/Colourful']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def get_all_external_products():
    resp_err = 0
    resp_ok = 0
    data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        future_to_url = {executor.submit(load_url, url, 1): url for url in addresses}
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                print('in here')
                data.append(future.result())
            except Exception as exc:
                resp_err = resp_err + 1
            else:
                resp_ok = resp_ok + 1
        executor.shutdown(wait=True)
        get_prices_per_product(data)
    pass


def get_prices_per_product(data):
    min = 100
    for d in data:
        data_json = json.loads(d)
        if min > data_json['price']:
            min = float(data_json['price'])
    min = min - 0.000001

    if min >= 10:
        requests.put('http://localhost:8000/product/Colourful', data=json.dumps({'product': 'Colourful', 'price': min}))

    print(min)


if __name__ == '__main__':
    while True:
        get_all_external_products()
