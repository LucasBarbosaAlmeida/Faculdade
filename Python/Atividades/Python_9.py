'''
import math
print("Qual Lane do Lol você mais gosta?")
print("1-Top\n2-Jg\n3-Mid\n4-Adc\n5-Sup\n")
lane = int(input())
if lane == 1:
    print("Qual lvl do champion vc deseja ver:")
    level = int(input())
    print("Você pode escolher:\n1-Sett\n2-Jax\n3-Nocturne")
    top = int(input())
    if top == 1:
        print("Seu boneco é um lixo")
        print("Os status do sett é: \nHP {}\nSP {}\n AD {}".format(520+(level*3.5),350+(level*2),85+(level*1.85)))
    elif top == 2:
        print("Seu boneco é um Muitooooooo lixo")
        print("Os status do sett é: \nHP {}\nSP {}\n AD {}".format(550+(level * 3.5), 300+(level * 2), 90+(level * 1.85)))
    elif top == 3:
        print("Seu boneco é um esse boneco é lindo")
        print("Os status do sett é: \nHP {}\nSP {}\n AD {}".format(600+(level * 3.5), 350+(level * 2), 85+(level * 1.85)))
    else:
        print("Opção Errada")
else:
    print("Opção Errada")
'''



#x = -10
#while x != 10:
#    print(x)
#    x += 1



import random

#x = random.randint(1,6)
#print(x)
'''
y = int(input("Digite um numero:"))
x = random.randint(1,100)
if x == y:
    print("Você acertou")
    print(x)
else:
    print("Você errou o numero")
    print(x)
'''




'''
class Dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce deseja rodar o dado? "

    def iniciar(self):
        resposta = input(self.mensagem)
        if resposta == "sim" or resposta == "s":
            self.GerarValorDoDado()
        elif resposta == "nao" or resposta == "n":
            print("Muito obrigado")
        else:
            print("Favor digitar sim ou nao")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

Simulador = Dado()
Simulador.iniciar()



'''
class Numero:
    def __init__(self):
        self.Valor_Aleatorio = 0
        self.TentarNovamente = True

    def inciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.TentarNovamente == True:
            if self.Valor_Do_Chute > self.Valor_Aleatorio:
                print("Chute um valor mais baixo")
                self.PedirValorAleatorio()
            elif self.Valor_Do_Chute < self.Valor_Aleatorio:
                print("Chute um valor mais alto")
                self.PedirValorAleatorio()

            self.TentarNovamente = False
            print("Você Acertou")

    def PedirValorAleatorio(self):
        self.Valor_Do_Chute = int(input("Chute um numero: "))

    def GerarNumeroAleatorio(self):
        self.Valor_Aleatorio = random.randint(1,100)


Simulador = Numero()
Simulador.inciar()