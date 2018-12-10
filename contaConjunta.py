import conta
class ContaConjunta(Conta):
	def __init__(self, nomeTitular, cpfTitular, nomeTitular2, cpfTitular2):
		self.nomeTitular = nomeTitular
		self.nomeTitular2 = nomeTitular
		self.__cpfTitular = cpfTitular
		self.__cpfTitular2 = cpfTitular2
		self.__saldo = 0.0
	def getCPFTitular2(self):
		return self.cpfTitular2
