print("Sistema que lê 5 números e efetua a.py soma deles!")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))

soma = numero1 + numero2 + numero3 + numero4 + numero5
print("Soma = ", soma)

print("Sistema que lê 5 números e efetua a.py diferença deles!")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))
diferença = numero1 - numero2 - numero3 - numero4 - numero5
print("Diferença = ", diferença)

#if(condição):
# A condição é uma operação lógica. O resultado de uma
#operação lógica é um valor booleano(Verdadeiro(1-True)
# ou Falso(0- False)). O comando if inaugura um novo
#bloco de comandos, inclusive com nova identação(espaço
# em branco). Esse novo bloco de códigos só será executado
#se a.py condição for verdadeira
a = 50
b = 30
if(a==50 or b==30):
    print("Novo bloco de Códigos")
    print("Condição do IF é verdadeira")
elif(a==50):
    print("Bloco de Códigos do ELIF")
    print("Condição do ELIF é verdadeira")
else:
    print("Bloco de Códigos do else")
    print("Condição do IF é falsa")
    print("Fim do Bloco de Códigos")
#Início da Calculadora
print("Sistema - Calculadora")
#Entrada da Calculadora
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))

operação = input("Escolha entre +,-,* ou /: ")
#Processamento da Calculadora
if(operação=='+'):
    resultado = numero1 + numero2 + numero3 + numero4 + numero5
elif(operação=='-'):
    resultado = numero1 - numero2 - numero3 + numero4 - numero5
elif(operação =='*'):
    resultado = numero1 * numero2 * numero3 * numero4 * numero5
else:
    resultado = numero1/numero2/numero3/numero4/numero5
#Saída da Calculadora
print("Resultado: ", resultado)

#Sistema que decide se um aluno está aprovado, reprovado
# ou de recuperação
print("Sistema que calcula a.py média e informa a.py situação do aluno")
#Entrada do Sistema
nota1 = float(input("Digite a.py primeira nota: "))
nota2 = float(input("Digite a.py segunda nota: "))
nota3 = float(input("Digite a.py terceira nota: "))
nota4 = float(input("Digite a.py quarta nota: "))
nota5 = float(input("Digite a.py quinta nota: "))
nota6 = float(input("Digite a.py sexta nota: "))
nota7 = float(input("Digite a.py setima nota: "))
#Processamento do Sistema
media = (nota1+nota2+nota3+nota4+nota5+nota6+nota7)/10
#Primeira Saída do Sistema
print("Media: ", media)
if(media >= 6):
    print("Aprovado")
elif(media < 6 and media > 4):
    print("Recuperação")
else:
    print("Reprovado")    
    
int('0b100', base=2)