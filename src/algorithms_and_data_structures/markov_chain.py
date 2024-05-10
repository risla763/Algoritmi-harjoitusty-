import random
from algorithms_and_data_structures.trie_data_structure import Trie
from logic.parse_abc_notation import IgnoreSpecialMarks
from logic.convert_data_to_abc import ConvertToAbc

import random

class MarkovChain:
    def __init__(self):
        self.trie = Trie()
        self.numerical_data = IgnoreSpecialMarks()
        self.abc_converter = ConvertToAbc()
        self.dict_of_songs = {}



    def start(self):
        print("If you want to generate music press 1")
        print("If you want to listen songs you have generated press 2")
        user_input = int(input("Your input: ")) 
        while True:
            number_of_songs = input("How many songs do you want the data to consist of: ")
            if number_of_songs.isdigit() and int(number_of_songs) > 0:
                number_of_songs = int(number_of_songs)
                break
            else:
                print("Please enter a valid number greater than 0.")
        print("select the songs by writing the number next to it one by one")
        print("Songs:")
        print("The Musical Priest 1")
        print("Bung your eyes 2")
        print("Catherine Ogie 3")
        print("Hava Nagila 4")
        print("Rasputin 5")
        print("Ievan Polka 6")
        print("Taivas on sininen ja valkoinen 7")
        print("Lost my love 8")
        print("Krepatka 9")
        print("The Bear Dance 10")
        print("Sininen ja valkoinen 11")
        list_of_songs = []
        for i in range(number_of_songs):
            song = input("choose the songs you want the song to consist of:")
            if song == "4":
                song = "data/HavaNagila.abc"
                list_of_songs.append(song)
            if song == "1":
                song = "data/The_Musical_Priest.abc"
                list_of_songs.append(song)
            if song == "3":
                song = "data/Catherine_Ogie.abc"
                list_of_songs.append(song)
            if song == "2":
                song = "data/Bung_your_eyes.abc"
                list_of_songs.append(song)
            if song == "5":
                song = "data/Rasputin.abc"
                list_of_songs.append(song)
            if song == "6":
                song = "data/Ievan_polka.abc"
                list_of_songs.append(song)
            if song == "7":
                song = "data/Taivas_on_sininen_ja_valkoinen.abc"
                list_of_songs.append(song)
            if song == "8":
                song = "data/Lost_my_love.abc"
                list_of_songs.append(song)
            if song == "9":
                song = "data/Krepatka.abc"
                list_of_songs.append(song)
            if song == "10":
                song = "data/The_bear_dance.abc"
                list_of_songs.append(song)
            if song == "11":
                song = "data/Sininen_ja_valkoinen.abc"
                list_of_songs.append(song)
        notes_data = self.numerical_data.parse_songs(list_of_songs)
        self.choose_degree(notes_data)


    def choose_degree(self, notes_data):
        degree = input("Choose degree:")
        #print("Tässä data josta generoidaan biisi:",notes_data)
        #print("TÄSSÄ ASTE", degree)
        self.add_data_to_trie(notes_data,degree)
        self.choose_lenght(degree, notes_data)

    def choose_lenght(self, degree, notes_data):
        lenght = input("Choose lenght:")
        #käyttäjä valitsee pituuden
        self.generate_music(lenght,degree, notes_data)

    def add_data_to_trie(self, notes_data, degree): #!!!tähän vielä pitää tulla se miten dataa lisätään kun 2000 eli biisin loppu??
        print("data", notes_data)
        for song in notes_data:
            for i in range(len(song)-1):
                if i < len(song) -int(degree) :
                    #print(song[i:i+int(degree)+1], "tää setti triehen")
                    self.trie.insert(song[i:i+int(degree)+1]) #tässä Triehen lisättäisiin datasta asteen pituisia pätkiä
                else:
                    break

    def generate_music(self, length, degree, notes_data):
        song = []
        #print(list(self.trie.root.children.values()))
        first_note = random.choice(list(self.trie.root.children.values())) #TOIMII
        too_short_for_degree = True
        current = first_note
        song.append(current.note)
        i = 0
        j = 1
        while too_short_for_degree: #tässä siihen asti että biisissä asteen verran nuotteja
            #KOKEILU 1
            notes_data_that_search = song[i:j]
            #print("TÄSSÄ NOTES_DATA",notes_data_that_search )
            data_for_generating_next = self.trie.search(notes_data_that_search)
            j += 1
            length = int(length) -1
            if data_for_generating_next is None or data_for_generating_next is ([], []):
                next_note = random.choice(list(self.trie.root.children.values())) #ekalla solmulla ei lapsia
                song.append(next_note.note)
                #print(next_note, "randomilla")
            else:
                if data_for_generating_next[1]: 
                    next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
                    #print(next_note, "painojen kanssa")
                    song.append(next_note)
                elif data_for_generating_next[0]:
                    next_note = random.choice(data_for_generating_next[0]) #TÄSSÄ VALITSEE SEURAAVAN ILMAN PAINOJA
                    #print(next_note)
                    song.append(next_note)
                    #print(next_note, "ilman painoja")
                else:
                    next_note = random.choice(list(self.trie.root.children.values())) # Fallback to root children if no valid next notes found
                    song.append(next_note.note)
            if len(song) >= int(degree):
                too_short_for_degree = False
                #print("nyt tarpeeksi dataa biisissä", length)
        #KOKEILU LOPPUU
 
        for i in range(int(length) -1): 
            notes_data_that_search = song[len(song) - int(degree): len(song)] #-3 vikaa tai -4 vikaa #-degree
            data_for_generating_next = self.trie.search(notes_data_that_search)
            if data_for_generating_next == None:
                break
            else:
                next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
                #print(next_note)
                song.append(next_note)
        song = self.abc_converter.convert_numbers_to_notes(song)
        print("Generated song", song)
        self.choose_next_step(song)

    def choose_next_step(self, song):
        running = True
        while running:
            print(running, "mikä arvo")
            print("1 = play the song, 2 = save the song, 3 = generate new song with old data/go back to start")
            print("4 = exit, 5 = make song from new data, 6 = see the list of songs")
            user_input = input("Type a number:")
            if user_input == "2":
                key = input("Name of the song:")
                self.dict_of_songs[key] = song
            elif user_input == "1":
                self.player.play_note(song) #tässä ongelma jos painaa ei heti exit the program
            elif user_input == "3":
                self.choose_degree(notes_data)
            elif user_input == "4":
                running = False
                print("Exiting the program")
                break
            elif user_input == "5":
                self.start()
            elif user_input == "6":
                print(self.dict_of_songs)


        return song
            #play old song vielä myös
        #self.testi(length, degree)











