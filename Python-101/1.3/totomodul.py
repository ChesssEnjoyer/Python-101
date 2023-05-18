#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os
import json


def ustawienia():

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawienia:\nLiczb: %s\nZ Maks: %s\nLosowan: %s" %
              (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ile = int(input("Podaj ilosc typowanych liczb: "))
                maks = int(input("Podaj maksymalna losowana liczbe: "))
                if ile > maks:
                    print("Bledne dane!")
                    continue
                ilelos = int(input("Ile losowan: "))
                break
            except ValueError:
                print("Bledne dane!")
                continue
        gracz = [nick, str(ile), str(maks), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()
    return gracz


def losujliczby(ile, maks):
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby


def pobierztypy(ile, maks):
    print("Wytypuj %s z %s liczb: " % (ile, maks))
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbe %s: " % (i + 1)))
        except ValueError:
            print("Bledne dane!")
            continue

        if 0 < typ <= maks and typ not in typy:
            typy.add(typ)
            i = i + 1
    return typy


def wyniki(liczby, typy):
    trafione = liczby & typy
    if trafione:
        print("\nIlosc trafien: %s" % len(trafione))
        # print(trafione)
        trafione = ", ".join(map(str, trafione))
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafien")
    print("\n" + "x" * 40 + "\n")

    return len(trafione)


def czytaj_json(nazwapliku):
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane


def zapisz_json(nazwapliku, dane):
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)

