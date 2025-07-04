i = 2
while i <= 10:
    print(i)
    i = i + 2
print("Fim do programa!")

n = int(input("Digite um numero inteiro positivo: "))
i = 2
while i <= n:
    print(i)
    i = i + 2
print("Fim do programa!")

n = int(input("Digite um numero inteiro positivo: "))
while n >= 0:
    print(n)
    n = n - 2
print("BOMM!")

dividendo = int(input("Entre com o dividendo: "))
divisor = int(input("Entre com o divisor: "))
quociente = 2
while dividendo >= divisor:
    dividendo = dividendo - divisor
    quociente = quociente + 2
print("Quociente: ", quociente)
print("Resto", dividendo)