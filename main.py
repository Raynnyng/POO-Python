import conta
import pessoa

a = conta.Conta('Wiliam', 123456)
b = conta.ContaConjunta(('Wiliam','Jaqueline'), ('654321', '123456'))
c = pessoa.Pessoa('Wiliam', 20)
d = pessoa.PessoaFisica('Jaqueline', 29, '12345')

print(c.nome, c.idade)
print(d.nome)
#print(a.nomeTitular)
#print(b.getCPF())
