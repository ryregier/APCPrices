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

def apc_existence(x):#Determining if there is an APC, returning No for APC if not
    if x == 0 or x == "0":
        return "No"
    else:
        try:
            int(x)
            return "Yes"
        except:
            return ""

def oa_conv(x): #returning oa type. Hybrid if 1 and Gold if 0
    if x == "Open Access":
        return "Gold"
    elif x == "Hybrid" or x == "Hybrid ":
        return "Hybrid"
    else:
        return ""

def issn_conv(x): #converting issn to list format
    if len(x) > 10: #If too long to be an ISSN
        return ""
    else:
        try:
            return [x]
        except:
            return ""

Ecount = 0
Elist = list()

#opening E file and reading it
with open('E2018csv.csv', newline='', encoding="ISO-8859-1") as myFile:
    Edata = csv.reader(myFile)
    for Eitem in Edata:
        Ecount = Ecount + 1
        if Ecount == 1: continue #Skipping the first line that has the headings
        #if Ecount > 20: break
        if len(Eitem) < 1:continue
        Edict = { #Adding data from E file into dictionary
            "issn": grab(Eitem[0]),
            "journal_title": grab(Eitem[1]) ,
            "publisher": "Elsevier",
            "oa_type": grab(oa_conv(Eitem[2])),
            "last_update": "10/2/2018",
            "apc_price": grab(Eitem[4]),
            "apc": grab(apc_existence(Eitem[4])),
            "currency": grab(Eitem[3]),
            "source_of_apc": "Elsevier Price List"
            }

        Elist.append(Edict) #adding each dictionary of a journal to a list

APCprices = open('JSONtest4')

json_data = json.load(APCprices)

Eindexed_count = 0
Enew_journals = list()

for Eitem in Elist: #looping through E journal list
    issn_match = False
    title_match = False
    for j in json_data: #looping through JSON journal list to compare it to E journals
        if issn_match == True or title_match == True: continue #SO no duplicate matches
        for issn in j['issn']: #Checking ISSN matches they are in a list in the json file so need to go through in loop
            if Eitem["issn"] == issn:
                issn_match = True
                j["journal_title"] = Eitem["journal_title"] #if ISSN match making sure journal title is offical listed E title
        if issn_match == False: #If ISSN already matches, no need to match by title
            if Eitem["journal_title"] == j["journal_title"]: #checking title match
                title_match = True
                try:
                    j['issn'].append(Eitem["issn"]) #Adding E issn that is not already in json file
                except:
                    print ("ISSN error")

        if issn_match == True or title_match == True: #If journal is already in JSON, corrected details so has update E information
            j["publisher"] = Eitem["publisher"]
            j["oa_type"] = Eitem["oa_type"]
            j["last_update"] = Eitem["last_update"]
            j["apc_price"] = Eitem["apc_price"]
            j["apc"] = Eitem["apc"]
            j["currency"] = Eitem["currency"]
            j["source_of_apc"] = Eitem["source_of_apc"]

            Eindexed_count = Eindexed_count + 1 #Keeping track of how many journals have been corrected
            #print ("Journal corrected")

    if issn_match != True and title_match != True:#Adding new journals not already in json to a list to add to json file at the end.
        Enew_journals.append(Eitem)


for journal in Enew_journals: #adding new journals from the list to the json file
    journal["issn"] = issn_conv(journal["issn"]) #converting issn to list for new journals
    json_data.append(journal)

#print (json_data[0:5])

with open('JSONtest4', 'w') as outfile: #writing file as a JSON file
    json.dump(json_data, outfile)

print ("Elsevier analysis finished.",Eindexed_count,"corrected in json and",len(Enew_journals),"new journals added.")
