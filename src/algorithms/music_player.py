import pygame
import time

class Player:
   
    def __init__(self):
        pygame.init()

        self.note_mapping = {
            1: "sounds/c2.wav",
            2: "sounds/d2.wav",
            3: "sounds/e2.wav",
            4: "sounds/f2.wav",
            5: "sounds/g2.wav",
            6: "sounds/a2.wav",
            7: "sounds/b2.wav",
            12: "sounds/c.wav",
            12: "sounds/d.wav",
            11: "sounds/e.wav",
            14: "sounds/f.wav",
            15: "sounds/g.wav",
            16: "sounds/a.wav",
            17: "sounds/b.wav",
            21: "sounds/c3.wav",
            22: "sounds/d3.wav",
            23: "sounds/e3.wav",
            24: "sounds/f3.wav",
            25: "sounds/g3.wav",
            26: "sounds/a3.wav",
            27: "sounds/b3.wav",
            101: "sounds/c_sharp.wav",
            102: "sounds/d_sharp.wav",
            103: "sounds/e_sharp.wav",
            104: "sounds/f_sharp.wav",
            105: "sounds/g_sharp.wav",
            106: "sounds/a_sharp.wav",
            107: "sounds/b_sharp.wav",
            201: "sounds/c_flat.wav",
            202: "sounds/d_flat.wav",
            203: "sounds/e_flat.wav",
            204: "sounds/f_flat.wav",
            205: "sounds/g_flat.wav",
            206: "sounds/a_flat.wav",
            207: "sounds/b_flat.wav",
        }


    def play_note(self, notes):
        print("meneekö tänne")
        for note in notes:
            if note in self.note_mapping:
                sound_file = self.note_mapping[note]
                pygame.mixer.Sound(sound_file).play()
                time.sleep(0.5)

        time.sleep(len(notes_to_play) * 0.5)
        pygame.mixer.quit()
