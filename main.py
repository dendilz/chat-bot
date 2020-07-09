import requests
import os
import time
from dotenv import load_dotenv
from bot import bot

load_dotenv()
DVMN_SECRET_KEY = os.getenv('DEVMAN_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
timeout = 20


def get_data(timestamp):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': f'Token {DVMN_SECRET_KEY}'}
    params = {'timestamp': timestamp}

    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    response.raise_for_status()

    return response.json()


def get_timestamp(data):
    return data.get('last_attempt_timestamp') \
           or data.get('timestamp_to_request')


def get_lesson_notation(data):
    return data.get('new_attempts')[0]


def prepare_message(notation):
    lesson_title = notation['lesson_title']
    is_lesson_accepted = notation['is_negative']
    if is_lesson_accepted:
        reply_message = f'Работа "{lesson_title}" не принята, есть ошибки'
    else:
        reply_message = f'Работа "{lesson_title}" принята'
    return reply_message


if __name__ == "__main__":
    timestamp = ''
    while True:
        try:
            lesson_data = get_data(timestamp)

            lesson_notation = get_lesson_notation(lesson_data)
            lesson_timestamp = get_timestamp(lesson_data)

        except requests.ConnectionError:
            print('<сетевая ошибка>')
            time.sleep(10)
        except requests.exceptions.ReadTimeout:
            continue
        else:
            prepared_message = prepare_message(lesson_notation)
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=prepared_message)
