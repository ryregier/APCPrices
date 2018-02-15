#OAPC analysis finished. 16 corrected in json and 746 new journals added.
import json
import re


data = open('JSONtest5')
APC_Prices = json.load(data)

data1 = open('OAPCJSON')
OAPC_data = json.load(data1)

Windexed_count = 0
Wnew_journals = list()

for Witem in OAPC_data: #looping through E journal list
    issn_match = False
    title_match = False
    issn_list = list()
    for j in APC_Prices: #looping through JSON journal list to compare it to E journals
        if issn_match == True or title_match == True: continue #SO no duplicate matches

        for issn in Witem['issn']: #Comparing to see if ISSN's in their lists match
            if issn_match == True: break
            for compare_issn in j['issn']:
                if issn == compare_issn:
                    issn_match = True

        if issn_match == False: #If ISSN already matches, no need to match by title
            if Witem["journal_title"] == j["journal_title"]: #checking title match
                title_match = True
                issn_list = Witem['issn'] + j['issn'] #adding ISSN's to one list
                j['issn'] = list(set(issn_list)) #deduping ISSNs and adding them back to json list for that item

        if issn_match == True or title_match == True: #If journal is already in JSON, corrected details so has updated price information
            if j["apc_price"] == "unknown":
                j["apc_price"] = Witem["apc_price"]
                j["apc"] = Witem["apc"]
                #print (Witem["journal_title"])

                Windexed_count = Windexed_count + 1 #Keeping track of how many journals have been corrected
            #print ("Journal corrected")

    if issn_match != True and title_match != True:#Adding new journals not already in json to a list to add to json file at the end.
        Wnew_journals.append(Witem)


for journal in Wnew_journals: #adding new journals from the list to the json file
    APC_Prices.append(journal)

#print (json_data[0:5])

with open('JSONtest5', 'w') as outfile: #writing file as a JSON file
    json.dump(APC_Prices, outfile)

print ("OAPC analysis finished.",Windexed_count,"corrected in json and",len(Wnew_journals),"new journals added.")
