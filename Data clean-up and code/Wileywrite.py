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


def issn_conv(x): #converting issn to list format
    if len(x) > 10: #If too long to be an ISSN
        return ""
    else:
        try:
            return [x]
        except:
            return ""

Wcount = 0
Wlist = list()

#opening W file and reading it
with open('Wiley2018csv.csv', newline='', encoding="ISO-8859-1") as myFile:
    Wdata = csv.reader(myFile)
    for Witem in Wdata:
        Wcount = Wcount + 1
        if Wcount == 1: continue #Skipping the first line that has the headings
        #if Wcount > 20: break
        if len(Witem) < 1:continue
        Wdict = { #Adding data from E file into dictionary
            "issn": grab(Witem[0]),
            "journal_title": grab(Witem[1]) ,
            "publisher": "Wiley",
            "oa_type": grab(Witem[2]),
            "last_update": "25/1/2017",
            "apc_price": grab(Witem[4]),
            "apc": grab(apc_existence(Witem[4])),
            "currency": grab(Witem[3]),
            "source_of_apc": "Wiley Price List"
            }

        Wlist.append(Wdict) #adding each dictionary of a journal to a list

APCprices = open('JSONtest4')

json_data = json.load(APCprices)

Windexed_count = 0
Wnew_journals = list()

for Witem in Wlist: #looping through E journal list
    issn_match = False
    title_match = False
    for j in json_data: #looping through JSON journal list to compare it to E journals
        if issn_match == True or title_match == True: continue #SO no duplicate matches
        for issn in j['issn']: #Checking ISSN matches they are in a list in the json file so need to go through in loop
            if Witem["issn"] == issn:
                issn_match = True
                j["journal_title"] = Witem["journal_title"] #if ISSN match making sure journal title is offical listed E title
        if issn_match == False: #If ISSN already matches, no need to match by title
            if Witem["journal_title"] == j["journal_title"]: #checking title match
                title_match = True
                j['issn'].append(Witem["issn"]) #Adding E issn that is not already in json file

        if issn_match == True or title_match == True: #If journal is already in JSON, corrected details so has update E information
            j["publisher"] = Witem["publisher"]
            j["oa_type"] = Witem["last_update"] #Leaving oa type the same because Wiley doesn't state if journal is hybrid or gold
            j["last_update"] = Witem["oa_type"]
            j["apc_price"] = Witem["apc_price"]
            j["apc"] = Witem["apc"]
            j["currency"] = Witem["currency"]
            j["source_of_apc"] = Witem["source_of_apc"]

            Windexed_count = Windexed_count + 1 #Keeping track of how many journals have been corrected
            #print ("Journal corrected")

    if issn_match != True and title_match != True:#Adding new journals not already in json to a list to add to json file at the end.
        Wnew_journals.append(Witem)


for journal in Wnew_journals: #adding new journals from the list to the json file
    journal["issn"] = issn_conv(journal["issn"]) #converting issn to list for new journals
    json_data.append(journal)

#print (json_data[0:5])

with open('JSONtest4', 'w') as outfile: #writing file as a JSON file
    json.dump(json_data, outfile)

print ("WIley analysis finished.",Windexed_count,"corrected in json and",len(Wnew_journals),"new journals added.")
