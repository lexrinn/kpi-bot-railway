from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

def get_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Мой KPI"), KeyboardButton(text="Мои недоработки")]],
        resize_keyboard=True
    )