# app/handlers/kpi.py
import asyncio
from aiogram import Router, F
from aiogram.types import Message

from app.utils import get_kpi_indicator, get_emoji, get_sticker
from app.bot import get_keyboard

from app.dm import dm   # ← ЭТО ЕДИНСТВЕННЫЙ ПРАВИЛЬНЫЙ ИМПОРТ

router = Router()


@router.message(F.text == "Мой KPI")
async def my_kpi(message: Message):
    username = message.from_user.username
    if not username:
        return await message.answer("Установи @username в Telegram")

    row = await asyncio.to_thread(dm.get_user_data, "kpi", username)
    if not row or len(row) < 5:
        return await message.answer("Твои KPI не найдены 😔\nПопробуй /update")

    cr_val, qa_val = row[3], row[4]

    cr_indicator = get_kpi_indicator(cr_val, "CR")
    qa_indicator = get_kpi_indicator(qa_val, "QA")

    cr_emo = get_emoji(cr_indicator)
    qa_emo = get_emoji(qa_indicator)

    # Худший показатель → стикер
    priority = {"Red": 1, "Yellow": 2, "Green": 3, "Blue": 4, "Purple": 5}
    worst = cr_indicator if priority.get(cr_indicator, 0) < priority.get(qa_indicator, 0) else qa_indicator

    sticker = get_sticker(worst, "KPI")
    if sticker:
        try:
            await message.answer_sticker(sticker)
        except:
            pass  # старый стикер удалён — просто игнорим

    text = f"**Твой KPI**\n\n" \
           f"{cr_emo} CR: **{cr_val}**\n" \
           f"{qa_emo} QA: **{qa_val}**"

    await message.answer(text, parse_mode="Markdown", reply_markup=get_keyboard())