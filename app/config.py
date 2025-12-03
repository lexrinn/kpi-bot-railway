import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
DATA_FILE = "cached_data.json"
UPDATE_TIMES = [(10, 0), (16, 0)]
TIMEZONE = "Europe/Moscow"