import threading, time, queue
import random as rand

TAM_BUF = 10
fila = queue.Queue(TAM_BUF)

class Produtor():
	def __init__(self):
		pass
		
	def executa(self):
		while True:
			if not fila.full():
				print('Tamanho da fila = {}'.format(fila.qsize()))
				time.sleep(rand.random())
				item = rand.randint(1, 10)
				fila.put(item)
				print('Adicionado: {}'.format(item))
				time.sleep(rand.random())
		
class Consumidor():
	def __init__(self):
		pass
		
	def executa(self):
		while True:
			if not fila.empty():
				item = fila.get()
				print("Removido: {}".format(item))
				time.sleep(rand.random())
				print('Tamanho da fila = {}'.format(fila.qsize()))
				time.sleep(rand.random())
			if fila.empty():
				print('O consumidor está esperando por produto!')
				time.sleep(rand.random())
		
if __name__ == '__main__':
  	p = Produtor()
  	c = Consumidor()
  	tp = threading.Thread(target = p.executa, args = ())
  	tc = threading.Thread(target = c.executa, args = ())

tp.start()
tc.start()			
