# Телеграм бот для отслеживания проверок задач

### Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей.

В linux:
```
pip3 install -r requirements.txt
```
или
```
pip install -r requirements.txt
```
В Windows:
```
python -m pip install -r requirements.txt  
```
### Как запустить
В Linux:
```
python3 main.py
```
или
```
python main.py
```
В Windows:
```
python main.py
```
### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневой директории и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `TELEGRAM_TOKEN`=токен вашего бота. [Получаем токен бота](https://tlgrm.ru/docs/bots)
- `DEVMAN_TOKEN`=токен для работы с API Devman. [Получаем токен API Devman](https://dvmn.org/api/docs/)
- `TELEGRAM_CHAT_ID`=Ваш чат ID в телеграм. Чтобы его узнать, отправьте сообщение @userinfobot

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).