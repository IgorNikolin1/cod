import openai
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6046250022:AAGzYmd0vl_g8tLD6YHzm7SRZUDNUarnE-k'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=600,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)