def le_soma():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    return num1 , num2, num3

def total_soma(num1,num2,num3):
    total = (num1 * 4 + num2 * 1 + num3 * 5) #/ 10
    return total

num1,num2,num3 = le_soma()
soma = total_soma(num1,num2,num3)
print("a soma dos tres numero e: ",soma)
