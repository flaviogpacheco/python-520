#!/usr/bin/python3
# ==,  !=, <, <=, >, >=
# Se o numero resultado da soma for maior 100
# Escrever: "Que numero grandão..."
# Caso contrário: "Que numero pequeno..."

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = n1 + n2

print(n3) 

if  n3 > 100:
    print('Que número grandão...')
elif n3 == 50:
    print('...')
else:    
    print('Que número pequeno...')

