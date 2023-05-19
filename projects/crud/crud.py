#! usr/bin/env python3

import mysql.connector
import json
from mysql.connector import Error
from re import search

config = json.load(open('config.json'))
array = ()


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

    
def create(connection, array):
    table = input('To what table you want insert record? ')
    validate(table)
    col_name=(f'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{table}"')
    cursor = connection.cursor()
    result = None
    cursor.execute(col_name)
    results = cursor.fetchall()
    for result in results:
        array += result
    print(array)
    values = input('What values you want to insert? ')
    validate(values)
    query = (f'INSERT INTO {table} VALUES ({values});')
    operation(connection, query)


def read(connection):
    cursor = connection.cursor()
    result = None
    columns = input('What do you want to select? ')
    table = input('From what table? ')
    validate(columns)
    validate(table)
    query = (f'SELECT {columns} FROM {table} ;')
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
    except Error as err:
        print(f"Error: '{err}'")


def update(connection, array):
    table = input('What table do you want to update? ')
    validate(table)
    col_name=(f'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{table}"')
    
    cursor = connection.cursor()
    result = None
    cursor.execute(col_name)
    results = cursor.fetchall()
    for result in results:
        array += result
    print(array)
    columns = input('What do you want to update (column_name = "value")? ')
    where = input('For which record (WHERE clause)? ')
    validate(columns)
    validate(where)
    query = (f'UPDATE {table} SET {columns} WHERE {where};')
    operation(connection, query)
    connection.commit()


def delete(connection):
    table = input('In which table do you want to delete? ')
    where = input('For which record (WHERE clause)? ')
    validate(table)
    validate(where)
    query = (f'DELETE FROM {table} WHERE {where}')
    operation(connection, query)
    connection.commit()


def main():
    db = input("What database you want to connect? ")
    connect = create_server_connection(config['host'], config['user'], config['password'], db)
    while True:
        answer = input('Do you want to do something with database?(y/n) ').lower()
        if answer == 'n':
            connect.close()
            exit()
        option = input('What do you want to do(c/r/u/d)? ').lower()
        if option == 'c':
            create(connect, array)
        elif option == 'r':
            read(connect)
        elif option == 'u':
            update(connect)
        elif option == 'd':
            delete(connect)
        else:
            print('Select right option!!!')
            
            
main()