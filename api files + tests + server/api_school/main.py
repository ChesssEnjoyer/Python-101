#! usr/bin/env python3

import pymysql
from api_school import app
from config import mysql
from flask import jsonify
from flask import request


def json():
    _json = request.json
    _name = _json['FirstName']
    _lastname = _json['LastName']
    _class = _json['class']
    _id = _json['id']
    
    return _name, _lastname, _class, _id


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
        _name, _lastname, _class, _id= json()
        if _name and _lastname and _class and request.method == 'POST':
            query = "INSERT INTO students(FirstName, LastName, class, id) VALUES( %s, %s, %s, %s)"
            data = (_name, _lastname, _class, _id)
            return query_execute(connection, cursor, query, data)
        else:
            return showMessage()
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
        _id = request.json['id']
        connection, cursor = connect()	
        query = "SELECT * FROM students WHERE id = %s"
        cursor.execute(query, _id)
        stdRow = cursor.fetchone()
        respone = jsonify(stdRow)
        return respone
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor) 

@app.route('/students/update', methods=['PUT'])
def students_update():
    try:
        connection, cursor = connect()
        _name, _lastname, _class, _id= json()
        if _name and _lastname and _class and _id and request.method == 'PUT':			
            query = "UPDATE students SET FirstName=%s, LastName=%s, class=%s WHERE id=%s"
            data = (_name, _lastname, _class, _id)
            return query_execute(connection, cursor, query, data)
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)

@app.route('/students/delete', methods=['DELETE'])
def delete_std():
    try:
        connection, cursor = connect()
        _id = request.json['id']
        query = "DELETE FROM students WHERE id = %s"
        return query_execute(connection, cursor, query, _id)
    except Exception as e:
        print(e)
    finally:
        connection_close(connection, cursor)
        
       
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