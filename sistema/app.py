#!/usr/bin/python3

# Capturar do terminal nome, email e sexo
# cadastrar os dados no banco de dados
# INSERT INTO musicas (nome, disco, banda)
#   VALUES ('A Palo Seco', 'Alucinação', 'Belchior');
#------
# Quando a inserção estiver funcionado, cadastrar um usuário chamado
# Joana D'arc
#-----
# O email não pode ser repetir dentro do banco
# Antes de cadastrar os dados, buscar pelo email digitado
# Caso o email já exista, escrever: "e-mail já existente, por favor digite outro"

from modulos.mysql import cursor, db

nome = input('Digite o nome do usuário: ')
email= input('Digite o email do usuário: ')
sexo = input('Digite o sexo do usuário [0,1] : ')

sql = "SELECT id FROM usuarios WHERE email = %s"
encontrado = cursor.execute(sql, [email])
if encontrado:
    print('Email já existente, por favor digite outro')
exit()
    
#if email == "SELECT * FROM usuarios WHERE email)

#"SELECT * FROM usuarios WHERE nome LIKE '%{0}%'" .format(nome)

#sql = "INSERT INTO usuarios (nome, email, sexo) VALUES (%s, %s, %s)"
#cursor.execute(sql, (nome, email, sexo))  
#db.commit()


#exit()

#sql = "SELECT * FROM usuarios WHERE nome LIKE '%{0}%'" .format(nome)

#cursor.execute(sql)

#for linha in cursor:
 #   print(linha)
