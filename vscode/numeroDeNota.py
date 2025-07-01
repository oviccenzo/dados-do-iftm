nota = int(input("digite sua nota: "))

if nota >= 9:
    print("conceito A")
elif nota < 9 and nota >= 8:
    print("conceito B")
elif nota < 8 and nota >= 7:
    print("conceito C")
elif nota < 7 and nota >= 6:
    print("conceito D")
else:
    print("conceito F")