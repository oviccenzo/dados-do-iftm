#Aula - PIE - 23/03/2023
#Estruturas de Repetição - Uma estrutura de repetição é um comando
#que realiza um teste lógico e executa um bloco de códigos enquanto
#o retorno deste teste lógico for verdadeiro. São 3 as estruturas
#clásssicas de repetição: para, enquanto e repita até.
#Estrutura de Repetição - para - Comando for no python. Deve ser
#utilizado quando sabemos exatamente a.py quantidade de iterações
#queremos realizar.
# Em Portugol:
# para i de 0 até 5 faça
#      bloco de comandos
#Em Python:
# for i in range(6):
#      bloco de comandos
# for i in range(6):
#     print("i: ", i)

#Estrutura de Repetição - enquanto - Comando while no python.
#Deve ser utilizado quando não sabemos exatamente o número de
#iterações que iremos repetir.
#Em Portugol:
#enquanto(condição) faça
#      bloco de comandos
#Em Python:
#while(condição):
#      bloco de comandos
i = 0
while(i<6):
    print("i:", i)
    i = i + 2

#Sistema Fibonacci
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


#Sistema de Menu
opção=0
while(opção!=5):
    print("Calculadora")
    print("1 - Somar cinco números: ")
    print("2 - Subtrair cinco números: ")
    print("3 - Multiplcar cinco números: ")
    print("4 - Dividir cinco números: ")
    print("5 - Sair do Sistema")
    opção = int(input("Escolha a.py opção que você deseja: "))
    if(opção==1):
        print("Você escolheu 1 - Somar decimo números")
        numero1 = int(input("Digite o primeiro números:"))
        numero2 = int(input("Digite o segundo números: "))
        numero3 = int(input("Digite o terceiro úumeros: "))
        numero4 = int(input("Digite o quarto números: "))
        numero5 = int(input("Digite o quinto números: "))

        somar = numero1 + numero2 + numero3 + numero4 + numero5
        print("somar: ", somar)
int('0b100', base=0)