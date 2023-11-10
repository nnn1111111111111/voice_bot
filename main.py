import logging
from gtts import gTTS
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6303685319:AAH1Hdg-cYL6bnw3gE94ibieN_5XdHxmhzY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    tts = gTTS(message.text, lang='ru')
    tts.save(f'{message.from_user.id}.mp3')
    await message.answer_voice(open(f'{message.from_user.id}.mp3', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)