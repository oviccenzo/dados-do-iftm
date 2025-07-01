import tkinter as tk
import random

def JogarPedra(): 
    print("Jogador escolheu Pedra")
    computador = random.randint(0,2)
    jogadaComputador = listaJogadas[computador]
    if(jogadaComputador=="Papel"):
        print("Computador escolheu Papel")
        print("Computador Ganhou")
    elif(jogadaComputador=='Tesoura'):
        print("Computador escolheu Tesoura")    
        print("Jogador Ganhou")
    else:
        print("Computador escolheu Pedra")
        print("Empatou")
def jogarPapel():
    print("Jogador escolheu Papel")
    computador = random.randint(0, 2)
    jogadaComputador = listaJogadas[computador]
    if (jogadaComputador == "Papel"):
        print("Computador escolheur Papel")
        print("Empatou")           
    elif (jogadaComputador == 'Tesoura'):
        print("Computador escolheu Tesoura")
        print("Computador Ganhou")
    else:
        print("Computaor escolheu Pedra")
        print("Jogador Ganhou")        
def jogaTesoura():
            print("Jogador escolheu Tesoura")
            computador = random.randint(0,2)
            jogadaComputador = listaJogadas[computador]
            if (jogadaComputador== "Papel"):
                print("Computador escolheu Papel")
                print("Jogador Ganhou")
            elif(jogadaComputador == 'Tesoura'):
                print("Computador escolheu Tesoura")
                print("Empatou")
            else:
                print("Computador escolheu Pedra")
                print("Computador Ganhou")        
janela = tk.Tk()
janela.title("Pedra, Papel ou Tesoura")
janela.geometry("900x600")                
botaoPedra = tk.Button(janela, text="pedra", command=lambda:JogarPedra())
botaoPedra.place(x=50, y=50)
botaoPapel = tk.Button(janela, text="Papel", command=lambda:jogarPapel())
botaoPapel.place(x=250, y=50)
botaoTesoura = tk.Button(janela, text="Tesoura", command=lambda:jogaTesoura())
botaoTesoura.place(x=450, y=50)
listaJogadas = ["Pedras", "Papel", "Tesoura"]
janela.mainloop()