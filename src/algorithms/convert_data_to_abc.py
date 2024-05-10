import os
import re

class ConvertToAbc:

    def __init__(self):
        self.mapping = {1:'C', 2: 'D', 3: 'E', 4: 'F', 5:'G', 6:'A', 7:'B',
            11:'c', 12:'d',13:'e',14:'f',15:'g',16:'a',17:'b',21: "c'",22: "d'",23:"e'",
            24:"f'",25:"g'",26:"a'",27:"b'"}

    def convert_numbers_to_notes(self,song):
        abc_song = []
        for number in song:
            if 100 < number < 200: #jos on ylennys
                number -= 100
                note = self.mapping.get(number)
                if note:
                    note = "^" + note #lisää mappingilla löydetyn numeron ja siihen perään ^
                abc_song.append(str(note))
            elif number > 200: #jos on alennus
                number -= 200
                note = self.mapping.get(number)
                if note:
                    note = "_" + note
                abc_song.append(str(note))
            else:
                note = self.mapping.get(number)
                abc_song.append(str(note))
            
        self.abc_notation_form(abc_song)

    def abc_notation_form(self, song):
        abc_dataset = ''.join(song)
        print(abc_dataset)

#if __name__ == "__main__":
    #converter = ConvertToAbc()
    #song = [1, 101, 2, 102, 3, 103, 4, 104, 5, 105, 6, 106, 7, 107]
    #abc_song = converter.convert_numbers_to_notes(song)
    #song = [21, 221, 22, 222, 23, 223, 24, 224, 25, 225, 26, 226, 27, 227]
    #abc_song = converter.convert_numbers_to_notes(song)
    #song = [1, 2, 3, 4, 5, 6, 7]
    #abc_song = converter.convert_numbers_to_notes(song)