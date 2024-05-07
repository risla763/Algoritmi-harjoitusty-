import os
import re

class IgnoreSpecialMarks:

    def __init__(self):
        self.final_data = []

    def parse_songs(self,songs_list):
        for song in songs_list:
            parsed = self.am_data(song)
            self.final_data.append(parsed)
        return self.final_data

    def am_data(self, song):
        test_song = song
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
                #print(filtered_song4)
            else:
                print(f"File '{test_song}' not found.")

        filtered_song5 = []
        for i in filtered_song4:
            filtered_song5.append(i)
        #print(filtered_song5)
        return NumericalNotes().match_note_to_a_number(0,0,[],filtered_song5)

class NumericalNotes:

    def __init__(self):
        self.mapping = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7,
            'c': 11, 'd': 12, 'e': 13, 'f': 14, 'g': 15, 'a': 16, 'b': 17,
        }

    def match_note_to_a_number(self, note, index, lista,filtered_song5):
        for index, note in enumerate(filtered_song5):
            #print("nuotti", note)
            #print("indexi", index)
            if note == '^':
                    #kutsuu ylennys metodia
                    self.next_note_is_sharp(filtered_song5,note, index, lista)
            elif note == '_':
                    #kutsuu alennus metodia
                    self.next_note_is_flat(filtered_song5,note, index, lista)
            elif note == '=':
                    #kutsuu palautus metodia
                    self.next_note_is_returned(filtered_song5,note, index, lista)
            elif note == "'":
                    #jos nuotti on kolmannessa oktaavissa
                    self.previous_note_is_in_third_oktave(filtered_song5,note, index, lista)
            elif note == '(' or note == ')': #ignooraa nämä
                    continue
            elif note == '\n': #ignooraa
                    continue
            elif note == ':':  # biisin alku
                    continue
            elif note == ']':  # biisin loppu
                    continue
            elif note == 'I':  # ignooraa
                    continue
            else:
                    #perus nuotti eli iso kirjain tai pieni kirjain
                    note = self.mapping.get(note, 0)
                    lista.append(note) #lisää perus nuotti listaan
        #TAI TÄHÄN VOI TULLA LISTA ADD TO TRIE
        return lista #tulee palauttaa final_datan 


    def previous_note_is_in_third_oktave(self,filtered_song5,note, index, lista):
        lista[index-1] += 20 #muuta edellinen nuotti + 20 (suoraan listassa)
        index += 1 #seuraava indexi
        self.match_note_to_a_number(note,index,lista)


    def next_note_is_sharp(self,filtered_song5,note, index, lista):
       # print("tässä indexi," ,index)
        note = filtered_song5[index+1] #seuraava nuotti ^merkin jälkeen
        extra_case_value = 100 #seuraava nuotti on nuotti + 100 koska ylennys
        self.match_note_to_a_number_in_list(note,index,extra_case_value,lista, filtered_song5)

    def next_note_is_flat(self,filtered_song5,note, index, lista):
        note = filtered_song5[index+1] #seuraava nuotti _merkin jälkeen
        extra_case_value = 200 #seuraava nuotti on nuotti + 200 koska alennus
        self.match_note_to_a_number_in_list(note,index,extra_case_value,lista, filtered_song5)

    def next_note_is_returned(self, filtered_song5,note, index, lista):
        #print(index)
        #print(note)
        note = filtered_song5[index+1] #seuraava nuotti = merkin jälkeen
        extra_case_value = 0 #seuraava nuotti on nuotti + 0 koska palautettu eli mitään ei tapahdu
        self.match_note_to_a_number_in_list(note,index,extra_case_value,lista, filtered_song5)

    def match_note_to_a_number_in_list(self,note,index,extra_case_value,lista, filtered_song5):
        note = self.mapping.get(note, 0) #hakee seuraavan nuotin arvon
        note + extra_case_value
        lista.append(note) #lopullinen lista jossa numerot
        index += 2 #indexi hyppää erikoismerkin ja sitä seuraavan nuotin yli
        note = filtered_song5[index] #seuraava nuotti






