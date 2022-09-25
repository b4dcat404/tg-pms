import telebot
import json
import requests
from db import DBHelper
from trello import TrelloHelper

db = DBHelper()
db.setup()
th = TrelloHelper()

all_keys = {}

# add your tg telegram API key from @BotFather
bot = telebot.TeleBot('5558114835:AAGiSl7iE5oU4xN9A9_tfNTm_MOhM-XeJmc')

# Дефолтный старт
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я работаю ещё не в полную силу\n'
                                      'Но меня можно тестировать \n'
                                      'Я уже могу создавать карточки в доске Trello\n'
                                      'Что бы начать введи /setup')

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
    if message.chat.id not in db.get_items():
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')
    else:
        tg_id = message.chat.id
        query_api = db.get_api(tg_id)
        name = "%.25s"%message.text
        desc = message.text
        query = {
            'name': name,
            'desc': desc,
            'idList': query_api[0]["board"],
            'key': query_api[0]["api_key"],
            'token': query_api[0]["token"],
    }
        response = requests.request(
        "POST",
        th.url,
        params=query
        )
        if response.status_code == 200:
            # Проверка на верный запрос, что бы не ломали бота кривыми API ключами
            # Нужно добавить ссылку полученную в ответе (ShortURL) в слово "Карточка"
            bot.send_message(message.chat.id, 'Карточка создана')

        else:
            bot.send_message(message.chat.id, 'Неверно указаны данные\n'
                                              'Используй /reset, что бы настроить подлключение к Trello заново')


            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

bot.polling(none_stop=True, interval=0)