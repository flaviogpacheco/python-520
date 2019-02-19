#!/usr/bin/python3

# Criar uma classe humano
# Que receba nome, idade e cor
# Criar um humano chamado Paramahansa Yoganda com 45 anos e negro
# Criar um humano chamado Monja Coen com 50 anos e Branca

class humano():
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    
class homem(humano):
    def __init__(self, nome, idade, cor, veiculo):
        #Chama o construtor da classe de quem herdou
        #super(Homem, self).__init__(nome, idade, cor)
        super().__init__(nome, idade, cor)
        self.veiculo = veiculo

        #self.nome = nome
        #self.idade = idade
        #self.cor = cor
        #self.veiculo = veiculo
        
h1 = homem('Paramahansa Yoganda', 45, 'negro', 'Fan 125cc')
h2 = humano('Monja', 50, 'branca')

print(h1.nome, h1.veiculo)
print(h2.nome)