#TÄSSÄ ALLA TOINEN VERSIO
    def testi(self, length, degree):
        length = int(length)
        songg = []
        print(list(self.trie.root.children.values()), "tässä")
        first_note = random.choice(list(self.trie.root.children.values())) #TOIMII
        current = first_note
        songg.append(current.note)
        too_little_notes_for_degree = True
        for i in range(length-1):
            while True:
                data_for_generating_next = self.trie.search(songg)
                songg.append(current.note)
                print(data_for_generating_next)
                length = length - 1
                if len(songg) == degree:
                    too_little_notes_for_degree = False
            notes_data_that_search = song[len(songg) - int(degree): len(songg)] #-3 vikaa tai -4 vikaa #-degree
            data_for_generating_next = self.trie.search(notes_data_that_search)
            if data_for_generating_next == None:
                break #JA SE PIKKEUS ETTÄ EI OLE LAPSIA LAITA NONE JA BIISIN GENEROIMINEN LOPPUU RAISE ERROR
                #tai alkaa uutta generoimaan jos tällainen tilanne ja yrittää vaikka 100 kertaa
            else:
                next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
                print(next_note)
                song.append(next_note)
        print("LOPULLINEN TUOTOS 2", songg)
        running = True
        while running:
            print("1 = play the song, 2 = save the song, 3 = generate new song with old data/go back to start")
            print("4 = exit, 5 = make song from new data, 6 = see the list of songs")
            user_input = input("Your input:")
            if user_input == "2":
                key = input("Give your song a name:")
                self.dict_of_songs[key] = songg #TÄSSÄ LISTASSA BIISIT
            elif user_input == "1":
                self.player.play_note(songg)
            elif user_input == "3":
                MarkovChain().choose_degree()
            elif user_input == "4":
                runninhg = False
                break
            elif user_input == "5":
                MarkovChain().start()


        #ylempänä oleva looppi tähän





