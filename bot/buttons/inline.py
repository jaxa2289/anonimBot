import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.dispacher import TOKEN
from bot.handlers import dp
from bot.middilwares import all_middleware
from db.utils import db
from db.models import *

async def make_inline_buttons(inline_buttons: list[str], adjustments: list[int]):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(*[InlineKeyboardBuilder(text=button, callback_data=button)
                   for button in inline_buttons])
    keyboard.adjust(*adjustments)

    await keyboard.as_markup()
