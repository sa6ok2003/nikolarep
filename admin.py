from config import *
from aiogram import Bot, types, Dispatcher, executor
import sql
import time
import sqlite3
import asyncio


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def admin(id,id_pokupat):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    if id_pokupat !=0:
        kol = sql.execute(f"SELECT status FROM user_time WHERE id = '{id_pokupat}'").fetchone()
        kol = kol[0]

        if kol == 0: #Меняем статус
            sql.execute(f"UPDATE user_time SET status = {1} WHERE id ={id_pokupat}")
            db.commit()
            await bot.send_message(id, 'Покупатель зарегистрирован')

        else: #Делаем выплату
            status = 0
            for i in sql.execute(f"SELECT status FROM user_time WHERE ref = '{id}' and status = {1}"):
                status += 1
            sql.execute(f"UPDATE user_time SET viplata = {status} WHERE id ={id_pokupat}")
            db.commit()
            await bot.send_message(id, 'Выплата созданна')


    else: #Админ панель
        murkap = types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='Статистика',callback_data='stata') #Вывести статистику по боту
        bat2 = types.InlineKeyboardButton(text='Рассылка', callback_data='send_user')
        murkap.add(bat1,bat2)
        await bot.send_message(id,'Вы попали в админ панель',reply_markup=murkap)








