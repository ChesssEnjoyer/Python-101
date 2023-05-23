#! usr/bin/env python3

import mysql.connector
import json
from mysql.connector import Error
import argparse
from tabulate import tabulate
from re import search

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--option", help="c-insert into table, r-select from table, u-update existing record, d-delete row from table")
parser.add_argument("-t", "--table", help="table name")
parser.add_argument("-c", "--columns", help='column names/ with values (UPDATE [col = "value"])')
parser.add_argument("-w", "--where", help="condition")
parser.add_argument("-v", "--values", help="values of columns")
parser.add_argument("-d", "--database", help="name of databse you want to use", required=True)
args = parser.parse_args()


config = json.load(open('config.json'))


def validate(check):
    if search(";", check):
        print('Do not use ";". Script does it automatly.')
        exit()
        

def db_connect(host, user, password, database):
    connection = None
    try: 
        connection = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
        print("Connected")
    except Error as err:
        print(f"Error: {err}")

    return connection


def send_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed succesfully")
    except Error as err:
        print(f"Error: '{err}'")


def create(connection):
    vals = args.values
    values = vals.replace(',', '", "')
    validate(args.table)
    validate(values)
    query = (f'INSERT INTO {args.table} VALUES ("{values}");')
    send_query(connection, query)
    connection.commit()


def read(connection):
    cursor = connection.cursor()
    result = None
    validate(args.columns)
    validate(args.table)
    if args.columns == 'all':
        query = (f'SELECT * FROM {args.table}')
    else:
        query = (f'SELECT {args.columns} FROM {args.table}')
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        x = []
        for result in results:
            x.append(result)
        print(tabulate(x, tablefmt='fancy_grid'))
    except Error as err:
           print(f"Error: '{err}'")


def update(connection):
    validate(args.table)
    validate(args.columns)
    validate(args.where)
    cols = args.columns
    columns = cols.replace('=', '="')
    column = columns.replace(' ', '" ')
    query = (f'UPDATE {args.table} SET {column}" WHERE {args.where};')
    send_query(connection, query)
    connection.commit()
    
    
def delete(connection):
    validate(args.table)
    validate(args.where)
    query = (f'DELETE FROM {args.table} WHERE {args.where}')
    send_query(connection, query)
    connection.commit()


def operation(connection):
    if args.option == 'c':
        create(connection)
    elif args.option == 'r':
        read(connection)
    elif args.option == 'u':
        update(connection)    
    elif args.option == 'd':
        delete(connection)
    else: 
        print('Error. Select correct options')


def main():
    validate(args.database)
    connect = db_connect(config['host'], config['user'], config['password'], args.database)
    operation(connect)
    connect.close()
    
    
main()