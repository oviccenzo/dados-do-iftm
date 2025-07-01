quantidade = 0
nota = 7

while(nota > 0) and (nota < 10):
    nota = int(input("digite a nota: "))
    if nota >= 7:
        quantidade += 1
        
print("quantidade maiores ou iguais a 7: ",quantidade)