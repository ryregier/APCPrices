import json
import re

#DOAJ Excel sheet
doaj = open('DOAJ2018.csv',encoding="utf8")

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
            elif y == "" or y == " ":
                return [x]
            else:
                return [x,y]
        except:
            return ""


data = list()
count = 0 #Count to get an idea how many journals have been processed
for line in doaj:
    #if count > 15: break
    count = count + 1
    line = line.rstrip()
    if line.startswith("\ufeffJournal title"): #Workaround for unicode error on first line
        continue
    words=line.split(",")
    #words = words.rstrip()
    if len(words) < 1:continue
    #print (words)
    #print (words[0])
    #print (grab(words[0]))
    journal_dict ={
            "Journal Title": grab(words[0]),
            "OA_Type": "Gold",
            "ISSN": grab(ISSN_list(words[3],words[4])),
            "APC": grab(words[9]),
            "APC Price": grab(apc_existence(words[9],words[11])),
            "Currency": grab(curr_pull(words[9],words[12])),
            "Source of APC": "DOAJ",
            "Publisher": grab(words[5]),
            "Last_update": "10/02/2018"
        }
    data.append(journal_dict)
    #print (journal_dict)
    #break
#print (data)

with open('JSONtest', 'w') as outfile: #writing file as a JSON file
    json.dump(data, outfile)

print ("DOAJ analysis finished",count,"journals added to JSON file.")
