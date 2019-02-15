#!/usr/bin/python3

usuarios = [] 

def extrair(i):
    return i['nome']

for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip(), "idade" : int(idade.strip())})

for n in sorted(usuarios, key=extrair):
#for n in sorted(usuarios, key=lambda i : i ['nome']):
    print(n)
