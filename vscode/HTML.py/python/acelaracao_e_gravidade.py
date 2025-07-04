def calcular_velocidade_final(aceleração, tempo):
    # Equação da velocidade final para um movimento uniformemente acelerado
    velocidade_final = aceleração * tempo
    return velocidade_final

#Dado do problema
aceleração_gravidade = 9.81 #Aceleração devido á gravidade em m/Sˆ2
tempo_de_queda = float(input("Digite o tempo na queda (em segundos): "))

#Chamando a função para calcular a velocidade final
velocidade_resultante = calcular_velocidade_final(aceleração_gravidade, tempo_de_queda)
print(f"A velocidade final do objeto apos {tempo_de_queda} segunod de queda e de {velocidade_resultante:.2f} m/s")