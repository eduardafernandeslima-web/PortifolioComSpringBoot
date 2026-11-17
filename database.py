import sqlite3


def criar_tabela():
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')

    conexao.commit()
    conexao.close()


# Cadastrar Produto

def cadastrar_produto(nome, preco, quantidade):
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO produtos (nome, preco, quantidade)
    VALUES (?, ?, ?)
    ''', (nome, preco, quantidade))

    conexao.commit()
    conexao.close()


# Listar Produtos

def listar_produtos():
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    conexao.close()
    return produtos


# Atualizar Produto

def atualizar_produto(id, nome, preco, quantidade):
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()

    cursor.execute('''
    UPDATE produtos
    SET nome = ?, preco = ?, quantidade = ?
    WHERE id = ?
    ''', (nome, preco, quantidade, id))

    conexao.commit()
    conexao.close()


# Excluir Produto

def excluir_produto(id):
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()