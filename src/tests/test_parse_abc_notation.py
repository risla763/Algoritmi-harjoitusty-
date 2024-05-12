import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.parse_abc_notation import NumericalNotes
from logic.parse_abc_notation import IgnoreSpecialMarks
from logic.convert_data_to_abc import ConvertToAbc

class TestParseAbc(unittest.TestCase):

    def setUp(self):
        self.parse = IgnoreSpecialMarks()
        self.all_notes = [1, 2, 3, 4, 5, 6, 7, 
        11, 12, 13, 14, 15, 16, 17, 
        21, 22, 23, 24, 25, 26, 27, 
        201, 202, 203, 204, 205, 206, 207,
         211, 212, 213, 214, 215, 216, 217,
          221, 222, 223, 224, 225, 226, 227,
           1, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117
           , 121, 122, 123, 124, 125, 126, 127]

    def test_parser(self):
        test_all_notes = self.parse.am_data("data/test.abc")
        print(test_all_notes, "MOIIII")
        self.assertEqual(test_all_notes,self.all_notes)
        print(test_all_notes, "MOIIII")
