import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.convert_data_to_abc import ConvertToAbc
from logic.parse_abc_notation import NumericalNotes
class TestMarkovChain(unittest.TestCase):

    def setUp(self):
        self.markov_chain = MarkovChain()
        self.trie = Trie()
        self.convert = ConvertToAbc()
        self.numeric_data = NumericalNotes()
        self.data = [[13, 13, 6, 5, 3, 6, 6, 5, 6, 5,
         6, 11, 7, 6, 5, 13, 12, 7, 6, 5, 3, 6, 6, 5,
          6, 5, 6, 11, 7, 6, 5, 3, 6, 6, 7, 11, 11, 7,
           11, 13, 12, 11, 7, 5, 12, 5, 13, 5, 12, 11,
            7, 6, 7, 11, 12, 13, 16, 15, 13, 12, 7, 6,
             6, 7, 11, 6, 6, 16, 15, 13, 16, 15, 13, 12,
              7, 5, 6, 7, 12, 11, 6, 6, 16, 15, 13, 16,
               15, 13, 12, 7, 6, 6], [3, 5, 105, 5, 6, 7,
                11, 12, 13, 15, 115, 15, 16, 3, 6, 7, 6, 11,
                 12, 13, 12, 11, 7, 6, 5, 6, 5, 7, 11, 12, 15, 
                 13, 12, 7, 5, 6, 7, 6, 11, 12, 13, 12, 11, 7, 11
                 , 12, 13, 6, 7, 6, 105, 5, 6, 6, 5, 11, 12, 13, 15,
                  16, 15, 13, 11, 15, 13, 11, 5, 6, 5, 7, 11, 12, 15,
                   13, 12, 7, 5, 11, 12, 13, 15, 16, 15, 13, 11, 12, 13, 
                   115, 15, 16, 6, 7, 6, 105, 5, 6, 6]]
        self.degree = 3
        
    def test_sequence_existence(self):
        self.markov_chain.add_data_to_trie(self.data, self.degree)
        length = 10
        generated_song = self.markov_chain.generate_music(length, self.degree, self.data)
        #lista = self.convert.numeric_song_list(generated_song)
        print(generated_song, "lol") #tässä kirjaimet
        lista = []
        note = "a"
        note_index = 0
        generated_song = self.numeric_data.match_note_to_a_number(note, note_index, lista, generated_song)
        print(generated_song, "lollololol") 
        #data = self.convert.convert_numbers_to_notes(self.data[0])
        #print(self.data, "lol")
        self.find_common_combination(generated_song, self.data, self.degree)

    def find_common_combination(self, generated_song, data, degree):
        common = set()
        passed = True
        sublists = []
        result = [self.generate_sublists(sublist) for sublist in data]
        print(result, "mOIIII") #tämän sisällä kaksi listaa
        help_list_1 = []
        help_list_2 = []
        for i in range(2, len(generated_song) - (degree)):
            combination = generated_song[i:i + self.degree + 1]
            help_list_1.append(combination)
        #print(help_list_1, "HELP_LIST_1")
        found = False
        #if i in help_list:
        appeared_in_1 = False
        help_list_3 = []
        for i in help_list_1:
            if i not in help_list_3:
                help_list_3.append(i)

        for notes_list in help_list_3:
            if notes_list in result[0]:
                if notes_list not in help_list_2:
                    help_list_2.append(notes_list)
            if notes_list in result[1] and notes_list not in result[0]:
                if notes_list not in help_list_2:
                    help_list_2.append(notes_list)
        print(help_list_3, "1")
        print(help_list_2, "2")
        self.assertEqual(help_list_3,help_list_2)




    def generate_sublists(self, lst):
        sublists = []
        for i in range(len(lst) - 3):
            sublists.append(lst[i:i+4])
        return sublists


if __name__ == '__main__':
    unittest.main()
