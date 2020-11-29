#import random

#cara = "Cara"
#coroa = "Coroa"
#lista = [cara,coroa]
#escolha = random.choice(lista)
#print("A moeda caiu {}".format(escolha))



#n1 = str(input("qual o primeiro nome: "))
#n2 = str(input("qual o segundo nome: "))
#n3 = str(input("qual o terceiro nome: "))
#n4 = str(input("qual o quarto nome: "))
#n5 = str(input("qual o quinto nome: "))
#lista = [n1,n2,n3,n4,n5]
#escolha = random.choice(lista)
#print("O nome escolhido foi {}".format(escolha))




#print(random.randint(10,100))





#class Computador:
#    def __init__(self,marca,memoria_ram,placa_de_video):
#        self.marca = marca
#        self.memoria_ram = memoria_ram
#        self.placa_de_video = placa_de_video

#computador1 = Computador('Asus','8gb','Nvidia')
#print("A marca do computador é {}, a quantidade de memoria {} e sua placa de video é {}.".format(computador1.marca,computador1.memoria_ram,computador1.placa_de_video))
#computador2 = Computador('Dell','16gb','GeFroce')
#print("A marca do computador 2 é {}, a quantidade de memoria {} e sua placa de video é {}.".format(computador2.marca,computador2.memoria_ram,computador2.placa_de_video))

#    def Ligar(self):
 #       print("Ligado")

#    def Desligar(self):
#        print("Desligado")

#    def ExibirInformaçõesDesteComputador(self):
#        print(self.marca,self.memoria_ram,self.placa_de_video)

#computador1 = Computador('Asus','16gb','Nvidia')
#computador1.Ligar()
#computador1.Desligar()
#computador1.ExibirInformaçõesDesteComputador()



'''
class Carro:
    def __init__(self,marca,chasi,cor,ano):
        self.marca = marca
        self.chasi = chasi
        self.cor = cor
        self.ano = ano

carro1 = Carro('Honda','154687231','Vermelho','1998')
print("O carro é da marca {}, com o chasi {}, na cor {} e ano {}".format(carro1.marca,carro1.chasi,carro1.cor,carro1.ano))
'''



'''
class Restaurante:
    def __init__(self,comida,bebida,preço_bebida,preço_comida):
        self.comida = comida
        self.bebida = bebida
        self.preço_comida = int(preço_comida)
        self.preço_bebida = int(preço_bebida)
    def get_preço(self):
        return self.preço_bebida + self.preço_comida
Pessoa1 = Restaurante('Frango','Coca','14','20')
print("A pessoa 1 pediu {} e {} totalizando R$ {}.".format(Pessoa1.comida,Pessoa1.bebida,Pessoa1.get_preço()))
'''


'''
Valor1 = float(input("Qual o primeiro numero: "))
Valor2 = float(input("Qual o segundo numero: "))

print("O que deseja fazer?")
option = int(input("1 - Adição\n 2 - Subtração \n 3- Multiplicação \n 4- Divisão \n"))

if option == 1:
    result = Valor1 + Valor2
elif option == 2:
    result = Valor1 - Valor2
elif option == 3:
    result = Valor1 * Valor2
elif option == 4:
    result = Valor1 / Valor2
else:
    print("Valor invalido")
    exit()

print("Resultado = {}".format(result))

if result %2 == 0:
    print("Numero Par\n")
else:
    print("Numero Impar\n")

if result >= 0:
    print("Numero positivo\n")
else:
    print("Numero negativo\n")

if type(result) == int:
    print("Numero Inteiro\n")
else:
    print("Numero não inteiro\n")
'''


'''
print("Você deseja colocar Gasolina ou Alcool")
escolha = int(input("1- Gasolina\n2- Alcool\n"))

if escolha == 1:
    gasolina = int(input("Quantos litros de gasolina você deseja colocar? "))
    if gasolina >= 20:
        print("Você deve pagar R$ {}".format((gasolina*3.9)-(gasolina*6/100)))
    elif gasolina < 20:
        print("Você deve pagar R$ {}".format((gasolina*3.9)-(gasolina*4/100)))
if escolha == 2:
    alcool = int(input("Quantos litros de alcool você deseja colocar? "))
    if alcool >= 20:
        print("Você deve pagar R$ {}".format((alcool*2.8)-(alcool*5/100)))
    if alcool < 20:
        print("Você deve pagar R$ {}".format((alcool*2.8)-(alcool*3/100)))
else:
    print("Valor invalido")
    exit()
'''


'''
dinheiro = float(input("Quanto de dinheiro você possui? \n"))
print("Qual opção você deseja escolher ?\n1- Escolher uma comida\n2- Escolher uma Bebida\n3- Escolher um Doce")
escolha = int(input())

if escolha == 1:
    print("Qual comida você deseja escolher?\n1- Arroz com frango\n2- Bola de carne\n3- Escondidinho de Carne\n4- Escondidinho de Frango")
    comida = int(input())
    if comida == 1:
        print("Você escolheu Arroz com frango e ele custa R$ 20. Seu troco será {}".format(dinheiro-20))
    elif comida == 2:
        print("Você escolheu Bola de carne e ele custa R$ 15. Seu troco será {}".format(dinheiro - 15))
    elif comida == 3:
        print("Você escolheu Escondidinho de Carne e ele custa R$ 20. Seu troco será {}".format(dinheiro - 25))
    elif comida == 4:
        print("Você escolheu Escondidinho de frango e ele custa R$ 20. Seu troco será {}".format(dinheiro - 40))
    else:
        print("Opção invalida")
if escolha == 2:
    print("Qual bebida você deseja escolher?\n1- Coca cola\n2- Agua de coco\n3- Guarana\n4- Suco")
    bebida = int(input())
    if bebida == 1:
        print("Você escolheu Coca cola e ele custa R$ 4. Seu troco será {}".format(dinheiro - 4))
    elif bebida == 2:
        print("Você escolheu Agua de coco e ele custa R$ 3. Seu troco será {}".format(dinheiro - 3))
    elif bebida == 3:
        print("Você escolheu Guarana e ele custa R$ 5. Seu troco será {}".format(dinheiro - 5))
    elif bebida == 4:
        print("Você escolheu Suco e ele custa R$ 8. Seu troco será {}".format(dinheiro - 8))
    else:
        print("Opção invalida")
if escolha == 3:
    print("Qual Doce você deseja escolher?\n1- Sorvete\n2- Doce de morango\n")
    doce = int(input())
    if doce == 1:
        print("Você escolheu Sorvete e ele custa R$ 10. Seu troco será {}".format(dinheiro - 10))
    elif doce == 2:
        print("Você escolheu Doce de morango e ele custa R$ 3. Seu troco será {}".format(dinheiro - 15))
    else:
        print("Opção invalida")
else:
    print("Opção invalida")
'''
