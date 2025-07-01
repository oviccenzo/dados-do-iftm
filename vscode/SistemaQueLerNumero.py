print("Sistema que le 3 numero e efetua a soma deles")
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))
soma = num1 + num2 + num3
print("soma = ",soma)

print("Sistmea que le 3 numero e efetua diferenca deles!")
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))
diferenca = num1 - num2 - num3
print("diferenca = ",diferenca)

#if(condicao):
# a condicao e uma operacao logica. O resultado de uma
# operacao logica e um valor booleano(verdadeiro(1-True)
# ou falso(0-False)).O consumo do if inaugura um novo bloco
# de comandos ,inclusives com uma nova identacao (espaco
# em branco).Esse novo bloco de codigos so sera executado
# se a condicao for verdadeira
a = 5
b = 3
if(a == 5 or b == 30):
    print("Novo bloco de codigos")
    print("Condicao do IF e verdadeira")
elif (a == 50):
    print("Bloco de codigos do ELIF")
    print("Condicao do ELIF e verdadeira")
else:
    print("Bloco de Codigos do else")
    print("Condicao do IF e falsa")
print("Fim do Bloco de Codigos")


#Inicio da Calculadora
print("Sistema - Calculadora")
#Entrada da Calculadora
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacão = input("Escolha entre +,-,* ou /: ")
#Processamento da Calculadora
if(operacão=='+'):
    resultado = numero1 + numero2
elif(operacão=='-'):
    resultado = numero1 - numero2
elif(operacão =='*'):
    resultado = numero1 * numero2
else:
    resultado = numero1/numero2
#Saida da Calculadora
print("Resultado: ", resultado)

#Sistema que decide se um aluno esta aprovado, reprovado
# ou de recuperacão
print("Sistema que calcula a.py media e informa a.py situacão do aluno")
#Entrada do Sistema
nota1 = float(input("Digite a.py primeira nota: "))
nota2 = float(input("Digite a.py segunda nota: "))
#Processamento do Sistema
media = (nota1+nota2)/2
#Primeira Saida do Sistema
print("Media: ", media)
if(media>=6):
    print("Aprovado")
elif(media<6 and media>4):
    print("Recuperacão")
else:
    print("Reprovado")