import pygame, sys

pygame.init()

class enigme_2:

    def __init__(self):
        self.input_text = ""
        self.import_assets()
        self.choice_1 = ""
        self.choice_2 = ""
        self.choice_3 = ""

    def import_assets(self):
        background_path = './assets/img/tai_'
        self.backgrounds = {0: 'computer', 1: 'web', 2: 'cmd', 
                            3: 'wifi', 4: 'wifiok', 5: 'webok'}
        
        for key in self.backgrounds.key():
            full_path = background_path + self.backgrounds[key] + '.png'
            self.backgrounds[key] = pygame.image.load(full_path)

    def load_computer(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_event = "left"

            pygame.display.update()
            self.clock.tick(60)
