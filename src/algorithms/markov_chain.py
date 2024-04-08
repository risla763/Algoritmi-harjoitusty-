import random
from trie_data_structure import Trie

import random

class MarkovChain:
    def __init__(self, trie, degree: int):
        self.trie = trie
        self.degree = degree
        print("TÄSSÄ ASTE", degree)

    def generate_sequence(self, length=10): #length = biisin pituus
        sequence = []
        current_notes = [''] * (self.degree - 1)
        print("current_notes", current_notes)

        for _ in range(length):
            next_note = self._get_next_note(current_notes) #NUOTIT parametrina joiden perusteella etsitään 
            sequence.append(next_note) #next_note on note mitä get_next_note palauttaa
            current_notes.pop(0)
            current_notes.append(next_note)

        return sequence

    def _get_next_note(self, current_notes):
        possible_next_notes = self.trie.search(current_notes) #tässä pitäis olla nuotteja eikä ['','']
        if possible_next_notes:
            total_weight = sum(possible_next_notes.values())
            rand_val = random.uniform(0, total_weight)
            cumulative_weight = 0
            for note, weight in possible_next_notes.items():
                cumulative_weight += weight
                if rand_val <= cumulative_weight:
                    return note
        else:
            return None

trie = Trie
markov_chain = MarkovChain(trie, 3)
sequence = markov_chain.generate_sequence(length=20)
print("Generated sequence:", sequence)
