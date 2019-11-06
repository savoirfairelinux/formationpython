import  pymysql
from store import Store
from customer import Customer

dbServerName = "192.168.49.117"
dbUser = "root"
dbName = "socksdb"
charSet = "utf8mb4"
dbPort = 5432


addresses = ['192.168.49.117']
stores = []
product = {'sock_id':'3395a43e-2d88-40de-b95f-e00e1502085b',
           'name':'Colourful', 
           'price':'10',
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
        except Exception as e:
            print("Set up for "+ store.address + " ERROR==>" + e)
        else:
            print("Set up for "+ store.address + " DONE!!")
        finally:
            connection.close()

def generate_customers(stores=['localhost'], quantity=10):
    count = 0
    while count < quantity:
        yield Customer(stores)
        count += 1



def main():
    for address in addresses:
        stores.append(Store(address))
    initialize_stores()

if __name__ == "__main__":
    main()


