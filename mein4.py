import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F #new
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from mystates import Register

TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(Command("reg"))
async def register(message:Message,state:FSMContext):
    await message.answer(text = "Siz bizning kurslarimizga yozilish uchun ismingizni kiriting")
    await state.set_state(Register.first_name)
    
    
@dp.message(F.text,Register.first_name)
async def register_first_name(message:Message,state:FSMContext):
    first_name = message.text
    await message.answer(text = "Familyangizni kiriting")

    await state.update_data(first_name=first_name)
    await state.set_state(Register.ota)
    
@dp.message(F.text,Register.ota)
async def register_ota(message:Message,state:FSMContext):
    ota = message.text
    await state.update_data(ota=ota)
    await message.answer(text = "Otanggizni ismimi kiriting")
    await state.set_state(Register.ona)
    
@dp.message(F.text,Register.ona)
async def register_ona(message:Message,state:FSMContext):
    ona = message.text
    await state.update_data(ona=ona)
    await message.answer(text = "Onanggizni ismimi kiriting")
    await state.set_state(Register.last_name)

@dp.message(F.text,Register.last_name)
async def register_last_name(message:Message,state:FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)
    await state.set_state(Register.gmail)
    await message.answer(text = "Telefon nomeringizni kiriting")

@dp.message(F.text,Register.gmail)
async def register_gmail(message:Message,state:FSMContext):
    gmail = message.text
    await state.update_data(gmail=gmail)
    await message.answer(text = "Gmail kiriting")
    await state.set_state(Register.phone_number)

@dp.message(F.text,Register.phone_number)
async def register_phone_number(message:Message,state:FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await state.set_state(Register.course)
    await message.answer(text = "qaysi kursda o'qimoqchisiz")
    


@dp.message(F.text,Register.course)
async def register_course(message:Message,state:FSMContext):
    data = await state.get_data()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    ota = data.get("ota")
    ona = data.get("ona")
    gmail = data.get("gmail")
    phone_number = data.get("phone_number")
    course = message.text
    text = f"Yangi o'quvchi ro'yhatdan o'tdi:\nIsmi:{first_name}\nFamilyasi:{last_name}\nOtanggizni ismi:{ota}\nOnanggizni ismi:{ona}\nGmailiz:{gmail}\nTel raqami:{phone_number}\nTanlagan kursi:{course}"
    await message.answer("Siz muvaffaqiyatli royhatdan o'tdingiz")
    await bot.send_message(chat_id=1245143580,text=text)
    state.clear()

async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())  