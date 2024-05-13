import random
from algorithms_and_data_structures.trie_data_structure import Trie
from logic.parse_abc_notation import IgnoreSpecialMarks
from logic.convert_data_to_abc import ConvertToAbc

import random

class MarkovChain:
    """
    Tässä algoritmi, jolla generoidaan musiikkia.
    """
    def __init__(self):
        self.trie = Trie()
        self.numerical_data = IgnoreSpecialMarks()
        self.abc_converter = ConvertToAbc()
        self.dict_of_songs = {}
        self.running = True



    def start(self):
        print("Generate music from data by folowing the steps below")
        while True:
            number_of_songs = input("How many songs do you want the data to consist of (max 11 and min 1): ")
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
        choose_degree = True
        while choose_degree:
            degree = input("Choose degree (1-10):")
            if degree.isdigit():
                degree = int(degree)
                if 1 <= degree <= 10:
                    choose_degree = False
                    self.add_data_to_trie(notes_data,degree)
                    self.choose_lenght(degree, notes_data)
                else:
                    print("Please enter a valid degree.")

    def choose_lenght(self, degree, notes_data):
        choose_length = Trie
        while choose_length:
            length = input("Choose length (2-70): ")
            if length.isdigit():
                length = int(length)
                if 2 <= length <= 70:
                    choose_length = False
                    self.generate_music(length,degree, notes_data)
                else:
                    print("Please enter a number between 1 and 40.")
            else:
                print("Please enter a valid number.")

    def add_data_to_trie(self, notes_data, degree):
        for song in notes_data:
            for i in range(len(song)-1):
                if i < len(song) -int(degree) :
                    self.trie.insert(song[i:i+int(degree)+1])
                else:
                    break

    def generate_music(self, length, degree, notes_data):
        song = []
        first_note = random.choice(list(self.trie.root.children.values()))
        too_short_for_degree = True
        current = first_note
        song.append(current.note)
        i = 0
        j = 1
        while too_short_for_degree:
            notes_data_that_search = song[i:j]
            data_for_generating_next = self.trie.search(notes_data_that_search)
            j += 1
            length = int(length) -1
            if data_for_generating_next is None or data_for_generating_next is ([], []):
                next_note = random.choice(list(self.trie.root.children.values()))
                song.append(next_note.note)
            else:
                if data_for_generating_next[1]: 
                    next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0]
                    song.append(next_note)
                elif data_for_generating_next[0]:
                    next_note = random.choice(data_for_generating_next[0])
                    song.append(next_note)
                else:
                    next_note = random.choice(list(self.trie.root.children.values()))
                    song.append(next_note.note)
            if len(song) >= int(degree):
                too_short_for_degree = False
 
        for i in range(int(length) -1): 
            notes_data_that_search = song[len(song) - int(degree): len(song)]
            data_for_generating_next = self.trie.search(notes_data_that_search)
            if data_for_generating_next == None:
                break
            else:
                next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0]
                song.append(next_note)
        self.abc_converter.numeric_song_list(song)
        song = self.abc_converter.convert_numbers_to_notes(song)
        print("Here is your generated song in abc notation:", song)
        self.choose_next_step(song, notes_data)
        return song

    def choose_next_step(self, song, notes_data):
        while self.running:
            print("1 = save the song, 2 = generate new song with old data")
            print("3 = see the list of songs, 4 = make a new song from new data, 5 = exit")
            user_input = input("Type a number:")
            if user_input == "1":
                key = input("Name of the song:")
                self.dict_of_songs[key] = song
            elif user_input == "2":
                self.choose_degree(notes_data)
            elif user_input == "5":
                self.running = False
                print("Exiting the program")
                continue
            elif user_input == "4":
                self.start()
            elif user_input == "3":
                print(self.dict_of_songs)


        return song