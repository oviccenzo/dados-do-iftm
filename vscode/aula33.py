idade = int(input("Digite a.py idade de uma pessoa: "))
idade_mulher = int(input("Digite a.py idade da mulher: "))
idade_homem = int(input("Digite a.py idade do homem: "))
sexo = str(input("Digite o sexo de uma pessoa por favor: ('F' - Feminino) , ('M'- Masculino): "))

faixa_etaria = 0

if idade <= 15:
   faixa_etaria = 1
      
elif 16 <= idade <= 30:
   faixa_etaria = 2

elif 31 <= idade <= 45:
   faixa_etaria = 3

elif 46 <= idade <= 60:
   faixa_etaria = 4

else:
   faixa_etaria = 5
   
print("Faixas etarias: ", faixa_etaria)

media_idade_mulher = idade_mulher / faixa_etaria
media_idade_homem = idade_homem / faixa_etaria

print("Media da idade da mulher: ", media_idade_mulher)
print("Media da idade do homem: ",media_idade_homem)