inicio = int(input("Digite o valor de inicio(n): "))
fim = int(input("Digite o valor de fim: "))
intervalo = int(input("Digite o valo do intervalo: "))

for n in range(inicio,fim,intervalo):
    print(n , " = ", (3 * n / 5) + 90)
    