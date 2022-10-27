import pyowm
import telebot

def getFieldText_n(Field, Text):
	return Field + ':  ' + str(Text) + '\n'

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')#, {Language:"ru"})
mgr = owm.weather_manager()

TOKEN = "5281578033:AAFVfouIT7mlFyHtPxeS2PvOUYWG8cisnBs"
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# place = 'London,GB'
	# place = input('ENTER city:')
	# place = 'Minsk,BY'
	place = message.text
	observation = mgr.weather_at_place(place)
	w = observation.weather
	response = getFieldText_n('city', place)
	response = response + getFieldText_n('detailed_status',  w.detailed_status)
	response = response + getFieldText_n('wind', w.wind())                         # {'speed': 4.6, 'deg': 330}
	response = response + getFieldText_n('humidity', w.humidity)                   # 87
	response = response + getFieldText_n('temperature', w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	response = response + getFieldText_n('tC cur', w.temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	response = response + getFieldText_n('rain', w.rain)                           # {}
	response = response + getFieldText_n('heat_index', w.heat_index)               # None
	response = response + getFieldText_n('clouds', w.clouds)                       # 75
	bot.send_message(message.chat.id, response)  # рабочий код без мусора

bot.polling(none_stop = True)