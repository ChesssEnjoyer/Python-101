#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

liczba = random.randint(1, 10)

for i in range(3):
    odp = input("Jaka liczbe od 1 do 10 mam na mysli? ")
    # print("Podana liczba to:", odp)

    if liczba == int(odp):
        print("Zgadles!")
        break
    elif i == 2:
        print("Mialem na mysli liczbe: ", liczba)
    else:
        print("Nie zgadles")
    print()
    
