#! usr/bin/env python3

import mysql.connector
import json
from mysql.connector import Error
from re import search
array = ()

config = json.load(open('config.json'))

def create_server_connection(host, user, password, database):
    connection = None
    try: 
        connection = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
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

def validate(check):
    if search(";", check):
        print('Do not use ";". Script does it automatly.')
        exit()


def show_db(connection, array):
    query = ('SHOW DATABASES')
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        array += result
    print(array)


def show_tb(connection, array):
    query = ('SHOW TABLES')
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        array += result
    print(array)


def create_tb(connection):
    table = input("Table name: ")
    validate(table)
    columns = input('What columns will be in this table? (eg. id INT PRIMARY KEY, name VARCHAR(15)) ')
    validate(columns)
    query = (f'CREATE TABLE {table} ({columns})')
    operation(connection, query)
    connection.commit()
    show_tb(connection, array)


def delete_tb(connection):
    table = input("Table name: ")
    validate(table)
    query = (f'DROP TABLE {table}')
    operation(connection, query)
    connection.commit()
    show_tb(connection, array)
    
    
def create_db(connection):
    db = input("Database name: ")
    validate(db)
    query = (f'CREATE DATABASE {db}')
    operation(connection, query)
    connection.commit()
    show_db(connection, array)
    

def delete_db(connection):
    db = input("Database name: ")
    validate(db)
    query = (f'DROP DATABASE {db}')
    operation(connection, query)
    connection.commit()
    show_db(connection, array)
    
    
def main():
    db = input("What database you want to connect? ")
    connect = create_server_connection(config['host'], config['user'], config['password'], db)
    while True:
        answer = input('Do you want to create/delete table, database or nothing?(1/2/3/4/5) ')
        if answer == '5':
            connect.close()
            exit()
        elif answer == '4':
            delete_db(connect)
        elif answer == '3':
            create_db(connect)
        elif answer == '2':
            delete_tb(connect)
        elif answer == '1':
            create_tb(connect)
        else:
            print("Choose correct option!")

            
main()