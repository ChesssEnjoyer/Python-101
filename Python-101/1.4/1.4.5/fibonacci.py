#! /usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Z ilu liczb ma skladac sie ciag? "))
a, b = 1, 1
print(a)
print(b)
for i in range(1, n-1):
    a, b = b, a+b
    print(b)
