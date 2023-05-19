#! usr/bin/env python3

import mysql.connector
from mysql.connector import cursor
from mysql.connector import Error
import pandas as pd

host_name = 'localhost'
user_name = 'root'
user_password = 'Ubuntu12'
db_name = 'local_base'



def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try: 
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password, database=db_name)
        print("Connected")
    except Error as err:
        print(f"Error: {err}")

    return connection

def operation(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed succesfully")
    except Error as err:
        print(f"Error: '{err}'")

def main():
    connect =  create_server_connection(host_name, user_name, user_password, db_name)
    while True:
        answer = input('Do you want to do something with database?(y/n) ')
        if answer == 'n':
            break
        query = input('Type in query for mysql to execute ')
        operation(connect, query)

main()

