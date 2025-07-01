num = int(input("digite um numero: "))

soma = num
qtde = 2
media = 0

while(soma < 100):
    num = int(input("digite um numero: "))
    soma = soma + num
    qtde = qtde + 1

media = soma / qtde
print("quantos foram digitados: ", qtde, "de numero")
print("a soma dos numeros digitados e: ",soma)
print("a media dos numeros digitados e: ",soma)