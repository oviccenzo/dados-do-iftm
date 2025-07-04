import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
#Criando um objeto da classe circulo
Circulo1 = Circulo(5)

#Calculando a área e o perimetro do circulo
area = Circulo1.calcular_area()
perimetro = Circulo1.calcular_perimetro()

#Exibindo os resultados
print("Área do circulo: ", area)
print("Perimetro do circulo: ", perimetro)


