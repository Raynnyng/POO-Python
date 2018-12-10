'''listaContatos = []

for c in range (10):
	listaContatos.append(str(input('Digite o nome do contato {}: '.format(c+1))))

print(listaContatos)'''

'''jogador1 = {'nome':'Kaka', 'posicao':'MC'}
jogador2 = {'nome':'Fenômeno', 'posicao':'AT'}
jogador3 = {'nome':'Xandeus', 'posicao':'ZG'}
jogador4 = {'nome':'Vandeuslei', 'posicao':'GL'}

time = []
time.append(jogador1.copy())
time.append(jogador2.copy())
time.append(jogador3.copy())
time.append(jogador4.copy())

print(time[1])'''

time = []
jogador = {}

for c in range (4):
	jogador['nome'] = str(input('Digite o nome do jogador {}: '.format(c+1)))
	jogador['posicao'] = str(input('Digite a posição do jogador {}: '.format(c+1)))
	jogador['num_gols'] = str(input('Digite o numero de gols do jogador {}: '.format(c+1)))
	time.append(jogador.copy())

print(time)
