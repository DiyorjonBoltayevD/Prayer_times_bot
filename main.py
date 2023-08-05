from aiogram.dispatcher.filters import CommandStart

from Buttons.Reply import start_button
from config import dp
from aiogram.types import Message
from aiogram import executor
import requests
import json


@dp.message_handler(CommandStart())
async def start(message: Message):
    img = open('image/img_2.png', 'rb')
    text = f'Assalomu alaykum {message.from_user.full_name} botimizga xush kelibsiz👋\nO\'zingizga kerakli viloyatni tanlang🕌⏳'
    await message.answer_photo(img, caption=text, reply_markup=start_button)


@dp.message_handler(commands=["help"])
async def Help(message: Message):
    await message.answer(f'Kechirasiz {message.from_user.full_name},Yordam uchun +998-88-792-20-02 ga murojaat qiling!')


@dp.message_handler(text='Toshkent')
async def Tosh(message: Message):
    img = open('Image/img_3.png', 'rb')
    text = f'Toshkent namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Toshkent'
    tet = requests.get(url).text
    s = ''
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} :  {value}\n')
    await message.answer(s)


@dp.message_handler(text='Sirdaryo')
async def Sir(message: Message):
    img = open('Image/img.png', 'rb')
    text = f'Sirdaryo namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Jizzax'
    tet = requests.get(url).text
    s = ''
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} :  {value}\n')
    await message.answer(s)



@dp.message_handler(text='Jizzax')
async def jiz(message: Message):
    img = open('Image/img_1.png', 'rb')
    text = f'Jizzax namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Jizzax'
    tet = requests.get(url).text
    s = ''
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} :  {value}\n')
    await message.answer(s)


@dp.message_handler(text="Samarqand")
async def sam(message: Message):
    img = open('Image/img_4.png', 'rb')
    text = f'Samarqand namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Samarqand'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Navoiy")
async def navo(message: Message):
    img = open('Image/img_5.png', 'rb')
    text = f'Navoiy namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Navoiy'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Buxoro")
async def buxo(message: Message):
    img = open('Image/img_6.png', 'rb')
    text = f'Buxoro namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Buxoro'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Qashqadaryo")
async def qash(message: Message):
    img = open('Image/img_7.png', 'rb')
    text = f'Qashqadaryo namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Samarqand'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Surxandaryo")
async def sur(message: Message):
    img = open('Image/img_12.png', 'rb')
    text = f'Surxandaryo namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Buxoro'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Xorazm")
async def xor(message: Message):
    img = open('Image/img_11.png', 'rb')
    text = f'Xorazm namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Buxoro'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)

@dp.message_handler(text="Farg'ona")
async def far(message: Message):
    img = open('Image/img_10.png', 'rb')
    text = f'Farg\'ona namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Farg\'ona'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Andijon")
async def andi(message: Message):
    img = open('Image/img_9.png', 'rb')
    text = f'Andijon namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Andijon'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text="Namangan")
async def nam(message: Message):
    img = open('Image/img_8.png', 'rb')
    text = f'Namangan namoz vaqtlari⬇️'
    await message.answer_photo(img, caption=text)
    url = 'https://islomapi.uz/api/present/day?region=Namangan'
    s = ''
    tet = requests.get(url).text
    for key, value in json.loads(tet)['times'].items():
        s += (f'{key} : {value}\n')
    await message.answer(s)


