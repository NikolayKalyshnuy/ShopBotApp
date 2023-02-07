from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from flask import request
from app import app
# web_app = WebAppInfo(url="https://ideahold.github.io/")
# def webAppKeyboard(): #создание клавиатуры с webapp кнопкой

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #создаем клавиатуру
with app.test_request_context():
    url = request.url
webAppTest = WebAppInfo(url=url) #создаем webappinfo - формат хранения url
one_butt = KeyboardButton(text="Magazine", web_app=webAppTest) #создаем кнопку типа webapp
two_butt = KeyboardButton(text='MyOrder')
kb.add(one_butt) #добавляем кнопки в клавиатуру
kb.add(two_butt)

   # return keyboard #возвращаем клавиатуру