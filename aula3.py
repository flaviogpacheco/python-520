#!/usr/bin/python3


#arquivo = open('zen.txt') .read() .upper()

#arquivo = open('zen.txt')

# a linha nunca será apenas "-"
# enumerate
# mod -> 1 % 2 -> Se é par ou impar
# if 'belzebu' not  in demonios:
# printar apenas as linhas com palavras, ignorando as linhas com "-"


arquivo = open('zen.txt')
#i = 0
#for linha in arquivo:
#    linha = linha.strip()
#    if i % 2 == 0:  
#        print(linha)
#    i = i + 1

for i, linha in enumerate(arquivo):
    if i % 2 == 0:
         print(linha.strip())

#print(arquivo.readlines())

#print(arquivo.read())
#print(arquivo)