@dp.message_handler(text='Hadislar')
async def xad(message:Message):
    await message.answer(f"Birinchi hadis.\nUmar ibn Xattobdan  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam aytdilar: «Albatta, amallar niyat bilandir. Har bir kishi niyat qiluvchidir. Kimning hijrati Alloh va rasuli uchun bo‘lsa, bas, Alloh va rasuli uchun hijrat qilibdi. Kimning hijrati dunyoga yetishish yoki xotinga uylanish uchun bo‘lsa, uning hijrati o‘sha narsaga bo‘libdi».\n\n"
                         f"Ikkinchi hadis.\nOishadan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Kimki bizning ishimizda yangilik qilsa, bu undan bo‘lmasa, bas, u rad qilingandir», dedilar. Imom Buxoriy va Muslim  rivoyatlari.\n\n"
                         f"Uchinchi hadis.\nNu’mon ibn Bashirdan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Albatta halol ochiq-ravshan. Albatta harom ochiq-ravshan. Uning o‘rtasida shubhali narsalar bo‘lib, uni ko‘p insonlar bilishmaydi. Kimki shubhadan taqvo qilsa, dini va obro‘sini soflabdi. Kimki shubhaga voqe’ bo‘lsa, haromga yo‘liqibdi. Rioya qiluvchi qo‘riqxona atrofiga borib, uning ichiga kirib qolishi mumkin. Har bir podshohning qo‘riqxonasi bor. Ogoh bo‘ling, Allohning qo‘riqxonasi U harom qilgan narsalardir. Ogoh bo‘ling, jasadda bir parcha go‘sht bor. Agar u isloh bo‘lsa, jasadning barchasi isloh bo‘ladi. Agar u fasod bo‘lsa, jasadning barchasi fasod bo‘ladi. U ham bo‘lsa qalbdir», dedilar. Imom Buxoriy va Muslim  rivoyatlari.\n\n"
                         f"To‘rtinchi hadis.\n Ibn Mas’uddan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Sizlardan biringiz onasi qornida ekanida qirq kun maniy holatida xalq qilinishi jamlanadi. So‘ngra quyuq qon bo‘lib, o‘sha kabi xalq qilinishi jamlanadi. So‘ngra parcha go‘sht bo‘lib, o‘sha kabi xalq qilinishi jamlanadi. So‘ngra farishta yuborilib, unga ruh puflaydi. Va to‘rt kalima, ya’ni rizqi, ajali, amali, baxtli yoki baxtsizligini yozish buyuriladi. Undan boshqa iloh yo‘q bo‘lgan Zot ila qasamki, sizlardan biringiz jannat ahlining amalini qiladi. Hattoki, u bilan jannat orasida bir gaz (o‘lchov) qoladi. Bas, uning o‘sha yozilgan kitobi ilgarilaydi-da, u do‘zax ahlining amalini qilib, do‘zaxga kirib ketadi. Sizlardan biringiz do‘zax ahlining amalini qiladi-da, hattoki u bilan do‘zax orasida bir gaz qoladi. Bas, uning kitobi ilgarilaydi-da, u jannat ahli amalini qilib, jannatga kirib ketadi», dedilar. Imom Buxoriy va Muslim  rivoyatlari.\n\n"
                         f"Beshinchi hadis.\n Hasan ibn Alidan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Shubhali narsani shubhasiziga qo‘y», dedilar. (Ya’ni, shubhali narsani tark qilib, shubhasiz narsani ol.) Termiziy va Nasaiy  rivoyatlari.\n\n")
    await message.answer(f"Oltinchi hadis.\nAbu Hurayradan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Befoyda so‘zlarni tark qilish kishining Islomi chiroyligidan (dalolat)dir», dedilar. Imom Termiziy va Ibn Mojalar  rivoyati.\n\n"
                         f"Yettinchi hadis.\nAnasdan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Sizlardan biringiz o‘zi yaxshi ko‘rgan narsasini birodari uchun ham yaxshi ko‘rmaguncha haqiqiy mo‘min bo‘la olmaydi», dedilar. Imom Buxoriy va Muslim  rivoyatlari.\n\n"
                         f"Sakkizinchi hadis.\nAbu Hurayradan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Albatta Alloh taolo marhamatlidir. Faqat marhamatli bo‘lganni qabul qiladi. Alloh taolo yuborgan payg‘ambarlariga buyurgan narsalarini mo‘minlarga ham buyuradi. Bu haqda Alloh taolo quyidagi oyatlarni nozil qilgan: «(Yuborgan barcha payg‘ambarlarimizga shunday dedik): «Ey payg‘ambarlar, halol-pok taomlardan yenglar va yaxshi amallar qilinglar! Albatta Men qilayotgan amallaringizni bilguvchidirman» (Mo‘‘minun surasi, 51-oyat),«Ey mo‘minlar, sizlarga rizq qilib berganimiz - pokiza narsalardan yenglar»(Baqara surasi, 172-oyat). Bir kishi safarda uzoq yuradi. Sochlari to‘zib, kiyimlari changib ketadi. Va qo‘lini osmonga cho‘zib, «Ey Rabbim, ey Rabbim», deydi. Uning yeyayotgan taomi harom, ichayotgan ichimligi harom, kiyayotgan kiyimi harom hamda ozuqasi harom. Qaerdan uning (duolari) ijobat qilinsin?!» dedilar. Imom Muslim  rivoyatlari.\n\n"
                         f"To‘qqizinchi hadis\nZarar berish ham yo‘q. Zarar olish ham yo‘q. «Muvatto’» kitobida  rivoyat qilingan.\n\n"
                         f"O'ninchi hadis.\nTamiym ad-Doriydan (r.a.)  rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Din xayrixohlikdir», deganlarida, sahobalar: «Kim uchun, ey Rasululloh?» deyishdi. Shunda Rasululloh sollallohu alayhi vasallam: «Allohga, kitobiga, rasuliga va musulmonlar imomi hamda ommasiga», deb aytdilar. Imom Muslim  rivoyatlari.")





if __name__ == '__main__':
    executor.start_polling(skip_updates=True, dispatcher=dp)
print()