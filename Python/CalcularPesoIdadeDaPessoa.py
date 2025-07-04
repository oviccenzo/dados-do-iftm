idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))

if(idade >= 30) & (idade <= 65) & (peso >= 80):
    print("Voce pode doar sangue")
else:
    print("Voce nao pode doar sangue! ")