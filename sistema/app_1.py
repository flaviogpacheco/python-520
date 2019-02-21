#!/usr/bin/python3
from modulos.mysql import cursor
    
cursor.execute('SELECT * FROM usuarios')

for linha in cursor:
    print(linha)
