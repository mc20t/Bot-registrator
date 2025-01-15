import telebot
from telebot import types  # кнопки
from string import Template
import datetime
import time

bot = telebot.TeleBot('7633342363:AAHFLvrON94pCXlhnxGYSk3pqL_87zQSckI')
links_message = '''
https://t.me/OneDayLive
❤️Наши Горячие Свинг Вечеринки Проходят Стабильно:
🗓️ Вторник, Среда, Четверг, Пятница, Суббота
⏰ Запись на Секс Вечеринку начинается с 12 дня🥰
✍️ Писать Сюда 🥰 @Na_instinkte
✅😎Наши Чаты где можно Знакомится для Общения и Секса и Доска Объявлений 🥰
https://t.me/addlist/aNb7dazrr8NiNjFi
✅Наш Основной Канал о Секс Вечеринках Знакомств и о Датах Проведения Мероприятий 🥰
https://t.me/Swingznacom'''
photo_path = ["G:\Мой диск\Работа\Для бота\Обложка Вторник.jpg",
              "G:\Мой диск\Работа\Для бота\Обложка Среда.jpg",
              "G:\Мой диск\Работа\Для бота\Обложка Четверг.jpg",
              "G:\Мой диск\Работа\Для бота\Обложка Пятница.jpg",
              "G:\Мой диск\Работа\Для бота\Обложка Суббота.jpg"
]
user_dict = {}
evening_start = ""
evening_end = ""
help_message = 'Если возникли вопросы или трудности - обратитесь к оператору /contacts или задайте вопрос напрямую через бота /question'
all_message_group_chat_id = '-1002369162919'
questions_group_chat_id = '-4604127306'
applications_group_chat_id = '-1002294855038'

# Хранилище состояний пользователей
user_states = {}

# Получаем сегодняшнюю дату
today = (datetime.datetime.now() - datetime.timedelta(hours=3))
today_weekday = (datetime.datetime.now() - datetime.timedelta(hours=3)).weekday()

if today_weekday in [3]:
    evening_start = "20:00"
    evening_end = "1:00"
elif today_weekday in [4]:
    evening_start = "18:00"
    evening_end = "23:00"
elif today_weekday in [5]:
    evening_start = "18:30"
    evening_end = "23:30"
else:
    evening_start = "19:00"
    evening_end = "0:00"

# Словари для перевода на русский
days = {'Monday': 'в Понедельник', 'Tuesday': 'во Вторник', 'Wednesday': 'в Среду', 'Thursday': 'в Четверг', 'Friday': 'в Пятницу',
        'Saturday': 'Субботу', 'Sunday': 'Воскресенье'}
months = {'January': 'Января', 'February': 'Февраля', 'March': 'Марта', 'April': 'Апреля', 'May': 'Мая', 'June': 'Июня',
          'July': 'Июля', 'August': 'Августа', 'September': 'Сентября', 'October': 'Октября', 'November': 'Ноября',
          'December': 'Декабря'}

# Получаем день недели, число и месяц
day_of_week = days[today.strftime('%A')]
day = today.strftime('%d')
month = months[today.strftime('%B')]

# Форматируем строку
formatted_date = f'{day_of_week} {day} {month}'


class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'carDate']

        for key in keys:
            self.key = None


# если /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("Узнать больше")
    itembtn2 = types.KeyboardButton("Записаться")
    itembtn3 = types.KeyboardButton("Задать вопрос")
    itembtn4 = types.KeyboardButton("Контакты")
    itembtn5 = types.KeyboardButton("/start")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)

    if today_weekday not in [6, 0]:  # Not Sunday or Monday
        bot.send_message(message.chat.id, f"""
Привет, {message.from_user.first_name}!!!🥰😘
Мы Горячая Пара!!! Сегодня {formatted_date} Собираем Секс Свинг Вечеринку Знакомств в Шикарной VIP Сауне:
✅с {evening_start} до {evening_end} Вечерняя Party 🥰
✅с 23:50 до 05:00 Ночная Party 🥰
✅Групповой, Индивидуальный Секс и Оргии!!!🥰
Если Желаете к Нам Присоединиться Сегодня - воспользуйтесь кнопками ниже🥰
Для получения информации и записи на вечеринку😘""", reply_markup=markup)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")
    else:
        bot.send_message(message.chat.id,'Извините, на сегодня мероприятий нет.\nНаши вечеринки проходят стабильно со Вторника по Субботу.❤️')
        # Ждем 10 секунд
        time.sleep(10)
        bot.send_message(message.chat.id,links_message)
        bot.send_message(message.chat.id,'Добавляйтесь, пожалуйста, в наши чаты Телеграм, наши секс вечеринки проходят стабильно со Вторника по Субботу. Запись начинается с 12 дня❤️', reply_markup=markup)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")
    user_states[message.chat.id] = None  # Инициализируем состояние пользователя


