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

def oa_conv(x): #returning oa type. Hybrid if 1 and Gold if 0
    if x == 1 or x == "1":
        return "Hybrid"
    elif x == 0 or x == "0":
        return "Gold"
    else:
        return ""

def ISSN_FJ(x): # making sure ISSN coming from Flourish is correct
    if len(x) > 10: #If too long to be an ISSN
        return ""
    else:
        try:
            return x
        except:
            return ""

def ISSN_JSON(x): # making sure ISSN coming from Flourish is correct
    if len(x) > 10: #If too long to be an ISSN
        return ""
    else:
        try:
            return [x]
        except:
            return ""

def apc_existence(x):#Determining if there is an APC, returning No for APC if not
    if x == 0 or x == "0":
        return "No"
    else:
        try:
            int(x)
            return "Yes"
        except:
            return ""


def number(x): #For setting a default date and comparing for new updates
    if x == 'unknown':
        return 1970
    else:
        defaultldate = re.findall('[0-9]+/[0-9]+/([0-9]+)',x)
        return int(defaultldate[0])


FJcount = 0
FAPCcount = 0
FJlist = list()

with open('Flourishjournals.csv', newline='',encoding="utf8") as myFile1:
    FJ = csv.reader(myFile1)
    for FJline in FJ:
        FJcount = FJcount + 1
        if FJcount == 1: continue #Skipping the first line that has the headings
        #if FJcount > 20: break
        FJwords=FJline
        if len(FJwords) < 1:continue
        FJ_dict={
                "issn": grab(ISSN_FJ(FJwords[0])),
                "journal_title": grab(FJwords[1]) ,
                "publisher": grab(FJwords[2]),
                "oa_type": grab(oa_conv(FJwords[3])),
                "last_update": "unknown",
                "apc_price": "unknown"
                }
        FJlist.append(FJ_dict)
        #if FJcount > 10: break
        #print (FJlist)}


with open('FlourishAPCs.csv', newline='',encoding="utf8") as myFile2:
    FAPC = csv.reader(myFile2)
    for FAPCline in FAPC:
        FAPCcount = FAPCcount + 1
        if FAPCcount == 1: continue #Skipping the first line that has the headings
        #if FJcount > 1000: break
        FAPCwords = FAPCline
        if len(FAPCwords) < 1:continue
        #print (FAPCwords[2])
        date = re.findall('[0-9]+/[0-9]+/([0-9]+)',FAPCwords[2])
        date = int(date[0])
        for item in FJlist:
            if FAPCwords[3] != item["issn"]: continue
            if date > number(item["last_update"]):
                item["last_update"] = FAPCwords[2]
            item["apc_price"] = FAPCwords[1]
            #print (FAPCwords[3],item["issn"])
        #if FAPCcount > 10: break
print ("Flourish analysis finished",FJcount,"journals added")
print ("Comparing to DOAJ Journals...")

#Adding Flourish data to JSON file if not already in there

Json = open('JSONtest4')

json_data = json.load(Json)

ISSN_list = list()
jtitle_list = list()

Added = 0

for x in json_data: #Exporting ISSN and Journal title data to a list to compare against
    #print (x['ISSN'])
    for y in x['issn']:
        ISSN_list.append(y)
    jtitle_list.append(x["journal_title"])

for item in FJlist:
    exit = False
    for issn in ISSN_list: #Checking to see if Flourish ISSNs are in Json data file
        if item["issn"] == issn:
            exit = True
    if exit is True: continue #If ISSN is already in Json, exiting to not place it in json again

    for title in jtitle_list: #Checking to see if Flourish Journal titles are in Json data file
        if item["journal_title"] == title:
            exit = True
    if exit is True: continue #If title is already in Json, exiting to not place it in json again

    journal_dict ={
        "journal_title": item["journal_title"],
        "oa_type": item["oa_type"],
        "issn": grab(ISSN_JSON(item["issn"])),
        "apc": grab(apc_existence(item["apc_price"])),
        "apc_price": item["apc_price"],
        "currency": "USD",
        "source_of_apc": "Flourish",
        "publisher": item["publisher"],
        "last_update": item["last_update"]
        }
    Added = Added + 1
    #print (journal_dict)
    json_data.append(journal_dict)

with open('JSONtest4', 'w') as outfile: #writing file as a JSON file
    json.dump(json_data, outfile)

print ("Flourish Analysis finished",Added,"journals added to JSON file")
