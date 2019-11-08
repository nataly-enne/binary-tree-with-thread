#! /usr/bin/env python
import random
rand = random.random
 
consoantes = 'bcdfghjlmnpqrstvxz'
vogais = 'aeiou'
 
def pegaletra(tipo):
    if tipo == 0:
        return consoantes[int(rand()*len(consoantes))]
    if tipo == 1:
        return vogais[int(rand()*len(vogais))]
 
def gerapalavra():
    tamanho = int(rand()*4+3)
    atual = int(rand()*2)
    palavra = ''
    for letr in range(tamanho+1):
        letra = pegaletra(atual)
        if letra == 'q':
            letra = 'qu'
        palavra = palavra + letra
        if atual == 0:
            atual = 1
        else:
            atual = 0
    return palavra
