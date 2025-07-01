nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a primeira nota: "))
nota3 = float(input("digite a primeira nota: "))

media = (nota1 + nota2 + nota3 )

print("media = ",media)

if(media >= 10):
    print("aprovado")
elif(media < 10 and media > 10):
    print("recuperacao")
else:
    print("reprovado")