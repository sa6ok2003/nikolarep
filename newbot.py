from config import *
from aiogram import Bot, types, Dispatcher, executor
import sql
import admin
import asyncio
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


class reg(StatesGroup):
    name = State()
    fname = State()

memory_storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=memory_storage)


@dp.message_handler(commands=['start'])
async def welcome(mess: types.message):
    ref = mess.text[7:]
    sql.reg_user(mess.chat.id,ref)

    await bot.send_video_note(chat_id=mess.chat.id,
                              video_note='DQACAgIAAxkBAAIJfV_teqhyKb1DBbKk3BJopg35r9cHAAJjCgACGtdwS61pwkoRLtxzHgQ')
    await asyncio.sleep(40)
    markup = types.InlineKeyboardMarkup()

    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    bat1 = types.InlineKeyboardButton(text='ЧАТ', url='https://t.me/joinchat/HXrUH0V-pEm7AiZrWme0dw')
    bat2 = types.InlineKeyboardButton(text='ИНСТА',url='https://www.instagram.com/nikolanext')

    markup.add(bat0,bat1,bat2)
    msq = await bot.send_message(mess.chat.id, video_0, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(100)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video1')
    bat1 = types.InlineKeyboardButton(text='ЧАТ', url='https://t.me/joinchat/HXrUH0V-pEm7AiZrWme0dw')
    bat2 = types.InlineKeyboardButton(text='Инста', url='https://www.instagram.com/nikolanext')
    markup.add(bat0,bat1,bat2)

    await bot.edit_message_reply_markup(chat_id=mess.chat.id, message_id=msq, reply_markup=markup)


@dp.message_handler(commands=['ref'])
async def welcome(mess: types.message):
    info = sql.info_ref(mess.chat.id) #Возвращает информацию о рефералов
    await bot.send_message(mess.chat.id, 'Ваша реферафельная ссылка:\n'
                                         'https://t.me/nikolanext_bot?start='+f'{mess.chat.id}\n\n'
                                         f'Количество приглашенных: {info[0]}\n'
                                         f'Всего купили проект : {info[1]}\n'
                                         f'Получено выплат за: {info[2]}\n\n'
                                         f'Доступно для вывода:{(info[1]-info[2]) *100 } Руб')


@dp.callback_query_handler(text='none_video')  # Человек не досмотрел Видео
async def bat0(call: types.callback_query):
    await bot.send_message(call.message.chat.id, 'Не шали, сначала посмотри видео до конца.')


@dp.callback_query_handler(text='video1')  # Отправка первоего видео
async def bat0(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_1, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(170)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video2')
    markup.add(bat0)

    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)




@dp.callback_query_handler(text='video2')  # Отправка второго видео
async def bat0(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_2, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(240)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video3')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)


@dp.callback_query_handler(text='video3')  # Отправка третьего видео
async def bat0(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_3, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(90)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video4')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)


@dp.callback_query_handler(text='video4')  # Отправка Четвертого видео
async def bat0(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_4, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(300)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video5')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)


@dp.callback_query_handler(text='video5')  # Отправка Пятого видео
async def bat0(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_5, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(250)  #####  ЖДЕМ 60 СЕКУНД   ####
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='video6')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)


@dp.callback_query_handler(text='video6')  # Отправка Шестого видео
async def bat0(call: types.callback_query):
    sql.reg_time_bat_oplata(call.message.chat.id)
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_6, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(300)  #####  ЖДЕМ 60 СЕКУНД   ####

    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ',callback_data='video7')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)


@dp.callback_query_handler(text='video7')  # Отправка Седьмого видео
async def bat0(call: types.callback_query):
    sql.reg_time_bat_oplata(call.message.chat.id)
    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='none_video')
    markup.add(bat0)
    msq = await bot.send_message(call.message.chat.id, video_7, reply_markup=markup, parse_mode='HTML')
    msq = msq.message_id
    await asyncio.sleep(150)  #####  ЖДЕМ 60 СЕКУНД   ####

    markup = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='Менеджер',url='https://t.me/manager_nikola')
    markup.add(bat0)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msq, reply_markup=markup)






@dp.message_handler(content_types=['text'])
async def obrabotka(mess: types.message):
    id = mess.chat.id
    id_pokupatel = mess.forward_from

    if id_pokupatel == None:
        id_pokupatel = 0
    else:
        id_pokupatel = id_pokupatel.id

    if (id == ADMIN1_ID) or (id == ADMIN2_ID):
        await admin.admin(id,id_pokupatel) # Админ панель
    else:
        await bot.send_message(id, 'Я не умею реагировать на левые сообщения') #Реакция на рандомное сообщение


######################   АДМИН ПАНЕЛЬ (ХЕНДЛЕРЫ)  ####################################

@dp.callback_query_handler(text = 'stata')
async def stata (call:types.callback_query):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = 0
    for i in sql.execute('SELECT * FROM user_time'):
        a+=1
    await bot.send_message(call.message.chat.id, f'Всего юзеров: {a}')




@dp.callback_query_handler(text = 'send_user')
async def check(call: types.callback_query):
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    murkap.add(bat0)
    await bot.send_message(call.message.chat.id, 'Перешли мне сообщение которое нужно разослать',reply_markup=murkap)
    await reg.name.set()

@dp.message_handler(state=reg.name,content_types=['text','photo','video','video_note'])
async def name_step1(message: types.Message, state: FSMContext):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = 0
    for i in sql.execute("SELECT id FROM user_time"):
        a += 1
        if a == 20:
            a = 0
            await asyncio.sleep(10)

        await bot.send_message(ADMIN1_ID,'Готово')
        await message.copy_to(i[0])
        await asyncio.sleep(1)

    await state.finish()
    await bot.send_message(message.chat.id, 'Рассылка выполенена!')

@dp.callback_query_handler(text = 'otemena', state=reg.name)
async def otmena_stat(call: types.callback_query,state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Рассылка отменена')
    await state.finish()





#######################  КОНЕЦ АДМИН ХЕНДЛЕРОВ ###################################


if __name__ == '__main__':
    executor.start_polling(dp)
