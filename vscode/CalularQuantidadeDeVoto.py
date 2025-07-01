print("Quantidade total de voto para cada candidato")
print("1 - candidato 1")
print("2 - candidato 2")
print("3 - candidato 3")
print("4 - candidato 4")
print("5 - nulo")
print("6 - branco")
print("0 - sair")

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
sair = 0 

voto = int(input("Digite seu voto: "))

while(voto > 0):
    if (candidato1 == 1):
        candidato1 = candidato1 + 1
    if (candidato2 == 2):
        candidato2 = candidato2 + 1
    if (candidato3 == 3):
        candidato3 = candidato3 + 1
    if (candidato3 == 4):
        candidato4 = candidato4 + 1
    if (voto == 5):
        voto = nulo + 1
    if (voto == 6):
        voto = branco + 1           
    voto = int(input("Digite seu voto: "))  

print("Todtal de voto para cada candidato: ")
print("total de voto nulo: ")
print("Total de voto em branco: ")   
print("Candidato1: ")    
print("Candidato2: ")
print("Candidato3: ")
print("Candidato4: ")
print("Nulo: ")
print("Branco: ")
print("Sair: ")