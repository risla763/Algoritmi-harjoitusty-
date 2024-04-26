import pygame
#colors


class UI:

    def __init__(self, logic):
        print("TÄÄLLÄ")
        self.logic = logic #tähän logiikka metodi
        self.screen = pygame.display.set_mode([1200, 1000])
        self.play_button = False #soita musiikkia
        self.quit_button = False #exit sovellus
        self.generate_music_button = False #generoi
        #self.button_generate_music = Button(150, 100, 100, 50, (255, 0, 0), "Generate music",self.logic.generate_music, self.logic)
        #TÄSSÄ BIISIT
        self.hava_nagila = False
        #
        self.change_data_button = False


    def start(self):
        pygame.init()
        self.screen.fill((0, 255, 255))
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect((150, 100, 100, 50)).collidepoint(event.pos):
                        self.logic.generate_music()

            #tähän PIIRTO KOMENNOT MITÄ NÄYTÖLLÄ ON
            self.screen.fill((0, 255, 255))
            pygame.draw.rect(self.screen,(0, 0, 0),(150, 100, 100, 50))
            pygame.display.flip()
        pygame.quit()

class Button:
    def __init__(self, x, y, width, height, color, text, action,logic):
        self.logic = logic
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def perform_action(self):
        print(self.action)
        if self.action:
            self.logic.generate_music()

