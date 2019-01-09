import menus
import contas as Conta

class Banco():
    def __init__(self, nome):
        self.nome = nome 
        self.contas = []
    def cadastra(self, opc):
        menus.line(50)
        nome1 = str(input('\nTitular 1: '))
        cpf1 = str(input('CPF: '))
        if opc == 1:
            cc = Conta.Corrente(nome1, cpf1)
            self.contas.append(cc)
        elif opc == 2:
            cp = Conta.Poupanca(nome1, cpf1)
            self.contas.append(cp)
        elif opc == 3:
            nome2 = str(input('\nTitular 2: '))
            cpf2 = str(input('CPF: '))
            nomes = (nome1, nome2)
            cpfs = (cpf1, cpf2)
            ct = Conta.Conjunta(nomes, cpfs)
            self.contas.append(ct)
        elif opc == 4:
            cs = Conta.Salario(nome1, cpf1)
            self.contas.append(cs)
        else:
            if opc != 5:
                menus.line(50)
                print('Opção inválida!')
