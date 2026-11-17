import tkinter as tk
from tkinter import ttk, messagebox
import database


def listar_produtos():
    for item in tabela.get_children():
        tabela.delete(item)
    produtos = database.listar_produtos()
    for produto in produtos:
        tabela.insert("", tk.END, values=produto)


def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    tabela.selection_remove(tabela.selection())


def cadastrar_produto():
    nome = entrada_nome.get().strip().replace("'", "''")
    preco = entrada_preco.get().strip().replace("'", "''")
    quantidade = entrada_quantidade.get().strip()

    if not nome or not preco or not quantidade:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)
        if preco < 0 or quantidade < 0:
            messagebox.showerror("Erro", "Preço e quantidade devem ser valores positivos.")
            return
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preço deve ser um número válido e quantidade deve ser um número inteiro."
        )
        return

    database.cadastrar_produto(nome, preco, quantidade)
    limpar_campos()
    listar_produtos()


def selecionar_produto(event):
    item_selecionado = tabela.selection()
    if not item_selecionado:
        return
    dados = tabela.item(item_selecionado[0], 'values')
    entrada_nome.delete(0, tk.END)
    entrada_nome.insert(0, dados[1])
    entrada_preco.delete(0, tk.END)
    entrada_preco.insert(0, dados[2])
    entrada_quantidade.delete(0, tk.END)
    entrada_quantidade.insert(0, dados[3])


def atualizar_produto():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um produto para atualizar.")
        return

    id_produto = tabela.item(item_selecionado[0], 'values')[0]
    nome = entrada_nome.get().strip().replace("'", "''")
    preco = entrada_preco.get().strip().replace("'", "''")
    quantidade = entrada_quantidade.get().strip()

    if not nome or not preco or not quantidade:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)
        if preco < 0 or quantidade < 0:
            messagebox.showerror("Erro", "Preço e quantidade devem ser valores positivos.")
            return
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preço deve ser um número válido e quantidade deve ser um número inteiro."
        )
        return

    database.atualizar_produto(id_produto, nome, preco, quantidade)
    limpar_campos()
    listar_produtos()


def excluir_produto():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um produto para excluir.")
        return
    id_produto = tabela.item(item_selecionado[0], 'values')[0]
    database.excluir_produto(id_produto)
    limpar_campos()
    listar_produtos()


janela = tk.Tk()

janela.title("Cadastro de Produtos")
janela.geometry("480x400")

tk.Label(janela, text="Nome do Produto:").grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Preço:").grid(row=1, column=0, padx=5, pady=5)
entrada_preco = tk.Entry(janela)
entrada_preco.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=2, column=1, padx=5, pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(frame_botoes, text="Cadastrar", command=cadastrar_produto).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar_produto).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir_produto).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Limpar Campos", command=limpar_campos).pack(side=tk.LEFT, padx=5)

colunas = ("ID", "Nome", "Preço", "Quantidade")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Nome")
tabela.heading("Preço", text="Preço")
tabela.heading("Quantidade", text="Quantidade")

tabela.column("ID", width=50, anchor=tk.CENTER)
tabela.column("Nome", width=200, anchor=tk.W)
tabela.column("Preço", width=100, anchor=tk.E)
tabela.column("Quantidade", width=100, anchor=tk.E)

tabela.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

tabela.bind("<<TreeviewSelect>>", selecionar_produto)

database.criar_tabela()
listar_produtos()

janela.mainloop()