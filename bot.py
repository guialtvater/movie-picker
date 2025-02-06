import os
import discord
import json
from discord.ext import commands
import database
database.criar_tabela() 

# Configuração do bot
TOKEN = os.getenv("TOKEN")
FILMES_FILE = "filmes.json"
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia mensagens nos canais

bot = commands.Bot(command_prefix="/", intents=intents)

# Função para carregar os filmes do arquivo JSON
def carregar_filmes():
    try:
        with open(FILMES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar os filmes no arquivo JSON
def salvar_filmes(filmes):
    with open(FILMES_FILE, "w") as file:
        json.dump(filmes, file, indent=4)

# Carregar filmes na inicialização
filmes = carregar_filmes()

# Comando para escolher o próximo filme (do mais antigo para o mais novo)
@bot.command()
async def escolher(ctx):
    filmes = database.listar_filmes()  # Pega a lista de filmes do banco
    if filmes:
        filme_escolhido = filmes[0]  # Seleciona o mais antigo (primeiro da lista)
        database.remover_filme(filme_escolhido)  # Remove do banco
        await ctx.send(f"🎬 **Filme escolhido:** {filme_escolhido} 🍿")
    else:
        await ctx.send("📭 A lista de filmes está vazia. Adicione novos filmes com `!addfilme`.")

# Comando para adicionar um novo filme
@bot.command()
async def addfilme(ctx, *, nome_filme):
    database.adicionar_filme(nome_filme)
    await ctx.send(f"✅ **Filme adicionado:** {nome_filme}")

# Comando para listar os filmes na ordem de exibição
@bot.command()
async def listar(ctx):
    filmes = database.listar_filmes()
    if filmes:
        lista_filmes = "\n".join([f"{i+1}. {filme}" for i, filme in enumerate(filmes)])
        await ctx.send(f"📜 **Lista de Filmes:**\n{lista_filmes}")
    else:
        await ctx.send("📭 A lista de filmes está vazia. Adicione novos filmes com `!addfilme`.")

# Comando para remover um filme pelo nome
@bot.command()
async def remover(ctx, *, nome_filme):
    database.remover_filme(nome_filme)
    await ctx.send(f"❌ **Filme removido:** {nome_filme}")

# Evento de inicialização
@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

# Rodar o bot
bot.run(TOKEN)
