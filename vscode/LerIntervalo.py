inicio = int(input("digite o valor de inicio: "))
fim = int(input("digite o valor de fim: "))
intervalo = int(input("digite o valor de intervalo: "))

for i in range(inicio,fim,intervalo):
    print(i," = ", (9*i/5)+32)