#! usr/bin/env python3

from api_school import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ubuntu12'
app.config['MYSQL_DATABASE_DB'] = 'School'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)