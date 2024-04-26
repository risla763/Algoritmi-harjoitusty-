import random
from algorithms.trie_data_structure import Trie
from algorithms.parse_abc_notation import IgnoreSpecialMarks

import random

class MarkovChain:
    def __init__(self):
        self.trie = Trie()
        self.numerical_data = IgnoreSpecialMarks()



    def start(self):
        #If you want to generate new song press 1
        #If you want to listen generated songs press 2
        #If you want to 
        print("If you want to generate music press 1")
        print("If you want to listen songs you have generated press 2")
        print("If you want to alter the data you need to generate music press 3")
        user_input = int(input("Your input: ")) 
        while True:
            number_of_songs = input("How many songs do you want the data to consist of: ")
            if number_of_songs.isdigit() and int(number_of_songs) > 0:
                number_of_songs = int(number_of_songs)
                break
            else:
                print("Please enter a valid number greater than 0.") #raise error not print
        print("You can choose for example: src/data/HavaNagila.abc")
        list_of_songs = []
        for i in range(number_of_songs):
            #tähän lista biisejä
            song = input("Choose one song from songs:")
            if song == "3":
                song = "src/data/HavaNagila.abc"
                list_of_songs.append(song)
            if song == "2":
                song = "src/data/The_Musical_Priest.abc"
                list_of_songs.append(song)
            if song == "1":
                song = "src/data/Catherine_Ogie.abc"
                list_of_songs.append(song)
            if song == "4":
                song = "src/data/Bung_your_eyes.abc"
                list_of_songs.append(song)
            
        notes_data = self.numerical_data.parse_songs(list_of_songs)
        #tässä kutsutaan omaa luokkaansa, joka kutsuu parse_abc_notation josta saadaan lista dataa
        print("TÄRKEIN ATM", notes_data)
        self.choose_degree(notes_data)

    def choose_degree(self, notes_data):
        degree = input("Choose degree:")
        #print(notes_data)
        #print("TÄSSÄ ASTE", degree)
        self.add_data_to_trie(notes_data,degree) #tätä pitää muokata
        self.choose_lenght(degree)

    def choose_lenght(self, degree):
        lenght = input("Choose lenght:")
        #käyttäjä valitsee pituuden
        self.generate_music(lenght,degree)

    def add_data_to_trie(self, notes_data, degree): #!!!tähän vielä pitää tulla se miten dataa lisätään kun 2000 eli biisin loppu??
        for song in notes_data:
            for i in range(len(song)-1):
                print(i,"lol", degree)
                if i < len(song) -int(degree) :
                    print(song[i:i+int(degree)+1], "tää setti triehen")
                    #print("kolmen setti joka laitetaan",notes_data[i:i+int(degree)]) NÄMÄ KOLME KERRALLAAN SEARCHIIN
                    self.trie.insert(song[i:i+int(degree)+1]) #tässä Triehen lisättäisiin datasta asteen pituisia pätkiä
                else:
                    break

    def generate_music(self, length, degree):
        song = []
        print(list(self.trie.root.children.values()))
        first_note = random.choice(list(self.trie.root.children.values())) #TOIMII
        too_short_for_degree = True
        current = first_note
        song.append(current.note)
        i = 0
        j = 1
        while too_short_for_degree: #tässä siihen asti että biisissä asteen verran nuotteja
            #KOKEILU 1
            #search kutsu tyhjällä pitäisi palauttaa juuren, 1 nuotti pitäisi palauttaa h nuotin lapset
            #loppuu liian aikasin jos lapsia
            #
            notes_data_that_search = song[i:j] #EKALLA NUOTILLA ETITÄÄN
            print("TÄSSÄ NOTES_DATA",notes_data_that_search )
            data_for_generating_next = self.trie.search(notes_data_that_search)
            j += 1
            length = int(length) -1
            if data_for_generating_next is None or data_for_generating_next is ([], []):
                next_note = random.choice(list(self.trie.root.children.values())) #ekalla solmulla ei lapsia
                song.append(next_note.note)
                print(next_note, "randomilla")
            else:
                if data_for_generating_next[1]: 
                    next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
                    print(next_note, "painojen kanssa")
                    song.append(next_note)
                elif data_for_generating_next[0]:
                    next_note = random.choice(data_for_generating_next[0]) #TÄSSÄ VALITSEE SEURAAVAN ILMAN PAINOJA
                    print(next_note)
                    song.append(next_note)
                    print(next_note, "ilman painoja")
                else:
                    next_note = random.choice(list(self.trie.root.children.values())) # Fallback to root children if no valid next notes found
                    song.append(next_note.note)
            if len(song) >= int(degree):
                too_short_for_degree = False
                print("nyt tarpeeksi dataa biisissä", length)
        #nyt siinä on kaks

        #KOKEILU LOPPUU
 
        for i in range(int(length) -1): 
            notes_data_that_search = song[len(song) - int(degree): len(song)] #-3 vikaa tai -4 vikaa #-degree
            data_for_generating_next = self.trie.search(notes_data_that_search)
            if data_for_generating_next == None:
                break #JA SE PIKKEUS ETTÄ EI OLE LAPSIA LAITA NONE JA BIISIN GENEROIMINEN LOPPUU RAISE ERROR
            #tai alkaa uutta generoimaan jos tällainen tilanne ja yrittää vaikka 100 kertaa
            else:
                next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
                print(next_note)
                song.append(next_note)
        print("LOPULLINEN TUOTOS", song)
        #self.testi(length, degree)

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
        #ylempänä oleva looppi tähän

        
#s 
#onko pituus korkeempi kuin aste
#sh 
#onko pituus isompi kuin aste

#shko

#if lause kattoo jos hakusana on liian pitkä
#niin eka pois ja vikat asteen verran mukana






    def _get_next_note(self, current_notes):
        possible_next_notes = self.trie.search(current_notes) 
        if possible_next_notes:
            total_weight = sum(possible_next_notes.values())
            rand_val = random.uniform(0, total_weight)
            weight = 0
            for note, weight in possible_next_notes.items():
                weight += weight
                if rand_val <= weight:
                    return note
        else:
            return None






