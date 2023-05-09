#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

n = int(input("Ile liczb ma miec lista? "))
lista = []
for i  in range(0, n):
    lista.append(randint(0, 100))

print("Elementy listy i ich indeksy: ")
x= 0 
for i, v in enumerate(lista):
    print("[",i,"]", v, end=" ")
    x+=1
    if x == 3:
        print()
        x=0
print("\n")

print("Elementy w odwroconej kolejnosci: ")
for a in reversed(lista):
    print(a, end=" ")
print("\n")

print("Lista posortowana")
for a in sorted(lista):
    print(a, end=" ")
print("\n")

tczyn = input("Czy chcesz usunac jakas liczbe? (t/n) ")
if tczyn == "t":
    r = int(input("Jaka liczbe chcesz usunac? "))
    lista.remove(r)
    print(lista, "\n")
else :
    print()

tcn = input("Czy chcesz usunac liczbe o konkretnym indeksie? (t/n) ")
if tcn == "t":
    ind = int(input("Element o jakim indeksie chcesz usunac? "))
    del lista[ind]
    print(lista, "\n")
else:
    print()

c = int(input("Podaj liczbe ktora chcesz sprawdzic "))
print("Liczba ta wystepuje: ", lista.count(c), "razy")
if lista.count(c):
    print("Indeks wystapienia po raz pierwszy: ", lista.index(c), "\n")
else:
    print("Ta liczba nie wystepuje w liscie \n")

i, j = eval(input("Podaj pierwszy i ostatni indeks wycinka listy ktory chcesz wyswietlic oddzielone przecinkiem"))
print(lista[i:j])
