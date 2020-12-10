
import telebot
#import config2
import config

from telebot import types

bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def welcome(message):
   # bot.send_message(message.chat.id, "Привет, тут ты найдешь своё расписание (:")
    listok=types.InlineKeyboardMarkup(row_width=3)
    g6=types.InlineKeyboardButton(text='Группа 6',callback_data="g6",)
    g7=types.InlineKeyboardButton(text='Группа 7',callback_data="g7")
    # g8=types.InlineKeyboardButton(text='Группа 8',callback_data="g8")
    # g9=types.InlineKeyboardButton(text='Группа 9',callback_data="g9")
    # q=types.InlineKeyboardButton(text='Info',callback_data="inf")
    listok.add(g6,g7)
    bot.send_message(message.chat.id, "Привет, тут ты найдешь расписание \nВыбери группу:",reply_markup=listok)


@bot.message_handler(commands=['group'])
def chose(message):
    listok=types.InlineKeyboardMarkup(row_width=3)
    g6=types.InlineKeyboardButton(text='Группа 6',callback_data="g6",)
    g7=types.InlineKeyboardButton(text='Группа 7',callback_data="g7")
    # g8=types.InlineKeyboardButton(text='Группа 8',callback_data="g8")
    # g9=types.InlineKeyboardButton(text='Группа 9',callback_data="g9")
    # q=types.InlineKeyboardButton(text='Info',callback_data="inf")
    listok.add(g6,g7,)
    bot.send_message(message.chat.id, 'Выбери группу:',reply_markup=listok)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):

    if call.data=='g7': # 0 space
        table=types.ReplyKeyboardMarkup()
        b1=types.KeyboardButton('Пн')
        b2=types.KeyboardButton('Вт')
        b3=types.KeyboardButton('Ср')
        b4=types.KeyboardButton('Чт')
        b5=types.KeyboardButton('Пт')
        b6=types.KeyboardButton('Сб')
        b7=types.KeyboardButton('Вс')
        b8=types.KeyboardButton('???')
        table.add(b1,b2,b3,b4,b5,b6,b7,b8)
        bot.send_message(call.message.chat.id,"Выбери день:",reply_markup=table)
    elif call.data=='g6': # 1 space
        table=types.ReplyKeyboardMarkup()
        b1=types.KeyboardButton('Пн.')
        b2=types.KeyboardButton('Вт.')
        b3=types.KeyboardButton('Ср.')
        b4=types.KeyboardButton('Чт.')
        b5=types.KeyboardButton('Пт.')
        b6=types.KeyboardButton('Сб.')
        b7=types.KeyboardButton('Вс')
        b8=types.KeyboardButton('???')
        table.add(b1,b2,b3,b4,b5,b6,b7,b8)
        bot.send_message(call.message.chat.id,"Выбери день:",reply_markup=table)




