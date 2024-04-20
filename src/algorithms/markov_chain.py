import random
from trie_data_structure import Trie
from parse_abc_notation import IgnoreSpecialMarks

import random

class MarkovChain:
    def __init__(self):
        self.trie = Trie()
        self.numerical_data = IgnoreSpecialMarks()



    def choose_key(self):
        key = input("Choose key:")
        if key == "am":
            notes_data = self.numerical_data.am_data()
        #tässä kutsutaan omaa luokkaansa, joka kutsuu parse_abc_notation josta saadaan lista dataa
        self.choose_degree(notes_data)

    def choose_degree(self, notes_data):
        degree = input("Choose degree:")
        print(notes_data)
        print("TÄSSÄ ASTE", degree)
        self.add_data_to_trie(notes_data,degree)
        self.choose_lenght(degree)

    def choose_lenght(self, degree):
        lenght = input("Choose lenght:")
        #käyttäjä valitsee pituuden
        self.generate_music(lenght,degree)

    def add_data_to_trie(self, notes_data, degree): #tähän vielä pitää tulla se miten dataa lisätään kun 2000 eli biisin loppu??
        for i in range(len(notes_data)-1):
            print(i,"lol", degree)
            if i < len(notes_data) -1 :
                self.trie.insert(notes_data[i:i+int(degree)]) #tässä Triehen lisättäisiin datasta asteen pituisia pätkiä
            else:
                break

    def generate_music(self, length, degree):
        print(self.trie.print_trie())
        print(self.trie.search("3"))
        result = self.trie.search("3")
        if result:
            list_of_keys, list_of_frequencies = result
            total_weight = sum(list_of_frequencies)
            print(f"Total weight: {total_weight}")
            if total_weight > 0:
                rand_val = random.uniform(0, total_weight)
                weight = 0
                for note, freq in zip(list_of_keys, list_of_frequencies):
                    weight += freq
                    if rand_val <= weight:
                        print(f"Selected note: {note}")
                        break
        else:
            print("No notes found.")
        #print(self.trie.print_trie())
        print(self.trie.search("3"), "testi")
        print(list(self.trie.root.children.values()))
        first_note = random.choice(list(self.trie.root.children.values()))
        print(f"Eka nuotti {first_note.note}")






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





markov_chain = MarkovChain()
markov_chain.choose_key()
#current_notes tulee Trie 

