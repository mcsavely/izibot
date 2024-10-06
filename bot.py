import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Укажите токен вашего бота
API_TOKEN = '7904801443:AAGN_nEhw2BU_jD1eQniwoe24FkZiy4b7Os'  # Замените на свой токен

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Создаем inline-клавиатуру
    keyboard = InlineKeyboardMarkup(row_width=2)

    # Укажите ссылку на ваш Web App
    menu_button = InlineKeyboardButton("Меню", web_app={"url": "https://izi.html"})

    # Кнопка для отправки адреса
    address_button = InlineKeyboardButton("Наш адрес", callback_data="send_address")

    # Добавляем кнопки на клавиатуру
    keyboard.add(menu_button, address_button)

    # Отправляем сообщение с кнопками
    await message.reply("Привет! Выберите раздел:", reply_markup=keyboard)

# Обработчик callback для кнопки "Наш адрес"
@dp.callback_query_handler(lambda c: c.data == 'send_address')
async def process_callback(callback_query: types.CallbackQuery):
    # Отправляем адрес
    await bot.send_message(callback_query.from_user.id, "Наш адрес: г. Ярославль площадь Труда 1")
    # Отмечаем callback как обработанный
    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
