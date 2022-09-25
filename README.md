<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/b4dcat404/trello-tg-bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TG Project Management System</h3>

  <p align="center">
    Телеграм бот упрощающий работу с системами управления проектов.<br />В основном помогает быстро создавать задачи поступающие в телеграм или создавать задачи для себя. 
    <br />
    <a href="https://github.com/b4dcat404/trello-tg-bot/README.md"><strong>Документация »</strong></a>
    <br />
    <br />
    <a href="https://t.me/dostavka82_bot">Демо</a>
    ·
    <a href="https://github.com/b4dcat404/Trello-TG-bot/issues">Сообщить о баге</a>
    ·
    <a href="https://github.com/b4dcat404/Trello-TG-bot/issues">Прделожить идею</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Содержание</summary>
  <ol>
    <li>
      <a href="#about-the-project">О проекте</a>
      <ul>
        <li><a href="#built-with">Интсрументы</a></li>
      </ul>
    </li>
    <li><a href="#Использование">Использование</a></li>
    <li><a href="#roadmap">Цели</a></li>
    <li><a href="#contributing">Принять участие</a></li>
    <li><a href="#license">Лицензия</a></li>
    <li><a href="#contact">Контакты</a></li>
    <li><a href="#acknowledgments">Ресурсы</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О проекте

[![Product Name Screen Shot][product-screenshot]](https://b4dcat404.github.io/tg-deliveries-evp)

Это проект с открытым кодом для реализации подбного в рамках пет-проектов и даже коммерческой реализации 
Мы стремимся развивать скилы нашей команды на подобного рода проектах.

На данный момент бот умеет добавлять карточки в Trello, обрабатывать пересланные сообщения.

Не работает обработка сообщений с изображением (ВРЕМЕННО)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Инструменты

* [![Python][Python]][Python-url]
* [![JQuery][JQuery.com]][JQuery-url]
* [![Telegram API][TGAPI]][TGAPI-url]
<!--* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]-->


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Подготовка к работе

Установка подразумевает, что у вас уже подготовлен сервер на *Ubuntu 20.04* 
и установленным *Python3* и *pip*

### Подготовка

Установка необходимых библиотек
* API Telegram
  ```sh
  pip3 install pyTelegramBotAPI
  ```
* nodejs
  ```sh
  sudo apt install nodejs
  ```
* npm
  ```sh
  sudo apt install npm
  ``` 
* pm2
  ```sh
  sudo npm install pm2 -g
  ``` 
* Установка SQLite3 и созадние 
    * Создайте папку для бота
    ```sh
    mkdir tg-pms(ваше название папки)
   ```
    * Установка sqlite3
    ``` sh
  sudo apt install sqlite3
  ```
    * Создайте базу данных в папке проекта с название db

### Установка

1. Получите API у [@BotFather](https://t.me/BotFather)
2. Клонируйте репозиторий
   ```sh
   cd tg-pms
   git clone https://github.com/b4dcat404/trello-tg-bot.git
   ```
3. Введите API key в  `main.py`
   ```py
   bot = telebot.TeleBot('###HERE###')
   ```
4. Запуск бота
    ```sh
   cd tg-pms
   pm2 start main.py --interpreter=python3 (замените main на имя исполняемого файла бота)
   ```
5. Просмотр запущенных ботов
    ```sh
   pm2 list
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Использование

_Гайд по использованию бота можно найти в [документации](https://b4dcat404.github.io/trello-tg-bot/documentations.html)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Дорожная карта

- [x] Создание и базовая настройка бота
- [x] Подключение к БД SQLite3
- [x] Сохранение сессии пользователя
- [x] Trello
  - [x] Подключение к Trello
  - [x] Проверка на верное подключение
  - [x] Создание карточки
  - [x] Обработка пересланных сообщений
  - [ ] Обработка сообщений с изображением (issue)
  - [ ] Получение списка последних 10ти карточек
  - [ ] Удаление карточек
- [ ] Notion
- [ ] ClickUp
- [ ] Pyrus (?)

Посмотрите [открытые проблемы](https://github.com/b4dcat404/trello-tg-bot/issues) для получения полного списка предлагаемых функций (и известных проблем).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Прийми участие

Вклад - это то, что делает сообщество с открытым исходным кодом таким удивительным местом для обучения, вдохновения и творчества. Любой ваш вклад **высоко ценится**.

Если у вас есть предложение, которое сделало бы этого бота лучше, сделайте форк репозитория и создайте пул реквест. Вы также можете просто создать новый [Issue](https://github.com/b4dcat404/trello-tg-bot/issues) с тегом "улучшение".
Не забудьте дать проекту звезду! Еще раз спасибо!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## Лицензия

Распространяется под лицензией GPL-3.0. Подробности в  `LICENSE.txt` 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Котакты

**Dev Team Twitter** - [Twitter @b4dcat404](https://twitter.com/b4dcat404) 

**Разработчик** - [Twitter @vi_dev0](https://twitter.com/vi_dev0)

**Поддержка** - [Telegram @b4dcat404_support](https://t.me/b4dcat404_support)

**Новостной канал TG** - [Telegram @b4dcat404](https://t.me/b4dcat404)

**Ссылка на проект:** [https://github.com/b4dcat404/trello-tg-bot](https://github.com/b4dcat404/trello-tg-bot)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Ресурсы

* [pyTelegrambotapi](https://pypi.org/project/pyTelegramBotAPI/)
* [SQLite3](https://www.sqlite.org/)
* [Trello](https://trello.com/)
* Дальше больше

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/b4dcat404/trello-tg-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/b4dcat404/trello-tg-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/b4dcat404/trello-tg-bot.svg?style=for-the-badge
[forks-url]: https://github.com/b4dcat404/trello-tg-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/b4dcat404/trello-tg-bot.svg?style=for-the-badge
[stars-url]: https://github.com/b4dcat404/trello-tg-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/b4dcat404/trello-tg-bot.svg?style=for-the-badge
[issues-url]: https://github.com/b4dcat404/trello-tg-bot/issues
[license-shield]: https://img.shields.io/github/license/b4dcat404/Trello-TG-bot.svg?style=for-the-badge
[license-url]: https://github.com/b4dcat404/Trello-TG-bot/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/85617305
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-blueviolet?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[TGAPI]: https://img.shields.io/badge/Telegram-black?style=for-the-badge&logo=Telegram&logoColor=white
[TGAPI-url]: https://telegram.org