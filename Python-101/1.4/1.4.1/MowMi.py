#! /usr/bin/env python3
# -*- coding: utf-8 -*-

pythonRok = 1989
aktRok = int(input("Podaj aktualny rok "))
if aktRok == 2023:
    print("Dzieki ze mowisz prawde")
else:
    print("Podaj aktualny rok!!!!")
wiekPython = aktRok - pythonRok

imie = input("Podaj swoje imie ")
wiek = int(input("Podaj swoj wiek "))

print("Mow mi python, mam ", wiekPython, "lat." )
print("Witaj w moim swiecie ", imie)
if wiek > wiekPython:
    print("Jestes starszy ode mnie")
else:
    print("Jestes mlodszy ode mnie")
