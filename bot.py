# -*- coding: utf-8 -*-

#Questo è un bot per telegram costruito per FIUP
#File principale
#È stato costruito Alessandro Massarenti
#V 1.0

# Inporta dipendenze esterne 
import time
import telepot
from telepot.loop import MessageLoop
import sqlite3
#inporta dipendenze interne
from config import *
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from funzioni import *

# Handle input
def handle(msg):

    content_type, chat_type, chat_id= telepot.glance(msg)
    user_id = msg['from']['id']
    print(content_type, chat_type, chat_id, user_id)
    
    # Prova a vedere se l'utente è conosciuto
    try: 
        user_data = checkUser(user_id)
        bot.sendMessage(chat_id, text = user_data) 
    except:
        bot.sendMessage(chat_id, text = 'No ti se nessuni, torna a casa imbriagon!')

    # Controlla se il messaggio ricevuto è testo
    if content_type == 'text':
        # Mette il messaggio come variabile
        comando = msg['text']

        # Avvia la pulsantiera principale
        if (comando == '/start') or (comando == '/home'):
            bot.sendMessage(chat_id, text = select + '\n' + info + faq + regolamento + unipdbot,
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text = '/info'), KeyboardButton(text = '/FAQ')],
                    [KeyboardButton(text = '/regolamento'), KeyboardButton(text = '/unipdbot')],
                    ]))

        # Avvia la pulsantiera delle categorie delle info
        if (comando == '/info'):
            bot.sendMessage(chat_id, text = select + '\n' + info + faq + regolamento + unipdbot + user_data,
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text = '/iscrizioni'), KeyboardButton(text = '/laboratori')],
                    [KeyboardButton(text = '/altro')],
                    ]))

        # Avvia la pulsantiera delle FAQ
        if comando == '/FAQ':
            bot.sendMessage(chat_id, text = rules,)

        # Avvia la pulsantiera del regolamento
        if comando == '/regolamento':
            bot.sendMessage(chat_id, text = rules,)
        
        # Avvia la chat con il bot di UniPd
        if comando == '/unipdbot':
            bot.sendMessage(chat_id, text = '@unipdbot')

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Mantiene attivo il programma
while 1:
    time.sleep(10)