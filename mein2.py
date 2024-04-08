import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Salom 007, Bu birinchi botimiz")



async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F #new
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

# @dp.message(F.text)
# async def text_message(message:Message):
#     text = message.text
    
#     await message.reply("Siz text yubordingiz")
#     await message.answer("Sizning yuborgan habar:"+text)

# @dp.message(F.video)
# async def video_message(message:Message):
#     await message.answer("Sizning video yubordingiz")


# @dp.message(F.photo)
# async def photo_message(message:Message):
#     await message.answer("Sizning photo yubordingiz")


# @dp.message(F.audio)
# async def audio_message(message: Message):
#     await message.answer("Sizning audio yubordingiz")


# @dp.message(F.location)
# async def location_message(message: Message):
#     await message.answer("Sizning location yubordingiz")


# @dp.message(F.animation)
# async def animation_message(message: Message):
#     await message.answer("Sizning animation yubordingiz")


# @dp.message(F.video_note)
# async def video_note(note: Message):
#     await note.answer("Sizning video_note yubordingiz")


# @dp.message(F.contact)
# async def contact_message(message: Message):
#     await message.answer("Sizning contact yubordingiz")


# @dp.message(F.game)
# async def geme_message(message: Message):
#     await message.answer("Sizning game yubordingiz")


# @dp.message(F.dice)
# async def dice_message(message: Message):
#     await message.answer("Sizning dice yubordingiz")


# @dp.message(F.voice)
# async def voice_message(message: Message):
#     await message.answer("Sizning voice yubordingiz")


# @dp.message(F.media)
# async def media_group(group: Message):
#     await group.answer("Sizning voice yubordingiz")


# @dp.message(F.poll)
# async def poll_message(message: Message):
#     await message.answer("Sizning poll yubordingiz")



async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F #new
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(F.sticker)
async def text_message(message:Message):
    text = message.text
    await message.answer("Siz stiker yubordingiz")

async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())