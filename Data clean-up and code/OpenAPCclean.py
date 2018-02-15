import json
import re
import csv

def grab(x): #returning values and returning "unknown" if value error
    if x is False or x == " " or x == "" or x == "NA" or x == []:
        return "unknown"
    else:
        try:
            return x
        except:
            return "unknown"

def oa_conv(x): #returning oa type. Hybrid if 1 and Gold if 0
    if x == "TRUE":
        return "Hybrid"
    elif x == "FALSE":
        return "Gold"
    else:
        return ""

def ISSN_dedup(x,y,a,b): #Adding ISSNs in to a list and getting rid of duplicates
    ISSNlist = list()
    varlist = [x,y,a,b]
    for item in varlist:
        if item == "NA" or item == "": #Not adding any NAs or blanks
            continue
        ISSNlist.append(item)
    #print (ISSNlist)
    ISSNlist = list(set(ISSNlist)) #Removing duplicate ISSNs
    #print (ISSNlist)
    return ISSNlist

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
            float(x)
            return "Yes"
        except:
            return ""


def number(x): #For setting a default date and comparing for new updates
    if x == 'unknown':
        return 1970
    else:
        defaultldate = re.findall('[0-9]+/[0-9]+/([0-9]+)',x)
        return int(defaultldate[0])


OAPCcount = 0
Messy_OAPClist = list()


with open('OpenAPCdata1.csv', newline='',encoding="utf8") as myFile:
    OAPC = csv.reader(myFile)
    for line in OAPC:
        OAPCcount = OAPCcount + 1
        if OAPCcount == 1: continue #skipping first line with headings
        if int(line[1]) < 2015 or int(line[1]) > 2017: continue #Only looking at years 2015-2017
        #print (line)
        #if OAPCcount > 2000 : break
        #if OAPCcount !=10: continue
        Messy_OAPCdict = { #Adding data from E file into dictionary
            "issn": ISSN_dedup(line[7],line[8],line[9],line[10]),
            "journal_title": grab(line[6]) ,
            "publisher": grab(line[5]),
            "oa_type": grab(oa_conv(line[4])),
            "apc_price": float(line[2]),
            "article_count": 1,
            "apc": grab(apc_existence(line[2])),
            'doi': line[3],
            'record': "unused"
            }
        #print (Messy_OAPCdict)
        Messy_OAPClist.append(Messy_OAPCdict)

print(len(Messy_OAPClist))
print ("Pulling journal info....This could take a long time...")

Clean_OPAClist = list()
count = 0

for Mitem in Messy_OAPClist:
    if Mitem['record'] != "unused": continue
    for compare_item in Messy_OAPClist:
        if Mitem == compare_item:
            #print ("skipped")
            continue
        if compare_item['record'] != "unused": continue
        issn_list = list()
        issn_match = False
        title_match = False

        if Mitem["journal_title"]== compare_item["journal_title"]: #comparing to see if journal title's mathces
            title_match == True
            #print (Mitem["journal_title"],compare_item["journal_title"])

        for issn in Mitem['issn']: #Comparing to see if ISSN's in their lists match
            if issn_match == True: break
            for compare_issn in compare_item['issn']:
                if issn == compare_issn:
                    issn_match = True
                    #print (issn,compare_issn)

        if issn_match == True or title_match == True:
            issn_list = Mitem['issn'] + compare_item['issn'] #adding ISSN's too one list and deduping them
            issn_list = list(set(issn_list))

        if issn_match == True or title_match == True:
            Mitem['issn'] = issn_list
            Mitem['apc_price'] = compare_item['apc_price'] + Mitem["apc_price"]
            Mitem["article_count"] = Mitem["article_count"] + 1
            Mitem['record'] = "master"
            #if Mitem["article_count"] > 50: print ("Merged")
            compare_item['record'] = "child" #Setting status to merged so I am not comparing agains same item twice

    print (Mitem["journal_title"], "details pulled and added")

#Clean_OPAClist = Messy_OAPClist

for Mitem in Messy_OAPClist:
    if Mitem['record'] == "master":
        Clean_OAPCdict={
            "issn": Mitem['issn'],
            "journal_title": Mitem["journal_title"],
            "publisher": Mitem["publisher"],
            "oa_type": Mitem["oa_type"],
            "apc_price": int(Mitem["apc_price"]/Mitem["article_count"]),
            "apc": Mitem["apc"],
            "source_of_apc": "Open APC 2015-2017 Average",
            "currency": "EUR",
            "last_update": "10/2/2018"
        }
        Clean_OPAClist.append(Clean_OAPCdict)

with open('OAPCJSON', 'w') as outfile: #writing file as a JSON file
    json.dump(Clean_OPAClist, outfile)

print ("OAPCJSON exported")
print (len(Clean_OPAClist), "items")
