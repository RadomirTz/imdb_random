import telebot
from imdb import IMDb
import random

ab = False

API_KEY = '2050624983:AAECMstZdgkQelbVY1KoACI95xXwY4j0j4Q'
bot = telebot.TeleBot(API_KEY)

ip_movie = IMDb()

# title, year, directors, synopsis, full-size cover url


@bot.message_handler(commands=['random'])
def send_text(message):
    global ab
    bot.send_message(message.chat.id, 'Please wait...')
    ab = False
    while ab == False:
        try:
            a = random.randint(1, 9900000)
            b = str(a)

            if len(b) == 1:
                b = '000000' + b
            if len(b) == 2:
                b = '00000' + b
            if len(b) == 3:
                b = '0000' + b
            if len(b) == 4:
                b = '000' + b
            if len(b) == 5:
                b = '00' + b
            if len(b) == 6:
                b = '0' + b

            keys = ip_movie.get_movie(b)

            str_genres = ''
            str_directors = ''

            for i in keys['genres']:
                str_genres += i + ', '

            for director in keys['directors']:
                str_directors += director['name'] + ', '

            result = '🚧' + keys['title'] + '' + '(' + str(keys["year"]) + ')' + '\n' +'⚡Genres: ' + str_genres + '\n' +'👨‍🎓Directors: ' + str_directors + '\n' + '⭐Rating: '  + str(keys['rating']) + '\n' + '📋Description: ' + str(keys['plot outline']) + '\n' + '🔎URL: ' + 'imdb.com/title/tt' + b
            
            img = keys['full-size cover url']
            bot.send_photo(message.chat.id, img, caption=result)
            print('ID: ' + str(a))
            ab = True
        except:
            ab = False
            print('Не существует')

@bot.message_handler(content_types=['text'])
def unknown_command(message):
    bot.send_message(message.chat.id, 'Please use "/random" to get random movie')

bot.polling(none_stop=True)