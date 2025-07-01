# w = int(input("Digite um numero: "))
# a = (4 + (-4) ** w) // 20
# print("As recorrencia da formula fechada e: ",a)


# for a in range(0,10):
#     print((4 + (-4)**a) // 20)
n_termo = 10

a_n = 3

for n in range(1,n_termo + 1):
    a_n = a_n + (n - 1) * 5
    print( f"a{n} = {a_n}" )
    

