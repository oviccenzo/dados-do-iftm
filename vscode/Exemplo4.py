import math

for i in range(1,30):
    numero = int(input("Digite um numero: "))
    permutacao = math.perm(numero)
    numero += permutacao

    print("A soma da permutacoes é: ", permutacao)