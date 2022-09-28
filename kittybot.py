from telegram import Bot


bot = Bot(token='5519495382:AAEEDWKhxsOabr8S40p5z8A5sw22sjNmFgw')

chat_id = 988057934
text = 'Вам телеграмма!'

bot.send_message(chat_id, text)