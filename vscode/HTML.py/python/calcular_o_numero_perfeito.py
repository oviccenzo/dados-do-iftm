def e_um_numero_perfeito(numero):
    #Variavel para armazenar a soma dos divisores
    sum = 0
    
    #Encontre todos os divisores proprios do numero e os soma
    for i in range(1,numero):
        if numero % i == 0:
            sum += i
            
    #verifica se a soma dos divisores e igual ao numero original
    if sum == numero:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))

#Chama a funcao e_um_numero_perfeito e exibe o resultado
if e_um_numero_perfeito(numero):
    print(numero, "e um numero perfeito.")
else:
    print(numero, "Nao e um numero perfeito.")    