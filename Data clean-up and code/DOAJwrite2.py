import json
import re
import csv


def grab(x): #returning values and returning "unknown" if value error
    if x is False or x == " " or x == "" or x == "No Information":
        return "unknown"
    else:
        try:
            return x
        except:
            return "unknown"

def apc_existence(x,y):#Determining if there is an APC, returning 0 for APC cost if there isn't.
    if x == "No":
        return 0
    else:
        try:
            int(y)
            return int(y)
        except:
            return ""

def curr_pull(x,y): #Determining the currency. Returning None if no APC. Returning first three letters of currency if APC.
    if x == "No":
        return "None"
    else:
        try:
            return y[0:3]
        except:
            return ""

def ISSN_list(x,y): #Collecting the ISSNs and adding them to a list
    if len(x) > 10 or len(x) > 10: #If too long to be an ISSN
        return ""
    else:
        try:
            if x == y:
                return [x]
            elif x == "" or x == " ":
                return [y]
            elif y == "" or y == " ":
                return [x]
            else:
                return [x,y]
        except:
            return ""


data = list()
count = 0 #Count to get an idea how many journals have been processed

#importing DOAJ CSV file
with open('DOAJ2018.csv', newline='',encoding="utf8") as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        count = count + 1
        if count == 1: continue #Skipping the first line with headings
        #if count > 20: break
        if len(row) < 1:continue
        journal_dict ={
                "journal_title": grab(row[0]),
                "oa_type": "Gold",
                "issn": grab(ISSN_list(row[3],row[4])),
                "apc": grab(row[9]),
                "apc_price": grab(apc_existence(row[9],row[11])),
                "currency": grab(curr_pull(row[9],row[12])),
                "source_of_apc": "DOAJ",
                "publisher": grab(row[5]),
                "last_update": "10/02/2018"
            }
        data.append(journal_dict)
    #print (journal_dict)
    #break
#print (data)

with open('JSONtest4', 'w') as outfile: #writing file as a JSON file
    json.dump(data, outfile)

print ("DOAJ analysis finished",count,"journals added to JSON file.")
