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

def read(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
    except Error as err:
        print(f"Error: '{err}'")

def main():
    connect = create_server_connection(host_name, user_name, user_password, db_name)
    while True:
        answer = input('Do you want to do something with database?(y/n) ').lower()
        if answer == 'n':
            break
        option = input('What do you wnat do to(c/r/u/d)? ').lower()
        if option == 'r':
            first = input('What do you want to select? ')
            second = input('From what table? ')
            query = (f'SELECT {first} FROM {second} ;')
            read(connect, query)
        elif option == 'c':
            first = input('What table do you want to create? ')
            second = input('What are columns (column_name TYPE)? ')
            query = (f'CREATE TABLE {first} ({second});')
            operation(connect, query)
        elif option == 'u':
            first = input('What table do you want to update? ')
            second = input('What do you want to update (column_name = "value")? ')
            third = input('For which record (WHERE clausule)? ')
            query = (f'UPDATE {first} SET {second} WHERE {third};')
            operation(connect, query)
            connect.commit()
        elif option == 'd':
            first = input('In what table do you want to delete smth? ')
            second = input('For which record (WHERE clausule)? ')        
            query = (f'DELETE FROM {first} WHERE {second}')
            operation(connect, query)
            connect.commit()
        else:
            print('Wybierz poprawna opcje!!!')
main()

