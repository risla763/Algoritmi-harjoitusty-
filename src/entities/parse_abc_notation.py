import os
import re
test_song = "src/data/HavaNagila.abc"
file = os.path.join(test_song)
with open(file) as file:
    if os.path.exists(test_song):
        sisalto = file.read()
        print(sisalto)
        filtered_song = sisalto.replace('|','')
        filtered_song2 =  re.sub(r'\d','', filtered_song) #numerot pois
        filtered_song3 = re.sub(r'(?m)^[wXTOZNMLK]:[^\n]*\n','',filtered_song2)
        filtered_song4 = re.sub(r'"(?:E|Dm)"\s*:','',filtered_song3)
        filtered_song4 =  re.sub(r'"[CDEFAB]"','', filtered_song4) 
        filtered_song4 = re.sub(r'"[A-Z]m"', '', filtered_song4)
        filtered_song4 = re.sub(r'w:[^\n]*?[\.\n]\n?','', filtered_song4)
        filtered_song4 = filtered_song4.replace('/','')
        filtered_song4 = filtered_song4.replace('>','')
        filtered_song4 = filtered_song4.replace(' ','')
        print(filtered_song4)
    else:
        print(f"File '{test_song}' not found.")

list = []
for i in filtered_song4:
    list.append(i)
print(list)

for i in filtered_song4: #tämä on kesken ja tämän pointti olisi voida muuttaa listassa olevat nuotit numeroiksi ja tehdä uusi lista
    if i == "'": #jos toinen oktaavi esim 'c
        continue
    elif filtered_song4[i+1] == "'": #jos toinen oktaavi ja nuotti!
        if filtered_song4[i-1] == "^": #ylennetty tokan oktaavin nuotti
            i = ord(i) + 200
        elif filtered_song4[i-1] == "_": #alennettu tokan oktaavin nuotti
            i = ord(i) + 200 + 200
        else:                   #normi tokan oktaavin nuotti
            i = ord(i) + 200 + 300
    elif i is char.isupper():
        if filtered_song4[i-1] == "^": #ylennetty alemman oktaavin nuotti
            i = ord(i) -200
        elif filtered_song4[i-1] == "_": #alennettu tokan oktaavin nuotti
            i = ord(i) - 200 - 200
        else:                   #normi alennetun oktaavin nuotti
            i = ord(i) - 200 - 300 #jos yksi oktaavi alempana
    elif i == '(' or ')' or '/n': #turhaa karsitaan
        break
    elif i == "^": #ylennys
        continue
    elif filtered_song4[i-1] == "^": #ylennyksestä nuotti
        i = ord(i) + 100
    elif filtered_song4[i-1] == "_": #ylennyksestä nuotti
        i = ord(i) - 100
    elif i == ':': #laulun alku
        i = 1000
    elif i == ']': #laulun loppu
        i = 2000
    else:           #normi nuotti
        i = ord(i)
        
    #ylennys,alennus,palutus merkit yhteen alkioon, suluissa oleva pois,
    #  : biisin aloitus yhdessä alkiossa, ] biisin lopetus yhdessä alkiossa
    # jos on /n älä lisää
    list.append(i)
print(list)

#^ylennys
#_ alennus
#= palautus
#


#funktio, joka muuttaa abc notaation listaksi 
#ohjelma käy listaa läpiS
#looppaa

#trie kaks metodia 1. tallettaa 1 sekvenssin
#2. saa parametrina yhden sekvenssin ja palauttaa seuraajat ja sekvenssit


#tai tuple 

#trie olion metodi talletetaan
#trieolio 56 mittanen lista alussa täynnä nollia
#ja kun sävelelle 1 esim löytää seuraaja siihen tulee linkki

#trie solmuolio 
#-0..60 sävelet listassa


#replace!
#separator


