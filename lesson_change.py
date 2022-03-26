import pandas as pd
import pathlib
from pathlib import Path
import time
from datetime import datetime
old_data = ""
old_rows = []
rows = []
changed_class = []
res = ''
days = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena"]
sheet_url = "https://docs.google.com/spreadsheets/d/1XNKJfUdtsb386wiZkGrKtZ0EKm5LqU5YI2G5P0mS6aw/edit#gid=1616216493"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
data = pd.read_csv(url_1, header = 1)
index = data.index
number_of_rows = len(index)
old_data = data

#print(data)
def lesson_changes(class_num):
    changes = False
    weekday_num = datetime.today().weekday()
    res = weekdate_num_to_name(weekday_num)
    for index, row in data.iterrows():
        for i in range(len(days)):
            if "NaN" in str(row):
                if days[i] in str(row[0]):
                    l = len(res)
                    if res[l-3:l-2] == ":":
                        res += "Nav izmaiņas \n"
                    res = res + days[i] + ": \n"
        row_class_num = str(row['Klase(s)'])
        if row_class_num.lower() == class_num:
            if row['Tips'] == "Atcelts":
                changes = True
                res += (f"{row['Stundas']}. stunda ir atcelta.\n")
            elif row['Tips'] == "Aizvietojums" or row['Tips'] == "Pārraudzība":
                changes = True
                tips = str(row['Tips'])
                res += (f"{row['Stundas']}. stunda - {tips.lower()}, priekšmets: {row['Priekšmets']}, skolotajs: {row['Aizvietotājs']}, telpa: {row['Telpa']}.\n")
    if changes == False:
        res = "Nav izmaiņas"
    if res[-3] == ":":
        res += "Nav izmaiņas"
    return res  
        


def weekdate_num_to_name(num):
    if num == 0 or num == 5 or num == 6:
        return "Pirmdiena: \n"
    elif num == 1:
        return "Otrdiena: \n"
    elif num == 2:
        return "Trešdiena: \n"
    elif num == 3:
        return "Ceturtdiena: \n"
    elif num == 4:
        return "Piektdiena: \n"


def check_updates():
    if str(old_data) != "":
        for index, row in old_data.iterrows():
            old_rows.append(f"{row['Tips']} {row['Stundas']} {row['Klase(s)']} {row['(Skolotājs)']} {row['Aizvietotājs']} {row['Telpa']} {row['Priekšmets']}")

        for index, row in data.iterrows():
            rows.append(f"{row['Tips']} {row['Stundas']} {row['Klase(s)']} {row['(Skolotājs)']} {row['Aizvietotājs']} {row['Telpa']} {row['Priekšmets']}")

        for i in range(len(rows)):
            if rows[i] in old_rows:
                pass
            else:
                text = rows[i].split()
                if text[2] == "-":
                    print(text[4])
                else:
                    print(text[2])
                changed_class.append(text)
                
    return changed_class

