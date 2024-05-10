import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.convert_data_to_abc import ConvertToAbc

class TestMarkovChain(unittest.TestCase):

    def setUp(self):
        self.markov_chain = MarkovChain()
        self.trie = Trie()
        self.data = [[1, 0, 0, 0, 0, 16, 0, 0, 0, 
                      0, 0, 16, 0, 0, 0, 16, 0, 0, 0, 0, 
                      16, 0, 15, 0, 6, 0, 6, 0, 6, 0, 7, 
                      0, 1, 2, 0, 3, 0, 2, 2, 2, 3, 4, 5, 
                      0, 6, 0, 0, 5, 0, 5, 5, 5, 6, 5, 4, 
                      0, 3, 0, 4, 4, 4, 4, 3, 2, 0, 3, 0, 
                      0, 7, 11, 11, 11, 11, 7, 6, 0, 11, 11,
                      11, 11, 7, 6, 5, 0, 0, 4, 0, 2, 0, 4, 
                      0, 1, 0, 0, 4, 0, 7, 0, 0, 4, 6, 0, 0, 
                      0, 5, 0, 7, 7, 7, 7, 6, 5, 0, 7, 7, 7, 
                      7, 6, 5, 4, 0, 0, 3, 0]]
        self.degree = 3
        
    def test_sequence_existence(self):
        self.markov_chain.add_data_to_trie(self.data, self.degree)
        length = 20
        generated_song = self.markov_chain.generate_music(length, self.degree, self.data)
        generated_notes = [generated_song[i:i+self.degree] for i in range(len(generated_song) - self.degree + 1)]
        self.assertEqual(len(generated_notes), length)

if __name__ == '__main__':
    unittest.main()
