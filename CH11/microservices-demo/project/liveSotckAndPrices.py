import requests
import json
import time
import os


addresses ={'172.16.17.91':  'Simone',
             '172.16.17.81':  'Jean-Philippe',
             '172.16.17.30': 'Gary',
             '172.16.17.51':  'Yassine',
             '172.16.17.85': 'Marc',
             '172.16.17.132': 'Bilal',
             '172.16.17.143': 'Mikhail'
            }


def getStockAndPrice(url):
    try:
        response = requests.get('http://' + str(url) +
                                   ':8000/product/Colourful', timeout=5).content
        return json.loads(response)
    except:
        return {'NO DATA': 'NO DATA'}


while True:
    os.system('reset')
    for address, name in addresses.items():
        try:
            data = getStockAndPrice(address)
            print("IP " + str(address) + " " + str(name) + "'s  Price " + str(data['price']) + "$ --  And Colourful Count is " + str(data['count']))
        except:
            print('Error on address: ' + str(address))
    time.sleep(3)
    print("=========================")
