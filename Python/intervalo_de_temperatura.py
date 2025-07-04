print("Conversao de Fahrenheit para Celsius")

#Solicitacao dos valores iniciais, finais e intervalo
valor_inicial = int(input("Digite o valor inicial em Fahrenheit: "))
valor_final = int(input("Digite o valor final em Fahrenheit: "))
intervalo = int(input("Digite o intervalo desejado entre os valores (ex: 1, 2, etc.): "))

#Cabeçalho da tabela
print("Fahrenheit  Celsius")
print("---------------------")

#Loop para a conversao com base nos valores fornecidos pelo usuario
for fahrenheit in range(valor_inicial, valor_final + 1, intervalo):
    celsius = int((fahrenheit - 32) * 5 / 9)
    print(f"{fahrenheit:^10}  {celsius:^7}")