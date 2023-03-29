import telebot
bot = telebot.TeleBot('YOUR TOKEN')

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
            #bot.polling(none_stop=True)
            #bot.infinity_polling()
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as ex:
            logger.error(ex)
