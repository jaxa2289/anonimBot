import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import KeyboardButton
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.dispacher import TOKEN
from bot.handlers import dp
from bot.middilwares import all_middleware
from db.utils import db
from db.models import *




async def make_buttons(buttons_list: list[str], adjustments: list[int]):
        keyboard = ReplyKeyboardBuilder()
        keyboard.add(*[KeyboardButton(text=button) for button in buttons_list])
        keyboard.adjust(*adjustments)

        await keyboard.as_markup(resize_keyboard=True)