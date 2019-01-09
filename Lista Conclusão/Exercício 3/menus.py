from contas import Conta, Corrente
from banco import Banco

def menu_opcoes():
    line(50)
    print('\n1. Saque')
    print('2. Depósito')
    print('3. Transferência')
    print('4. Saldo')
    print('5. Extrato')
    print('6. CANCELAR')
    try:
        opc = int(input('\n>>> '))
    except ValueError:
        line(50)
        print('Digite apenas números!')
    else:
        print()
        return opc

def menu_contas():
    line(50)
    print('\nEscolha um tipo de conta\n')
    print('1. Conta Corrente')
    print('2. Conta Poupança')
    print('3. Conta Conjunta')
    print('4. Conta Salário')
    print('5. CANCELAR')
    try:
        opc = int(input('\n>>> '))
    except ValueError:
        line(50)
        print('Digite apenas números')
    else:
        print()
        return opc

def menu_principal():
    b = Banco('Banco')
    while True:
        line(50)
        try:
            opc = int(input('\n1. Entrar\n2. Cadastrar cliente\n3. ANULAR\n\n>>> '))
        except ValueError:
            line(50)
            print('Digite apenas números')
        else:
            if opc == 1:
                while True:
                    a = menu_opcoes()
                    if a == 1:
                        line(50)
                        nome = str(input('Nome: '))
                        valor = float(input('Valor: '))
                        checa = 0
                        for conta in b.contas:
                            if conta.nome_titular == nome:
                                conta.saque(valor)
                                checa += 1
                        for conta in b.contas:
                            if conta.nome_titular[0] == nome:
                                conta.saque(valor)
                                checa += 1
                        if checa == 0:
                            line(50)
                            print('Conta não encontrada')
                            pass
                    elif a == 2:
                        line(50)
                        nome = str(input('Nome: '))
                        valor = float(input('Valor: '))
                        checa = 0
                        for conta in b.contas:
                            if conta.nome_titular == nome:
                                conta.deposito(valor)
                                checa += 1
                        for conta in b.contas:
                            if conta.nome_titular[0] == nome:
                                conta.deposito(valor)
                                checa += 1
                        if checa == 0:
                            line(50)
                            print('Conta não encontrada')
                            pass
                    elif a == 3:
                        line(50)
                        orig = str(input('De (nome): '))
                        dest = str(input('Para (nome): '))
                        valor = float(input('Valor: '))
                        info = [orig, dest, valor]
                        Corrente.transfere(b, info)
                                    
                    elif a == 4:
                        line(50)
                        nome = str(input('Nome: '))
                        checa = 0
                        for conta in b.contas:
                            if conta.nome_titular == nome:
                                line(50)
                                print('\nSaldo: {}'. format(conta.get_saldo()))
                                checa += 1
                        for conta in b.contas:
                            if conta.nome_titular[0] == nome:
                                line(50)
                                print('Saldo: {}'. format(conta.get_saldo()))
                                checa += 1
                        if checa == 0:
                            line(50)
                            print('Conta não encontrada')
                            pass

                    elif a == 5:
                        nome = str(input('Nome: '))
                        Conta.extrato(nome)

                    elif a == 6:
                        break
                    pass
            elif opc == 2:
                while True:
                    c = menu_contas()
                    if c == 5:
                        break
                        pass
                    b.cadastra(c)
                    break
                    pass
            elif opc == 3:
                break
                pass
            else:
                line(50)
                print('Opção inválida!')
                pass

def line(n):
    print('-' * n)
