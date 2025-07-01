numero = int(input("Digite um numero:  "))
contador = 0
soma = 0

while(contador < 8):
    soma = soma + numero
    contador = contador + 1
    numero = int(input("Digite um numero: "))     

print("Resultado: ", soma)