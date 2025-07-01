numeroA = int(input("digite o numero A: "))
numeroB = int(input("digite o numero B: "))

contador = numeroA + 12
resultado = numeroA

while contador <= numeroB:
    resultado = resultado + contador
    contador += 2

print("resultado: ",resultado)