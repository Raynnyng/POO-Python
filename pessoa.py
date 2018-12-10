class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

class PessoaFisica(Pessoa):
	def __init__(self, nome, idade, cpf):
		super().__init(nome, idade)
		self.__cpf = cpf
		
class PessoaJuridica(Pessoa):
	def __init__(self, nome, idade, cnpj):
		super().__init(nome, idade)
		self.__cnpj = cnpj
		
				
	
