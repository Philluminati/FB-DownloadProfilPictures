#!/usr/bin/python
import urllib
import re
import json

# Open a file
fo = open("data.html", "r+")
str = fo.read();

#int1 = str.find('InitialChatFriendsList",[],{groups:[],list:[')
int1 = str.find('list:[')   # Findet die Position im Dokument wo die ID Freundesliste beginnt

int1 += 6                   # Weil sonst "list:[" auch noch in der Liste dabei ist die wir einlesen
int2 = str.find('],shortProfiles')



# Calc how many char. for reading
new = int2-int1

#Read in the ID's from the html file
fo.seek(int1, 0);           #Spring an die Postion der Variable int1
data = fo.read(new);        # String wo die ID's gespeichert sind

splitdata = data.split("\",\"")         # Auslesen der ID's aus den json format


friends = len(splitdata)/2  #Anzahl der Freunde
listAnz = len(splitdata)    #Anzahl der Elemente in der Liste


IDs = []

for i in range(0, listAnz): # start, stop

    id, check = splitdata[i].split("-")
    if check is "2":
        IDs.append(id)



print(IDs)

AnzIDs = len(IDs)

abgleich = -1
print(abgleich)

downloadlist = []

for i in range(0, AnzIDs): # start, stop
    #print("%s: %s  " % (i, newlist[i]))
    url = "https://graph.facebook.com/" + IDs[i] + "?fields=picture.width(720).height(720)"
    print(AnzIDs - i)
    response = urllib.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    search = "error"
    check = text.find(search)  # search the term "error"
                                # Wenn nichts gefunden wird check=-1
    if check is abgleich:
        resp_dict = json.loads(text)
        mitgabe = "" + resp_dict['picture']['data']['url'] + "#" + IDs[i] + ""
        downloadlist.append(mitgabe)





downlen = len(downloadlist)

Fehler = friends - downlen
print("Fehler: %s  " % (Fehler))

for i in range(0, downlen): # start, stop
    print(downloadlist[i])
    url, id = downloadlist[i].split("#")

    urllib.urlretrieve(url, "" + id + ".jpg")



# Close opend file
fo.close()
