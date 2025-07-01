hora_extra = int(input("Quantas hora extra trabalhada: "))
faltas = int(input("Quantas horas por falta: "))
ponto = hora_extra - 2/20 * faltas

if(ponto > 40):
   print("bônus R$ 5000,00")
elif(ponto > 30 and ponto <= 40):
   print("bônus R$ 4000,00")
elif(ponto > 20 and ponto <= 30):
   print("bônus R$ 3000,00")
elif(ponto > 10 and ponto <= 20):
   print("bônus R$ 2000,00")
else:
   (ponto <= 10)
   print("bônus R$ 1000,00")