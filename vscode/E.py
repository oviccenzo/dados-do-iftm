totalminuto = int(input("Digite um numero: "))
horas = totalminuto // 60
minuto = totalminuto % 60
print(totalminuto, " = ",  horas, " hora é ", minuto," minutos ")
import random

# Gerar número secreto (igual à função gerarNumeroAleatorio no JS)
numero_secreto = random.randint(1, 10)

# Exibir o título e o texto na tela (sem usar def)
print('Jogo do número secreto')
print('Escolha um número entre 1 e 10:')

# A lógica de verificação do chute
chute_usuario = int(input('Digite seu chute: '))

# Mostrar o número secreto (igual ao console.log(numeroSecreto) no JS)
print(f'Número secreto: {numero_secreto}') 