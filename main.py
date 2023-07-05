from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['1'])
async def rt(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<i>курсив</i>')

@bot.message_handler(commands=['2'])
async def rt2(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<b>жирный</b>')

@bot.message_handler(commands=['3'])
async def rt3(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<u>подчёркивание</u>')

@bot.message_handler(commands=['4'])
async def rt4(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<s>зачеркнутый</s>')

@bot.message_handler(commands=['5'])
async def rt5(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<code>для выделения кода</code>')

@bot.message_handler(commands=['6'])
async def rt6(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<pre>для выделения большого фрагмента кода</pre>')

@bot.message_handler(commands=['7'])
async def rt7(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<tg-spoiler>защита от спойлера</tg-spoiler>')

@bot.message_handler(commands=['8'])
async def rt8(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<a href="https://github.com/">ссылка</a>')

@bot.message_handler(commands=['9'])
async def rt9(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<a href="tg://user?id=5794033915">my account</a>')

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет')
    print(message)

@bot.message_handler(commands=['help'])
async def send_welcome2(message):
    await bot.reply_to(message, 'i cant help')

@bot.message_handler(commands=['hi'])
async def welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Ку', disable_notification=True, protect_content=True)

@bot.message_handler(commands=['finish'])
async def send_welcome3(message):
    await bot.reply_to(message, 'Пока')

@bot.message_handler(commands=['random'])
async def random(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')
    print(bot_message.dice.value)

@bot.message_handler(commands=['sticker'])
async def sticker(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAIiO2SkC6hdyiy5JTM1hZ8FOpE76QOuAAKBJQACXrlQSf8jCDja8tXKLwQ')

@bot.message_handler(commands=['file'])
async def file(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_document(chat_id, open('text.txt', 'rb'))

@bot.message_handler(commands=['location'])
async def location(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_location(chat_id, 58.00153542656655, 56.24533566181892)

@bot.message_handler(commands=['photo'])
async def photo(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_photo(chat_id, 'Obama.png', caption='Заголовок')

@bot.message_handler(commands=['start1'])
async def start(message):
    chat_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardMarkup('Первая кнопка', callback_data='first')
    button2 = InlineKeyboardMarkup('Первая кнопка', callback_data='second')
    button3 = InlineKeyboardMarkup('Первая кнопка', callback_data='third')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send_message(chat_id, 'Первый вариант кнопок', reply_markup=markup)

@bot.message_handler(commands=['timer'])
async def timer(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_message(chat_id, 'Таймер начался - 5 секунд')
    for i in range(1, 6):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{5-i} секуунд прошло', chat_id, bot_message.id)
    await bot.delete_message(chat_id, bot_message.id)

@bot.message_handler(func=lambda message: True)
async def echo(message):
    if 'дела' in message.text or 'настроение'in message.text:
        await bot.reply_to(message, 'Хорошо')
    else:
        await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())