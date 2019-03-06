# -*- coding: utf-8 -*-

#Questo è un bot per telegram costruito per FIUP
#Configurazione
#È stato costruito Alessandro Massarenti
#V 1.0

# Inporta dipendenze esterne 
import telepot
import sqlite3 

# Bot token
bot = telepot.Bot(# Insert bot token)

# Database position
def connessione():
    conn = sqlite3.connect('/var/bot/fiupbotdatabase.db')
    c = conn.cursor()
    return c

# Variabili
# Regolamento
rules = 'FIUP/Getting-Started (http://telegra.ph/FIUPGetting-Started-12-13)'

# Spiegazioni comandi
select = 'Seleziona una voce dalla tastiera! \n'
info = '/info apre il menù per avere informazioni generali tramite comunicazione diretta ad un utente certificato \n'
unipdbot = "/unipdbot Ti da l' indirizzo del bot dell' università di padova, carico di info utili \n"
faq = '/faq Ritorna le Frequently asked questions (Domande più poste) \n'
regolamento = '/regolamento Ritorna il regolamento da rispettare sui gruppi e nelle risorse del FIUP \n'
home = '/home Ritorna alla pagina principale del bot \n'

# Messaggio in GUI
print ("config.py caricato")