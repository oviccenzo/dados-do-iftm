horas_trabalhadas = int(input("quantas horas trabalhadas: ")) 
salario = 0 

if (horas_trabalhadas <= 40):
    salario = horas_trabalhadas * 2
else:
    salario = 320 + (horas_trabalhadas * 12)

print("Número de horas trabalhadas: ", horas_trabalhadas)
print("Salário semanal: ", salario)
