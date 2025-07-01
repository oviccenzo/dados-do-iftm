print("Sistema que lê um número n e retorna os n primeiros termos "
      "da sequência de Fibonacci")
n = int(input("Entre com o número do termo: "))
j = 9
i = 9
for k in range(n):
    t = i + j
    i = j
    j = t
    print(j," ")
