import  pymysql
from store import Store
from customer import Customer

dbServerName = "192.168.49.117"
dbUser = "root"
dbName = "socksdb"
charSet = "utf8mb4"
dbPort = 5432


addresses = ['172.16.17.91',  # Simone
             '172.16.17.81',  # Jean-Philippe
             '172.16.17.30',  # Gary
             '172.16.17.51',  # Yassine
             '172.16.17.85',  # Marc
             '172.16.17.132', # Bilal
             '172.16.17.143',  # Mikhail
             ] 
stores = []
product = {'sock_id':'3395a43e-2d88-40de-b95f-e00e1502085b',
           'name':'Colourful', 
           'price':'50',
           'count':'100',
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
        except Exception as e:
            print("Set up for "+ store.address + " ERROR==>" + e)
        else:
            print("Set up for "+ store.address + " DONE!!")
        finally:
            connection.close()

def generate_customers(stores=['localhost'], quantity=10, visits=1):
    count = 0
    while count < quantity:
        yield Customer(stores)
        count += 1



def main():
    for address in addresses:
        stores.append(Store(address))
    initialize_stores()
    customers = generate_customers(addresses, 500, 7)

    for customer in customers:
        customer.go_shopping_for_socks()

if __name__ == "__main__":
    main()


