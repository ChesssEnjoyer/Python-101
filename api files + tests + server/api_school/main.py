import pymysql
from api_school import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_std():
    try:        
        _json = request.json
        _name = _json['FirstName']
        _lastname = _json['LastName']
        _class = _json['class']
        if _name and _lastname and _class and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO students(FirstName, LastName, class) VALUES( %s, %s, %s)"
            bindData = (_name, _lastname, _class)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Student added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
@app.route('/students')
def std():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, FirstName, LastName, class FROM students")
        stdRows = cursor.fetchall()
        respone = jsonify(stdRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/students/')
def student_details():
    try:
        _json = request.json
        _id = _json['id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM students WHERE id =%s", _id)
        stdRow = cursor.fetchone()
        respone = jsonify(stdRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/update', methods=['PUT'])
def update_std():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['FirstName']
        _lastname = _json['LastName']
        _class = _json['class']
        if _name and _lastname and _class and _id and request.method == 'PUT':			
            sqlQuery = "UPDATE students SET FirstName=%s, LastName=%s, class=%s WHERE id=%s"
            bindData = (_name, _lastname, _class , _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Student updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/delete', methods=['DELETE'])
def delete_std():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.json
        _id = _json['id']
        cursor.execute("DELETE FROM students WHERE id = %s", _id)
        conn.commit()
        response = jsonify('Student deleted successfully')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.debug = True
    app.run()