try:
	a = int(input())
	b = int(input())
	c = a/b
except ValueError:
	print("Deu Erro")
except ZeroDivisionError:
	print("Não é possível dividir por 0")
else:
	print(c)
finally:
	print("Cabou")
