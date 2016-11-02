#!/usr/bin/python
import urllib
import re
import json

# Open a file
fo = open("data.html", "r+")
str = fo.read();

int1 = str.find('InitialChatFriendsList",[],{groups:[],list:[')
int1 += 45
int2 = str.find('],shortProfiles')


# Calc how many char. for reading
new = int2-int1

#Read in the ID's from the html file
fo.seek(int1, 0);
data = fo.read(new);


splitdata = data.split("\",\"")
friends = len(splitdata)/2
zinger = len(splitdata)

newlist = []

for i in range(0, zinger): # start, stop

    id, check = splitdata[i].split("-")
    if check is "2":
        newlist.append(id)
        

zingerNew = len(newlist)
abgleich = -1
print(abgleich)

downloadlist = []

for i in range(0, zingerNew): # start, stop
    #print("%s: %s  " % (i, newlist[i]))
    url = "https://graph.facebook.com/" + newlist[i] + "?fields=picture.width(720).height(720)"
    print(zingerNew - i)
    response = urllib.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    search = "error"
    check = text.find(search)
    if check is abgleich:
        resp_dict = json.loads(text)
        mitgabe = "" + resp_dict['picture']['data']['url'] + "#" + newlist[i] + ""
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
