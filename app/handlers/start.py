from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from ..bot import get_keyboard

from app.dm import dm   

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Выбери пункт меню:", reply_markup=get_keyboard())

@router.message(Command("update"))
async def upd(message: Message):
    await message.answer("Обновляю кэш...")
    ok = await dm.update_cache()

    await message.answer("Готово!" if ok else "Ошибка при обновлении")