@bot.message_handler(commands=['contacts'])
def send_help_text2(message):
    bot.send_message(message.chat.id, '''
✅ Пишите сюда Телеграм: https://t.me/Na_instinkte 🥰
✅ Или звоните +79015679060 Настя и Миша (WhatsApp) 🥰
❤️🥰 Мы Вас проконсультируем''')

    # Пересылаем сообщение в группу
    # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
    bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


@bot.message_handler(func=lambda message: message.text == "Контакты")
def send_help_text1(message):
    bot.send_message(message.chat.id, '''
✅ Пишите сюда Телеграм: https://t.me/Na_instinkte 🥰
✅ Или звоните +79015679060 Настя и Миша (WhatsApp) 🥰
❤️🥰 Мы Вас проконсультируем''')

    # Пересылаем сообщение в группу
    # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
    bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


# Обработчик выбора "Задать вопрос"
@bot.message_handler(commands=['question'])
def send_question_prompt(message):
    bot.send_message(message.chat.id, 'Напишите в одном сообщении все свои вопросы и ожидайте ответ 😘')
    user_states[message.chat.id] = "awaiting_question"
    # Пересылаем сообщение в группу
    # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
    bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


# Обработчик выбора "Задать вопрос"
@bot.message_handler(func=lambda message: message.text == "Задать вопрос")
def send_question_prompt(message):
    bot.send_message(message.chat.id, 'Напишите в одном сообщении все свои вопросы и ожидайте ответ 😘')
    user_states[message.chat.id] = "awaiting_question"
    # Пересылаем сообщение в группу
    # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
    bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")

# Обработчик сообщений с вопросами после "Задать вопрос"
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "awaiting_question")
def handle_user_question(message):
    user_states[message.chat.id] = None  # Сброс состояния после получения вопроса
    bot.send_message(questions_group_chat_id, f"ID: {message.from_user.id}\nИмя: @{message.from_user.username}\nВопрос от {message.from_user.first_name}:\n\n{message.text}")
    bot.send_message(message.chat.id, "Ваше сообщение отправлено.🥰 Ожидайте ответ")


