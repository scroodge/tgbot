import telebot
bot = telebot.TeleBot('1848862976:AAG-K4fSB6JWlb0ZJgUBDBAo0ICRc1iSOJc')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
     
while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            logger.error(ex)
