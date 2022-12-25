genero = str(input("homem ou mulher? "))
altura = float(input("digite sua altura: "))

if (genero == "homem"):
	peso = (72.7 * altura) - 58
elif (genero == "mulher"):
	peso = (62.1 * altura) - 44.7
else: 
	print("Inválido!")
	peso = "ERRO"
	
print("Seu peso ideal é", peso)
