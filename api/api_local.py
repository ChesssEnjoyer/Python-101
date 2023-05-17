#! usr/bin/env python3

import requests
import json

url = "http://localhost:3000/users/1"
url1 = "http://localhost:3000/users/2"
url2 = "http://localhost:3000/users/3"

todo1 = {"id": 3, "name": "James", "age": 45}
todo2 = {"name": "Jacob"}

headers =  {"Content-Type":"application/json"}

response1 = requests.get(url)
response2 = requests.put(url1, todo1)
response3 = requests.patch(url2, todo2)

print("Operation: \n", response1.json())
print("Returned status code: ", response1.status_code)

print("Operation: \n", response2.json())
print("Returned status code: ", response2.status_code)

print("Operation: \n", response3.json())
print("Returned status code: ", response3.status_code)

