baralho = ['K',2,4,6,8,'J',3,5,7,9,'Q',10,'A']
ordenado = [0] * 13 

for carta in baralho:

	if (type(carta) == str):
		if (carta == 'A'):
			ordenado[0] = carta
		elif (carta == 'J'):
			ordenado[10] = carta
		elif (carta == 'Q'):
			ordenado[11] = carta
		elif (carta == 'K'):
			ordenado[12] = carta
		
	else:
		i = carta - 1
		ordenado[i] = carta
		
print(baralho)
print(ordenado)
