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

    def add_data_to_trie(self, notes_data, degree): #!!!tähän vielä pitää tulla se miten dataa lisätään kun 2000 eli biisin loppu??
        for i in range(len(notes_data)-1):
            #print(i,"lol", degree)
            if i < len(notes_data) -1 :
                #print("kolmen setti joka laitetaan",notes_data[i:i+int(degree)]) NÄMÄ KOLME KERRALLAAN SEARCHIIN
                self.trie.insert(notes_data[i:i+int(degree)]) #tässä Triehen lisättäisiin datasta asteen pituisia pätkiä
            else:
                break

    def generate_music(self, length, degree):
        song = []
        print(list(self.trie.root.children.values()))
        first_note = random.choice(list(self.trie.root.children.values())) #TOIMII
        print(f"Eka nuotti {first_note.note}")
        current = first_note #hyvä...
        song.append(current.note)
        #tähän se että jos degree on x niin x verran niitä lapsia current_nodesta listaan
        for i in range(int(degree)-1): #tässä looppaa listaan degreen verran nuotteja
            next_note = random.choice(list(current.children.values()))
            song.append(next_note.note)
            current = next_note
            print("lol", current.note) #TÄHÄN VIELÄ JOS SOLMULLA EI LAPSIA NIIN SEN EKan nuOTIN PITÄÄ OLLA SOLMU JOLLA DEGREEN VERRAN LAPSIA
        #Tässä oikea markovin ketju voi alkaa
        #TÄHÄN TULEE SEARCH METODI TRIESTÄ
        for i in range(int(length) -1):
            notes_data_that_search = song[-int(degree):-1] #laulun lopusta asteen verran  (aina lisätään 1, joten järjestyksen pitäisi pysyä)
            data_for_generating_next = self.trie.search(notes_data_that_search)
            #ylemmän pitäisi olla tuple nuotteja ja painoja mitä sitten??
            print("data seuraavaan nuotit:",data_for_generating_next[0])
            print("data seuraavaan painot:",data_for_generating_next[1])
            next_note = random.choices(data_for_generating_next[0],data_for_generating_next[1])[0] #TÄSSÄ VALITSEE SEURAAVAN
            print(next_note)
            song.append(next_note)








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

