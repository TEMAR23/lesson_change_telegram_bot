
import telebot
from bs4 import BeautifulSoup
from telebot import types
from datetime import datetime
import threading

import lesson_change_db as db
import lesson_change as lc
import lesson_time as lt

allclasses = ["7a", "7b", "7c", "8a", "8b", "8c", "9a", "9b", "9c", "9d", "10a", "10b", "10c", "10d", "11a", "11b", "11c", "11d", "11sb", "10e", "10sb", "11e", "12a", "12b", "12c", "12d", "12e", "12sb"]
writingclassnum = False
bot = telebot.TeleBot("5263000009:AAE-fotKHih84A9HsAzY9ImchbbOwGxobfs", parse_mode=None)

MainKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
Mainbtn1 = types.KeyboardButton("Iestatījumi")
Mainbtn2 = types.KeyboardButton("Izmaiņas manā klasē")
Mainbtn3 = types.KeyboardButton("Stundu laiki")
Mainbtn4 = types.KeyboardButton("Stundu saraksts")
Mainbtn5 = types.KeyboardButton("Konsultācijas")
MainKeyboard.add(Mainbtn1, Mainbtn2, Mainbtn3, Mainbtn4, Mainbtn5)
SetKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
Setbtn1 = types.KeyboardButton("Mainīt klasi")
Setbtn2 = types.KeyboardButton("Izslēgt izziņas")
Setbtn3 = types.KeyboardButton("Atgriezties")
SetKeyboard.add(Setbtn1, Setbtn2, Setbtn3)

ClassKeyboard = types.InlineKeyboardMarkup()
ClassBtn1 = types.InlineKeyboardButton('7a', callback_data='7a')
ClassBtn2 = types.InlineKeyboardButton('7b', callback_data='7b')
ClassBtn3 = types.InlineKeyboardButton('7c', callback_data='7c')
ClassBtn4 = types.InlineKeyboardButton('8a', callback_data='8a')
ClassBtn5 = types.InlineKeyboardButton('8b', callback_data='8b')
ClassBtn6 = types.InlineKeyboardButton('8c', callback_data='8c')
ClassBtn7 = types.InlineKeyboardButton('9a', callback_data='9a')
ClassBtn8 = types.InlineKeyboardButton('9b', callback_data='9b')
ClassBtn9 = types.InlineKeyboardButton('9c', callback_data='9c')
ClassBtn10 = types.InlineKeyboardButton('9d', callback_data='9d')
ClassBtn11 = types.InlineKeyboardButton('10a', callback_data='10a')
ClassBtn12 = types.InlineKeyboardButton('10b', callback_data='10b')
ClassBtn13 = types.InlineKeyboardButton('10c', callback_data='10c')
ClassBtn14 = types.InlineKeyboardButton('10d', callback_data='10d')
ClassBtn15 = types.InlineKeyboardButton('10e', callback_data='10e')
ClassBtn16 = types.InlineKeyboardButton('10sb', callback_data='10sb')
ClassBtn17 = types.InlineKeyboardButton('11a', callback_data='11a')
ClassBtn18 = types.InlineKeyboardButton('11b', callback_data='11b')
ClassBtn19 = types.InlineKeyboardButton('11c', callback_data='11c')
ClassBtn20 = types.InlineKeyboardButton('11d', callback_data='11d')
ClassBtn21 = types.InlineKeyboardButton('11sb', callback_data='11sb')
ClassBtn22 = types.InlineKeyboardButton('11e', callback_data='11e')
ClassBtn23 = types.InlineKeyboardButton('12a', callback_data='12a')
ClassBtn24 = types.InlineKeyboardButton('12b', callback_data='12b')
ClassBtn25 = types.InlineKeyboardButton('12c', callback_data='12c')
ClassBtn26 = types.InlineKeyboardButton('12d', callback_data='12d')
ClassBtn27 = types.InlineKeyboardButton('12e', callback_data='12e')
ClassBtn28 = types.InlineKeyboardButton('12sb', callback_data='12sb')
ClassKeyboard.row(ClassBtn1, ClassBtn2, ClassBtn3, ClassBtn4)
ClassKeyboard.row(ClassBtn5, ClassBtn6, ClassBtn7, ClassBtn8)
ClassKeyboard.row(ClassBtn9, ClassBtn10, ClassBtn11, ClassBtn12)
ClassKeyboard.row(ClassBtn13, ClassBtn14, ClassBtn15, ClassBtn16)
ClassKeyboard.row(ClassBtn17, ClassBtn18, ClassBtn19, ClassBtn20)
ClassKeyboard.row(ClassBtn21, ClassBtn22, ClassBtn23, ClassBtn24)
ClassKeyboard.row(ClassBtn25, ClassBtn26, ClassBtn27, ClassBtn28)
ClearInlineKeyboard = types.InlineKeyboardMarkup()

DaysKeyboard = types.InlineKeyboardMarkup()
DaysBtn1 = types.InlineKeyboardButton('Pirmdiena', callback_data='Monday')
DaysBtn2 = types.InlineKeyboardButton('Otrdiena', callback_data='Tuesday')
DaysBtn3 = types.InlineKeyboardButton('Trešdiena', callback_data='Wensday')
DaysBtn4 = types.InlineKeyboardButton('Ceturtdiena', callback_data='Thursday')
DaysBtn5 = types.InlineKeyboardButton('Piektdiena', callback_data='Friday')
DaysKeyboard.row(DaysBtn1,DaysBtn2)
DaysKeyboard.row(DaysBtn3,DaysBtn4)
DaysKeyboard.row(DaysBtn5)

