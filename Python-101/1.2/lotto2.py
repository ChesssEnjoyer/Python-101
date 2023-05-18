#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

try: 
    ileliczb = int(input("Ile liczb chialbys wylosowac? "))
    maksliczba = int(input("Podaj maksymalna liczbe losowania "))

    if ileliczb > maksliczba : 
        print("Bledne dane!")
        exit()
except ValueError:
    print("Bledne dane!")
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba)==0:
        liczby.append(liczba)
        i = i + 1

for i in range(3):
    print("Wytypuj %s z %s liczb: " %(ileliczb, maksliczba))
    lista = set()
    i = 0
    while i < ileliczb:
        try:
            typ  = int(input("Podaj liczbe %s: " %(i + 1)))
        except ValueError:
            print("Bledne dane!")
            continue

        if 0 < typ <= maksliczba and typ not in lista:
            lista.add(typ)
            i = i + 1 

    trafione = set(liczby) & lista
    if trafione:
        print("\nIlosc trafien: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Nic nie trafiles")

    print("\n" + "X" * 30 + "\n")

print("Wylosowane liczby to: ", liczby)
