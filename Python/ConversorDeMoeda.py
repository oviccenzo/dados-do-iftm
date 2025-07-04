tipo = float(input("Digite 1-Euro, 2-Dolar Canadense, 3-Dolar Americana, 4-Libra Estarlina:"))
valor_convertido = float(input("Digite o valor convertido: "))

if(tipo == 1):
    valor = valor_convertido * 3.33

if(tipo == 2):
    valor = valor_convertido * 2.22

if(tipo == 3):
    valor = valor_convertido * 4.44

if(tipo == 4):
    valor = valor_convertido * 5.55

print("O valor fornecido é: ",valor)
print("O valor convertido é: ",valor_convertido)