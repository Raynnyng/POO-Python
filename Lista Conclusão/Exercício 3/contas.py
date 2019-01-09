from datetime import datetime
from abc import ABCMeta, abstractmethod
import menus

class Conta(object):
    def __init__(self, nome, cpf):
        self.nome_titular = nome
        self.__cpf_titular = cpf
        self.__saldo = 0.0

    def set_saldo(self, valor):
        self.__saldo += valor
        
    def get_saldo(self):
        return self. __saldo
            
    def get_cpf(self):
        return self. __cpf_titular
            
    def saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente!')
        if type(self) is Conjunta:
            try:
                arquivo1 = open(self.nome_titular[0] + '.txt', 'a+')
            except FileNotFoundError:
                menus.line(50)
                print('Arquivo não encontrado!')
        else :
            try:
                arquivo2 = open(self.nome_titular + '.txt', 'a+')
                agora = datetime.now()
                arquivo2.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                    '\tsaque\t\t' + str(valor) + '\t' + str(self.__saldo) + '\n')
                arquivo2.close()
            except FileNotFoundError:
                menus.line(50)
                print('Arquivo não encontrado!')
        if type(self) is Conjunta:
            agora = datetime.now()
            arquivo1.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                '\tsaque\t\t' + str(valor) + '\t' + str(self.__saldo) + '\n')
            arquivo1.close()

    def deposito(self, valor):
        if type(self) is not Salario:
            if valor > 0:
                self.__saldo += valor
            if type(self) is Poupanca:
                self.rende(valor)
            if type(self) is Conjunta:
                try:
                    arquivo1 = open(self.nome_titular[0] + '.txt', 'a+')
                except FileNotFoundError:
                    menus.line(50)
                    print('Arquivo não encontrado!')
            else:
                try:
                    arquivo2 = open(self.nome_titular + '.txt', 'a+')
                    agora = datetime.now()
                    arquivo2.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                        '\tdeposito\t' + str(valor) + '\t' + str(self.__saldo) + '\n')
                    arquivo2.close()
                except FileNotFoundError:
                    menus.line(50)
                    print('Arquivo não encontrado!')
            if type(self) is Conjunta:
                agora = datetime.now()
                arquivo1.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                    '\tdeposito\t' + str(valor) + '\t' + str(self.__saldo) + '\n')
                arquivo1.close()
        else:
            menus.line(50)
            print('Operação negada!')

    @abstractmethod
    def transfere(banco, info):
        pass

    @staticmethod
    def extrato(nome):
        try:
            arquivo = open(nome + '.txt', 'r')
            extrato = arquivo.read()
            menus.line(50)
            print(extrato)
            arquivo.close()
        except FileNotFoundError:
            menus.line(50)
            print('Arquivo não encontrado!')

class Corrente(Conta):
    def __init__(self, nome, cpf):
        self.possui_cheque = False
        self.possui_cartao_credito = False
        super().__init__(nome, cpf)

    @staticmethod
    def transfere(banco, info):
        checa = 0
        try:
            arquivo1 = open(info[0] + '.txt', 'a+')
            arquivo2 = open(info[1] + '.txt', 'a+')
        except FileNotFoundError:
            menus.line(50)
            print('Arquivo não encontrado!')
        agora = datetime.now()
        if info[0] == info[1]:
            menus.line(50)
            print('Destino igual a origem')
        else:
            for conta in banco.contas:
                if conta.nome_titular == info[0] or conta.nome_titular[0] == info[0]:
                    if type(conta) is Corrente or type(conta) is Conjunta:
                        if conta.get_saldo() >= info[2]:
                            checa += 1
                        else: 
                            menus.line(50)
                            print('Saldo insuficiente')
                            print('Operação não realizada')
                    else:
                        menus.line(50) 
                        print('Operação negada!')
            if checa == 1 or checa == 0:
                for conta in banco.contas:
                    if conta.nome_titular == info[1] or conta.nome_titular[0] == info[1]:
                        checa += 1
            if checa == 2:
                for conta in banco.contas:
                    if conta.nome_titular == info[0] or conta.nome_titular[0] == info[0]:
                        conta.set_saldo(-info[2])
                        arquivo1.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                            '\ttransferência\t' + str(info[2]) + '\t' + str(conta.get_saldo()) + '\n')
                    if conta.nome_titular == info[1] or conta.nome_titular[0] == info[1]:
                        conta.set_saldo(info[2])
                        if type(conta) is Poupanca:
                            conta.rende(info[2])
                        arquivo2.write(str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year) + 
                            '\ttransferência\t' + str(info[2]) + '\t' + str(conta.get_saldo())  + '\n')
            if checa == 0:
                menus.line(50)
                print('Contas não encontradas')
            arquivo1.close()
            arquivo2.close()
        
class Poupanca(Conta):       
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    def rende(self, valor):
        rendimentos = valor - (valor * 0.005)
        rendimentos = valor - rendimentos
        self.set_saldo(rendimentos)
   
class Conjunta(Corrente):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class Salario(Conta):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
