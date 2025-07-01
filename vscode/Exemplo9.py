tipo = int(input("1-euro, 2-Peso Argetina, 3-iene, 4-libra esterlina, 5-dolar americana, 6-coroa dinamarquesa, 7-renmibi, 8-dolar honk kong, 9-Coroa Checa, 10-Dolar dos Estados Unidos: "))
valor = float(input("Digite o valor a.py ser convertido: "))
valor_convertido = 0

if (tipo == 1):
    valor_convertido = valor * 1.1

if (tipo == 2):
    valor_convertido = valor * 1.2    
    
if (tipo == 3):
    valor_convertido = valor * 1.3    
    
if (tipo == 4):
    valor_convertido = valor * 1.4
    
if(tipo == 5):
    valor_convertido = valor * 1.5

if (tipo == 6):
    valor_convertido = valor * 1.6   
    
if(tipo == 7):
    valor_convertido = valor * 1.7
       
if(tipo == 8):
    valor_convertido = valor * 1.8 
    
if (tipo == 9):
    valor_convertido = valor * 1.9
    
if (tipo == 10):
     valor_convertido = valor * 2.0          
    
print("Valor fornecido: ",valor) 
print("Valor convertido: ",valor_convertido)    
