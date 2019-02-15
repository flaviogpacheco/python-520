#!/usr/bin/python3

# Criar uma função que recebe uma letra
# e retorna esta letra em maiusculo

def upper(letra):
    return letra.upper()

print(upper('H'))

letras = ['a', 'Z', 'b', 'c', 'A']
ordenadas = sorted(letras)

for l in ordenadas:
    print(l)
