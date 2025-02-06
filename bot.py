import os
import discord
import json
from discord.ext import commands
import database
import random
database.criar_tabela() 
database.adicionar_coluna_status()

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
    filmes = database.listar_filmes()
    if not filmes:
        await ctx.send("📭 Nenhum filme para assistir. Adicione novos com `!addfilme`.")
        return

    filme_escolhido = filmes[0]  # Mantém a ordem de adição
    #database.marcar_como_assistido(filme_escolhido)  # Apenas altera o status
    await ctx.send(f"🎬 **Filme escolhido:** {filme_escolhido} 🍿")


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
        lista_filmes = "\n".join([f"{i+1}. {filme[1]}" for i, filme in enumerate(filmes)])
        await ctx.send(f"📜 **Lista de Filmes Para Assistir:**\n{lista_filmes}")
    else:
        await ctx.send("📭 Nenhum filme para assistir. Adicione novos com `!addfilme`.")

# Comando para remover um filme pelo nome
@bot.command()
async def excluir(ctx, *, entrada):
    if entrada.isdigit():
        posicao = int(entrada)
        filme = database.obter_filme_por_posicao(posicao)
        if filme:
            database.excluir_filme(filme[1])
            await ctx.send(f"❌ **Filme removido do banco:** {filme[1]}")
        else:
            await ctx.send("❌ Posição inválida. Use `!listar` para ver os números corretos.")
    else:
        database.excluir_filme(entrada)
        await ctx.send(f"❌ **Filme removido do banco:** {entrada}")

# Comando para marcar um filme como assistido
@bot.command()
async def assistido(ctx, *, entrada):
    if entrada.isdigit():  # Se o usuário inserir um número
        posicao = int(entrada)
        filme = database.obter_filme_por_posicao(posicao)
        if filme:
            database.marcar_como_assistido(filme[1])
            await ctx.send(f"✅ **Filme marcado como assistido:** {filme[1]}")
        else:
            await ctx.send("❌ Posição inválida. Use `!listar` para ver os números corretos.")
    else:  # Se for um nome
        database.marcar_como_assistido(entrada)
        await ctx.send(f"✅ **Filme marcado como assistido:** {entrada}")


# Comando para escolher um filme de maneira aleatória
import random

@bot.command()
async def aleatorio(ctx):
    filmes = database.listar_filmes()
    if not filmes:
        await ctx.send("📭 Nenhum filme para assistir. Adicione novos com `!addfilme`.")
        return

    filme_escolhido = random.choice(filmes)
    #database.marcar_como_assistido(filme_escolhido)  # Apenas altera o status
    await ctx.send(f"🎲 **Filme escolhido aleatoriamente:** {filme_escolhido} 🍿")

@bot.command()
async def assistidos(ctx):
    filmes = database.listar_filmes_assistidos()
    if filmes:
        lista_filmes = "\n".join([f"{i+1}. {filme}" for i, filme in enumerate(filmes)])
        await ctx.send(f"📜 **Lista de Filmes Assistidos:**\n{lista_filmes}")
    else:
        await ctx.send("📭 Nenhum filme foi assistido ainda.")

# Evento de inicialização
@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

# Rodar o bot
bot.run(TOKEN)
