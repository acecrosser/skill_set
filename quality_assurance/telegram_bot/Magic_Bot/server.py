import random
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1328164745:AAFvR9tm2ivPlJsU1OGCpjjjdoOXct3GjaE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    await message.answer('Привет, задай любой вопрос и получи ответ!')


@dp.message_handler()
async def send_answer(message: types.Message):
    messages = [
        'Это точно!',
        'Это решительно так!',
        'Да',
        'Сложно, попробуй еще раз',
        'Спроси позже',
        'Сконцентрируйся и спроси еще раз',
        'Мой ответ - нет!',
        'Выглядит не очень',
        'Очень сомнительно'
    ]
    answer = messages[random.randint(0, len(messages) - 1)]
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)