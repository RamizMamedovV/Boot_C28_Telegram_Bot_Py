import telebot
from random import *
import json
import requests
films=[]

API_URL='https://7012.deeppavlov.ai/model'

API_TOKEN = '6574903644:AAGy5ukTAeNdI1KrQb28fRRfeXBp0wQL9ks'
bot = telebot.TeleBot(API_TOKEN) # инициализируем конструктор Телебот

@bot.message_handler(commands=['start'])    # декоратор обрабатывающий ввод '/start'
def start_message(message): 
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append(" Техасская резня ")
        films.append(" Санта Барбара") 
        bot.send_message(message.chat.id," Фильмотека Готова по умолчанию!")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Вот списокІ")
        bot.send_message(message.chat.id, ", ".join(films))
    except:
         bot.send_message(message.chat.id,"пока пустая фильмотека))")

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json","w",encoding="utf-8") as fh:  # режим 'w'
        fh.write(json.dumps(films,ensure_ascii=False))
    bot.send_message(message.chat.id,"Фильмотека сохранена в films.json")
   
@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:] # считываем строку, но без начального 'wiki'
    qq=" ".join(quest)               # получаем строковое значение введенного запроса
    data = { 'question_raw': [qq]}
    try:
        # Get - для получения а post - для отправки в HHTP
        # с помощью запроса requests.post по адресу "API_URL", с "json=data"
        # м отключает проверку сертификата SSL - хотя так делать не нужно
    # json() разбирает JSON-ответ,от сервера, и возвращает его в виде объекта Python.
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res) # отправим пользователю то, что получили
    except:
        bot.send_message(message.chat.id, "Ничего не нашёл » :-(")  


# чтобы некоторые команды не воспринимались как тестовые, 
# этот декоратор лучше ставить в конце
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "дела" in message.text.lower() :
       bot.send_message(message.chat.id, "Нормально, Сам как?")


bot.polling() # запуск бот-а, здесь спрятан 'while(True)'