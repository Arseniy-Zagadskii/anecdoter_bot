import random

import telebot
import requests
from bs4 import BeautifulSoup
import re
import schedule
import time

bot = telebot.TeleBot('6163172958:AAHrUbWtGfxafHzAucoWJErQSFbv4qEsHD0')
a = []
for i in range(1, 20001):
    a.append(i)


def bot_sendtext():
    n = a[random.randint(0, 20000)]
    del a[n]
    URL = 'https://humor.rin.ru/cgi-bin/show.pl?razdel=13&anekdot=' + str(n)
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    textWithHTML = soup.find('div', {'class': 'anekdot-text'}).prettify()

    pattern = re.compile('<.*?>')
    result = re.sub(pattern, '', textWithHTML)
    formated = '\n'.join(el.strip() for el in result.split('\n') if el.strip())
    text = formated.strip()

    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + text

    response = requests.get(send_text)

    return response.json()


def run(function):
    schedule.every().day.at('08:00').do(bot_sendtext)
    schedule.every().day.at('12:00').do(bot_sendtext)
    schedule.every().day.at('18:00').do(bot_sendtext)

    while True:
        schedule.run_pending()
        time.sleep(1)


run(bot_sendtext)
