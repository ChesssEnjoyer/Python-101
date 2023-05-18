# /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

tczyn = "t"

while tczyn != "n":
    bok1, bok2, bok3 = input("Podaj dlugosc trzech bokow oddzielone przecinkami").split(",")

    print("Podane boki: ", bok1, bok2, bok3)
    a = int(bok1)
    b = int(bok2)
    c = int(bok3)

    if a + b > c and a + c > b and b + c > a:
        print("Mozna zbudowac trojkat")
        if (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2):
            print("Trojkat ten jest prostokatny")
        print("Obwod: ", (a+b+c))
        p = 0.5 * (a + b  + c)
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole:", P)
        tczyn = "n"
    else:
        print("Nie da sie zbudowac trojkata :(")
        tczyn = input("Jeszcze raz?(t/n)")
