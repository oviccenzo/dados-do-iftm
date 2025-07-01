valor = 0
media = 0
soma = 0
contador = 0

while(valor >= 0):
    valor = int(input("Digite um valor:"))
    soma = soma + valor
    contador = contador + 1

media = valor / contador    
print("A media dos valores: ",media)
print("Resultado: ",media)   
