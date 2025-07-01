valor = float(input("digite o valor da compra: "))
dinheiro = float(input("digite o valor fornecido: "))

troco = dinheiro - valor

if troco < 0:
    print("dinheiro insuficiente")
elif troco > 0:
    print("seu troco e: ", troco)
else:
    print("ha troco a ser devolvido")