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
            a = random.randint(1000000, 9900000)

            keys = ip_movie.get_movie(a)

            str_genres = ''
            str_directors = ''

            for i in keys['genres']:
                str_genres += i + ', '

            for director in keys['directors']:
                str_directors += director['name'] + ', '

            result = '🚧' + keys['title'] + '' + '(' + str(keys["year"]) + ')' + '\n' +'⚡' + 'Genres: ' + str_genres + '\n' +'👨‍🎓' + 'Directors: ' + str_directors + '\n' + '⭐' + 'Rating: '  + str(keys['rating'])
            
            img = keys['full-size cover url']
            bot.send_photo(message.chat.id, img, caption=result)

            ab = True
        except KeyError:
            ab = False
            print('Не существует')


bot.polling(none_stop=True)