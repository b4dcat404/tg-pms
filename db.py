import sqlite3

class DBHelper:
    def __init__(self, dbname="db.db",): # Подключение к БД SQLite3
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.cur = self.conn.cursor()

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS tg1 (id	INTEGER UNIQUE,chat_id	INTEGER UNIQUE,api_key	TEXT,token	TEXT,board	TEXT,PRIMARY KEY(id AUTOINCREMENT))" # Создаем таблицу если ее нет
        self.conn.execute(stmt)
        self.conn.commit()

    def trello_connect(self, chatid, apikey, token, board): # Заносим данные Trello в БД
        stmt = "INSERT INTO tg1 (chat_id, api_key, token, board) VALUES (?, ?, ?, ?)"
        args = (chatid, apikey, token, board)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def trello_check(self, chatid): # Проверяем верный ли ключи API
        stmt = "SELECT chat_id FROM tg1"

    def delete_item(self, item_text): # /reset удаление данных Trello из БД
        stmt = "DELETE FROM tg1 WHERE chat_id = (?)"
        args = (item_text,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self): # Проверяем наличи TG ID в БД
        stmt = "SELECT chat_id FROM tg1"
        return [x[0] for x in self.conn.execute(stmt)]

    def get_api(self, chat_id): # Получаем API, Token, IdList для вывода в /status и добавления карточки
        query_api = []
        stmt = "SELECT * FROM tg1 WHERE chat_id = ?"
        args = (chat_id, )
        row_api = self.conn.cursor().execute(stmt, args)
        for row in row_api:
            query_api.append({'chat_id': str(row[1]), 'api_key': str(row[2]), 'token': str(row[3]), 'board': str(row[4])})
        return query_api
