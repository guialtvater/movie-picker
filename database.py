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
        nome TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'lista'
    )
    """)
    conn.commit()

# Adicionar um filme ao banco de dados
def adicionar_filme(nome_filme):
    cursor.execute("INSERT INTO filmes (nome, status) VALUES (%s, 'lista')", (nome_filme,))
    conn.commit()

# Listar os filmes do banco
def listar_filmes():
    cursor.execute("SELECT nome FROM filmes WHERE status = 'lista'")
    return [row[0] for row in cursor.fetchall()]

# Remover um filme do banco
def remover_filme(nome_filme):
    cursor.execute("DELETE FROM filmes WHERE nome = %s", (nome_filme,))
    conn.commit()

# Marcar como assistido
def marcar_como_assistido(nome_filme):
    cursor.execute("UPDATE filmes SET status = 'assistido' WHERE nome = %s", (nome_filme,))
    conn.commit()

def adicionar_coluna_status():
    try:
        cursor.execute("ALTER TABLE filmes ADD COLUMN status TEXT NOT NULL DEFAULT 'para assistir'")
        conn.commit()
        print("✅ Coluna 'status' adicionada ao banco de dados.")
    except Exception as e:
        print(f"⚠️ Erro ao adicionar coluna 'status': {e}")    