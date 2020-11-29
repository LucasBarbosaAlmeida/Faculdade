'''
class Ed:
    def __init__(self):
        self.TenteNovamente = True

    def iniciar(self):
        self.DescobrirNomeAluno()
        self.SabeQualAnoDoAluno()
        self.MateriaDoAluno()
        while self.TenteNovamente == True:
            if self.AnoDoAluno >= 7 and self.AnoDoAluno <= 9:
                print("O aluno {} esta preparado para estudar a materia {}".format(self.NomeAluno,self.MateriaAluno))

            elif self.AnoDoAluno < 7 and self.AnoDoAluno > 1:
                print("O aluno {} não esta preparado para estudar".format(self.NomeAluno))

            else:
                print("Escolha uma opção correta")

            self.TenteNovamente = False
            print("Muito obrigado")

    def SabeQualAnoDoAluno(self):
        self.AnoDoAluno = int(input("Qual o ano do aluno? "))

    def DescobrirNomeAluno(self):
        self.NomeAluno = input("Qual o nome do aluno? ")

    def MateriaDoAluno(self):
        self.MateriaAluno = input("Qual a máteria o aluno esta? ")

Codigo = Ed()
Codigo.iniciar()
'''



import math
class Calc:
    def __init__(self):
        self.TentarNovamente = True

    def iniciar(self):
        self.Opções()
        while self.TentarNovamente == True:
            if self.op == 1:
                self.OpçãoDoUsuario1()
                print("A tabuada de {} é:\n {}x1 = {}\n {}x2 = {}\n {}x3 = {}\n {}x4 = {}\n {}x5 = {}\n {}x6 = {}\n {}x7 = {}\n {}x8 = {}\n {}x9 = {}\n {}x10 = {}".format(self.usuario,self.usuario,(self.usuario*1),self.usuario,(self.usuario*2),self.usuario,(self.usuario*3),self.usuario,(self.usuario*4),self.usuario,(self.usuario*5),self.usuario,(self.usuario*6),self.usuario,(self.usuario*7),self.usuario,(self.usuario*8),self.usuario,(self.usuario*9),self.usuario,(self.usuario*10)))
                self.Opções()
            elif self.op == 2:
                self.OpçãoDoUsuario1()
                self.OpçãoDoUsuario2()
                print("A multiplicação de {} mais {} é igual a = {}".format(self.usuario,self.usuario2,(self.usuario*self.usuario2)))
                self.Opções()
            elif self.op == 3:
                self.OpçãoDoUsuario1()
                self.OpçãoDoUsuario2()
                print("A soma de {} mais {} é igual a = {}".format(self.usuario, self.usuario2,(self.usuario + self.usuario2)))
                self.Opções()
            elif self.op == 4:
                self.OpçãoDoUsuario1()
                self.OpçãoDoUsuario2()
                print("A subtração de {} mais {} é igual a = {}".format(self.usuario, self.usuario2,(self.usuario - self.usuario2)))
                self.Opções()
            elif self.op == 5:
                self.OpçãoDoUsuario1()
                self.OpçãoDoUsuario2()
                print("A divisão de {} mais {} é igual a = {}".format(self.usuario, self.usuario2,(self.usuario / self.usuario2)))
                self.Opções()
            elif self.op == 6:
                self.OpçãoDoUsuario1()
                print("A raiz de {} é = {}".format(self.usuario,int(math.sqrt(self.usuario))))
                self.Opções()
            elif self.op == 7:
                self.TentarNovamente = False
                print("\nMuito obrigado por participar do meu projeto!")

            else:
                print("Opção errada! ")
                self.Opções()


    def OpçãoDoUsuario1(self):
        self.usuario = int(input("Qual o primeiro numero? "))

    def OpçãoDoUsuario2(self):
        self.usuario2 = int(input("Qual o segundo numero? "))

    def Opções(self):
        self.op = int(input("''''''''''''''''''''''''\n"
                        "' 1- Tabuada           '\n"
                        "' 2- Multiplicação     '\n"
                        "' 3- Soma              '\n"
                        "' 4- Subtração         '\n"
                        "' 5- Divição           '\n"
                        "' 6- Raiz              '\n"
                        "' 7- Sair do sistema   '\n"
                        "''''''''''''''''''''''''\n"))


Matematica = Calc()
Matematica.iniciar()