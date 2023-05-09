#! /usr/bin/env python3
# -*- coding: utf-8 -*-
def szyfruj_cezar(tekst, klucz):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                zaszyfrowany_znak = chr((ord(znak) - 65 + klucz) % 26 + 65)
            else:
                zaszyfrowany_znak = chr((ord(znak) - 97 + klucz) % 26 + 97)
        else:
            zaszyfrowany_znak = znak
        zaszyfrowany_tekst += zaszyfrowany_znak
    return zaszyfrowany_tekst


tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz szyfru Cezara: "))

zaszyfrowany_tekst = szyfruj_cezar(tekst, klucz)

print("Zaszyfrowany tekst: ", zaszyfrowany_tekst)

def odszyfruj_cezar(tekst, klucz):
    odszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                odszyfrowany_znak = chr((ord(znak) - 65  - klucz) % 26 + 65)
            else:
                odszyfrowany_znak = chr((ord(znak) - 97 - klucz) % 26 + 97)
        else:
            odszyfrowany_znak = znak
        odszyfrowany_tekst += odszyfrowany_znak
    return odszyfrowany_tekst


tekst = input("Podaj tekst do odszyfrowania: ")
klucz = int(input("Podaj klucz szyfru Cezara: "))

odszyfrowany_tekst = odszyfruj_cezar(tekst, klucz)

print("Odszyfrowany tekst: ", odszyfrowany_tekst)

