import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.convert_data_to_abc import ConvertToAbc
from logic.parse_abc_notation import NumericalNotes
class TestMarkovChain(unittest.TestCase):
    """
        Tämä luokka testaa että esiintyykö generoidussa
        kappaleessa olevat sävelkulut/säveljonot myös
        datassa, josta se on generoitu.
    """

    def setUp(self):
        self.markov_chain = MarkovChain()
        self.trie = Trie()
        self.convert = ConvertToAbc()
        self.numeric_data = NumericalNotes()
        self.data = [[3, 3, 5, 3, 5, 105, 7, 6,
         5, 6, 6, 11, 7, 6, 105, 3, 4, 5, 5, 3,
          4, 3, 5, 5, 4, 3, 3, 3, 4, 4, 3, 2, 2, 2, 2,
           4, 3, 2, 2, 6, 5, 3, 4, 5, 5, 3, 4, 3, 6, 11,
            6, 11, 6, 11, 6, 6, 6, 11, 7, 6, 11, 7, 6, 6, 6, 6,
             11, 7, 6, 11, 7, 6, 7, 7, 7, 12, 11, 7, 12, 11, 7, 7, 7, 
             7, 12, 11, 7, 12, 11, 7, 7, 7, 7, 13, 7, 7, 7, 13, 3, 3, 3,
              11, 7, 6, 5, 6]]

        self.degree = 3
        
    def test_sequence_existence(self):
        self.markov_chain.add_data_to_trie(self.data, self.degree)
        length = 10
        generated_song = self.markov_chain.generate_music(length, self.degree, self.data)
        lista = []
        note = "a"
        note_index = 0
        previous = 0
        generated_song = self.numeric_data.match_note_to_a_number(note, note_index, lista, generated_song, previous)
        self.find_common_combination(generated_song, self.data, self.degree)

    def find_common_combination(self, generated_song, data, degree):
        common = set()
        passed = True
        sublists = []
        result = [self.generate_sublists(sublist) for sublist in data]
        help_list_1 = []
        help_list_2 = []
        for i in range(2, len(generated_song) - (degree)):
            combination = generated_song[i:i + self.degree + 1]
            help_list_1.append(combination)
        found = False
        appeared_in_1 = False
        help_list_3 = []
        for i in help_list_1:
            if i not in help_list_3:
                help_list_3.append(i)
        for notes_list in help_list_3:
            if notes_list in result[0]:
                if notes_list not in help_list_2:
                    help_list_2.append(notes_list)

        self.assertEqual(help_list_3,help_list_2)

    def generate_sublists(self, lst):
        sublists = []
        for i in range(len(lst) - 3):
            sublists.append(lst[i:i+4])
        return sublists

