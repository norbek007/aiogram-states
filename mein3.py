# import asyncio
# import logging
# import sys
# from aiogram import Bot, Dispatcher,F #new
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart,Command
# from aiogram.types import Message,input_file
# from cat import get_cat_image
# import wikipedia
# from cat import get_cat_image  # Assuming you have a function to get a cat image

# TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

# logging.basicConfig(level=logging.INFO, stream=sys.stdout)
# dp = Dispatcher()


# @dp.message(CommandStart())
# async def command_start(message: Message):
#     full_name = message.from_user.full_name
#     text = f"Salom {full_name}, Bu Norbekning birinchi boti"
#     await message.answer(text)


# @dp.message(Command("cat"))
# async def get_cat(message: Message):
#     image_content = get_cat_image()  # Assuming you have a function to get a cat image
#     if image_content:
#         await message.reply_photo(photo=input_file.BufferedInputFile(file=image_content, filename="cat.png"))


# @dp.message(Command("wiki"))
# async def wiki_summary(message: Message):
#     wikipedia.set_lang("uz")

#     try:
#         summary_content = wikipedia.summary("Navoiy")

#         await message.reply(summary_content)
#     except wikipedia.exceptions.DisambiguationError as e:
#         await message.reply(f"DisambiguationError: {e.options}")
#     except wikipedia.exceptions.PageError:
#         await message.reply("Page not found.")
#     except Exception as e:
#         await message.reply(f"An error occurred: {e}")


# async def main():
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from wiki import malumot

TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"

dp = Dispatcher()
 
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(F.text)
async def wiki_message(message:Message):
    text = message.text
    natija = malumot(text)
    await message.reply(text=natija)
    

async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
