#Lendo os 20 valores 
for i in range(1 , 11):
    n = int(input(f"Digite o {i} valor para calular a tabuada: "))
    print(f"Tabuada de {n}: ")
    for j in range(1, 11):
        print(f"{n} x {j} = {n * j}")
    print("-------------")