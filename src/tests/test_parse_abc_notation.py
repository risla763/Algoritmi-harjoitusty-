import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.parse_abc_notation import NumericalNotes
from logic.convert_data_to_abc import ConvertToAbc

class TestParseAbc(unittest.TestCase):

    def setUp(self):
        self.markov_chain = MarkovChain()
        self.trie = Trie()
        self.convert = ConvertToAbc()
        self.numeric_data = NumericalNotes()

    def test_parser(self):
        self.numeric_data.am_data("data/HavaNagila.abc")




        #[':', 'E', 'E', '^', 'G', 'F', 'E', '^', 'G', 'G',
        #  'B', 'A', 'G', 'A', 'A', 'c', 'B', 'A', '\n', '^', 'G',
        #  'F', 'E', 'F', 'G', ':', '^', 'G', 'F', 'E', 'F', 'E', ':',
        #  '^', 'G', 'G', 'F', 'E', 'E', 'E', '\n', 'F', 'F', 'E', 'D',
        #  'D', 'D', 'D', 'F', 'E', 'D', 'D', 'A', '^', 'G', 'F', 'E', 'F',
        #  'G', ':', '\n', '^', 'G', 'F', 'E', 'F', 'E', 'A', 'c', 'A', 'c',
        #  'A', 'c', '\n', 'A', 'A', 'A', 'c', 'B', 'A', 'c', 'B', 'A', 'A',
        #  'A', 'A', 'c', 'B', 'A', 'c', 'B', 'A', '\n', 'B', 'B', 'B', 'd',
        #  'c', 'B', 'd', 'c', 'B', 'B', 'B', 'B', 'd', 'c', 'B', 'd', 'c', 'B', 
        # '\n', 'B', 'B', 'B', 'e', 'B', 'B', 'B', 'e', 'E', 'E', 'E', '(', 'c', 'B', 
        # 'A', '^', 'G', ')', 'A', ']', '\n']
