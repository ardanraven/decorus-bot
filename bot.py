from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Palavras-chave e respostas
respostas = {
    "banho": "🛁 Banhos de ervas limpam corpo e alma. Experimente arruda, alecrim ou lavanda na lua minguante para proteção.",
    "cristal": "💎 Cristais são guardiões da energia. Ametista acalma, quartzo limpa, turmalina protege.",
    "ritual": "🕯️ Rituais conectam o visível ao invisível. Use velas, intenções claras e círculos mágicos.",
    "lua": "🌑 As fases da lua guiam os feitiços: nova para começos, cheia para poder, minguante para libertações.",
    "proteção": "🔮 Para se proteger, use sal grosso nos cantos da casa, incenso de arruda e cristal de turmalina negra.",
    "limpeza": "💨 Faça defumação com sálvia branca ou alecrim. Banho de sal grosso e mentalização ajudam na limpeza energética."
}

# Função que detecta palavras-chave
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text.lower()

    for palavra, resposta in respostas.items():
        if palavra in mensagem:
            await update.message.reply_text(resposta)
            return

    # Caso nenhuma palavra-chave seja encontrada
    await update.message.reply_text("🌙 Não entendi muito bem... Tente perguntar sobre banhos, cristais, rituais, fases da lua ou proteção.")

# Inicia o bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Captura todas as mensagens de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("🔮 Decorus-Bot escutando palavras místicas...")
    app.run_polling()

if __name__ == "__main__":
    main()
