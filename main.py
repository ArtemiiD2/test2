from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('6309899359:AAF0nGsudYSuFxHqTcpj7wWaNmLnsBvtX8k')
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет')
@bot.message_handler(commands=['help'])
async def send_welcome(message):
    await bot.reply_to(message, 'i cant help')
@bot.message_handler(commands=['finish'])
async def send_welcome(message):
    await bot.reply_to(message, 'Пока')
@bot.message_handler(func=lambda message: True)
async def echo(message):
    #await bot.reply_to(message, message.text)
    if 'дела' or 'настроение'in message.text:
        await bot.reply_to(message, 'Хорошо')
import asyncio
asyncio.run(bot.polling())