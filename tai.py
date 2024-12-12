# # 1. Arriver dans la salle -> clicque sur l'ordinateur (positionX: 180, 421 - positionY: 609, 682)
# # 2. on est sur le computeur -> il ne démarre pas -> on change le matos
# # 3. interface de l'énigme
# # 4. On fait le jeu
# # 5. si réussi on charge l'énigme 2

import pygame, sys
from start import EscapeGame

class tai_enigme_1:

    def __init__(self):
        self.game = EscapeGame()
        self.index = 0
        self.steps = (self.step_1, self.step_2, self.step_3, self.step_4, self.step_5, self.step_6, self_step_7, self.step_8)
        self.input_text = ""
        self.import_assets()
        self.choice_1 = ""
        self.choice_2 = ""
        self.choice_3 = ""

    def import_assets(self):
        background_path = './assets/img/tai_'
        self.backgrounds = {0: 'web', 1: 'cmd', 
                            2: 'wifi', 3: 'wifiok', 4: 'webok', 5: 'roomAI', 6: 'computer', 7: 'composantbckgrd'}
        
        for key in self.backgrounds.keys():
            full_path = background_path + self.backgrounds[key] + '.png'
            self.backgrounds[key] = pygame.image.load(full_path)

    def load_enigme(self):
        """ Boucle principale du jeu """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')
            
            # Lancer la boucle principale de l'énigme (récursive)
            loop_game = self.tai_game_loop(self.index)
            if loop_game == 8:
                break

            pygame.display.update()

    def tai_game_loop(self, index):
        """ Fonction récursive qui gère les énigmes """
        if index == 8:  # Condition d'arrêt
            return index

        # Dessiner le fond de l'énigme actuelle
        self.game.draw_background(self.backgrounds[index])
        pygame.display.update()  # On met à jour l'affichage

        # On appelle l'étape correspondante
        step_function = self.steps[index % 4]  # On prend l'étape actuelle
        success = step_function(index)  # Appel de la fonction (ex: step_1, step_2, ...)

        if success:
            index += 1  # On avance vers l'énigme suivante
        
        return self.tai_game_loop(index)  # Appel récursif avec la mise à jour de l'index

    def step_1(self, index):
        """ Énigme 1 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 1 complete")
                    return True  # L'énigme est résolue
        
        return False  # L'énigme n'est pas encore résolue

    def step_2(self, index):
        """ Énigme 2 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 2 complete")
                    return True
        
        return False

    def step_3(self, index):
        """ Énigme 3 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 3 complete")
                    return True
        
        return False

    def step_4(self, index):
        """ Énigme 4 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 4 complete")
                    return True
        
        return False
    def step_5(self, index):
        """ Énigme 4 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 4 complete")
                    return True
        
        return False
    def step_6(self, index):
        """ Énigme 4 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 4 complete")
                    return True
        
        return False
    def step_7(self, index):
        """ Énigme 4 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 4 complete")
                    return True
        
        return False
    def step_8(self, index):
        """ Énigme 4 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"Key A pressed, step 4 complete")
                    return True
        
        return False
