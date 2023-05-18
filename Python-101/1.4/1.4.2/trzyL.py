#! /usr/bin/env python3
# -*- coding: utf-8 -*-

tczyn = "t"
while tczyn.lower() == "t":
    a, b, c = input("Podaj trzy liczby").split(",")

    print("Podane liczby to:", a, b, c)
    print("Najmniejsza liczba to: ")
    if a < b:
        if a < c:
            najmniejsza = a
        else: 
            najmniejsza = c
    elif b < c:
        najmnijesza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    tczyn = input("Powtarzamy? (t/n)")

