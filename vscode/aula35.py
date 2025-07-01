import tkinter as tk
from tkinter import ttk


class Produto:
    def _init_(self, marca, barra, validade, valor, fornecedor, foto):
        self.marca = marca
        self.barra = barra
        self.validade = validade
        self.valor = valor
        self.fornecedor = fornecedor
        self.foto = foto


produtos = []
arquivo = open("/Users/rlresende/Documents/viccenzo.iftm/projeto/produtos.txt")
contadorDelinha = 0


def new_func(marca):
    return marca


for linha in arquivo.readlines():
    if (contadorDelinha % 4 == 0):
        marca = linha.strip('\n')
    elif (contadorDelinha % 4 == 1):
        barra = linha.strip('\n')
    elif (contadorDelinha % 4 == 2):
        validade = linha.strip('\n')
    elif (contadorDelinha % 4 == 3):
        valor = linha.strip('\n')
    elif (contadorDelinha % 4 == 4):
        fornecedor = linha.strip('\n')
    elif (contadorDelinha % 4 == 5):
        foto = linha.strip('\n')
        novoProduto = Produto(new_func(marca), barra, validade, valor, fornecedor, foto)  # type: ignore
        produtos.append(novoProduto)
    contadorDelinha = contadorDelinha + 1
arquivo.close()
janela = tk.Tk()
janela.title("Cadastro de Produtos")
janela.geometry("900x600")
janela.config(bg="silver")
labelProduto = tk.Label(janela, text="Produtos: ")
labelProduto.place(x=10, y=10)
vetorOpcoes = []
for i in produtos:
    marca = i.marca
    vetorOpcoes.append(marca)
comboProduto = ttk.Combobox(janela, values=vetorOpcoes)
comboProduto.current()
comboProduto.place(x=110, y=10)
labelMarca = tk.Label(janela, text="Marca: ")
labelMarca.place(x=10, y=50)
labelMarca = tk.Text(janela, width=50, height=2)
labelMarca.place(x=110, y=50)
labelBarra = tk.Label(janela, text="Cód.Barra: ")
labelBarra.place(x=10, y=80)
textoBarra = tk.Text(janela, width=50, height=2)
textoBarra.place(x=110, y=80)
labelValidade = tk.Label(janela, text="Data Validade:")
labelValidade.place(x=10, y=110)
textoValidade = tk.Text(janela, width=50, height=2)
textoValidade.place(x=110, y=110)
labelValor = tk.Label(janela, text="Custo:")
labelValor.place(x=10, y=140)
textoValor = tk.Text(janela, width=50, height=2)
textoValor.place(x=110, y=140)
labelFornecedor = tk.Label(janela, text="Fornecedor:")
labelFornecedor.place(x=10, y=170)
textoFornecedor = tk.Text(janela, width=50, height=2)
textoFornecedor.place(x=110, y=170)
labelFoto = tk.Label(janela, text="Foto:")
labelFoto.place(x=650, y=10)
textoFoto = tk.Text(janela, width=30, height=15)
textoFoto.place(x=550, y=30)
labelVenda = tk.Label(janela, text="Preço Venda:")
labelVenda.place(x=210, y=230)
textoVenda = tk.Text(janela, width=50, height=15)
textoVenda.place(x=50, y=250)
labelMargem = tk.Label(janela, text="Lucro:")
labelMargem.place(x=650, y=280)
textoMargem = tk.Text(janela, width=30, height=10)
textoMargem.place(x=550, y=310)
botaoCadastrar = tk.Button(janela, text="Cadastrar")
botaoCadastrar.place(x=50, y=200)
botaoVenda = tk.Button(janela, text="Vender")
botaoVenda.place(x=130, y=200)
botaoReceber = tk.Button(janela, text="Receber")
botaoReceber.place(x=210, y=200)
botaoBaixar = tk.Button(janela, text="Baixar")
botaoBaixar.place(x=290, y=200)
janela.mainloop()
