import unittest
from algorithms_and_data_structures.trie_data_structure import Trie
from algorithms_and_data_structures.markov_chain import MarkovChain
from logic.parse_abc_notation import NumericalNotes
from logic.parse_abc_notation import IgnoreSpecialMarks
from logic.convert_data_to_abc import ConvertToAbc

class TestParseAbc(unittest.TestCase):
    """
    Testaa vastaavatko numerot oikeita abc notaatio merkintöjä.
    
    """

    def setUp(self):
        self.converter = ConvertToAbc()
        self.all_notes = [1, 2, 3, 4, 5, 6, 7, 
        11, 12, 13, 14, 15, 16, 17, 
        21, 22, 23, 24, 25, 26, 27, 
        201, 202, 203, 204, 205, 206, 207,
         211, 212, 213, 214, 215, 216, 217,
          221, 222, 223, 224, 225, 226, 227,
           1, 102, 103, 104, 105, 106, 107, 111, 112, 113, 114, 115, 116, 117
           , 121, 122, 123, 124, 125, 126, 127]
        self.all_abc = "CDEFGABcdefgabc'd'e'f'g'a'b'_C_D_E_F_G_A_B_c_d_e_f_g_a_b_c'_d'_e'_f'_g'_a'_b'C^D^E^F^G^A^B^c^d^e^f^g^a^b^c'^d'^e'^f'^g'^a'^b'"
    
    def test_converting(self):
        converted = self.converter.convert_numbers_to_notes(self.all_notes)
        print("111", self.all_abc)
        print("222",converted)
        self.assertEqual(converted,self.all_abc)
        print(converted)