# /about
@bot.message_handler(func=lambda message: message.text == "Узнать больше")
def send_about(message):
    if today_weekday not in [6, 0]:  # Not Sunday or Monday
        photo_p = photo_path[today_weekday - 1] # -1, так как список фото начинается с индекса 0 для вторника
        with open(photo_p, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        chat_id = message.chat.id
        voice = open("G:\Мой диск/Работа/Для бота/audio1.ogg",'rb')
        bot.send_voice(chat_id, voice)
        bot.send_message(message.chat.id, f'''
❤️‍🔥😏
Здравствуйте! Сегодня {formatted_date}
ГРАНДИОЗНАЯ СВИНГ ВЕЧЕРИНКА в Шикарной VIP Сауне: 🥰

✅с {evening_start} до {evening_end} Вечерняя Party 🥰
✅с 23:50 до 05:00 Ночная Party 🥰

Приглашаем Вас на Секс Свинг Вечеринку в Сауне❗️
🟢(Собирается около 25-30 и более человек) 🟢

❗️Взнос за участие (входной билет):                     
🙋🏼‍♂️Мужчины - 5000₽
👫Пары МЖ - 3000
💃Девушки - бесплатно .
(❗️Взнос за участие не возвращается❗️)
💰ОПЛАТА ТОЛЬКО НАЛИЧНЫМИ💰
Взнос за участие только при входе, никаких предоплат!
😘Для Записи На Вечеринку Пришли пожалуйста Свое Имя и Последние Четыре Цифры Мобильного 😘''')
        photos = ["G:\Мой диск\Работа\Для бота\Ася.jpg","G:\Мой диск\Работа\Для бота\Лера.jpg","G:\Мой диск\Работа\Для бота\Наташа.jpg","G:\Мой диск\Работа\Для бота\Николь.jpg"]
        media = []
        for photo in photos:
            media.append(types.InputMediaPhoto(open(photo, 'rb')))
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, '''
😘Вот как все происходит на Нашей Секс Свинг Вечеринке 🥰: 
➖Вы приходите, оплачиваете по факту входной Билет! (Стоимость взноса за участие указаны выше👆)
➖Переодеваетесь! (❗️Дресс-код: интим бельё, нижнее бельё или голые + полотенце, тапочки❗️)
➖После - Вас встретят и проведут экскурсию, узнают Ваши предпочтения и помогут познакомиться с Гостями (если вы стеснительный).
⚠️Приходят Обычные Гости, Пары, Девушки, Парни и Все занимаются Сексом при Взаимной Симпатии и по Обоюдному Согласию 😘
✅ В 98 % Случаев Секс есть у Всех. У Нас Тематическая Вечеринка по Интересам. У Вас есть Шанс Познакомиться и Шанс Заняться Сексом! Все приходят Ради Него 😘 
✅Включено :
- Лёгкий фуршет (алкоголь приносите свой!)
- Роскошные комнаты для Секса
- Душ и туалет все есть
- Приятный отдых и общение😍😘

⛔️Ограничения по возрасту: от 18+ 🔞 до без Ограничений (Мы Всем Рады)!!! Средний возраст Гостей 35 - 45 лет (Молодые тоже часто бывают 🥰). 
🚫Фото- и Видео-съемка на территории проведения вечеринки ЗАПРЕЩЕНА 🚫. 
⚠️Правила!!! Секс Только при Взаимной Симпатии и по Обоюдному Согласию!!! У НАС НЕ БОРДЕЛЬ!!!
❗️ФОТО ГОСТЕЙ НЕ ВЫСЫЛАЕТСЯ - ВЕЧЕРИНКА ПОЛНОСТЬЮ КОНФИДЕНЦИАЛЬНАЯ❗️''')
        bot.send_message(message.chat.id, f'''
✅🥰 Сегодня {formatted_date}

✅с {evening_start} до {evening_end} Вечерняя Party 🥰
✅с 23:50 до 05:00 Ночная Party 🥰

Приглашаем Вас на Частную Секс Свинг Вечеринку!!! 
Вас Записать и Внести в Список на Сегодня?🥰
✅Если Вы Готовы Сегодня приехать 100% на Сегодняшнюю Секс Вечеринку 🥰
Для Записи Пришлите Пожалуйста Своё Имя, фото для фейсконтроля и Последние Четыре Цифры Мобильного''')
        chat_id = message.chat.id
        voice = open("G:\Мой диск/Работа/Для бота/audio2.ogg", 'rb')
        bot.send_voice(chat_id, voice)
        bot.send_message(message.chat.id, f'''
✅Если Вы Готовы Сегодня приехать 100% на Сегодняшнюю Секс Вечеринку 🥰
Для записи на сегодня на Секс Свинг Вечеринку:
✅с {evening_start} до {evening_end} Вечерняя Party 🥰
✅с 23:50 до 05:00 Ночная Party 🥰
пришлите пожалуйста ваше имя и последние четыре цифры мобильного и фото для фейсконтроля Мы Вас внесём в список и вышлем адрес будем рады вас видеть🥰😘''')
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")
    else:
        bot.send_message(message.chat.id,'Извините, на сегодня мероприятий нет.\nНаши вечеринки проходят стабильно со Вторника по Субботу.❤️')
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


