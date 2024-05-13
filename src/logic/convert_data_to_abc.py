import os
import re

class ConvertToAbc:
    """
        Luokka, joka muuttaa numeroita 
        sisältävän listan merkkijonoksi.
        Merkkijono on generoitu kappale abc notaationa.
    """

    def __init__(self):
        self.mapping = {1:'C', 2: 'D', 3: 'E', 4: 'F', 5:'G', 6:'A', 7:'B',
            11:'c', 12:'d',13:'e',14:'f',15:'g',16:'a',17:'b',21: "c'",22: "d'",23:"e'",
            24:"f'",25:"g'",26:"a'",27:"b'"}
        self.list_of_songs_numeric = []

    def convert_numbers_to_notes(self,song):
        abc_song = []
        help = True
        for number in song:
            help = True
            if 100 < number < 200:
                number -= 100
                note = self.mapping.get(number)
                if note:
                    note = "^" + note
                abc_song.append(note if note is not None else "") 
                help = False
            elif number > 200:
                number -= 200
                note = self.mapping.get(number)
                if note:
                    note = "_" + note
                abc_song.append(note if note is not None else "")  
                help = False
            elif help == True:
                note = self.mapping.get(number)
                abc_song.append(note if note is not None else "")  
                continue

        
        return self.abc_notation_form(abc_song)

    def abc_notation_form(self, song):
        abc_dataset = ''.join(song)
        return abc_dataset

    def numeric_song_list(self, song):
        self.list_of_songs_numeric.append(song)
        return self.list_of_songs_numeric