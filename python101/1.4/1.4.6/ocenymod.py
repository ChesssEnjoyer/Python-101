#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def drukuj(a, kom="Sekwencja zawiera: "):
    print(kom)
    for i in a:
        print(i, end=" ")

def srednia(oceny):
    suma = sum(oceny)
    return suma / float(len(oceny))

def mediana(oceny):
    oceny.sort()
    if len(oceny)%2 == 0:
        half = int(len(oceny) / 2)
        return float((oceny[half-1]+oceny[half]) / 2.0)
    else:
        return oceny[int(len(oceny)/2)]

def wariancja(oceny, srednia):
    s=0.0
    for ocena in oceny:
        s += (ocena-srednia)**2
    return s / len(oceny)

def odchylenie(oceny, srednia):
    w = wariancja(oceny, srednia)
    return math.sqrt(w)
