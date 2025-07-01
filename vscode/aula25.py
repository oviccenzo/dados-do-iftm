import math

a = float(input("coeficiente de a: "))
b = float(input("coeficiente de b: "))
c = float(input("coeficiente de c: "))

delta = math.pow(b,2) - 4 * a * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print("as raizes da equacao x1 e: ",x1)
print("as raizes da equacao x2 e: ",x2)