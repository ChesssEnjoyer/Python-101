#! usr/bin/env python3
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def func():
    seba = "seba"
    adi = "adi"
    karol = "karol"
    a = 4
    with app.app_context():
        st = jsonify("Imie")
        print(st)
    a = a**2
    
    return seba, adi, karol, a

adi, karol, seba, a= func()
