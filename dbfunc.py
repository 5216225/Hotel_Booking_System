import mysql.connector
from mysql.connector import errorcode
 
# MYSQL CONFIG VARIABLES
hostname    = "127.0.0.1"
username    = "rutvik2samant"
passwd  = "Innsworth@164"
db = "rutvik2samant"

def getConnection():    
    try:
        conn = mysql.connector.connect(host=hostname, user=username, password=passwd, database=db)  
        print("sql ")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or Password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)                        
    else:  #will execute if there is no exception raised in try block
        return conn         