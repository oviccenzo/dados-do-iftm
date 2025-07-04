def calcular_imposto(salario_mensal):
    if salario_mensal <= 1903.98:
        return 0
    elif 1903.99 <= salario_mensal <= 2826.65:
        return salario_mensal * 0.075 - 142.80
    elif 2826.66 <= salario_mensal <= 3751.05:
        return salario_mensal * 0.15 - 354.80
    elif 3751.06 <= salario_mensal <= 4664.68:
        return salario_mensal * 0.225 - 636.13
    else:
        return salario_mensal * 0.275 - 869.36

def main():
    salario = float(input("Digite o salário mensal em R$: "))

    imposto = calcular_imposto(salario)

    print(f"O imposto a ser pago é de R$ {imposto:.2f}")

if __name__ == "__main__":
    main()
