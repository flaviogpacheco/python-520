#!/usr/bin/python3

# Criar uma função que recebe uma letra
# e retorna esta letra em maiusculo

def parama(letra):
    return letra.upper()

letras = ['a', 'Z', 'b', 'c', 'A']
ordenadas = sorted(letras, key=parama)

for l in ordenadas:
    print(l)
