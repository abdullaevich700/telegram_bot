import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from decouple import config

bot = Bot(token=config('TOKEN'))
dp = Dispatcher()


# Основная команда /start
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!')


# Получение id/имени с помощью message.from_user.id
@dp.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')
    await message.answer_photo(
        photo='https://micros.uz/upload/iblock/85a/nwx4nuozlvjg8a4h57kqtpdqginf5ovg/python_programming_language.png',
        caption='описание')


# Пример отправки картинок
@dp.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(
        photo='https://micros.uz/upload/iblock/85a/nwx4nuozlvjg8a4h57kqtpdqginf5ovg/python_programming_language.png',
        caption='описание')


# Пример обработки фотографий
@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(message.photo[-1].file_id)


# Пример отправки документов
@dp.message(F.text == '/send_doc')
async def cmd_send_doc(message: Message):
    await message.answer_document(document='id',
                                  caption='описание')


# Пример обработки документов
@dp.message(F.document)
async def get_document(message: Message):
    await message.answer(message.document.file_id)


# Хэндлер без фильтра, сработает, если ни один выше не сработает.
@dp.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')


# Polling, т.е бесконечный цикл проверки апдейтов
async def main():
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
