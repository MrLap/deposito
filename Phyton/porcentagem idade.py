# -*- coding: utf-8 -*-
"""
10- Faça um programa que receba a idade de 15 pessoas e que calcule e mostre: 
A quantidade de pessoas em cada faixa etária; 
A percentagem de pessoas na primeira e na última faixa etária, 
com relação ao total de pessoas.

       faixa1 =   Até 15 anos
       faixa2 =   De 16 a 30 anos
       faixa3 =   De 31 a 45 anos
       faixa4 =  De 46 a 60 anos
       faixa5 =  Acima de 61 anos
"""
import random

p = 15

age = [random.randint(1,100) for i in range(p)]

faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0
 
for i in range(p):
    if age[i] <= 15:
        faixa1 += 1

    elif 16 <= age[i] <= 30:
        faixa2 += 1

    elif 31 <= age[i] <= 45:
        faixa3 += 1

    elif 46 <= age[i] <= 60:
        faixa4 += 1

    else:
        faixa5 += 1

    
def pct(fx):
    if fx == 1:
        return (faixa1 / p) * 100
    if fx == 2:
        return (faixa2 / p) * 100
    if fx == 3:
        return (faixa3 / p) * 100
    if fx == 4:
        return (faixa4 / p) * 100
    if fx == 5:
        return (faixa5 / p) * 100
    
while True:
    gp = int(input('Qual grupo deseja saber a porcentagem? (1, 2, 3, 4 ou 5): '))
    print("Porcentagem do grupo", gp, ":", pct(gp), "%")
    
    sair = input('\n Deseja sair? (q para sair, qualquer outra tecla para continuar): ')
    if sair == 'q':
        break
        
        









































