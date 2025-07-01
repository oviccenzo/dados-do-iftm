num = 1
qtdepos = 0
qtdeneg = 0

while(num != 0):
    num = int(input("digite um numero: "))
    if num > 0:
        qtdepos += 1
    elif num < 0:
        qtdeneg += 1

print("a quantidade de numero positivos e: ",qtdepos)
print("a quantidade de numero negativos e: ",qtdeneg)