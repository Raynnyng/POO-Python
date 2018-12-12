arquivo = open('carros.txt', 'r')

"""
linha = arquivo.readline()
print(linha)
"""

lista = arquivo.readlines()
print(lista)
#print(lista.pop(1))
#lista.remove('Celta\n')
#lista.pop(1)
print(lista)
arquivo.close()

arquivo = open('carros.txt', 'w')
arquivo.writelines(lista)
arquivo.close()

arquivo = open('carros.txt', 'r')
lista = arquivo.readlines()
lista.append('Suprema\n')
print(lista)
arquivo.close()

arquivo = open('carros.txt', 'w')
arquivo.writelines(lista)
arquivo.close()

