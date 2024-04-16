import telebot

# استبدل 'TOKEN' برمز الوصول الخاص بك
bot = telebot.TeleBot('7021635279:AAEt3R8M1VX37Qq4PE-OXIv61ExUchA03KM')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا! كيف يمكنني مساعدتك؟")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
