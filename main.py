from transliterate import to_latin, to_cyrillic
import telebot

token = '1935020169:AAGhpkmAWcaho_dM9s03RKc06XKTqMWw' # Bot token
bot = telebot.TeleBot(token, parse_mode=HTML)

@bot.message_handler(commands=['start'])
def welcome_msg(msg):
	answer = "Assalomu alaykum, bu bot yordamida matnlarni <b>krilldan lotinga</b> yoki aksincha <b>lotindan krillga</b> o'girishingiz mumkin"
	answer += '\nIstalgan matnni yuboring:'
	bot.reply_to(msg, answer)

@bot.message_handler(func=lambda msg: msg.text is not None)
def translator(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.polling(none_stop=True)