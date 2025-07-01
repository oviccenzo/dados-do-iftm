idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

if(idade >= 18) & (idade <= 65) &(peso >= 18):
    print("voce pode doar sangue!")
else:
    print("voce nao pode doar sangue!")