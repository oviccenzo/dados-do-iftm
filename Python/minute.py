def minutes_para_fahrenheit(minutes):
    return (minutes * 9 / 5) + 32

def escolher_vestuario(minutes):
    fahrenheit = minutes_para_fahrenheit(minutes)
    if fahrenheit < 65:
        return "calças"
    else:
        return "bermudas"

# Solicitar entrada do tempo em minutos
tempo_em_minutos = float(input("Digite o tempo em minutos: "))

# Converter tempo para Fahrenheit
temperatura_fahrenheit = minutes_para_fahrenheit(tempo_em_minutos)

# Determinar o vestuario adequado para Fahrenheit
vestuario = escolher_vestuario(tempo_em_minutos)

# Exibir temperatura em Fahrenheit e o vestuario recomendado
print(f"A temperatura e, Fahrenheit é: {temperatura_fahrenheit}°F")
print(f"Voce deve vestir {vestuario}.")

notas = [7.5, 8.2, 6.9, 9.1, 5.8]
notas_minima = min(notas)
print(f"A menor nota é: {notas_minima}")
