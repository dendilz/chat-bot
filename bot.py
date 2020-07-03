import os
from dotenv import load_dotenv
import telegram

load_dotenv()

TG_SECRET_KEY = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=TG_SECRET_KEY)