# -*- coding: utf-8 -*-
"""
#5- Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida.
#Em seguida, mostre-os em ordem crescente e decrescente.
"""

a = float(input('didite a '))
b = float(input('didite b '))
c = float(input('didite c '))

d = c = [a, b, c]

j = 1

for i in range(len(c)):
    for j in range(len(c)):

        if c[i] < c[j]:
            aux = c[i]
            c[i] = c[j]
            c[j] = aux

print('crescente', c)

for i in range(len(d)):
   for j in range(len(d)):

       if d[i] > d[j]:

           aux = d[i]
           d[i] = d[j]
           d[j] = aux

print('decrescente', d)
