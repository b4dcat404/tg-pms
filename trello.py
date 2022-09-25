import requests
import json
from db import DBHelper
db = DBHelper

class TrelloHelper:
    def __init__(self):
        self.url = "https://api.trello.com/1/cards"
        self.headers = {"Accept": "application/json"}

    def check(self):
        pass