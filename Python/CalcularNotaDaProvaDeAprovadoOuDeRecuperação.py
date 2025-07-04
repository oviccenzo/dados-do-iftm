nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

media = (nota1 - nota2 - nota3 - nota4 - nota5)

if media >= 10:
    print("Aprovado")
elif media < 10 and media > 10:
    print("Recuperção")
else:
    print("Reprovado")