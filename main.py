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
            a = random.randint(1, 99000000)
            b = str(a)
            g = 0

            if len(b) == 1:
                g = random.randint(1,4)
                if g == 1:
                    b = '000000' + b
                elif g == 2:
                    b = '0000000' + b
                elif g == 3:
                    b = b + '000000'
                elif g == 4:
                    b = b + '0000000'
            if len(b) == 2:
                g = random.randint(1,4)
                if g == 1:
                    b = '00000' + b
                elif g == 2:
                    b = '000000' + b
                elif g == 3:
                    b = b + '00000'
                elif g == 4:
                    b = b + '000000'
            if len(b) == 3:
                g = random.randint(1,4)
                if g == 1:
                    b = '0000' + b
                elif g == 2:
                    b = '00000' + b
                elif g == 3:
                    b = b + '0000'
                elif g == 4:
                    b = b + '00000'
            if len(b) == 4:
                g = random.randint(1,4)
                if g == 1:
                    b = '000' + b
                elif g == 2:
                    b = '00000' + b
                elif g == 3:
                    b = b + '0000'
                elif g == 4:
                    b = b + '00000'
            if len(b) == 5:
                g = random.randint(1,4)
                if g == 1:
                    b = '00' + b
                elif g == 2:
                    b = '000' + b
                elif g == 3:
                    b = b + '00'
                elif g == 4:
                    b = b + '000'
            if len(b) == 6:
                g = random.randint(1,2)
                if g == 1:
                    b = '0' + b
                else: 
                    b = b + '0'
            if len(b) == 7:
                g = random.randint(1,2)
                if g == 1:
                    d = random.randint(1,2)
                    if d == 1:
                        b = '0' + b
                    else:
                        b = b + '0'

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