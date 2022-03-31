import telebot
import config
import random

from telebot import types

global sac, vac


bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)
	o = open('text.txt', 'r')

	#keybord
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Выбрать место погрузки")
	item2 = types.KeyboardButton("Выбрать место разгрузки")
	item3 = types.KeyboardButton("Расчитать")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, o, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Выбрать место погрузки':
			markup = types.InlineKeyboardMarkup(row_width=5)
			item1 = types.InlineKeyboardButton("Москва", callback_data='Moskow')
			item2 = types.InlineKeyboardButton("Санк-Петербург", callback_data='Peterburg')
			item3 = types.InlineKeyboardButton("Нур-Султан", callback_data='Sultan')
			item4 = types.InlineKeyboardButton("Алматы", callback_data='Almaty')
			item5 = types.InlineKeyboardButton("Костанай", callback_data='Kostonay')
			markup.add(item1, item2, item3, item4, item5)
			
			bot.send_message(message.chat.id, 'Выберите место погрузки:', reply_markup=markup)



		if message.text == 'Выбрать место разгрузки':
			markup = types.InlineKeyboardMarkup(row_width=5)
			item1 = types.InlineKeyboardButton("Москва", callback_data='Moskow1')
			item2 = types.InlineKeyboardButton("Санк-Петербург", callback_data='Peterburg1')
			item3 = types.InlineKeyboardButton("Нур-Султан", callback_data='Sultan1')
			item4 = types.InlineKeyboardButton("Алматы", callback_data='Almaty1')
			item5 = types.InlineKeyboardButton("Костанай", callback_data='Kostonay1')
			markup.add(item1, item2, item3, item4, item5)
			bot.send_message(message.chat.id, 'Выберите место разгрузки:', reply_markup=markup)

		if message.text == 'Расчитать':
			global vac
			global sac
			if vac == "Место погрузки: Москва" and sac == "Место разгрузки: Санк-Петербург":
				bot.send_message(message.chat.id, 'Расстояние с Москвы до Санк-Петербурга = 705 км')
			if vac == "Место погрузки: Москва" and sac == "Место разгрузки: Нур-Султан":
				bot.send_message(message.chat.id, 'Расстояние с Москвы до Нур-Султан = 2735 км')
			if vac == "Место погрузки: Москва" and sac == "Место разгрузки: Алматы":
				bot.send_message(message.chat.id, 'Расстояние с Москвы до Алматы = 3934 км')
			if vac == "Место погрузки: Москва" and sac == "Место разгрузки: Костанай":
				bot.send_message(message.chat.id, 'Расстояние с Москвы до Костанай = 2031 км')
			if vac == "Место погрузки: Санк-Петербург" and sac == "Место разгрузки: Москва":
				 bot.send_message(message.chat.id, 'Расстояние с Санк-Петербург до Москвы = 714 км')
			if vac == "Место погрузки: Санк-Петербург" and sac == "Место погрузки: Нур-Султан":
				bot.send_message(message.chat.id, 'Расстояние с Санк-Петербург до Нур-Султан = 3356 км')


		if message.text == '0xffff':
			markup = types.InlineKeyboardMarkup(row_width=5)
			item1 = types.InlineKeyboardButton("Переименовать", callback_data='Name')
			item2 = types.InlineKeyboardButton("Выключить", callback_data='vkl')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, 'Добро пожаловать супер пользователь', reply_markup=markup)
			

	

	
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    
    if call.message:
        if call.data == "Moskow":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место погрузки: Москва")
            global vac
            vac = "Место погрузки: Москва"
    if call.message:
        if call.data == "Peterburg":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место погрузки: Санк-Петербург")
            vac = "Место погрузки: Санк-Петербург"
    if call.message:
        if call.data == "Sultan":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место погрузки: Нур-Султан")
            vac = "Место погрузки: Нур-Султан"
    if call.message:
        if call.data == "Almaty":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место погрузки: Алматы")
            vac = "Место погрузки: Алматы"
    if call.message:
        if call.data == "Kostonay":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место погрузки: Костанай")
            vac = "Место погрузки: Костанай"
    if call.message:
        if call.data == "Moskow1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место разгрузки: Москва")
            global sac
            sac = "Место разгрузки: Москва"
    if call.message:
        if call.data == "Peterburg1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место разгрузки: Санк-Петербург")
            sac = "Место разгрузки: Санк-Петербург"
    if call.message:
        if call.data == "Sultan1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место разгрузки: Нур-Султан")
            sac = "Место разгрузки: Нур-Султан"
    if call.message:
        if call.data == "Almaty1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место разгрузки: Алматы")
            sac = "Место разгрузки: Алматы"
    if call.message:
        if call.data == "Kostonay1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Место разгрузки: Костанай")
            sac = "Место разгрузки: Костанай"
    if call.message:
        if call.data == "Name":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приветствие переименновано")
            f = open("text.txt", 'w')
            f.write('Велком')
            f.close()
    if call.message:
        if call.data == "vkl":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выключен")
            sac = 123/0
  

			
    
	
	
	


# RUN
bot.polling(none_stop=True)