distancia = float(input("informe a distancia por favor: "))
valor = 4

if(0 <= distancia <= 3):
    valor = valor + (distancia * 0.5)
if(3 < distancia <= 6):
    valor = valor + (distancia * 0.75)

if(distancia > 6):
    valor = valor + (distancia * 1)

print("a distancia e: ",distancia)
print("o valor e: ",valor)