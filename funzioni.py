# -*- coding: utf-8 -*-

#Questo è un bot per telegram costruito per FIUP
#File principale
#È stato costruito Alessandro Massarenti
#V 1.0

# Inporta dipendenze esterne 
import sqlite3
#inporta dipendenze interne
from config import *

# Controlla se l' utente esiste ed è certificato
def checkUser(user_id):
    user_id = int(user_id)
    c = connessione()
    c.execute('SELECT nome FROM utenti WHERE telegramID = ?', (user_id,))
    user_data = c.fetchone()
    return user_data