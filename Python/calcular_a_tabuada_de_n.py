#Inicializando as variaveis com valores extremos para garantir a com comparação correta
maior_valor = float('-inf')
menor_valor = float('inf')

#Lendo os 50 valores
for i in range(1,51):
    valor = float(input("Digite o {i} valor: "))
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

print(f"O maior valor com entre os numeros digitados é: {maior_valor}")
print(f"O menor valor com entre os numeros digitados é: {menor_valor}")