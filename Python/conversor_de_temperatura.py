print("Fahrenheit  Celsius")
print("---------------------")

for fahrenheit in range(32, 81):
    celsius = int((fahrenheit - 32) * 5 / 9)
    print(f"{fahrenheit:^10} {celsius:^7}")