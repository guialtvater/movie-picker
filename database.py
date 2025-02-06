import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

# Função para conectar ao banco de dados
def conectar_banco():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cursor = conn.cursor()
        print("✅ Conectado ao PostgreSQL")
        return conn, cursor
    except Exception as e:
        print(f"🚨 Erro ao conectar ao banco: {e}")
        return None, None

# Criando conexão inicial
conn, cursor = conectar_banco()

# Corrige erro de transação falha
def resetar_conexao():
    global conn, cursor
    if conn:
        conn.rollback()  # Limpa transações falhas
        conn.close()
    conn, cursor = conectar_banco()

# Criar a tabela com status
def criar_tabela():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'para assistir'
        )
        """)
        conn.commit()
    except Exception as e:
        print(f"⚠️ Erro ao criar tabela: {e}")
        resetar_conexao()

# Adicionar um filme ao banco de dados
def adicionar_filme(nome_filme):
    try:
        cursor.execute("INSERT INTO filmes (nome, status) VALUES (%s, 'lista')", (nome_filme,))
        conn.commit()
    except Exception as e:
        print(f"⚠️ Erro ao adicionar filme: {e}")
        resetar_conexao()

# Listar os filmes do banco
def listar_filmes():
    try:
        cursor.execute("SELECT nome FROM filmes WHERE status = 'lista'")
        return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"⚠️ Erro ao listar filmes: {e}")
        resetar_conexao()
        return []

def listar_filmes_assistidos():
    try:
        cursor.execute("SELECT nome FROM filmes WHERE status = 'assistido'")
        return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"⚠️ Erro ao listar filmes: {e}")
        resetar_conexao()
        return []        

# Remover um filme do banco
def remover_filme(nome_filme):
    cursor.execute("DELETE FROM filmes WHERE nome = %s", (nome_filme,))
    conn.commit()

# Marcar como assistido
def marcar_como_assistido(nome_filme):
    try:
        cursor.execute("UPDATE filmes SET status = 'assistido' WHERE nome = %s", (nome_filme,))
        conn.commit()
    except Exception as e:
        print(f"⚠️ Erro ao marcar como assistido: {e}")
        resetar_conexao()

def adicionar_coluna_status():
    try:
        cursor.execute("ALTER TABLE filmes ADD COLUMN status TEXT NOT NULL DEFAULT 'para assistir'")
        conn.commit()
        print("✅ Coluna 'status' adicionada ao banco de dados.")
    except Exception as e:
        print(f"⚠️ Erro ao adicionar coluna 'status': {e}")    