class Conta:
	def __init__(self, nomeTitular, cpfTitular):
		self.nomeTitular = nomeTitular
		self.__cpfTitular = cpfTitular
		self.__saldo = 0.0
	def getSaldo(self):
		return self.__saldo
	def setSaldo(self, valor):
		self.__saldo = valor
	def getCPF(self):
		return self.__cpfTitular
	def __sacar(self, quantia):
		if(quantia <= self.__saldo):
			self.__saldo -= quantia
			print('Saque realizado com sucesso!')
		else:
			print('Saque não realizado. Saldo insuficiente.')
	def depositar(self, quantia):
		self.__saldo += quantia
		print('Deposito realizado com sucesso!')

class ContaConjunta(Conta):
	def __init__(self, nomeTitular, cpfTitular):
		super().__init__(nomeTitular, cpfTitular)
		self.__saldo = 0.0
class ContaPoupanca(Conta):
	def __init__(self, nomeTitular, cpfTitular):
		super().__init__(nomeTitular, cpfTitular)
		self.__saldo = 0.0
		self.rendimento = 0.01
	
