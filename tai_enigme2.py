import pygame, sys
from start import EscapeGame

# pygame.init()

class TaiEnigme2:

    def __init__(self):
        self.game = EscapeGame()
        self.input_text = ""
        self.import_assets()
        self.choice_1 = ""
        self.choice_2 = ""
        self.choice_3 = ""

    def import_assets(self):
        background_path = './assets/img/tai_'
        self.backgrounds = {0: 'web', 1: 'cmd', 
                            2: 'wifi', 3: 'wifiok', 4: 'webok'}
        
        for key in self.backgrounds.keys():
            full_path = background_path + self.backgrounds[key] + '.png'
            self.backgrounds[key] = pygame.image.load(full_path)

    def load_enigme(self):
        enigme_on = True
        bg = 0
        
        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_event = "left"

            self.game.screen.fill((0, 0, 0))
            self.game.draw_background(self.backgrounds[bg])

            pygame.display.update()
