# 🎬 Movie Picker Bot 🎬

Um bot do Discord para **gerenciar sua lista de filmes**, escolhê-los aleatoriamente e acompanhar o que já foi assistido.  
Os dados são armazenados de forma **persistente no PostgreSQL**, garantindo que nada se perca, mesmo após reiniciar.  

---

## 🚀 **Recursos**
✅ **Adicionar filmes** a uma lista com status **"para assistir"**.  
✅ **Listar os filmes** que ainda não foram assistidos, com numeração.  
✅ **Escolher um filme automaticamente** e marcá-lo como assistido.  
✅ **Escolher um filme aleatório** e marcá-lo como assistido.  
✅ **Marcar um filme como assistido** pelo **número** na lista ou pelo **nome**.  
✅ **Excluir um filme permanentemente** pelo **número** na lista ou pelo **nome**.  
✅ **Armazenamento persistente** no **PostgreSQL** (via Railway).  
✅ **Rodando 24/7** na nuvem.  

---

## 🔧 **Instalação e Configuração**
### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

### **2️⃣ Criar e ativar um ambiente virtual (opcional)**
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

### **3️⃣ Instalar dependências**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar as variáveis de ambiente**
Crie um arquivo `.env` e adicione:
```
TOKEN=SEU_TOKEN_DO_DISCORD
DATABASE_URL=URL_DO_SEU_BANCO_POSTGRES
```

Se estiver rodando no Railway, adicione essas variáveis em **Deployments > Variables**.

---

## 🚀 **Rodando o Bot Localmente**
```bash
python bot.py
```

Se quiser rodar em **background** (sem precisar deixar o terminal aberto):
```bash
nohup python bot.py &
```

---

## 🌍 **Rodando no Railway**
### **1️⃣ Criar um banco de dados no Railway**
1. Vá até o [Railway](https://railway.app/).
2. Crie um novo projeto e clique em **"Add Plugin"** → **PostgreSQL**.
3. Copie a **DATABASE_URL** gerada.

### **2️⃣ Adicionar as variáveis de ambiente**
No Railway:
- Vá para **"Variables"**.
- Adicione:
  - **`TOKEN`** → Cole o token do bot do Discord.
  - **`DATABASE_URL`** → Cole a URL do PostgreSQL.

### **3️⃣ Fazer deploy**
1. **Suba seu código para o GitHub**:
   ```bash
   git add .
   git commit -m "Deploy no Railway"
   git push origin main
   ```
2. **No Railway**, conecte o repositório e clique em **"Deploy"**.
3. O bot ficará online automaticamente! 🎉

---

## 🎮 **Comandos do Bot**
| Comando                 | O que faz? |
|-------------------------|------------|
| `!addfilme <nome>`      | Adiciona um filme à lista (status: "para assistir"). |
| `!listar`               | Mostra apenas os filmes **"para assistir"** com numeração. |
| `!escolher`             | Escolhe o **mais antigo** da lista e marca como assistido. |
| `!randomfilme`          | Escolhe um **aleatório** da lista e marca como assistido. |
| `!remover <num/nome>`   | **Marca como assistido** um filme pelo **número na lista** ou pelo **nome**. |
| `!excluir <num/nome>`   | **Exclui permanentemente** um filme pelo **número na lista** ou pelo **nome**. |

---

## **📌 Como Usar os Novos Comandos?**
1️⃣ **Listar filmes**:
   ```
   !listar
   ```
   📜 **Exemplo de saída**:
   ```
   📜 Lista de Filmes Para Assistir:
   1. Matrix
   2. O Senhor dos Anéis
   3. Star Wars
   ```

2️⃣ **Marcar um filme como assistido pelo número**:
   ```
   !remover 2
   ```
   ✅ **Resposta esperada**:
   ```
   ✅ Filme marcado como assistido: O Senhor dos Anéis
   ```

3️⃣ **Marcar um filme como assistido pelo nome**:
   ```
   !remover Matrix
   ```
   ✅ **Resposta esperada**:
   ```
   ✅ Filme marcado como assistido: Matrix
   ```

4️⃣ **Excluir um filme pelo número**:
   ```
   !excluir 3
   ```
   ❌ **Resposta esperada**:
   ```
   ❌ Filme removido do banco: Star Wars
   ```

5️⃣ **Excluir um filme pelo nome**:
   ```
   !excluir Matrix
   ```
   ❌ **Resposta esperada**:
   ```
   ❌ Filme removido do banco: Matrix
   ```

---

## 🛠 **Tecnologias Usadas**
- **Python** 🐍
- **discord.py** 🎤
- **PostgreSQL** 🗄
- **Railway** 🚆

---

## 🔥 **Contribuição**
Se quiser contribuir:
1. **Faça um fork** 🍴
2. **Crie uma branch** (`git checkout -b minha-melhoria`)
3. **Faça suas alterações e commit** (`git commit -m "Melhoria X"`)
4. **Envie um PR** 🚀

---

## 🏆 **Créditos**
Criado por [SEU_NOME] ✨  
Se precisar de ajuda, me chame no Discord! 📨  

---

## 📜 **Licença**
Este projeto é de código aberto sob a licença **MIT**.  
Sinta-se livre para modificar e usar! 🎬