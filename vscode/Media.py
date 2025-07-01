def f_media(nota1,nota2,nota3):
    return ((nota1 * 2 + nota2 * 3 + nota3 * 4) / 9.0)

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = f_media(nota1,nota2,nota3)
    print(f"imprimir a media das tres provas: {media:.2f}")

if __name__ == "__main__":
    main()
