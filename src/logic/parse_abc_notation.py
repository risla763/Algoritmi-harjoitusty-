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
                #print(sisalto)
                #filtered_song = sisalto.replace('|','')
                filtered_song2 =  re.sub(r'\d','', sisalto) #numerot pois
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
        print(filtered_song5)
        return NumericalNotes().match_note_to_a_number(0,0,[],filtered_song5,0)

class NumericalNotes:

    def __init__(self):
        self.mapping = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7,
            'c': 11, 'd': 12, 'e': 13, 'f': 14, 'g': 15, 'a': 16, 'b': 17,
        }
        self.lista = []
        self.previous = 0
        self.third_octave = False
        self.flat = False
        self.skip = False

    def match_note_to_a_number(self, note, note_index, lista,filtered_song5, previous):
        sharp = False
        flat = False
        for note_index, note in enumerate(filtered_song5):
            self.skip = False
            print("nuotti", note)
            #print("indexi", note_index)
            #print("tää index homma", filtered_song5[note_index-1]) #oikein
            if filtered_song5[note_index-2] == '_' or filtered_song5[note_index-2] == '^':
                self.skip = True
            elif filtered_song5[note_index-1] == '^':
                continue #jos edellinen oli ylennys
            #if filtered_song5[note_index-1] == '_':
               # continue
            if note == '^':
                    #kutsuu ylennys metodia
                    sharp = True
                    self.next_note_is_sharp(filtered_song5,note, note_index, lista, previous)
            elif note == '_':
                    #kutsuu alennus metodia
                    self.flat = True
                    self.next_note_is_flat(filtered_song5,note, note_index, lista, previous)
            #elif note == '=':
                    #kutsuu palautus metodia
                    #self.next_note_is_returned(filtered_song5,note, note_index, lista)
            elif note == "'":
                    #jos nuotti on kolmannessa oktaavissa
                    self.third_octave = True
                    self.previous_note_is_in_third_oktave(filtered_song5,note, note_index, lista, previous)
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
            elif note == '<':  # ignooraa
                    continue
            elif note == '>':  # ignooraa
                    continue
            elif note == '=':  # ignooraa
                    sharp = False
                    flat = False
                    continue
            elif note == '|':
                    sharp = False
                    flat = False
                    self.previous = 0
                    continue
            else:
                note = self.mapping.get(note)
                #if note+100 == self.previous and sharp == True and note != None:
                   # note = note + 100
                   # self.lista.append(note) 
                if note is not None and self.skip != True:
                    self.lista.append(note) 
                   # print("Jiii")#lisää perus nuotti listaan
                #elif note+200 == self.previous and flat == True:
                   # note = note + 200
                   # self.lista.append(note) 

        return self.lista


    def previous_note_is_in_third_oktave(self,filtered_song5,note, note_index, lista, previous):
        new_note = self.lista[-1]
        self.lista.pop()
        new_note = new_note + 10
        self.lista.append(new_note)
        note_index += 1
        self.third_octave = False


    def next_note_is_sharp(self,filtered_song5,note, note_index, lista, previous):
       # print("tässä indexi," ,note_index) VANHA
        note = filtered_song5[note_index+1] #seuraava nuotti ^merkin jälkeen #VANHA
        extra_case_value = 100 #seuraava nuotti on nuotti + 100 koska ylennys
        self.match_note_to_a_number_in_list(note,note_index,extra_case_value,lista, filtered_song5, previous)

    def next_note_is_flat(self,filtered_song5,note, note_index, lista, previous):
        print("Meni tännee", filtered_song5[note_index+1])
        note = filtered_song5[note_index+1] #seuraava nuotti ^merkin jälkeen #VANHA
        extra_case_value = 200 #seuraava nuotti on nuotti + 100 koska ylennys
        self.match_note_to_a_number_in_list(note,note_index,extra_case_value,lista, filtered_song5, previous)

    def next_note_is_returned(self, filtered_song5,note, note_index, lista, previous):
        #print(note_index)
        #print(note)
        note = filtered_song5[note_index+1] #seuraava nuotti = merkin jälkeen
        extra_case_value = 0 #seuraava nuotti on nuotti + 0 koska palautettu eli mitään ei tapahdu
        self.match_note_to_a_number_in_list(note,note_index,extra_case_value,lista, filtered_song5, previous)

    def match_note_to_a_number_in_list(self,note,note_index,extra_case_value,lista, filtered_song5, previous):
        note = self.mapping.get(note) #hakee seuraavan nuotin arvon
        print("no mikäs",note)
        if note is not None:
            note += extra_case_value
            print("no mikäs",note)
            self.lista.append(note) 
            self.previous = note
        note_index += 2 #indexi hyppää erikoismerkin yli ja sitä seuraavan nuotin yli seuraavaan nuottiin 
        if note_index < len(filtered_song5):
            note = filtered_song5[note_index]
        return note, note_index 