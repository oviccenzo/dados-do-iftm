minuto = float(input("Calcular o minuto: "))
segundo = float(input("Calcular o segundo: "))
tempo = float(input("Calcular o tempo: "))

VelocidadeMedia = segundo / tempo
hora = tempo / 3600

print("O tempo gasto em hora é: ",VelocidadeMedia,"hora")

print("O minuto equivale a hora: ",hora)
