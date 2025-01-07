import mysql.connector
from mysql.connector import Error

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host = 'tuya.mysql.pythonanywhere-services.com',
            user = 'tuya',
            password = 'tuyadatabases',
            database = 'tuya$moment-logistics'
            )

        return connection
    except Error as e:
        print(f"The error '{e}' occured")
        return None