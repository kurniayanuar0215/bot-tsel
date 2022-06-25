import telebot
from telebot import apihelper
import os
from telebot import types

bot = telebot.TeleBot('1991240221:AAEjSgb1_IigklBwPHGlse9e8LO6xJKBvwI')
apihelper.proxy = {
  'https': 'https://10.59.66.1:8080'
}

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, '/prod, /prod2, /proddaily, /dataplan, /transport, /trendlat, /apps')

@bot.message_handler(commands=['prod'])
def welcome(message):
    bot.reply_to(message, 'Checking lastest Productivity, please wait...')
    os.system('python' + ' ' + 'F:/KY/check_prod/prod.py')

@bot.message_handler(commands=['prod2'])
def welcome(message):
    bot.reply_to(message, 'Checking lastest Productivity, please wait...')
    os.system('python' + ' ' + 'F:/KY/check_prod/prod_v2.py')

@bot.message_handler(commands=['proddaily'])
def welcome(message):
    bot.reply_to(message, 'Get lastest Productivity, please wait...')
    os.system('python' + ' ' + 'F:/KY/prod/start_prod.py')

@bot.message_handler(commands=['trendlat'])
def welcome(message):
    bot.reply_to(message, 'Get Trend Latency, please wait...')
    os.system('python' + ' ' + 'F:/KY/latency_v2/start_latency_v2.py')

@bot.message_handler(commands=['daily'])
def welcome(message):
    bot.reply_to(message, 'Daily Process, please wait...')
    os.system('python' + ' ' + 'F:/KY/daily.py')

@bot.message_handler(commands=['dsp'])
def welcome(message):
    bot.reply_to(message, 'DSP Process, please wait...')
    os.system('python' + ' ' + 'F:/KY/dsp/dsp.py')
    os.system('python' + ' ' + 'F:/KY/dsp_daily/gaet_dsp_daily.py')

@bot.message_handler(commands=['dataplan'])
def welcome(message):
    bot.reply_to(message, 'Data Plan process update, please wait...')
    os.system('python' + ' ' + 'F:/KY/dataplan/get.py')

@bot.message_handler(commands=['transport'])
def welcome(message):
    bot.reply_to(message, 'Cek Transport, please wait...')
    os.system('python' + ' ' + 'F:/KY/transport/cek.py')

@bot.message_handler(commands=['apps'])
def welcome(message):
    bot.reply_to(message, 'Get Apps daily, please wait 20-30 minute...')
    os.system('python' + ' ' + 'F:/KY/Apps_daily/start_apps.py')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()