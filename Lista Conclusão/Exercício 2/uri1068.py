def main():
	while True:
		try:
			expr = str(input())
			aux = []
			for char in expr:
				if char == '(':
					aux.append('(')
				elif char == ')':
					if len(aux) > 0:
						aux.pop()
					else:
						aux.append(')')
						break

			if len(aux) == 0:
				print('correct')
			else:
				print('incorrect')
		except (EOFError):
			break

main()