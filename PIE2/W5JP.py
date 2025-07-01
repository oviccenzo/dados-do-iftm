#A biblioteca tkinter é a responsável por cirar elementos
#gráfico - tela,labels, botões.Nós iremos utilizar
#as classes e outros elementos existentes nessa
#biblioteca para construímos nossa interface com o 
#usuario.
import tkinter as tk
from tkinter import ttk

def gravarArquivos():
    #Após a finalização do sistema pelo usuário.Ou seja após o usuário escolher
    #a opção 5, devemos gravar as informações no arquivos novamente
    arquivo = open("C:/Users/10780099613/Documents/clientes.txt", "w")
    #Percorre a lista de clientes
    for i in clientes:
        #Acrescenta o cliente ao arquivo final
        arquivo.write(i.cpf + '\n')
        arquivo.write(i.nome + '\n')
        arquivo.write(i.endereco + '\n')
        arquivo.write(i.telefone + '\n')
    #Fecha o Arquivo
    arquivo.close()
    janela.destroy()
    
def carregarClientes():
    for i in clientes:
        if(comboCliente.get()==i.nome):
            textoNome.delete("1.0","end")  
            textoCPF.delete("1.0","end")
            textoTelefone.delete("1.0","end")
            textoEndereco.delete("1.0","end")
            textoNome.insert
            textoCPF.insert("1.0","end")            
            textoTelefone.insert("1.0","end")
            textoEndereco.insert("1.0","end")
   
            
def inserirClientes():
    novoCliente = Cliente(textoCPF.get("1.0","end-1c"),textoNome.get("1.0","end-1c"),textoEndereco.get("1.0","end-1c"))
    clientes.append(novoCliente)
    #vetorOpções.append(novoCliente.nome)
    my_insert()

def my_insert(): #removing option from the Combobox
    #if e1.get() not in cb1['value']:
    comboCliente['values'] +=(textoNome.get("1,0","end-1c"),)#add option
    
def remove_combo(): #removing option from the combobox
    my_new=[]#Blank list to hold new values
    for opt in comboCliente['values']:# Loop through all option
        if (opt != comboCliente.get()):
             #print(opt)
             my_new.append(opt) # Add to nwe list
    comboCliente['values']=my_new #assign to new list
    comboCliente.delete(0,'end') # remove from current selection text
    comboCliente.current()
    
def apagarClientes():
    for cliente in clientes:
        if(comboCliente.get()==cliente.nome):
           clientes.remove(cliente)
           remove_combo()            


def alterarClientes():
    print("inserirClientes")
    
#Criando uma classe - um novo tipo de dados.No nosso caso a Classe
#tem o nome de Cliente e possui quatro atributos(características)
#cpf.nome,idade,telefone.                 

class Cliente:
    #Método Construtor chamado __init__. É o método responsável por
    #reservar o espaçna memória no momento que uma variáve; (objeto
    #ou instância da classe) é criada.No nosso caso além dos quatro
    #atribustos recebe como parâmetro  o atributo self. Que faz referência
    #a variável que será criada.
    def __init__(self,cpf,nome,enderco,telefone):
        self.cpf = cpf
        self.nome = nome
        self.endereco = enderco
        self.telefone = telefone
#Criamos uma lista de Clientes Vazia - sem nenhum cliente
clientes = []
#O comado open abre um arquivo a lê o mesmo.O comado possui dois parâmetros
#Endereço do Arquivo no Hd - C:/Users/10780099613/Documents/clientes.txt no
#nosso caso.E o segundo parâmetro indica o que poderemos fazer no arquivo
#No nosso caso o parâmetro é o "r" - que indica que iremos ler o 
#arquivo         
arquivo = open("/Users/rlresende/Documents/viccenzo.iftm/projeto/Clientes.txt")
contadorDelinha = 0
#Percorrw todas as linhas do arquivo atravésdo comando readlines()
for linha in arquivo.readlines():
    #Cada linha do nosso arquivo indica o nome de um cliente.
    #Dessa forma iremos acrescentar cada linha do arquivo na lista
    #de cliente através do comando append
    #O arquivo traz consigo as quebras de linha.Por isso utilizamos
    #o comando strip para retirar as quebras de linha.
    if(contadorDelinha%4==0):
      CPF = linha.strip('\n')  
    elif(contadorDelinha%4==1):
      nome = linha.strip('\n')  
    elif(contadorDelinha%4==2):        
      endereco = linha.strip('\n')  
    elif(contadorDelinha%4==3):    
      telefone = linha.strip('\n')  
      novoCliente = Cliente(CPF,nome,endereco,telefone)
    contadorDelinha = contadorDelinha + 1
#Fecha o arquivo após extrair todos os dados nele existentes
arquivo.close()

#Criando a janela
janela = tk.Tk()
#Configurando o título da janela
janela.title("Cadastro de Clientes- supermercado")
#Configurando as dimensões da janela
janela.geometry("900x600")
bg = tk.PhotoImage(file = "/Users/rlresende/Documents/viccenzo.iftm/projeto/fundo.txt.png")
label1 = tk.Label(janela, image = bg)      
label1.place(x = 0 , y = 0)
#Adicionandp um label na janela
labelCliente = tk.Label(janela, text="Clientes: ") 
labelCliente.place(x=10,y=10)
#Adicionando um combo no cliente
inp_var = tk.StringVar()
vetorOpções = []
for i in clientes:
    nome = i.nome
    vetorOpções.append(nome)
comboCliente = ttk.Combobox(janela, values=vetorOpções)
comboCliente.current()
comboCliente.place(x=110 , y=10)    
botãoCarregar = tk.Button(janela, text="Carregar", command =lambda:carregarClientes())
botãoCarregar.place(x=400 , y=10)
#Adicionando as informações referente ao Nome do Cliente
labelNome = tk.Label(janela, text="Nome: ")
labelNome.place(x=10, y=50)
textoNome = tk.Text(janela, width=50 , height=1)
textoNome.place(x=110, y=50)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = tk.Label(janela , text="CPF: ")
labelCPF.place(x=10 , y=80)
textoCPF = tk.Text(janela,width=50, height=1)
textoCPF.place(x=110, y=80)
#Adicionando as informações referentes ao Endereco do Cliente
labelEndereco = tk.Label(janela, text="Endereco: ")
labelEndereco.place(x=10, y=110)
textoEndereco = tk.Text(janela, width=50 ,height=1 )
textoEndereco.place(x=110, y=110)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = tk.Label(janela, text="Telefone: ")
labelTelefone.place(x=10, y=140)
textoTelefone = tk.Text(janela, width=50, height=1)
textoTelefone.place(x=110, y=140)
#Adicionando um botão a nossa tela
botãoInserir = tk.Button(janela, text="Inserir", command=lambda:inserirClientes())
botãoInserir.place(x=50, y=170)
botãoApagar = tk.Button(janela, text="Apagar",command=lambda:apagarClientes())
botãoApagar.place(x=150, y=170)
botãoApagar = tk.Button(janela, text="Alterar",command=lambda:alterarClientes())
botãoApagar.place(x=250, y= 170)
botãoSair = tk.Button(janela, text="Sair",command=lambda:gravarArquivos)
botãoSair.place(x=350, y=170)


#Executando o loop principal da janela
janela.mainloop()


