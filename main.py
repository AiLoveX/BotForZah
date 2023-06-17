import telebot
from telebot import types
import config
from knopki import Knopki
from news import News
from postup import Postup
from opisun import Opis

"""import logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)"""

bot = telebot.TeleBot(config.token, threaded=False)

cn = Knopki()
nw = News()
po = Postup()
opisanie = Opis()

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.full_name}</b>'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('О университете')
    item2 = types.KeyboardButton('Календарь мероприятий')
    item3 = types.KeyboardButton('Факультеты')
    item4 = types.KeyboardButton('Задать вопрос')
    item5 = types.KeyboardButton('Как поступить')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

def back_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('О университете')
    item2 = types.KeyboardButton('Календарь мероприятий')
    item3 = types.KeyboardButton('Факультеты')
    item4 = types.KeyboardButton('Задать вопрос')
    item5 = types.KeyboardButton('Как поступить')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id,'Что вы хотите узнать?', reply_markup=markup)

@bot.message_handler(commands=['question'])
def question(message):
    msg = bot.send_message(message.chat.id, 'Введите текст вопроса')
    bot.register_next_step_handler(msg,create_request)

def create_request(message):
    bot.send_message(message.chat.id, 'Ваш вопрос принят')
    bot.forward_message(config.grup_id, str(message.chat.id), message.message_id)

@bot.message_handler(func=lambda message: message.reply_to_message != None)
def reply_message_handler(message):
    bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=f'Ответ на ваш вопрос:\n{message.text}')



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        try:
            if message.text == "О университете":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    item1 = types.KeyboardButton('Об университете')
                    item2 = types.KeyboardButton('Приемная комиссия')
                    item3 = types.KeyboardButton('Последние новости')
                    item4 = types.KeyboardButton('Как добраться')
                    back = types.KeyboardButton('Назад')
                    markup.add(item1, item2, item3, item4, back)
                    bot.send_message(message.chat.id, 'Про что вы хотите узнать?', reply_markup=markup)
            elif message.text == "Календарь мероприятий":
                    bot.send_message(message.chat.id, '\n'.join(map(str, nw.сalendar_events())))
            elif message.text == "Факультеты":
                    bot.send_message(message.chat.id, 'Выберите факультет', parse_mode='html', reply_markup=cn.create_menu())
            elif message.text =="Задать вопрос":
                    bot.send_message(message.chat.id, 'Что бы задать вопрос введите команду\n /question')
                    return 0
            elif message.text =="Как поступить":
                    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    butt1 = types.KeyboardButton('Для выпускников средних школ')
                    butt2 = types.KeyboardButton('Для абитуриентов, имеющих диплом СПО')
                    butt3 = types.KeyboardButton('Для абитуриентов, имеющих диплом о высшем образовании')
                    back = types.KeyboardButton('Назад')
                    markup2.add(butt1, butt2, butt3, back)
                    bot.send_message(message.chat.id,'Подать документы в Мининский университет можно одним из способов:')
                    bot.send_message(message.chat.id, '\n'.join(map(str, po.postuplenie())), reply_markup=markup2)
            elif message.text == "Назад":
                     back_start(message)
            elif message.text == "Об университете":
                    bot.send_message(message.chat.id, opisanie.opisanie)
                    return 0
            elif message.text == "Приемная комиссия":
                    bot.send_message(message.chat.id, f'Приемная комиссия Мининского университета работает: \n'
                                                      'с понедельника по пятницу с 9 до 16 часов\n'
                                                      'Адреса:\n'
                                                      '1. 603950, г. Нижний Новгород, ул. Ульянова, д. 1, Приемная комиссия.\n'
                                                      '2. кабинет 303 - ответственный секретарь приемной комиссии\n'
                                                      '3. Челюскинцев, 9, каб. 206\n'
                                                      'Вы можете позвонить в приемную комиссию по телефонам:\n'
                                                      '+7(831)262-26-20\n+7(800)444-19-52\n'
                                                      '*1952\n Обратиться по электронной почте:\n priem@mininuniver.ru')
            elif message.text == "Последние новости":
                    bot.send_message(message.chat.id, '\n'.join(map(str, nw.last_news())))
                    return 0
            elif message.text == "Как добраться":
                    lat = 56.326248
                    lon = 44.007819
                    bot.send_location(message.chat.id, lat, lon)
                    bot.send_message(message.chat.id, 'Мы распологаемся по адресу:\n ул. Ульянова, 1, Нижний Новгород')
                    return 0
            elif message.text == "Для выпускников средних школ":
                    bot.send_message(message.chat.id, '\n'.join(map(str, po.pravilaSchool())))
            elif message.text == "Для абитуриентов, имеющих диплом СПО":
                    bot.send_message(message.chat.id, '\n'.join(map(str, po.pravilaSPO())))
            elif message.text =="Для абитуриентов, имеющих диплом о высшем образовании":
                     bot.send_message(message.chat.id, '\n'.join(map(str, po.pravilaMag())))
            elif message.text =="Вернуться":
                    bot.send_message(message.chat.id, 'Выберите факультет', parse_mode='html', reply_markup=cn.create_menu())
            elif message.text == message.text:
                    if (message.text[:7] == 'Кафедра'):
                        opis2 = cn.inforcafedr(message.text)
                        bot.send_message(message.chat.id, text=opis2, reply_markup=cn.create_napr(message.text))
                    else:
                        opis = cn.inform(message.text)
                        bot.send_message(message.chat.id, text=opis, reply_markup=cn.create_faceltet(message.text))
        except telebot.apihelper.ApiTelegramException:
            bot.send_message(message.chat.id, 'К сожалению произошла ошибка в момент обработки сообщения. Попробуй что-то другое.')


@bot.callback_query_handler(func=lambda call: True)
def napravlenie(call):
     opis = cn.naprltinf(call.data)
     bot.send_message(call.message.chat.id, text=opis)
     bot.answer_callback_query(call.id)


bot.polling(none_stop=True)
