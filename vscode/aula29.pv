#A biblioteca tkinter é a.py responsável por criar elementos
#gráficos - tela, labels, botões. Nós iremos utilizar
#as classes e outros elementos existentes nessa
# biblioteca para construírmos nossa interface com o
# usuário.
import tkinter as tk
from tkinter import ttk

# Criando a.py janela
janela = tk.Tk()
# Configurando o título da janela
janela.title("Cadastro de Cliente - Supermercado")
# Configurando as dimensões da janela
janela.geometry("900x600")
# Adicionando um label na janela
labelCliente = tk.Label(janela, text="Clientes: ")
labelCliente.place(x=10,y=10)
#Adicionando um combo no cliente
vetorOpcoes = ["Masculino", "Feminino"]
comboCliente = ttk.Combobox(janela,values=vetorOpcoes)
comboCliente.current()
comboCliente.place(x=110,y=10)
#Adicionando as informações referentes ao nome do Cliente
labelNome = tk.Label(janela, text="Nome: ")
labelNome.place(x=10,y=50)
textoNome = tk.Text(janela,width=50, height=1)
textoNome.place(x=110,y=50)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = tk.Label(janela, text="CPF:")
labelCPF.place(x=10, y=80)
textoCPF = tk.Text(janela,width=50, height=1)
textoCPF.place(x=110, y=80)
#Adicionando as informações referentes ao endereço do Cliente
labelEndereco = tk.Label(janela, text="Endereço:")
labelEndereco.place(x=10,y=110)
textoEndereço = tk.Text(janela,width=50,height=1)
textoEndereço.place(x=110, y=110)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = tk.Label(janela, text="Telefone:")
labelTelefone.place(x=10,y=140)
textoTelefone = tk.Text(janela,width=50,height=1)
textoTelefone.place(x=110,y=140)
#Adicionando um botão a.py nossa tela
botaoInserir = tk.Button(janela, text="Inserir")
botaoInserir.place(x=50, y=170)
botaoApagar = tk.Button(janela, text="Apagar")
botaoApagar.place(x=150, y=170)
botaoAlterar = tk.Button(janela, text="Alterar")
botaoAlterar.place(x=250,y=170)
# Executando o loop principal da janela
janela.mainloop()