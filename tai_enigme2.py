import pygame, sys
from start import EscapeGame

class TaiEnigme2:

    def __init__(self):
        self.game = EscapeGame()
        self.input_text = ""
        self.import_assets()
        self.choice_1 = ""
        self.choice_2 = ""
        self.choice_3 = ""
        self.index = 0
        
    def import_assets(self):
        background_path = './assets/img/tai_'
        self.backgrounds = {0: 'web', 1: 'cmd', 
                            2: 'wifi', 3: 'wifiok', 4: 'webok'}
        
        for key in self.backgrounds.keys():
            full_path = background_path + self.backgrounds[key] + '.png'
            self.backgrounds[key] = pygame.image.load(full_path)

    def load_enigme(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')

            loop_game = self.tai_game_loop(self.index)
            if loop_game == 8:
                break

    def tai_game_loop(self, index):
        
        if index == 8:
            return index
      
        self.step = (self.step_1(), self.step_2(), self.step_3(), self.step_4())

        success = self.step[index]

        self.game.draw_background(self.backgrounds[index])
        pygame.display.update()
        
        if success:
            index+=1
        
        return self.tai_game_loop(index)

    def step_1(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A , step1")
                        return True

                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')

    def step_2(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A , step2")

                        return True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')

    
    def step_3(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A , step3")

                        return True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')
    
    def step_4(self):
        enigme_on = True

        while enigme_on:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A , step4")

                        return True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')
