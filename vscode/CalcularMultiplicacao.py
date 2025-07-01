# def multiplicacao():
#     num1 = float(input("Digite o primeiro numero: "))
#     num2 = float(input("Digite o segundo numero: "))
#     num3 = float(input("Digite o terceiro numero: "))
#     num4 = float(input("Digite o quarto numero: "))
#     return num1,num2,num3,num4

# def le_numero(num1,num2,num3,num4):
#     return (num1 * 2 + num2 * 2 + num3 * 2 + num4 * 2) / 8

# num1,num2,num3,num4 = multiplicacao()
# multiplicar = le_numero(num1,num2,num3,num4)
# print(f"o resultado da multiplicacao e: {multiplicar:.2f}")


# Exercício 24: Custo de Entrega
distancia = float(input("Digite a distância em km: "))
custo_base = 4
if distancia <= 3:
    custo = custo_base + distancia * 0.5
elif distancia <= 6:
    custo = custo_base + distancia * 0.75
else:
    custo = custo_base + distancia * 1.0
print("Valor da entrega:", custo)