peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if (imc <= 18.5):
	print("Seu IMC é {}. Isso indica que você está abaixo do peso.".format(imc))

elif (18.6 <= imc <= 24.9):
	print("Seu IMC é {}. Isso indica que você está saudável.".format(imc))

elif (25 <= imc <= 29.9):
	print("Seu IMC é {}. Isso indica que você possui peso em excesso.".format(imc))

elif (30 <= imc <= 34.9):
	print("Seu IMC é {}. Isso indica que você possui obesidade grau I.".format(imc))

elif (35 <= imc <= 39.9):
	print("Seu IMC é {}. Isso indica que você possui obesidade grau II, severa.".format(imc))

elif (40 <= imc):
	print("Seu IMC é {}. Isso indica que você possui obesidade grau III, mórbida".format(imc))
