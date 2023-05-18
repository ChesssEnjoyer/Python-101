#! usr/bin/env python3

import requests
import json

url1 = "https://jsonplaceholder.typicode.com/todos"
url2 = "https://jsonplaceholder.typicode.com/todos/10"
url3 = "https://jsonplaceholder.typicode.com/todos/4"

todo = {"userId": 1,"id": 201, "title": "Do something", "completed": False}
todo2 = {"userId": 1,"id": 10, "title": "Buy groceries", "completed": True}

headers = {"Content-Type": "aplication/json"}


response1 = requests.post(url1, todo, headers)
response2 = requests.put(url2, todo2)
response3 = requests.get(url3)

print("Operacja: \n", response1.json())
print("Zwrocila kod: ", response1.status_code)

print("Operacja: \n", response2.json())
print("Zwrocila kod: ", response2.status_code)


print("Operacja: \n", response3.json())
print("Zwrocila kod: ", response3.status_code)

