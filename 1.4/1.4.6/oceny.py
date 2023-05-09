#! usr/bin/env python3
# -*- coding: utf-8 -*-

from ocenymod import drukuj, srednia, mediana, odchylenie

def main(args):
    przedmioty = set()
    drukuj(przedmioty)

    print("\nAby przerwac dodanie przedmiotu, prosze wciasnac enter")
    while True:
        przedmiot = input("Podaj przedmiot ")
        if len(przedmiot):
            if przedmiot in przedmioty:
                print("Taki przedmiot jest juz dodany")
            przedmioty.add(przedmiot)
        else:
            drukuj(przedmioty)
            przedmiot = input("\nZ jakiego przedmiotu chcesz wprowadzic oceny? ")
            if przedmiot not in przedmioty:
                print("Nie ma takiego przedmiotu ")
            else: 
                break

    oceny = []
    ocena = None
    print("\nAby przerwac wprowadzanie ocen podaj 0")
    while not ocena:
        try:
            ocena = int(input("Podaj ocene"))
            if (ocena > 0 and ocena < 7):
                oceny.append(int(ocena))
            elif ocena == 0:
                break
            else:
                print("Podaj poprawna ocene")
            ocena = None
        except ValueError:
            print("Podaj poprawna ocene")

    drukuj(oceny, przedmiot.capitalize())
    s = srednia(oceny)
    m = mediana(oceny)
    o = odchylenie(oceny, s)
    print("\nSrednia ocen wynosi: ", format(s))
    print("\nMediana ocen wynosi: ", format(m))
    print("\nOdchylenie: ", format(o))
    return 0

if __name__=='__main__':
   import sys
   sys.exit(main(sys.argv))
