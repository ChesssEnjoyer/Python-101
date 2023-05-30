#! usr/bin/env python3

import json
import pymysql
from api_school import app
from config import mysql
from flask import jsonify
from flask import request


def validate(check):
    blocked = [";", "<", ">"]
    if any([x in check for x in blocked]):
        quit()



def connect():
    connect = mysql.connect()	
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    
    return connect, cursor
    
    
def connection_close(connection, cursor):
    connection.close()
    cursor.close()
    return "Closed"


def query_execute(connection, cursor, query, data):
    cursor.execute(query, data)
    connection.commit()
    return "Query executed successfully!"
    


@app.route('/students/add', methods=['POST'])
def add_student():
    try:
        connection, cursor = connect()
        tab = request.json
        for i in range(0, len(tab)):
            dict = tab[i]
            validate(dict)
            _name = dict['FirstName']
            _lastname = dict['LastName']
            _class = dict['class']
            if _name and _lastname and _class and request.method == 'POST':
                data = (_name, _lastname, _class)
                query1 = "SELECT * FROM students WHERE FirstName = %s AND LastName = %s AND class = %s"
                boolean = cursor.execute(query1, data)
                if boolean != 1:
                    query = "INSERT INTO students(FirstName, LastName, class) VALUES(%s, %s, %s)"
                    query_execute(connection, cursor, query, data)
                else:
                    exist ='This student already exists in our system.' 
                    return exist
        return 'Query executed successfully'
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)        
     
     
@app.route('/students/list')
def students_list():
    try:
        connection, cursor = connect()
        query = "SELECT id, FirstName, LastName, class FROM students"
        cursor.execute(query)
        stdRows = cursor.fetchall()
        respone = jsonify(stdRows)
        return respone
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)


@app.route('/students/details')
def student_details():
    try:
        connection, cursor = connect()
        tab = request.json
        response = []
        
        for i in range(0, len(tab)):
            dict = tab[i]
            validate(dict)
            
            if dict.get('id') is not None:
                data = dict['id']
                query = "SELECT * FROM students WHERE id = %s"
            elif dict.get('FirstName') is not None:
                data = dict['FirstName']
                query = "SELECT * FROM students WHERE FirstName = %s"
            elif dict.get('LastName') is not None:
                data = dict['LastName']
                query = "SELECT * FROM students WHERE LastName = %s"
            elif dict.get('class') is not None:
                data = dict['class']
                query = "SELECT * FROM students WHERE class = %s"
            cursor.execute(query, data)
            stdRow = cursor.fetchall()
            response.append(stdRow)
        return response
    
    except Exception as e:
        print(e)
        
    finally:
        connection_close(connection, cursor) 


@app.route('/students/update', methods=['PUT'])
def students_update():
    try:
        connection, cursor = connect()
        tab = request.json
        for i in range(0, len(tab)):
            dict = tab[i]
            validate(dict)
            _name = dict['FirstName']
            _lastname = dict['LastName']
            _class = dict['class']
            _id = dict['id']
            if _name and _lastname and _class and _id and request.method == 'PUT':			
                query = "UPDATE students SET FirstName=%s, LastName=%s, class=%s WHERE id=%s"
                data = (_name, _lastname, _class, _id)
                query_execute(connection, cursor, query, data)
            else:
                return showMessage()
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)
        return "Query executed succesfully"
        

@app.route('/students/delete', methods=['DELETE'])
def delete_std():
    try:
        connection, cursor = connect()
        tab = request.json
        for i in range(0, len(tab)):
            dict = tab[i]
            validate(dict)
            _id = dict['id']
            query = "DELETE FROM students WHERE id = %s"
            query_execute(connection, cursor, query, _id)
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)
        return "Query executed successfully"
        
       
@app.errorhandler(404)
def showMessage(self):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    return respone
        
if __name__ == "__main__":
    app.debug = True
    app.run()