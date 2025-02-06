from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, BotCommand
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Pair
from bot.dispacher import dp
from aiogram.types import ReplyKeyboardRemove

# SQLAlchemy setup
engine = create_engine("postgresql+psycopg2://postgres:3@localhost:5432/postgres")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

main_router = Router()



@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.bot.set_my_commands(
        [BotCommand(command="/start", description="start"), BotCommand(command="/pair", description="Juft qidirish")])
    user = session.query(User).filter_by(chat_id=message.chat.id).first()
    if not user:
        new_user = User(
            first_name=message.chat.first_name or '',
            last_name=message.chat.last_name or '',
            chat_id=message.chat.id
        )
        session.add(new_user)
        session.commit()
        await message.reply("Anonim botga hushkelibsiz 👋🏻")
    else:
        await message.reply('🌤️🥱')


@dp.message(Command("pair",prefix="/"))
async def pair_handler(message: Message):
    available_user = session.query(User).filter(User.status == False, User.chat_id != message.chat.id).first()

    existing_pair = session.query(Pair).filter(
        (Pair.chat_id_1 == message.chat.id) | (Pair.chat_id_2 == message.chat.id)
    ).first()

    if existing_pair:
        await message.reply("Siz allaqachon juftlashgansiz!")
        return

    if available_user:

        stop_button = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Suhbatni to'xtatish 🚫")]],
            resize_keyboard=True
        )

        new_pair = Pair(chat_id_1=message.chat.id, chat_id_2=available_user.chat_id, status=True)
        session.add(new_pair)
        user = session.query(User).filter_by(chat_id=message.chat.id).first()
        user.status = True
        available_user.status = True
        session.commit()

        await message.reply(
            f"Siz {available_user.first_name} bilan juftlashdingiz!",
            reply_markup=stop_button
        )
        await message.bot.send_message(
            available_user.chat_id,
            f"Siz {message.chat.first_name} bilan juftlashdingiz!",
            reply_markup=stop_button
        )
    else:
        await message.reply("Afsuski, hozircha hech kim mavjud emas.")


@dp.message(F.text == "Suhbatni to'xtatish 🚫")
async def stop_pair_handler(message: Message):

    pair = session.query(Pair).filter(
        (Pair.chat_id_1 == message.chat.id) | (Pair.chat_id_2 == message.chat.id)
    ).first()

    if pair:

        if pair.chat_id_1 == message.chat.id:
            recipient_id = pair.chat_id_2
        else:
            recipient_id = pair.chat_id_1


        user1 = session.query(User).filter_by(chat_id=pair.chat_id_1).first()
        user2 = session.query(User).filter_by(chat_id=pair.chat_id_2).first()

        user1.status = False
        user2.status = False


        session.delete(pair)
        session.commit()


        await message.reply(
            "Juftlik muvaffaqiyatli to'xtatildi.",
            reply_markup=ReplyKeyboardRemove()
        )
        await message.bot.send_message(
            chat_id=recipient_id,
            text="Sizning juftingiz suhbatni to'xtatdi.",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.reply("Siz juftlashmagansiz.")


@dp.message()
async def forward_message_to_pair(message: Message):

    pair = session.query(Pair).filter(
        (Pair.chat_id_1 == message.chat.id) | (Pair.chat_id_2 == message.chat.id)
    ).first()

    if pair:

        recipient_id = pair.chat_id_2 if pair.chat_id_1 == message.chat.id else pair.chat_id_1
        await message.bot.send_message(chat_id=recipient_id, text=message.text)
    else:
        await message.reply("Siz juftlashmagansiz. Iltimos, /pair buyrug'idan foydalaning.")
