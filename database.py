import os
import psycopg2

# Pega a URL do banco de dados no Railway
DATABASE_URL = os.getenv("DATABASE_URL")

# Conecta ao PostgreSQL
conn = psycopg2.connect(DATABASE_URL, sslmode="require")
cursor = conn.cursor()

# Criar a tabela se não existir
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL
    )
    """)
    conn.commit()

# Adicionar um filme ao banco de dados
def adicionar_filme(nome_filme):
    cursor.execute("INSERT INTO filmes (nome) VALUES (%s)", (nome_filme,))
    conn.commit()

# Listar os filmes do banco
def listar_filmes():
    cursor.execute("SELECT nome FROM filmes")
    return [row[0] for row in cursor.fetchall()]

# Remover um filme do banco
def remover_filme(nome_filme):
    cursor.execute("DELETE FROM filmes WHERE nome = %s", (nome_filme,))
    conn.commit()