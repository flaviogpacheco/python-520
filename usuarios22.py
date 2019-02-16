#!/usr/bin/python3
#Abrir o arquivos usuários
# Seperar os valores por ","
# E escrever na tela o dicionario:
# {"nome : "Hector", "idade" : 27, "email" : hecto.silva@4linux.com.br}

#arquivo = open('arquivos.csv')
#for linha in arquivo:
#print(linha{"nome" : 

for l in open('usuarios.csv'):
    # aqui eu preciso separar por ","
    nome, email = l.split(',')
    print({
        "nome"  : nome.strip(), 
        "email" : email.strip()})
