import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.parse_abc_notation import NumericalNotes
from logic.parse_abc_notation import IgnoreSpecialMarks
from logic.convert_data_to_abc import ConvertToAbc

class TestParseAbc(unittest.TestCase):
    """
        Testaa sitä että abc nuotit 
        muuttuvat niitä vastaaviksi oikeiksi nuoteiksi.
    """

    def setUp(self):
        self.parse = IgnoreSpecialMarks()
        self.all_oktaves = [1, 2, 3, 4, 5, 6, 7, 
        11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27] 
    def test_parser(self):
        test_all_notes = self.parse.am_data("data/test.abc")
        print(test_all_notes, "MOIIII")
        self.assertEqual(test_all_notes,self.all_)
        #print(test_all_notes, "MOIIII")