ConsListKeyboard = types.InlineKeyboardMarkup()
ClistBtn1 = types.InlineKeyboardButton('1', callback_data='1page')
ClistBtn2 = types.InlineKeyboardButton('2', callback_data='2page')
ClistBtn3 = types.InlineKeyboardButton('3', callback_data='3page')
ConsListKeyboard.row(ClistBtn1, ClistBtn2, ClistBtn3)

db.createdb()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    global todeletemessid
    todeletemessid = bot.send_message(message.chat.id, 
    f" Čau, {message.from_user.first_name}.\n"
    "Šis bots sūtīs tev zīņojumus par stundu izmaiņam.\n"
    "Lai sāktu izvēlies savu klasi.", reply_markup=ClassKeyboard).message_id
    
    #writingclassnum = True

@bot.message_handler(content_types=['text'])  
def ContentTypeisText(message):
    global todeletemessid
    if message.text == "Iestatījumi":
        bot.send_message(message.chat.id, "Noklikšķiniet, lai mainītu iestatījumus", reply_markup=SetKeyboard)
    if message.text == "Mainīt klasi":
        #writingclassnum = True
        todeletemessid = bot.send_message(message.chat.id, "Izvēlies savu klasi.", reply_markup=ClassKeyboard).message_id
    if message.text == "Izslēgt izziņas":
        if db.deleteuser(message.chat.id) == "success":
            bot.send_message(message.chat.id, "Izziņas ir izslēgti, lai to ieslēgt uzklikšķini 'Mainīt klasi'.", reply_markup=MainKeyboard)
        else:
            bot.send_message(message.chat.id, "Parādas kļūda", reply_markup=MainKeyboard)

    if message.text == "Izmaiņas manā klasē":
        class_num = db.return_class_num(message.chat.id)
        text = lc.lesson_changes(class_num)
        bot.send_message(message.chat.id, text, reply_markup=MainKeyboard)

    if message.text == "Atgriezties":
        bot.send_message(message.chat.id, "Izvēlne", reply_markup=MainKeyboard)

    if message.text == "Stundu laiki":
        class_num = db.return_class_num(message.chat.id)
        time_group = lt.return_time_group(class_num)
        text = db.send_time_till_next_les(time_group)
        text = f"{text}\n{db.les_time(time_group)}"
        bot.send_message(message.chat.id, text)
    
    if message.text == "Stundu saraksts":
        day = datetime.today().isoweekday()
        if day == 6 or day == 7:
            day = 1
        text = db.return_lesson_table(day)
        bot.send_message(message.chat.id, text, reply_markup=DaysKeyboard)

    if message.text == "Konsultācijas":
        bot.send_message(message.chat.id, lt.send_consultations_list(1), reply_markup=ConsListKeyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global todeletemessid
    if call.data == "1page":
        bot.send_message(call.message.chat.id, lt.send_consultations_list(1), reply_markup=ConsListKeyboard)
    elif call.data == "2page":
        bot.send_message(call.message.chat.id, lt.send_consultations_list(2), reply_markup=ConsListKeyboard)
    elif call.data == "3page":
        bot.send_message(call.message.chat.id, lt.send_consultations_list(3), reply_markup=ConsListKeyboard)
    
    if call.data == "Monday":
        text = db.return_lesson_table(1)
        bot.send_message(call.message.chat.id, text, reply_markup=DaysKeyboard)
    elif call.data == "Tuesday":
        text = db.return_lesson_table(2)
        bot.send_message(call.message.chat.id, text, reply_markup=DaysKeyboard)
    elif call.data == "Wensday":
        text = db.return_lesson_table(3)
        bot.send_message(call.message.chat.id, text, reply_markup=DaysKeyboard)
    elif call.data == "Thursday":
        text = db.return_lesson_table(4)
        bot.send_message(call.message.chat.id, text, reply_markup=DaysKeyboard)
    elif call.data == "Friday":
        text = db.return_lesson_table(5)
        bot.send_message(call.message.chat.id, text, reply_markup=DaysKeyboard)

    if call.data == "7a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard) 
    elif call.data == "7b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)    
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)         
    elif call.data == "7c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard) 
    elif call.data == "8a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)         
    elif call.data == "8b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "8c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "9a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "9b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)         
    elif call.data == "9c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)         
    elif call.data == "9d":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "10a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "10b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)         
    elif call.data == "10c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)     
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)       
    elif call.data == "10d":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)            
    elif call.data == "10e":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "10sb":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "11a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "11b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "11c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "11d":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "11e":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "11sb":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "12a":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "12b":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)  
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)           
    elif call.data == "12c":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "12d":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)   
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)          
    elif call.data == "12e":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard) 
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard)            
    elif call.data == "12sb":
        if (db.addclass(call.message.chat.id, call.data)) == "success":
            bot.send_message(call.message.chat.id, "Klase pievienota", reply_markup=MainKeyboard)
            bot.edit_message_reply_markup(call.message.chat.id, todeletemessid, reply_markup=ClearInlineKeyboard) 






    

def repeat():
    db.delete_repeated_user()
    changed_class = lc.check_updates()
    if changed_class != []:
        for i in range(len(changed_class)):
            mestosend = lc.lesson_changes(changed_class)
            sendnotifilication(mestosend, changed_class[i])
    threading.Timer(300.0, repeat).start()
    changed_class = []
    
def sendnotifilication(message, class_num):
    ids = db.return_ids(class_num)
    for i in range(len(ids)):
        bot.send_message(id[i], message)
        


repeat()

bot.polling(none_stop=True)

