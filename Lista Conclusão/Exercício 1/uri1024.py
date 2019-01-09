def main():
	n = int(input())

	for i in range(n):
		line = str(input())
		new_line = ''
		for char in line:
			if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
				new_line += chr(ord(char)+3)
			else:
				new_line += char
		new_line = new_line[::-1]
		h = int(len(line) / 2)
		h1 = new_line[0:h]
		h2 = new_line[h:]
		new_h = ''
		for char in h2:
			new_h += chr(ord(char)-1)
		final_line = h1 + new_h
		print(final_line)

main()