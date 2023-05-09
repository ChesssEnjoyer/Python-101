#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("Alfabet")
x = 0
p = int(input("Co ktora grupa ma sie wyswietlac? "))
c = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera + " => " + litera.lower()
    if i > 65 and x == 5:
        x = 0
        c += 1
        tmp += "\n"
    if c % p == 0: 
        print(tmp, end=" ")
print("Alfabet od konca: ")
y = 0
for i in range(90, 64, -1):
    litera = chr(i)
    y += 1
    tmp = litera.lower() + " => " + litera
    if i > 65 and y == 5:
        y = 0
        c += 1
        tmp += "\n"
    if c % p == 0:
        print(tmp, end=" ")
