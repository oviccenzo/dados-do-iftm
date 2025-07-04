num1 = int(input("Digite o primeiro numero inteiro positivos: "))
num2 = int(input("Digite o segundo numero inteiro positivos: "))

if num1 > num2:
    num1, num2 = num2, num1
    
print("Múltiplo de 7 entre",num1,"e",num2,":")
while num1 <= num2:
    if num1 % 7 == 0:
        print(num1)
    num1 += 1