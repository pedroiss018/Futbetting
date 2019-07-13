from random import randint
def ver_jogos(x,y):
	y.append([x[0],' x ',x[1], '     COD: 001'])
	y.append([x[2],' x ',x[3], '     COD: 002'])
	y.append([x[4],' x ',x[5], '     COD: 003'])
	y.append([x[6],' x ',x[7], '     COD: 004'])
	y.append([x[8],' x ',x[9], '     COD: 005'])
	y.append([x[10],' x ',x[11], '     COD: 006'])
	y.append([x[12],' x ',x[13], '     COD: 007'])
	y.append([x[14],' x ',x[15], '     COD: 008'])
	y.append([x[16],' x ',x[17], '     COD: 009'])
	y.append([x[18],' x ',x[19], '     COD: 0010'])
	for n in range(0,10):
		print(''.join(y[n]))
		print('_'*50)

def apostar(x,y):
	apt = float(input('Valor da aposta: R$'))
	y.append(apt)
	cod = int(input('Código do jogo: 00'))
	print('''
[1] CASA
[2] FORA
[3] EMPATE''')
	print('')
	ppt = int(input('Palpite: '))
	if ppt==1:
		ppt = str('APOSTA: CASA')
		cod = str('COD: 00{}'.format(cod))
		apt = ('VALOR: R${:.2f}'.format(apt))
	elif ppt == 2:
		ppt = str('APOSTA: FORA')
		cod = str('COD: 00{}'.format(cod))
		apt = ('VALOR: R${:.2f}'.format(apt))
	elif ppt == 3:
		ppt = str('APOSTA: EMPATE')
		cod = str('COD: 00{}'.format(cod))
		apt = ('VALOR: R${:.2f}'.format(apt))
	print('')
	print('APOSTA CONFIRMADA!')
	print('_'*50)
	x.append([apt, cod, ppt])

def verapt(x):
	qt = int(len(x))
	num = 1
	for n in range(0, qt):
		print(num,'-','   |   '.join(x[n])) 
		num += 1

def cancel(x):
	k = int(input('Número da aposta que deseja cancelar? '))
	k = k-1
	x.remove(x[k])
	print('APOSTA CANCELADA!')
	print('_'*50)

def resultados(x,y,z,t,v):
        print('='*18, 'RESULTADOS', '='*18)
        for i in range(0,10):
                c = randint(0,5)
                f = randint(0,5)
                x.append([c,'x',f])
        print(y[0],x[0],y[1])
        print('_'*80)
        print(y[2],x[1],y[3])
        print('_'*80)
        print(y[4],x[2],y[5])
        print('_'*80)
        print(y[6],x[3],y[7])
        print('_'*80)
        print(y[8],x[4],y[9])
        print('_'*80)
        print(y[10],x[5],y[11])
        print('_'*80)
        print(y[12],x[6],y[13])
        print('_'*80)
        print(y[14],x[7],y[15])
        print('_'*80)
        print(y[16],x[8],y[17])
        print('_'*80)
        print(y[18],x[9],y[19])
        print('_'*80)

        qt = int(len(z))
        numer = 1
        aptn = 1
        print('='*9,'Resultados das suas apostas','='*9)
        for n in range(0, qt):
#vitoria
                if z[n][2] == 'APOSTA: CASA':
                        print('   |   '.join(z[n]))
                        if(t[n][0] > t[n][2]):
                                print('Aposta:',aptn,'-','Ganho: R${:.2f}'.format(v[n]*3))
                        else:
                                print('Aposta:',aptn,'-','Infelizmente você perdeu.')
                        print('_'*80)
                elif(z[n][2] == 'APOSTA: FORA'):
                        print('   |   '.join(z[n]))
                        if(t[n][0] < t[n][2]):
                                print('Aposta:',aptn,'-','Ganho: R${:.2f}'.format(v[n]*3))
                        else:
                                print('Aposta:',aptn,'-','Infelizmente você perdeu.')
                        print('_'*80)
                else:
                        print('   |   '.join(z[n]))
                        if(t[n][0] == t[n][2]):
                                print('Aposta:',aptn,'-','Ganho: R${:.2f}'.format(v[n]*3))
                        else:
                                print('Aposta:',aptn,'-','Infelizmente você perdeu.')
                        print('_'*80)
                aptn += 1