# /reg
@bot.message_handler(func=lambda message: message.text == "Записаться")
def user_reg(message):
    if today_weekday not in [6, 0]:  # Not Sunday or Monday
        if today_weekday in [1, 2]: # Вторник Среда
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Вечер: Крестьянская Застава (19:00-0:00)',callback_data='Вечер: Крестьянская Застава (19:00-0:00)')
            itembtn2 = types.InlineKeyboardButton('Ночь: Крестьянская Застава (23:50-5:00)',callback_data='Ночь: Крестьянская Застава (23:50-5:00)')
            markup.add(itembtn1, itembtn2)
        elif today_weekday in [3]: # Четверг
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Вечер: Отрадное (20:00-1:00)',callback_data='Вечер: Отрадное (20:00-1:00)')
            itembtn2 = types.InlineKeyboardButton('Ночь: Отрадное (23:50-5:00)',callback_data='Ночь: Отрадное (23:50-5:00)')
            markup.add(itembtn1, itembtn2)
        elif today_weekday in [4]: # Пятница
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Вечер: Отрадное (18:00-23:00)',callback_data='Вечер: Отрадное (18:00-23:00)')
            itembtn2 = types.InlineKeyboardButton('Ночь: Отрадное (23:50-5:00)',callback_data='Ночь: Отрадное (23:50-5:00)')
            itembtn3 = types.InlineKeyboardButton('Ночь: Чистые пруды (23:50-5:00)',callback_data='Ночь: Чистые пруды (23:50-5:00)')
            markup.add(itembtn1, itembtn2, itembtn3)
        elif today_weekday in [5]: # Суббота
            markup = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Вечер: Шаболовская (18:30-23:30)', callback_data='Вечер: Шаболовская (18:30-23:30)')
            itembtn2 = types.InlineKeyboardButton('Ночь: Крестьянская Застава (23:50-5:00)', callback_data='Ночь: Крестьянская Застава (23:50-5:00)')
            itembtn3 = types.InlineKeyboardButton('Ночь: Чистые пруды (23:50-5:00)', callback_data='Ночь: Чистые пруды (23:50-5:00)')
            markup.add(itembtn1, itembtn2, itembtn3)

        bot.send_message(message.chat.id, 'Выберите какое метро вам ближе и в какое время удобнее приехать', reply_markup=markup)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")
    else:
        bot.send_message(message.chat.id,'Извините, на сегодня мероприятий нет.\nНаши вечеринки проходят стабильно со Вторника по Субботу.❤️')
        # Ждем 10 секунд
        time.sleep(10)
        bot.send_message(message.chat.id, links_message)
        bot.send_message(message.chat.id,'Добавляйтесь, пожалуйста, в наши чаты Телеграм, наши секс вечеринки проходят стабильно со Вторника по Субботу. Запись начинается с 12 дня❤️')
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


@bot.callback_query_handler(func=lambda call: call.data in ['Вечер: Крестьянская Застава (19:00-0:00)', 'Ночь: Крестьянская Застава (23:50-5:00)',
                                                            'Вечер: Отрадное (18:00-23:00)', 'Вечер: Отрадное (20:00-1:00)',
                                                            'Вечер: Отрадное (19:00-0:00)', 'Ночь: Отрадное (23:50-5:00)',
                                                            'Вечер: Шаболовская (18:30-23:30)', 'Ночь: Чистые пруды (23:50-5:00)'])
def process_city_step(call):
    try:
        chat_id = call.message.chat.id
        user_dict[chat_id] = User(call.data)

        # удалить старую клавиатуру
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)

        msg = bot.send_message(chat_id, 'Введите Ваше имя и последние четыре цифры мобильного одним сообщением')
        bot.register_next_step_handler(msg, process_fullname_step)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, call.chat.id, call.message_id)

    except Exception as e:
        bot.reply_to(call.message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, call.chat.id, call.message_id)


