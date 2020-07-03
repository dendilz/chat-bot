import requests
import os
from dotenv import load_dotenv
from bot import bot

load_dotenv()
DVMN_SECRET_KEY = os.getenv('DEVMAN_TOKEN')
chat_id = os.getenv('CHAT_ID')
timeout = 20


def get_check_list(timestamp=''):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': DVMN_SECRET_KEY}
    params = {'timestamp': timestamp}

    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    response.raise_for_status()

    timestamp = response.json().get('last_attempt_timestamp') \
                or response.json().get('timestamp_to_request')
    message = response.json().get('new_attempts')[0]

    return message, timestamp


def format_message(message):
    lesson_title = message['lesson_title']
    lesson_status = message['is_negative']
    if lesson_status:
        reply_message = f'Работа "{lesson_title}" не принята, есть ошибки'
    else:
        reply_message = f'Работа "{lesson_title}" принята'
    return reply_message


if __name__ == "__main__":
    timestamp = ''
    while True:
        try:
            message, timestamp = get_check_list(timestamp=timestamp)
        except requests.ConnectionError:
            print('<сетевая ошибка>')
        except requests.exceptions.ReadTimeout:
            continue
        else:
            reply_message = format_message(message)
            bot.send_message(chat_id=chat_id, text=reply_message)
