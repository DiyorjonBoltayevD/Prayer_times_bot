from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


start_button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Toshkent'),KeyboardButton('Sirdaryo'),KeyboardButton('Jizzax')
        ],
        [
            KeyboardButton('Samarqand'),KeyboardButton('Navoiy'),KeyboardButton('Buxoro'),
        ],
        [
            KeyboardButton('Qashqadaryo'),KeyboardButton('Surxandaryo'),KeyboardButton('Xorazm')
        ],
        [
            KeyboardButton('Farg\'ona'),KeyboardButton('Andijon'),KeyboardButton('Namangan'),
        ],
        [
            KeyboardButton('Hadislar')
        ],
    ],
    resize_keyboard=True
)