def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'В какое время вы будете на выбранной станции метро или рядом с ней?')
        bot.register_next_step_handler(msg, process_carDate_step)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")

    except Exception as e:
        bot.reply_to(message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")


def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")

        # ваша заявка "Имя пользователя"
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtn1 = types.InlineKeyboardButton('Всё верно',callback_data='Всё верно')
        itembtn2 = types.InlineKeyboardButton('Исправить',callback_data='Исправить')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id,getRegData(user,'Ваша заявка',message.from_user.first_name),parse_mode="Markdown",reply_markup=markup)
        bot.send_message(applications_group_chat_id, f"ID: {message.from_user.id}\nИмя: @{message.from_user.username}\nЗаявка от {message.from_user.first_name}\n")

    except Exception as e:
        bot.reply_to(message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{message.from_user.username}\n{message.text}")

@bot.callback_query_handler(func=lambda call: call.data in ['Всё верно','Исправить'])

def process_End_step(call):
    global first, instruction, addres
    try:
        chat_id = call.message.chat.id
        user = user_dict[chat_id]
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{call.message.from_user.username}\n{call.message.text}")

        if call.message:
            if call.data == 'Всё верно':
                bot.send_message(chat_id, 'Ваша заявка отправлена!❤️ Ожидайте ответа!😘')
                # отправить в группу
                bot.send_message(applications_group_chat_id,getRegData(user,f"ID: {call.message.from_user.id}\nИмя: @{call.message.from_user.username}\nЗаявка от {call.message.from_user.first_name}\n",bot.get_me().username),parse_mode="Markdown")

            elif call.data == 'Исправить':
                bot.send_message(chat_id, 'Запишитесь заново')

            # удалить старую клавиатуру
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text,
                                  reply_markup=None)


    except Exception as e:
        bot.reply_to(call.message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
        bot.send_message(all_message_group_chat_id, f"@{call.message.from_user.username}\n{call.message.text}")


# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template(
        '$title *$name* \n Бронь: *$userCity* \n Имя: *$fullname* \n Время: *$carDate*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'carDate': user.carDate
    })

    ## Ждем 10 секунд
    #time.sleep(10)
    #bot.send_message(message.chat.id, links_message)
    #bot.send_message(message.chat.id,'Добавляйтесь, пожалуйста, в наши чаты Телеграм, наши секс вечеринки проходят стабильно со Вторника по Субботу. Запись начинается с 12 дня❤️')


# Функция для отправки сообщения выбранному пользователю
def send_message_to_user(chat_id, text):
    try:
        bot.send_message(chat_id, text)
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при отправке сообщения пользователю {chat_id}: {e}")

@bot.message_handler(commands=['send_message'])
def handle_send_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Напишите ответ пользователю в одном сообщении")
    bot.register_next_step_handler(msg, handle_send_message_next)

def handle_send_message_next(message):
    global qwerty
    try:
        chat_id = message.chat.id
        qwerty = message.text
        msg = bot.send_message(chat_id,"Введите ID пользователя")
        bot.register_next_step_handler(msg, handle_send_message_next1)

    except Exception as e:
        bot.reply_to(message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, call.chat.id, call.message_id)

def handle_send_message_next1(message):
    chat_id = message.chat.id
    user_id = message.text
    bot.send_message(user_id, f"Ответ на ваше обращение:\n\n{qwerty}")
    bot.send_message(chat_id, "Сообщение отправлено пользователю.")

@bot.message_handler(commands=['send_address'])
def handle_send_address(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton('Крестьянская Застава',callback_data='Крестьянская Застава')
    itembtn2 = types.InlineKeyboardButton('Чистые пруды',callback_data='Чистые пруды')
    itembtn3 = types.InlineKeyboardButton('Шаболовская',callback_data='Шаболовская')
    itembtn4 = types.InlineKeyboardButton('Отрадное',callback_data='Отрадное')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id,'Выберите по какому метро адрес',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['Крестьянская Застава','Чистые пруды','Шаболовская','Отрадное'])
def handle_send_address_next(call):
    global location
    # удалить старую клавиатуру
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,reply_markup=None)
    try:
        chat_id = call.message.chat.id
        if call.message:
            if call.data == "Крестьянская Застава":
                location = 1
            elif call.data == "Отрадное":
                location = 2
            elif call.data == "Шаболовская":
                location = 3
            elif call.data == "Чистые пруды":
                location = 4

        msg = bot.send_message(chat_id,"Введите ID пользователя")
        bot.register_next_step_handler(msg, handle_send_address_next1)

    except Exception as e:
        bot.reply_to(call.message, help_message)
        # Пересылаем сообщение в группу
        # bot.forward_message(all_message_group_chat_id, call.chat.id, call.message_id)

