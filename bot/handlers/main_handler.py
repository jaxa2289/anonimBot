from aiogram import html, Router,F
from aiogram.exceptions import TelegramForbiddenError
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand
from sqlalchemy import insert
from aiogram import Bot, Dispatcher

from bot.buttons.reply import make_buttons
from bot.dispacher import dp
from db.models import User, Juftlar
from bot.buttons import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db = Dispatcher(Router=Router)
engine = create_engine("postgresql+psycopg2://postgres:3@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session_user = Session()


main_router = Router()
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom anonim chatga hush kelibsiz 👋🏻!")
    await message.bot.set_my_commands([BotCommand(command="/about", description = "Bot Haqida") , BotCommand(command="/restart", description = "restart")])

    new_user = User(first_name=message.from_user.first_name or  'firstnmae_null',
                    last_name=message.from_user.last_name or 'lastnmae_null',
                    chat_id=message.from_user.id,
                    status=False)
    userch = session_user.query(User).filter(User.chat_id == message.from_user.id).first()
    if not userch:
        session_user.add(new_user)
        session_user.commit()

    user_false = session_user.query(User.chat_id).filter(User.status == False,).first()
    juft_false = session_user.query(Juftlar.chat_id_1,Juftlar.chat_id_2)

    new_user = Juftlar(chat_id_1=message.from_user.id,chat_id_2=user_false.chat_id,status=True)
    if  user_false and juft_false or juft_false.chat_id_2 != user_false.chat_id:
        session_user.add(new_user)
        session_user.commit()
        await message.answer("Siz yang suxbat dosh bilan bogladingiz ✅")
        await message.bot.send_document(userch.chat_id, caption=F.text)
    else:
        await message.answer("Siz yang suxbat dosh qidirlmoqt ⏳")





@main_router.message(Command("about",prefix="/"))
async def pexix_menu(message: Message) :
    await message.answer(f"""
Qoidalar:
  Anonimlig saqlanish 🔐
  Nomaqul sozlardan saqlaning 🚫
  Qoida buzgalar botan chetlashtirilad 📵


""")


#
#
# from aiogram import Router, F
# from aiogram.types import Message
#
# from motor.core import AgnosticDatabase as MDB
#
# router = Router()
#
#
# @router.edited_message()
# async def editing_messages(message: Message, db: MDB) -> None:
#     user = await db.users.find_one({"chat_id": message.from_user.id})
#     if user["status"] == 2:
#         if message.text:
#             await message.bot.edit_message_text(
#                 message.text, user["interlocutor"], message.message_id + 1
#             )
#         elif message.caption:
#             await message.bot.edit_message_caption(
#                 message.caption,
#                 user["interlocutor"],
#                 message.message_id + 1,
#                 caption_entities=message.caption_entities,
#                 parse_mode=None
#             )
#
#
# @router.message(
#     F.content_type.in_(
#         [
#             "text", "audio", "voice",
#             "sticker", "document", "photo",
#             "video"
#         ]
#     )
# )
# async def echo(message: Message, db: MDB) -> None:
#     user = await db.users.find_one({"_id": message.from_user.id})
#
#     if user["status"] == 2:
#         if message.content_type == "text":
#             reply = None
#             if message.reply_to_message:
#                 if message.reply_to_message.from_user.id == message.from_user.id:
#                     reply = message.reply_to_message.message_id + 1
#                 else:
#                     reply = message.reply_to_message.message_id - 1
#
#             await message.bot.send_message(
#                 user["interlocutor"],
#                 message.text,
#                 entities=message.entities,
#                 reply_to_message_id=reply,
#                 parse_mode=None
#             )
#         if message.content_type == "photo":
#             await message.bot.send_photo(
#                 user["interlocutor"],
#                 message.photo[-1].file_id,
#                 caption=message.caption,
#                 caption_entities=message.caption_entities,
#                 parse_mode=None,
#                 has_spoiler=True
#             )
#         if message.content_type == "audio":
#             await message.bot.send_audio(
#                 user["interlocutor"],
#                 message.audio.file_id,
#                 caption=message.caption,
#                 caption_entities=message.caption_entities,
#                 parse_mode=None
#             )
#         if message.content_type == "voice":
#             await message.bot.send_voice(
#                 user["interlocutor"],
#                 message.voice.file_id,
#                 caption=message.caption,
#                 caption_entities=message.caption_entities,
#                 parse_mode=None
        #     )
        # if message.content_type == "document":
        #     await message.bot.send_document(
        #         user["interlocutor"],
        #         message.document.file_id,
        #         caption=message.caption,
        #         caption_entities=message.caption_entities,
        #         parse_mode=None
        #     )
        # if message.content_type == "sticker":
        #     await message.bot.send_sticker(
        #         user["interlocutor"],
        #         message.sticker.file_id
        #     )
        # if message.content_type == "video":
        #     await message.bot.send_video(
        #         user["interlocutor"],
        #         message.video.file_id,
        #         caption=message.caption,
        #         caption_entities=message.caption_entities,
        #         parse_mode=None,
        #         has_spoiler=True
        #     )