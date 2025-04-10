import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Respostas específicas por múltiplas palavras-chave (prioridade alta)
respostas_contextuais = {
    ("banho", "proteção"): "🛡️ Banho de proteção: use sal grosso e alecrim. Faça em uma lua minguante ou quando sentir necessidade de afastar energias negativas.",
    ("banho", "prosperidade"): "💰 Banho de prosperidade: louro, manjericão e canela são ótimos. Faça durante a lua crescente e mentalize abundância.",
    ("banho", "amor"): "❤️ Banho de amor: use rosas vermelhas, mel e manjericão. Ideal na lua cheia para atrair paixão e carinho."
}

# Palavras-chave únicas com prioridade média
respostas_palavra_unica = {
    "banho": "✨ Os banhos espirituais purificam corpo e alma. Quer saber sobre proteção, amor ou prosperidade?",
    "proteção": "🧿 Proteção espiritual: use cristais como turmalina ou banhos com arruda e alecrim.",
    "prosperidade": "🌟 Para atrair prosperidade, use canela, louro e mentalize abundância.",
    "amor": "💘 Para o amor, rosas, mel e alfazema são poderosos ingredientes!",
    "ervas": "🌿 Ervas comuns: alecrim, lavanda, arruda, guiné... Cada uma tem um poder especial!"
}

mensagem_padrao = "Desculpe, não entendi. Mas posso falar sobre banhos, ervas, proteção, prosperidade, amor e mais! 🌙"

def detectar_contexto(mensagem):
    palavras_usuario = mensagem.lower().split()

    # Verifica se alguma combinação contextual bate
    for chaves, resposta in respostas_contextuais.items():
        if all(palavra in palavras_usuario for palavra in chaves):
            return resposta

    # Verifica se pelo menos uma palavra-chave individual aparece
    for palavra, resposta in respostas_palavra_unica.items():
        if palavra in palavras_usuario:
            return resposta

    return mensagem_padrao

async def responder_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text.strip().lower()
    resposta = detectar_contexto(mensagem)
    await update.message.reply_text(resposta)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌙 Olá! Eu sou o Decorus-Bot. Me pergunte sobre banhos espirituais, proteção, amor, ervas e mais!")

# Comando /banhos
async def banhos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Banhos espirituais limpam e energizam. Quer saber sobre amor, proteção ou prosperidade?")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("banhos", banhos))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensagem))

    print("🔮 Decorus-Bot rodando...")
    app.run_polling()
