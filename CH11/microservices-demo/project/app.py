import  pymysql

dbServerName = "localhost"
dbUser = "root"
dbName = "socksdb"
charSet = "utf8mb4"
dbPort = 5432

connection = pymysql.connect(db=dbName, user=dbUser, host=dbServerName, port=dbPort) 

try:
    cr = connection.cursor()  
    sqlQuery = "show tables"
    cr.execute(sqlQuery)
    rows = cr.fetchall()
except Exception as e:
    print(e)
finally:
    connection.close()