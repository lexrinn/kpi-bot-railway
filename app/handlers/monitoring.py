# app/handlers/monitoring.py
import asyncio
from aiogram import Router, F
from aiogram.types import Message

from app.utils import get_bugs_indicator, get_emoji, get_sticker
from app.bot import get_keyboard

from app.dm import dm   # ← ЭТО ЕДИНСТВЕННЫЙ ПРАВИЛЬНЫЙ ИМПОРТ

router = Router()


@router.message(F.text == "Мои недоработки")
async def my_bugs(message: Message):
    username = message.from_user.username
    if not username:
        return await message.answer("Установи @username в Telegram")

    row = await asyncio.to_thread(dm.get_user_data, "monitoring", username)
    if not row or len(row) < 5:
        return await message.answer("Данные по недоработкам не найдены 😔\nПопробуй /update")

    time_val = row[4]  # колонка E — время исправления багов
    indicator = get_bugs_indicator(time_val)
    emo = get_emoji(indicator)

    sticker = get_sticker(indicator, "BUGS")
    if sticker:
        try:
            await message.answer_sticker(sticker)
        except:
            pass

    text = f"**Недоработки**\n\n" \
           f"{emo} Время недоработок: **{time_val}**"

    await message.answer(text, parse_mode="Markdown", reply_markup=get_keyboard())