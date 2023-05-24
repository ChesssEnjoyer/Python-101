#! usr/bin/env python3
import json
from flask import jsonify
from flask import Flask
from re import search

# app = Flask(__name__)

# json = {"age": 12, "name": "karol", "age": 12, "name": "piotr"}
# array = json.loads(json)
# x = len(array)
# for i in range(x):
#     print(array[x-4])
#     x+=1

# def func():
#     seba = "seba"
#     adi = "adi"
#     karol = "karol"
#     a = 4
#     with app.app_context():
#         st = jsonify("Imie")
#         print(st)
#     a = a**2
    
#     return seba, adi, karol, a

# adi, karol, seba, a= func()


def validate(check):
    ara = [";", "<", ">"]
    if any([x in check for x in ara]):
        print("spierdalaj")
    else:
        print("Jest ok")
        
slowko = "elo>"
validate(slowko)