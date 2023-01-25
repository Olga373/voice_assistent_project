import requests
import voice
import webbrowser
import sys
import datetime


def weather():
    #сайт https://openweathermap.org
    try:
        params = {'q': 'Minsk', 'units': 'metric', 'lang': 'ru', 'appid': '553763b3e0b108fb16c272b0c81f4d2d'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Ошибка при попытке запроса к ресурсу API, проверь код')


def browser():
   webbrowser.open('https://www.kinopoisk.ru/ ', new=4)


def exchange():
    webbrowser.open('https://select.by/kurs/', new=2)


def time_now():
    now = datetime.datetime.now()
    voice.speaker("Сейчас " + str(now.hour) + ":" + str(now.minute))

def just_answer():
    pass


def offBot():
    sys.exit()
