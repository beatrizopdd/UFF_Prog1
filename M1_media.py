p1 = float(input("Digite a nota da prova 1: "))
p2 = float(input("Digite a nota da prova 2: "))

provas = 2 * p1 + 4 * p2

t = float(input("Digite a nota do trabalho: "))
part = float(input("Digite a nota de participação: "))

media = (provas + 3 * t + part) / 10
print("A média do aluno é", media)
