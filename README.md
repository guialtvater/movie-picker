# 🎬 Movie Picker Bot 🎬

Um bot do Discord para escolher filmes de uma lista, armazená-los no **banco de dados PostgreSQL** e garantir que os dados não sejam perdidos, mesmo após reiniciar. Criado para rodar no **Railway**.

---

## 🚀 **Recursos**
✅ **Adicionar filmes** a uma lista.  
✅ **Listar todos os filmes** armazenados.  
✅ **Escolher um filme** e removê-lo da lista.  
✅ **Armazenamento persistente** usando PostgreSQL no Railway.  
✅ **Rodando 24/7** na nuvem.  

---

## 🔧 **Instalação e Configuração**
### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/guialtvater/movie-picker.git
cd movie-picker
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
| Comando         | Descrição                                        |
|----------------|------------------------------------------------|
| `!addfilme <nome>` | Adiciona um filme à lista. |
| `!listar` | Lista todos os filmes armazenados. |
| `!escolher` | Escolhe o **filme mais antigo** da lista e o remove. |
| `!remover <nome>` | Remove um filme manualmente pelo nome. |

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
Criado por Guilherme Altvater ✨  
Se precisar de ajuda, me chame no Discord! 📨  

---

## 📜 **Licença**
Este projeto é de código aberto sob a licença **MIT**.  
Sinta-se livre para modificar e usar! 🎬