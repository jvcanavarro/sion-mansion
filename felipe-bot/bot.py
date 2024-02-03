from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import requests

BOT_TOKEN = "6790579397:AAGp2aNRLU5dY9Ze64iEWNQphXa2XlHP8Xo"
API_KEY = "hJrrXZX8OVAvZeEPrK4N4Q==3RzmrplwkPVtbidS"

LIMIT = 1
FACTS_URL = f"https://api.api-ninjas.com/v1/facts?limit={LIMIT}"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get(FACTS_URL, headers={"X-Api-Key": API_KEY}).json()
    fact = response[0]["fact"]
    await update.message.reply_text(f"Fact: {fact}")


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("random_fact", random_fact))

app.run_polling()
