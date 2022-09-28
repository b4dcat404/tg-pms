import telebot
import json
import requests
from db import DBHelper
from trello import TrelloHelper
from datetime import datetime, date


now = datetime.now()
time = now.strftime("%H:%M:%S") + '  ' + str(date.today())

db = DBHelper()
db.setup()
th = TrelloHelper()

all_keys = {}

# add your tg telegram API key from @BotFather
bot = telebot.TeleBot('HERE')
bot_credits = "\n\n\n*Карточка создана с помощью бота [@trello_bdct_bot](https://t.me/trello_bdct_bot)*\n"
# Дефолтный старт
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я работаю ещё не в полную силу\n'
                                      'Но меня можно тестировать \n'
                                      'Я уже могу создавать карточки в доске Trello\n', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '*Команды*\n\n'
                                      '/start & /help - Информация о боте и командах\n'
                                      '/setup - Установка подключения бота с Trello\n'
                                      '/status - Проверка подключения к Trello и вывод API ключей\n'
                                      '/reset - Сброс всех данных', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'После настройки подключения, все полученные ботом сообщения будут создавать '
                                      'карточки в Trello\n\n'
                                      'В данный момент бот не обрабатывает сообщения с изображениями', parse_mode='MarkdownV2')

# Подключение к Trello
@bot.message_handler(commands=["setup"])
def addapimessage(message):
    if message.chat.id in db.get_items():
        bot.send_message(message.chat.id, 'Ты уже настроил подлкючение к Trello')
    else:
        setup = bot.send_message(message.chat.id, '*Начнём*\n'
                                              '\n'
                                              'Получи ключ API по [ссылке](https://trello.com/app-key)\n'
                                              'И введи его ниже\n'
                                              '*ВАЖНО*: Вводи ключ без пробелов и лишних сиволов, '
                                              'лучше использовать _Ctrl\+C & Ctrl\+V_'
                                              '', parse_mode='MarkdownV2')
        bot.register_next_step_handler(setup, addapi)

# Сохранение API в словарь привязанный к TG ID
def addapi(message):
    if message.chat.id not in all_keys:
        all_keys[message.chat.id] = {}
    all_keys[message.chat.id]["api_key"] = message.text
    setup_api = bot.send_message(message.chat.id, 'Твой API ключ: ' + '||' + all_keys[message.chat.id]["api_key"] + '||'
                                                   + '\n\nТеперь отправь токен\n'
                                            'Получит Токен по [ссылке](https://trello.com/1/authorize?'
                                                     'expiration=never&scope=read,write,account&response_type=token'
                                                     '&name=Server%20Token&key='
                                            '' + all_keys[message.chat.id]["api_key"] + ')', parse_mode='MarkdownV2')
    bot.register_next_step_handler(setup_api, addtokenmessage)

# Сохранение Токена в словарь привязанный к TG ID
def addtokenmessage(message):
    all_keys[message.chat.id]["token"] = message.text
    setup_token = bot.send_message(message.chat.id, 'Твой Token: ' + '||' + all_keys[message.chat.id]["token"] + '||'
                                                    + "\n\nТеперь подключим Список\n"
                                                     "Тут немного посложнее\.\n"
                                                     "Открой Trello на ПК или в мобилном браузере \(там удобнее\)\n"
                                                     "Выбери доску где находится нужны список\n"
                                                     "Добавь в конце URl *\.json*\n"
                                                     "\n"
                                                     "Теперь в поиске по странице введи название нужного списка\n"
                                                     "Рядом возле названия будет нужны ID\n"
                                                     "Введи его ниже\n\n"
                                                     "*ВАЖНО:* Этот пункт в будущем будет исправлен \(временная "
                                                     "необходимость\)", parse_mode='MarkdownV2')
    bot.register_next_step_handler(setup_token, setup_list)

# Сохранение IdList в словарь привязанный к TG ID
def setup_list(message):
    all_keys[message.chat.id]["list"] = message.text
    chat_id = message.chat.id
    db.trello_connect(chatid=chat_id, apikey=all_keys[message.chat.id]["api_key"], token=all_keys[message.chat.id]["token"], board=all_keys[message.chat.id]["list"])
    bot.send_message(message.chat.id, 'Настройка выполнена\n'
                                      'Посмотреть ключи - /status\n'
                                      'Если ты допустил ошибку, можешь начать сначала используя /reset\n\n'
                                      '*ВАЖНО*: Все последующие сообщения боту, кроме команд, будут создавать карточки в Trello')

# Проверка успешной установки, вывод /status
@bot.message_handler(commands=["status"])
def status(message):
    tg_id = message.chat.id
    query_api = db.get_api(tg_id)
    if message.chat.id not in db.get_items():
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')
    else:
        bot.send_message(message.chat.id, 'Твои ключи:\n'
                                      'API: ' + '||' + query_api[0]["api_key"] + '||' + '\n'
                                      'Токен: ' + '||' + query_api[0]["token"] + '||' + '\n'
                                      'Список: ' + '||' + query_api[0]["board"] + '||'
                                       '', parse_mode='MarkdownV2')

# Сброс настроек подключения к трелло
@bot.message_handler(commands=["reset"])
def reset(message):
    tg_id = message.chat.id
    if message.chat.id in db.get_items():
        db.delete_item(tg_id)
        bot.send_message(message.chat.id, 'Настройки сброшены\n'
                                      'Подключи Trello - /setup')
    else:
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # Проверка на наличиие caht_id в БД
    if message.chat.id not in db.get_items():
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')
    else:
        tg_id = message.chat.id
        query_api = db.get_api(tg_id)
        name = "%.25s"%message.text
        message_text = message.text
        desc_urls = []
        desc_urls_str = ""
        desc_url = message.entities
        if message.forward_from_chat != None:
            forward = "*Переслано от [@" + message.forward_from_chat.username + "](https://t.me/" + message.forward_from_chat.username + ")*\n"
        elif message.forward_from != None:
            forward = "*Переслано от [@" + message.forward_from.username + "](https://t.me/" + message.forward_from.username + ")*\n"
        else:
            forward = ''

        # forward = message_from + message_from_chat
        # Прогоняем все ссылки через цикл, и добавляем в список
        if desc_url != None:
            for item in desc_url:
                desc_urls.append(item.url)
            for i in desc_urls:
                desc_urls_str += str(i) + "\n"
        else:
            desc_urls_str = '\nСсылок нет'
        print(message)
        # print()
        print(forward)
        desc = forward + "Ваше сообщение\n----------------\n\n" + message_text + "\n\n**URLs:** \n" + desc_urls_str + ' ' + '\n📆*Время создания:* ' + time + bot_credits
        source_url = ""
        query = {
            'name': name,
            'desc': desc,
            'urlSource' : source_url,
            'idList': query_api[0]["board"],
            'key': query_api[0]["api_key"],
            'token': query_api[0]["token"],
    }
        response = requests.request(
        "POST",
        th.url,
        params=query
        )
        # Проверка на верный запрос, что бы не ломали бота кривыми API ключами
        # Нужно добавить ссылку полученную в ответе (ShortURL) в слово "Карточка"
        url = json.loads(response.text)
        if response.status_code == 200:
            bot.send_message(message.chat.id,   '✅*Карточка создана*✅\n' +
                                                '📌*Название:* ' + name +
                                                '\n🌐*Ссылка:* ' + url["shortUrl"] +
                                                '\n📆*Время создания:* ' + time, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'Неверно указаны данные\n'
                                              'Используй /reset, что бы настроить подлключение к Trello заново')


bot.polling(none_stop=True, interval=0)