def handle_send_address_next1(message):
    chat_id = message.chat.id
    user_id = message.text
    if location == 1:
        first = '''
❗️Адрес: Метро Крестьянская Застава ул. Марксистская, дом 34, корп. 4, сауна Лукоморье❗️

✅с 19:00 до 24:00 (кроме Субботы)
✅с 23:50 до 05:00'''
        instruction = 'ул. Марксистская, дом 34, корп. 4, Сауна Лукоморье'
        addres = 'ул. Марксистская, дом 34, корп. 4, Сауна Лукоморье'
        photosView = ["G:\Мой диск\Работа\Для бота\Крестьянская застава/11.jpg",
                      "G:\Мой диск\Работа\Для бота\Крестьянская застава/5.jpg",
                      "G:\Мой диск\Работа\Для бота\Крестьянская застава/6.jpg",
                      "G:\Мой диск\Работа\Для бота\Крестьянская застава/7.jpg"]
        photosRoute = ["G:\Мой диск\Работа\Для бота\Крестьянская застава/1.jpg",
                       "G:\Мой диск\Работа\Для бота\Крестьянская застава/2.jpg",
                       "G:\Мой диск\Работа\Для бота\Крестьянская застава/3.jpg",
                       "G:\Мой диск\Работа\Для бота\Крестьянская застава/4.jpg"]
        videoMedia = ["G:\Мой диск\Работа\Для бота\Крестьянская застава/8.MP4",
                      "G:\Мой диск\Работа\Для бота\Крестьянская застава/9.MP4",
                      "G:\Мой диск\Работа\Для бота\Крестьянская застава/10.MP4"]

    elif location == 2:
        first = '''
❗️Адрес: Метро Отрадное, ул. Пестеля, дом 1А сауна Отрадное❗️

✅с 20:00 до 01:00 (по Четвергам )
✅с в 18:00 до 23:00 (по Пятницам)
✅с в 23:50 до 05:00'''
        instruction = '''
✅ПО АДРЕСУ: Метро Отрадное (8 Минут Ходьбы) 1-ый Вагон из Центра, Выход №3, ул. Пестеля 1А!
Вход со стороны улицы!
Идем Прямо, Заходим под Вывеску "Салон Красоты"!'''
        addres = 'Метро Отрадное, Ул. Пестеля, 1А'
        photosView = ["G:\Мой диск\Работа\Для бота\Отрадное/1.jpg",
                      "G:\Мой диск\Работа\Для бота\Отрадное/2.jpg"]
        photosRoute = ["G:\Мой диск\Работа\Для бота\Отрадное/4.jpg",
                       "G:\Мой диск\Работа\Для бота\Отрадное/5.jpg",
                       "G:\Мой диск\Работа\Для бота\Отрадное/6.jpg"]
        videoMedia = ["G:\Мой диск\Работа\Для бота\Отрадное/3.MP4"]

    elif location == 3:
        first = '''
❗️Адрес: Метро Шаболовская, ул. ХАВСКАЯ, д. 26, ст. 2 (САУНА ТРЮМ)❗️

✅с 18:30 до 23:30
✅с 23:50 до 05:00'''
        instruction = '''
✅ПО АДРЕСУ: Метро Шаболовская (7 Минут Ходьбы) 1-ый Вагон из Центра, Выход №1, ул. Хавская, Дом 26, корп. 2 (САУНА ТРЮМ)!
Вход со стороны улицы!
Идем Прямо, Заходим в 1-этажное Здание из Красного Кирпича!'''
        addres = 'ул. Хавская Дом 26, корп 2 (САУНА ТРЮМ)'
        photosView = ["G:\Мой диск\Работа\Для бота\Шаболовская/1.jpg",
                      "G:\Мой диск\Работа\Для бота\Шаболовская/2.jpg"]
        photosRoute = ["G:\Мой диск\Работа\Для бота\Шаболовская/3.jpg",
                       "G:\Мой диск\Работа\Для бота\Шаболовская/4.jpg",
                       "G:\Мой диск\Работа\Для бота\Шаболовская/5.jpg"]
        videoMedia = ["G:\Мой диск\Работа\Для бота\Шаболовская/6.MP4",
                      "G:\Мой диск\Работа\Для бота\Шаболовская/7.MP4"]

    elif location == 4:
        first = '''
❗️Адрес: Метро Чистые Пруды, Улица Архангельский переулок, д. 5, стр. 4❗️

✅с 23:50 до 05:00'''
        instruction = '''
❗️Адрес: Метро Чистые Пруды, Улица Архангельский переулок, д. 5, стр. 4❗️
✅ Последний Вагон из Центра, Выход Номер 1
От метро 07 минут ходьбы'''
        addres = '❗️Улица Архангельский переулок, д. 5, стр. 4❗️'
        photosView = ["G:\Мой диск\Работа\Для бота\Чистые пруды/1.jpg",
                      "G:\Мой диск\Работа\Для бота\Чистые пруды/5.jpg"]
        photosRoute = ["G:\Мой диск\Работа\Для бота\Чистые пруды/2.jpg",
                       "G:\Мой диск\Работа\Для бота\Чистые пруды/3.jpg",
                       "G:\Мой диск\Работа\Для бота\Чистые пруды/4.jpg"]
        videoMedia = ["G:\Мой диск\Работа\Для бота\Чистые пруды/6.MP4"]

    bot.send_message(user_id, '✅МЕСТО ЗАБРОНИРОВАНО✅')
    bot.send_message(user_id, '⬇️⬇️⬇️ ‼️ ВОТ АДРЕС ‼️ ⬇️⬇️⬇️')
    bot.send_message(user_id, first + '''
✅ПРИЙТИ НА ВЕЧЕРИНКУ МОЖНО В ЛЮБОЕ ВРЕМЯ В УКАЗАННЫЕ ПРОМЕЖУТКИ

✅ВЗНОС ЗА УЧАСТИЕ:
для парней - 5000₽
с пары МЖ - 3000 ₽
Девушкам вход бесплатный
Взнос за участие только при входе, никаких предоплат!
❗️Взнос за участие не возвращается❗️

🔞✅❗️По Желанию Можно Взять с Собой Легкий Алкоголь: Пиво, Вино, Шампанское)🍷❗️🥰

‼️Дресс-код: интим белье, нижнее белье, голые + полотенце, тапочки (своё или на месте в аренду 300₽ комплект)‼️''')

    mediaView = []
    for photo1 in photosView:
        mediaView.append(types.InputMediaPhoto(open(photo1, 'rb')))
    bot.send_media_group(user_id, mediaView)

    bot.send_message(user_id, instruction)

    mediaRoute = []
    for photo2 in photosRoute:
        mediaRoute.append(types.InputMediaPhoto(open(photo2, 'rb')))
    bot.send_media_group(user_id, mediaRoute)

    mediaVideo = []
    for video in videoMedia:
        mediaVideo.append(types.InputMediaVideo(open(video, 'rb')))
    bot.send_media_group(user_id, mediaVideo)

    bot.send_message(user_id, """
✅Как приедете - Пожалуйста напишите в WhatsApp  или позвоните обязательно!!!
Как подойдете ко входу, идете прямо!!!
❗️На Входе Скажите от Насти и Миши❗️""")

    voice = open("G:\Мой диск\Работа\Для бота/1.ogg", 'rb')
    bot.send_voice(user_id, voice)

    bot.send_message(user_id, """
✅На Столе Будет Накрыт Легкий Фуршет и Безалкогольные Напитки 🥤 
По Желанию Можете Взять с Собой Легкий Алкоголь 🍷 (Пиво, Вино, Шампанское 🍾🥰)
Средний Возраст Гостей 35-45 лет 
🥰Молодые тоже по записи есть 🥰 
💰ОПЛАТА ТОЛЬКО НАЛИЧНЫМИ💰
Взнос за участие только при входе, никаких предоплат!
Ждём Вас! Будем Рады Вас Видеть! 😘
✅Вы Записаны Сегодня к Нам на Горячую Вечеринку Свинг Знакомств! 🥰
У Нас Количество Мест Ограничено! Ждем Вас 100% на Вечеринку 🥰
✅Если не Сможете Прийти, Пожалуйста, Сразу Напишите ❤️🥰😘
❗️На Входе Скажите, Пожалуйста, что Вы от Насти и Миши. Вас Встретят и Проведут в Нужный Зал❗️""")

    voice = open("G:\Мой диск\Работа\Для бота/2.ogg", 'rb')
    bot.send_voice(user_id, voice)
    
    bot.send_message(user_id, '⬇️⬇️⬇️ ‼️ ВОТ АДРЕС ‼️ ⬇️⬇️⬇️')
    bot.send_message(user_id, addres)
    bot.send_message(user_id, '⬆️⬆️⬆️ ‼️ ВОТ АДРЕС ‼️ ⬆️⬆️⬆️')

    bot.send_message(chat_id, "Адрес отправлен пользователю.")

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, help_message)

    # Пересылаем сообщение в группу
    #bot.forward_message(all_message_group_chat_id, message.chat.id, message.message_id)
    bot.send_message(all_message_group_chat_id,f"@{message.from_user.username}\n{message.text}")

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)