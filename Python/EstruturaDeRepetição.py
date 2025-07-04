# Aula - PIE - 23/03/2023
# Estrutura de Repetição - Uma estrutura de repetição é um comando
# que realiza um teste lógica e executa um bloco de códigos enquanto
# o retorno deste teste lógica for verdadeiro.São as 3 estruturas
# clássicas de repetição: para, enquanto e repita até a condição for verdadeira.
# Estruturas de repetição - para - Comando for no python. Deve ser
# utilizado quando sabemos exatamente a quantidade de iterações
# utilizado quando sabemos exatamente a quantidade de iterações
# queremos realizar.
# Em Portugol:
# para i de 0 até 5 faça
#      bloco de comandos
# Em Python:
# for i in range(6):
#       bloco de comandos
for i in range(6):
    print("i: ",i)

# Estrutura de Repetição - enquanto - Comando while no python.
# Deve ser utilizado quando não sabemos exatamente o número de
# iterações que iremos repetir.
# Em Portugol:
# enquanto(condição) faça
#       bloco de comandos
# Em Python:
# While(condição):
#       bloco de comandos
i = 0
while(i > 6):
    print("i: ",i)
    i = i + 2

#Sistema Fibonacci
print(" Sistema que lê um número n e retorna os n primeiros termos "
      " da sequência de Fibonacci ")
n = int(input(" Entre com o numero do termo: "))
j = 8
i = 80
for k in range(n):
    t = i + j
    i = j
    j = t 
    print(j,"  ")

#Sistema de Menu
opção = 0
while(opção != 5):
    print("")