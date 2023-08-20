import telebot
from random import *
import json
import requests
films=[]

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

bot.polling() # запуск бот-а, здесь спрятан 'while(True)'