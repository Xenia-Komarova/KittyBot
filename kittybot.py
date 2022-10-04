import requests
import datetime
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup


updater = Updater(token='5519495382:AAEEDWKhxsOabr8S40p5z8A5sw22sjNmFgw')
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat

def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())

def whats_time (update, context):
    chat = update.effective_chat
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    context.bot.send_message(chat_id=chat.id,text=f'Точное время: {time}.')

def my_id (update, context):
    chat = update.effective_chat
    my_id = update.message.chat.id
    context.bot.send_message(chat_id=chat.id, 
                             text='Твой id, {}!'.format(my_id))

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я KittyBot!')

def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    print(update)
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat'],
                                 ['/what_time'], 
                                 ['/my_id']
                                 ], 
                                 resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что включили меня, {}!'.format(name),
                             reply_markup=button
                            )

# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
updater.dispatcher.add_handler(CommandHandler('what_time', whats_time))
updater.dispatcher.add_handler(CommandHandler('my_id', my_id))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
