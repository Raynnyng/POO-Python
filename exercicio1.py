def menuDeSelecao():
	while True:
		try:
			print("Escolha uma das opçẽs a seguir:")
			print("[1] Opção 1 \n"
					"[2] Opção 2 \n"
					"[3] Opção 3 \n"
	   			"[4] Opção 4")
			a = int(input())
		except ValueError:
			print("Deu merda. Valor Inválido")
		else:
			if a == 1:
				print("Opção 1 escolhida")
				break
			elif a == 2:
				print("Opção 2 escolhida")
				break			
			elif a == 3:
				print("Opção 3 escolhida")
				break	
			elif a == 4:
				print("Opção 4 escolhida")
				break			
			elif a >= 5:
				print("Deu merda. Valor Inválido")
menuDeSelecao()
