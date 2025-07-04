def riaz_quadrado_aproximado(numero):
    soma_impares = 0
    raiz_aproximado = 0
    
    while soma_impares <= numero:
        raiz_aproximado += 1
        soma_impares += (2 * raiz_aproximado - 1)
        
    #Ajustando a raiz aproximado caso a soma dos impares seja maior que o numero 
    if soma_impares > numero:
        raiz_aproximado -= 1
        
    return raiz_aproximado

#Lendo o numero do usuario
numero = int(input("Digite um numero inteiro positivo para calcular a raiz quadrada: "))

resultado = riaz_quadrado_aproximado(numero)
print(f"A raiz quadrado inteira de {numero} e aproximadamente {resultado}") 