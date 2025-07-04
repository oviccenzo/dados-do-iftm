total_idade = 0
total_pessoas = 0
pessoas_mais_de_5_filhos = 0
pessoas_menos_de_20_com_filhos = 0
total_pessoas_com_filhos = 0

while True:
    idade = int(input("Digite a idade das pessoa (digite um numero negativo para encerrar): "))
    
    if idade < 0:
        break
    
    filhos = int(input("Digite a quantidade de filhos: "))
    
    total_pessoas += 1
    total_idade += idade
    
    if filhos > 5:
        pessoas_mais_de_5_filhos += 1
        
    if idade < 20 and filhos > 0:
        pessoas_menos_de_20_com_filhos += 1
        
    if filhos > 0:
        total_pessoas_com_filhos += 1
    
if total_pessoas > 0:
    media_idade =  total_idade / total_pessoas
    percent_menos_de_20_com_filhos = (pessoas_menos_de_20_com_filhos / total_pessoas_com_filhos) * 100 if total_pessoas_com_filhos > 0 else 0
    
    print(f"Media de idade do grupo: {media_idade:.2f}")
    print(f"Quantidade de pessoas com mais de 5 filhos: {pessoas_mais_de_5_filhos}")
    print(F"Porcentagem de pessoas com menos de 20 anos e com filho: {percent_menos_de_20_com_filhos:.2f}%")
    print(f"Quantidade de pessoas entrevistados: {total_pessoas}")
else:
    print("Nehum dado foi inserido.")