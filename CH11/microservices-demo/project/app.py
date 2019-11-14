import  pymysql
from store import Store
from customer import Customer
import threading

dbServerName = "192.168.49.117"
dbUser = "root"
dbName = "socksdb"
charSet = "utf8mb4"
dbPort = 5433


addresses = [('172.16.17.108', 'Marco'),
             #('172.16.17.151', 'Jordan'),
             ('172.16.17.106', 'Tim'),
             ('172.16.17.104', 'Kyle'),
             ('172.16.17.169', 'Andrew'),
             ('172.16.17.133', 'Hocine'),
             #('172.16.17.203', 'Kai'),
             ('172.16.17.166', 'JP'),
             ]
stores = []
product = {'sock_id':'3395a43e-2d88-40de-b95f-e00e1502085b',
           'name':'Colourful', 
           'price':'100',
           'count':'1000',
           }

def initialize_stores():
    sql_query = 'UPDATE sock SET price = '+ product['price'] + ', count = '\
        + product['count'] + ' WHERE sock_id = ' +"'" +product['sock_id']+"'"
    for store in stores:
        try:
            connection = pymysql.connect(db=dbName, user=dbUser, host=store.address, port=dbPort) 
            cr = connection.cursor()  
            cr.execute(sql_query)
            connection.commit()
            connection.close()
        except Exception as e:
            print("Set up for "+ store.name + " ERROR==>" + str(e))
        else:
            print("Set up for "+ store.name + " DONE!!")
            

def generate_customers(stores=['localhost'], quantity=10, visits=1):
    count = 0
    while count < quantity:
        yield Customer(stores, visits)
        count += 1



def main():
    customers = generate_customers(stores, 200, 3)
    for customer in customers:
        customer.go_shopping_for_socks()
        print("Summary of accounts:")
        for store in stores:
            print(store.name + " : " + str(store.money))
            print("Socks Sold:" + str(store.socks_sold) + "\n")

if __name__ == "__main__":
    threads = []
    for address in addresses:
        stores.append(Store(address[0], address[1]))
    initialize_stores()
    for store in stores:
        t = threading.Thread(target = main(), args=[])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
