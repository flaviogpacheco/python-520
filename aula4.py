#!/usr/bin/python3

# git clone https://github.com/hector-vido/python-520
#append
#Colocar todos os usuarios dentro de uma lista
#Percorrer essa lista, exibindo apenas o nome de cada um

# cria dicionario e joga para varialvel usuarios
usuarios = [] 
#usuarios.append({'bumbun' : 'guloso'}) 

for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip(), "idade" : int(idade.strip())})

for u in usuarios:
    print(u['nome'])

nomes = [] 
for u in usuarios:
    nomes.append(u['nome'])

for n in sorted(nomes):
    print(n)

#numeros = [2,3,4,6,7,0]
#ordenados = sorted(numeros)
#print(ordenados)
