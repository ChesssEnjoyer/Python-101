#! usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def wprowadz_dane():
    while True:
        slowo = input("Podaj obcy wyraz (lub wpisz 'koniec' aby zakończyć): ")
        if slowo == "koniec":
            break
        znaczenia = input("Podaj znaczenia oddzielone przecinkami: ")
        lista_znaczen = znaczenia.split(",")
        lista_znaczen = [z.strip() for z in lista_znaczen]
        slownik[slowo] = lista_znaczen

def zapisz_do_pliku(nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        json.dump(slownik, plik)

def wczytaj_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        return json.load(plik)

def wyswietl_slownik(slownik):
    print("Słownik:")
    for slowo, znaczenia in slownik.items():
        print(slowo + ":", ", ".join(znaczenia))

def usun_wpis(slownik):
    slowo = input("Które słowo chcesz usunąć? ")
    if slowo in slownik:
        del slownik[slowo]
        print("Wpis został usunięty.")
    else:
        print("Nie znaleziono takiego słowa.")

def ucz_sie(slownik):
    slowa_do_nauczenia = list(slownik.keys())
    while slowa_do_nauczenia:
        slowo = slowa_do_nauczenia.pop(0)
        znaczenia = slownik[slowo]
        print("Jakie są znaczenia słowa", slowo + "?")
        odpowiedzi = input("Podaj znaczenia oddzielone przecinkami: ")
        odpowiedzi = [z.strip() for z in odpowiedzi.split(",")]
        poprawne = [z for z in znaczenia if z in odpowiedzi]
        if poprawne:
            print("Poprawne odpowiedzi:", ", ".join(poprawne))
        else:
            print("Brak poprawnych odpowiedzi.")

nazwa_pliku = "slownik.json"
try:
    slownik = wczytaj_z_pliku(nazwa_pliku)
except FileNotFoundError:
    slownik = {}

while True:
    print("\nCo chcesz zrobić?")
    print("1. Wprowadzić nowe dane")
    print("2. Zmienić istniejące dane")
    print("3. Wyświetlić słownik")
    print("4. Usunąć wpis")
    print("5. Uczyć się")
    print("6. Zakończyć program")
    wybor = input("Twój wybór: ")
    if wybor == "1":
        wprowadz_dane()
        zapisz_do_pliku(nazwa_pliku)
    elif wybor == "2":
        slowo = input("Które słowo chcesz zmienić? ")
        if slowo in slownik:
            znaczenia = input("Podaj nowe znaczenia oddzielone przecinkami: ")
            lista_znaczen = znaczenia.split(",")
            lista_znaczen = [z.strip() for z in lista_znaczen]
            slownik[slowo] = lista_znaczen
            zapisz_do_pliku(nazwa_pliku)
            print("Zmiana została zapisana.")
        else:
            print("Nie znaleziono takiego słowa.")
    elif wybor == "3":
        wyswietl_slownik(slownik)
    elif wybor == "4":
        usun_wpis(slownik)
        zapisz_do_pliku(nazwa_pliku)
    elif wybor == "5":
        ucz_sie(slownik)
    elif wybor == "6":
        break
    else:
        print("Nieprawidłowy wybór.")
