#importações
from random import shuffle
import aposta

#listas
times = ['CORINTHIANS', 'PALMEIRAS','ATLÉTICO MG','BAHIA','SANTOS','FLAMENGO','INTERNACIONAL','BOTAFOGO','SÃO PAULO','ATLÉTICO PR','CEARÁ','GOIÁS','FORTALEZA', 'CRUZEIRO','CHAPECOENSE','FLUMINENSE','GRÊMIO','VASCO','CSA','AVAÍ']
jogos = []
apostas = []
valor = []
resultado = []
shuffle(times)

#variáveis
k = -1

#menu
print('='*10,'FUTBETING','='*10)
menu = '''
[1] - Ver jogos
[2] - Fazer nova aposta
[3] - Ver apostas
[4] - Cancelar uma aposta
[5] - Ver resultados
[0] - Sair
'''
while True:
	print(menu)
	k = int(input('Escolha uma opção: '))
	print('_'*50)
	if(k==1):
		print('='*22,'JOGOS','='*21)
		print('_'*50)
		aposta.ver_jogos(times, jogos)
	elif(k==2):
		aposta.apostar(apostas, valor)
	elif(k==3):
		aposta.verapt(apostas)
	elif(k==4):
		aposta.cancel(apostas)
	elif(k==5):
		aposta.resultados(resultado, times, apostas, resultado, valor)
	elif(k==0):
                break
