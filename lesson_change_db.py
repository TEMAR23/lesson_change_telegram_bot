from decimal import MIN_ETINY
import sqlite3
from datetime import datetime, timedelta
from xml.dom import minicompat

def createdb():
    global cursor, connect
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()

    #cursor.execute("DROP TABLE IF EXISTS SUBSCRIBES")
  
    # Creating table
    table = """ CREATE TABLE IF NOT EXISTS SUBSCRIBES (
                user_id INT,
                class_name CHAR(25) NOT NULL
            ); """
    
    cursor.execute(table)
    connect.commit()
    connect.close()
    

    print("database ready")

def addclass(userid, class_name):
    stop =False
  
    ins_values = [userid, class_name]
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute("SELECT user_id FROM SUBSCRIBES")
    result = cursor.fetchall()
    #print(result)
    for i in result:
        if stop == False:
            #print(f"if {userid} == {i[0]}")
            if userid == i[0]:
               #deleteuser(userid)
               #print("== true")
               cursor.execute(f"DELETE FROM SUBSCRIBES WHERE user_id = {userid}")
               cursor.execute("INSERT INTO SUBSCRIBES VALUES(?, ?);", ins_values)
            else:
               cursor.execute("INSERT INTO SUBSCRIBES VALUES(?, ?);", ins_values)
               #print("insert")
               stop = True
    if result == []:
        #print("True")
        cursor.execute("INSERT INTO SUBSCRIBES VALUES(?, ?);", ins_values)

    connect.commit()
    connect.close()
    
    return "success"

def deleteuser(userid):
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute(f"DELETE FROM SUBSCRIBES WHERE user_id='{userid}'")
    connect.commit()
    connect.close()
    return "success"

def return_ids(class_name):
    res = []
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute("SELECT user_id, class_name FROM SUBSCRIBES")
    result = cursor.fetchall()
    for i in result:
        if i[1] == class_name:
            res.append(i[0])
    connect.commit()
    connect.close()
    return(res)

def return_class_num(userid):
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute("SELECT user_id, class_name FROM SUBSCRIBES")
    result = cursor.fetchall()
    for i in result:
        if i[0] == userid:
            return i[1]

def delete_repeated_user():
    list = []
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute("SELECT user_id, class_name FROM SUBSCRIBES")
    result = cursor.fetchall()
    for i in result:
        if i[0] in list:
            insdata = i
            cursor.execute(f"DELETE FROM SUBSCRIBES WHERE user_id='{i[0]}'")
            cursor.execute("INSERT INTO SUBSCRIBES VALUES(?, ?);", insdata)
        else:
            list.append(i[0])
    connect.commit()
    connect.close()

def send_time_till_next_les(group):
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    if group == "A":
        cursor.execute("SELECT * FROM LESSONS_TIME_A")
    else:
        cursor.execute("SELECT * FROM LESSONS_TIME_B")
    result = cursor.fetchall()
    now = datetime.now()
    timenow = (now.strftime("%H:%M"))
    hours = int(timenow[:2])
    minutes = int(timenow[3:])
    timenow = timedelta(hours=hours, minutes=minutes)
    for i in result:
        text = i[1]
        hours = int(text[:2])
        minutes = int(text[3:])
        lesstime = timedelta(hours=hours, minutes=minutes)
        diff1 = lesstime - timenow
        text = i[2]
        hours = int(text[:2])
        minutes = int(text[3:])
        lesstime = timedelta(hours=hours, minutes=minutes)
        diff2 = lesstime - timenow
        #print(str(diff1), str(diff2))
        if "-1 day" in str(diff1):
            pass
        else:
            h = str(diff1)[:1]
            min = str(diff1)[2:4]
            if str(min) == "00":
                tm = ""
            elif str(min) == "01":
                tm = "1 minūtes"
            else:
                tm = min + " minūtēm"
            if str(h) == "0":
                th = ""
            elif str(h) == "1":
                th = " 1 stundas un"
            else:
                th = "" + h + " stundām un" 
            
            connect.commit()
            connect.close()
            return (f"Stunda sāksies pēc{th} {tm}")
            
        if "-1 day" in str(diff2):
            pass
        else:
            h = str(diff2)[:1]
            min = str(diff2)[2:4]
            if str(min) == "00":
                tm = ""
            elif str(min) == "01":
                tm = "1 minūtes"
            else:
                tm = min + " minūtēm"
            if str(h) == "0":
                th = ""
            elif str(h) == "1":
                th = " 1 stundas un"
            else:
                th = "" + h + " stundām un" 
            connect.commit()
            connect.close()
            return (f"Stunda beigsies pēc{th} {tm}")
        
def les_time(group):
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    res = ""
    if group == "A":
        cursor.execute("SELECT * FROM LESSONS_TIME_A")
    else:
        cursor.execute("SELECT * FROM LESSONS_TIME_B")
    result = cursor.fetchall()
    for i in result:
        res += f"{i[0]}.stunda {i[1]}-{i[2]}\n"
    return res

def return_lesson_table(day):
    connect = sqlite3.connect('D:\Programming\lesson_change\lesson_change.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM lesson_timetable_A WHERE weekday='{day}'")
    result = cursor.fetchall()
    res = ''
    for i in result:
        res = f'\n{i[1]}. stunda {i[3]}' + res
    if day == datetime.today().isoweekday():
        res = "\nŠodienas stundu saraksts:" + res
    else:
        if day == 1:
            res = f"\nPirmdiena:" + res
        elif day == 2:
            res = f"\nOtrdiena:" + res
        elif day == 3:
            res = f"\nTrešdiena:" + res
        elif day == 4:
            res = f"\nCeturdiena:" + res
        elif day == 5:
            res = f"\nPiektdiena:" + res
    return res
#def lesson_time()
        
