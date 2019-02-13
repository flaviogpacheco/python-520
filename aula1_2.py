#!/usr/bin/python3
# ==,  !=, <, <=, >, >=
# Se o numero resultado da soma for maior 100
# Escrever: "Que numero grandão..."
# Caso contrário: "Que numero pequeno..."

texto_grotesco = 'Por conseguinte, o novo modelo estrutural aqui preconizado nos obriga à análise das condições financeiras e administrativas exigidas. Ainda assim, existem dúvidas a respeito de como o surgimento do comércio virtual faz parte de um processo de gerenciamento das regras de conduta normativas. Neste sentido, a execução dos pontos do programa exige a precisão e a definição do fluxo de informações.'

nomes =  ['Hector', 'Guilherme', 'Joel', 'Flávio', 'Fabiano', 'Roger', 'Cícero', 'Hugo', 'Ayron', 'Leonel', 'Pedro', 'Lucas']

# Verificar se a palavra "virtual" está dentro do "texto_grotesco"
# Exibir apenas os 4 últimos nomes
# .split() contar quantas palavras tem no "texto_grotesco"

if 'virtua1' in texto_grotesco:
    print('Palavra "virtual" encontrada')
else:
    print('Palavra não encontrada')
 
print(nomes[-4:])
print(len(texto_grotesco.split()))

# Percorrer a lista "nomes e exibir apenas os nomes que começam 
# com a letra F e H
# for 
# if com [:] em cima do item "do momento"

for nome in nomes:
    # Mais elegante
    if nome[0] in 'FH':
       print(nome)
    # Segunda mais elegante
    if nome[0] == 'H' or nome[0] == 'F':
        print(nome)
    # A que funciona
    if nome[0] == 'F':
        print(nome)
    elif nome[0] == "H":
        print(nome)
    
exit()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = n1 + n2

print(n3) 

if  n3 > 100:
    print('Que número grandão...')
else:
    print('Que número pequeno...')