@bot.message_handler(content_types=['text'])
def otvet(message):
        if message.chat.type == "private":
            if message.text.lower()=='пн':
                bot.send_message(message.chat.id, "Расписание  7ой группы на ПОНЕДЕЛЬНИК:\n 8.15-9.35: Программирование.(Карпович)\n 9.45-11.05: Английский язык. (Брич 604(ЮФ), Ходинская 607(ЮФ)\n 11.15-12.35: МА. (Голухов 300-а)\n 13.00-14.20: Физическая культура.")

            elif(message.text.lower()=='вт'):
                bot.send_message(message.chat.id, "Расписание  7ой группы на ВТОРНИК:\n 8.15-9.35: ИМ История. (Маскевич 605)\n 9.45-11.05: Геометрия и Алгебра. (Филипцов 605)\n 11.15-12.35: Программирование. (Пазюра 522, Климук 600-г)\n 13.00-14.20: Программирование. (Пазюра, Климук, м 506)\n 14.30-15.50: Английский(начинающие). (Ситникова 600-б, Ходинская 600-в).")

            elif(message.text.lower()=='ср'):
                bot.send_message(message.chat.id, "Расписание  7ой группы на СРЕДУ:\n  8.15-9.35: Бел.яз (Ленкевич 600-а)\n 9.45-11.05: Программирование. (Карпович 605)\n 11.15-12.35: ГА. (Комраков 600-в)\n 13.00-14.20: Математический анализ. (Мазаник 605)")

            elif(message.text.lower()=='чт'):
                bot.send_message(message.chat.id, "Расписание  7ой группы на ЧЕТВЕРГ:\n 8.15-9.35: УП. (Мелещенко м 507)\n 9.45-11.05: Геометрия и алгебра. (Филипцов 605)\n 11.15-12.35:  Математический анализ. (Мазаник 605)\n 13.00-14.20: УП. (Пазюра м 506)\n 14.30-15.50: Английский(начинающие). (Ситникова 600-б, Ходинская 600-в)")

            elif(message.text.lower()=='пт'):
                bot.send_message(message.chat.id, "Расписание  7ой группы на ПЯТНИЦУ:\n 8.15-9.35: МА. (Голухов 518)\n 9.45-11.05: Геометрия и алгебра. (Комраков 600-в)\n 11.15-12.35: Математический анализ. (Мазаник 605)\n 13.00-14.20: Физическая культура.")

            elif(message.text.lower()=='сб'):
                bot.send_message(message.chat.id, "Расписание  7ой группы на СУББОТУ:\n 11.15-12.35: Английский язык. (Брич 604(ЮФ))")

            elif(message.text.lower()=='вс'):
                bot.send_message(message.chat.id, "ПАРЫ СОСАТЬ!1")
            elif(message.text=='???'):
                bot.send_message(message.chat.id, "По всем вопросам и предложениям сюда: @krome_pustoti \n") #Если хотите помочь проекту: 5470 8700 4532 1631
            elif(message.text.lower()=='пн.'):
                bot.send_message(message.chat.id,"Расписание 6ой группы на ПОНЕДЕЛЬНИК:\n 8.15-9.35: Программирование.(Карпович)\n 9.45-11.05: Программирование. (Зубович м 507, Мушко м 505)\n 11.15-12.35:Программирование. (Зубович м 507, Мушко м 505)\n 13.00-14.20: Физическая культура.")
            elif(message.text.lower()=='вт.'):
                 bot.send_message(message.chat.id,"Расписание 6ой группы на ВТОРНИК:\n 8.15-9.35: ИМ История. (Маскевич 605)\n 9.45-11.05: Геометрия и Алгебра. (Филипцов 605)\n 11.15-12.35: ГА. (Филипцов 518)\n 13.00-14.20: Бел. яз. (Ленкевич 600-в)")
            elif (message.text.lower()=='ср.'):
                bot.send_message(message.chat.id,"Расписание 6ой группы на CРЕДУ:\n 9.45-11.05: Программирование. (Карпович 605)\n 11.15-12.35: МА (Мазаник 600-б)\n 13.00-14.20: Математический анализ. (Мазаник 605)\n 14.30-15.50: УП (Зубкович м 507)")
            elif (message.text.lower()=='чт.'):
                bot.send_message(message.chat.id,"Расписание 6ой группы на ЧЕТВЕРГ:\n 8.15-9.35: Англ яз (Ситникова 519)\n 9.45-11.05: Геометрия и алгебра. (Филипцов 605)\n 11.15-12.35: Математический анализ. (Мазаник 605)\n 14.30-15.50: Английский(начинающие). (Ситникова 600-б, Ходинская 600-в ")
            elif (message.text.lower()=='пт.'):
                bot.send_message(message.chat.id,"Расписание 6ой группы на ПЯТНИЦУ:\n 8.15-9.35: Английский. (Ситникова 519, Ходинская 600-а)\n 9.45-11.05: МА (Мазаник 517)\n 11.15-12.35: Математический анализ. (Мазаник 605)\n 13.00-14.20: Физическая культура.")
            elif (message.text.lower()=='сб.'):
                bot.send_message(message.chat.id,"Расписание 6ой группы на СУББОТУ:\n 9.45-11.05: Английский (Ходинская 600-в)\n 11.15-12.35: ГА (Филипцов 513)\n 13.00-14.20: УП (Ветров м 505)")







bot.polling(none_stop=True)
