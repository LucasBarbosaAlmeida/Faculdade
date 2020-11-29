'''
class Carro:
    def __init__(self):
        self.IniciarNovamente = True

    def iniciar(self):
        self.MarcaCarro()
        while self.IniciarNovamente == True:
            if self.Marca == 'Ford':
                Ford = int(input("Escolha um carro!\n 1- Ford Ka\n 2- Ford Fusion\n"))
                if Ford == 1:
                    print("É um nice carro\n")
                    self.MarcaCarro()
                elif Ford == 2:
                    print("Esse é um carro caro porem, muito bom\n")
                    self.clear()
                    self.MarcaCarro()
                else:
                    print("Opção Errada")
                    break
            elif self.Marca == 'Honda':
                print("nice marca 2")
            elif self.Marca == 'Audi':
                print("nice marca 3")
            else:
                self.IniciarNovamente = False
                print("Muito obrigado por participar!")

    def MarcaCarro(self):
        self.Marca = input("Qual a marca do carro que você procura comprar? ")

Sistema = Carro()
Sistema.iniciar()
'''

class Crime:
    def __init__(self):
        self.ContinuarRodando = True
        self.Resposta = 0

    def inciar(self):
        self.NomePessoa()
        while self.ContinuarRodando == True:
            self.FazerPerguntas()
            if self.Pergunta1 == 'sim' or self.Pergunta1 == 's':
                self.Resposta += 1
            if self.Pergunta2 == 'sim' or self.Pergunta1 == 's':
                self.Resposta += 1
            if self.Pergunta3 == 'sim' or self.Pergunta1 == 's':
                self.Resposta += 1
            if self.Pergunta4 == 'sim' or self.Pergunta1 == 's':
                self.Resposta += 1
            if self.Pergunta5 == 'sim' or self.Pergunta1 == 's':
                self.Resposta += 1
            if self.Resposta < 2:
                print("A pessoa {} é inocente".format(self.Pessoa))
                print(self.Resposta)
                break
            if self.Resposta == 2:
                print("A pessoa {} é suspeita".format(self.Pessoa))
                print(self.Resposta)
                break
            if self.Resposta == 3 or self.Resposta == 4:
                print("A pessoa {} é cumplice".format(self.Pessoa))
                print(self.Resposta)
                break
            if self.Resposta == 5:
                print("A pessoa {} é Assassino".format(self.Pessoa))
                print(self.Resposta)
                break
            else:
                self.ContinuarRodando = False
                print("Muito obrigado por participar")

    def NomePessoa(self):
        self.Pessoa = str(input("Qual o nome do indivíduo? "))

    def FazerPerguntas(self):
        self.Pergunta1 = str(input("Telefonou para a vítima? "))
        self.Pergunta2 = str(input("Esteve no local do crime? "))
        self.Pergunta3 = str(input("Mora perto da vítima? "))
        self.Pergunta4 = str(input("Devia para a vítima? "))
        self.Pergunta5 = str(input("Já trabalhou com a vítima? "))

Sistema=Crime()
Sistema.inciar()
