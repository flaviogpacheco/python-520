#!/usr/bin/python3
from modulos.mysql import cursor

nome = input('Digite o nome do usuário: ')

sql = "SELECT * FROM usuarios WHERE nome LIKE '%{0}%'" .format(nome)

cursor.execute(sql)

for linha in cursor:
    print(linha)
