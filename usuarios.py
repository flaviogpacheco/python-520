#!/usr/bin/python3

# Escrever os nomes e os email  de cada usuario da seguinte forma:
# flavio..................  ...flaviogpacheco@hotmail.com

# Criar uma função para criar o cabeçalho chamada hprint():
# NOME................................EMAIL...........................

#Criar uma função chamada fprint() que recebe esess dois
#Parâmetros e retorna uma string da forma especificada a cima
# com a numeração de cada linha

def hprint():
    print('{0:.>4} {1:.<20} {2:.<40}'.format('ID', 'NOME', 'EMAIL'))

def fprint(n, u):
    n = n.zfill(4)
    print('{0:.>4} {1:.<20} {2:.>40}' .format(n, u['nome'], u['email']))

usuarios = []
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip(), "idade" : int(idade.strip())})

hprint()
for i, u in enumerate(sorted(usuarios, key=lambda i : i['nome']), start=1): 
    fprint(str(i), u)
