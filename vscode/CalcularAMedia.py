def le_nota():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    nota3 = float(input("Digite a terceira nota: "))
    return nota1, nota2, nota3

def f_media(nota1, nota2, nota3):
    media = (nota1 * 2 + nota2 * 3 + nota3 * 4) / 9
    return media

nota = le_nota()
media = f_media(*nota)
print(f"A média das três provas é: {media:.2f}")
