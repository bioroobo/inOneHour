# google: pip pytelegrambotapi
# https://pypi.org/project/pyTelegramBotAPI/
#pip install pyTelegramBotAPI
# для получения TOKEN:
# найти и начать общение с контактом @BotFather типа bot; или открыть ссылку в телеге https://tele.click/BotFather
# отправить контакту сообщение-команду: /newbot.
# на запрос "How are we going to call it? Please choose a name for your bot." отправить сообщение <имя_бота>: weathermymybot
# на запрос "Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot."
# отправить сообщение: userweathermymybot
# В ответ бот вышлет нам токен. его копируем и указываем в команде TeleBot
# так же написано, что перейти к боту: t.me/userweathermymybot
#
# Done! Congratulations on your new bot. You will find it at t.me/userweathermymybot. You can now add a description,
# about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished
# creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully
# operational before you do this.
#
# Use this token to access the HTTP API:
# 5281578033:AAFVfouIT7mlFyHtPxeS2PvOUYWG8cisnBs
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
#
# Бот из командной строки выключается Ctrl+C, в PyCharm кнопкой Stop

# чтобы бот работал с выключенным компом необходимо захостить бота, например, на хероку, ищи на ютубе "Деплой Python Telegram бота на Heroku"

# ссылки на уроки создания бота:
#      https://www.youtube.com/watch?v=eQrTCHW2UqY
#      https://www.youtube.com/watch?v=TtvNVDilh60
# ссылка на документацию "Боты: информация для разработчиков ": https://tlgrm.ru/docs/bots

import telebot

TOKEN = "5281578033:AAFVfouIT7mlFyHtPxeS2PvOUYWG8cisnBs"
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# ответ таким же сообщением, которое отсылается боту
	#bot.reply_to(message, 'response:' + message.text) # рабочий код с мусором
	bot.send_message(message.chat.id, message.text)  # рабочий код без мусора

bot.polling(none_stop = True)
