import telebot
import requests
import json
url = "https://api.trello.com/1/cards"

headers = {
   "Accept": "application/json"
}
all_keys = {}
#add your tg telegram API key from @BotFather
bot = telebot.TeleBot('YOUR_TELEGRAM_API_KEY')
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я работаю ещё не в полную силу\n'
                                      'Но меня можно тестировать \n'
                                      'Я уже могу создавать карточки в дсоке Trello\n'
                                      'Что бы начать введи /setup')

@bot.message_handler(commands=["setup"])
def addapimessage(message):
    setup = bot.send_message(message.chat.id, '*Начнём*\n'
                                              '\n'
                                              'Получи ключ API по [ссылке](https://trello.com/app-key)\n'
                                              'И введи его ниже\n'
                                              '*ВАЖНО*: Вводи ключ без пробелов и лишних сиволов, '
                                              'лучше использовать _Ctrl\+C & Ctrl\+V_'
                                              '', parse_mode='MarkdownV2')
    bot.register_next_step_handler(setup, addapi)

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
    #

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

def setup_list(message):
    all_keys[message.chat.id]["list"] = message.text
    bot.send_message(message.chat.id, 'Настройка выполнена\n'
                                      'Посмотреть ключи - /status\n'
                                      'Если ты допустил ошибку, можешь начать сначала используя /reset\n\n'
                                      '*ВАЖНО*: Все последующие сообщения боту, кроме команд, будут создавать карточки в Trello')
@bot.message_handler(commands=["status"])
def status(message):
    if message.chat.id not in all_keys:
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')
    else:
        bot.send_message(message.chat.id, 'Твои ключи:\n'
                                      'API: ' + '||' + all_keys[message.chat.id]["api_key"] + '||' + '\n'
                                      'Токен: ' + '||' + all_keys[message.chat.id]["token"] + '||' + '\n'
                                      'Список: ' + '||' + all_keys[message.chat.id]["list"] + '||'
                                       '', parse_mode='MarkdownV2')

@bot.message_handler(commands=["reset"])
def reset(message):
    if message.chat.id in all_keys:
        del all_keys[message.chat.id]
        bot.send_message(message.chat.id, 'Настройки сброшены\n'
                                      'Подключи Trello - /setup')
    else:
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.chat.id not in all_keys:
        bot.send_message(message.chat.id, 'Сначала подключи Trello - /setup')
    else:
        name = message.text
        query = {
            'name': name,
            'idList': all_keys[message.chat.id]["list"],
            'key': all_keys[message.chat.id]["api_key"],
            'token': all_keys[message.chat.id]["token"],
    }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            params=query
    )
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

bot.polling(none_stop=True, interval=0)
