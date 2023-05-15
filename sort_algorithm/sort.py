#! usr/bin/env python3

lista = [8,4,2,14,6,72,623,5,86,13]
n = len(lista)

def sort_list(list):
    for i in range(n):
        list_sorted = True

        for j in range (n - i - 1):
            if list[j] > list[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                list_sorted = False
        if list_sorted:
            break
    return lista
print(sort_list(lista))
