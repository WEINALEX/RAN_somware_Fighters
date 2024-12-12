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
        self.steps = (self.step_1, self.step_2, self.step_3, self.step_4, self.step_5, self.step_6, self.step_7, self.step_8)
        self.input_text = ""
        self.import_assets()
        self.choice_1 = ""
        self.choice_2 = ""
        self.choice_3 = ""

    def import_assets(self):
        background_path = './assets/img/tai_'
        self.backgrounds = {3: 'web', 4: 'cmd', 
                            5: 'wifi', 6: 'wifiok', 7: 'webok', 0: 'roomAI', 1: 'computer', 2: 'composantbckgrd'}
        
        for key in self.backgrounds.keys():
            full_path = background_path + self.backgrounds[key] + '.png'
            self.backgrounds[key] = pygame.image.load(full_path)

    def load_enigme(self):
        """ Boucle principale du jeu """
        self.index = 0
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
        if self.index == 8:  # Condition d'arrêt
            return self.index

        # Dessiner le fond de l'énigme actuelle
        self.game.draw_background(self.backgrounds[self.index])
        pygame.display.update()  # On met à jour l'affichage

        # On appelle l'étape correspondante
        step_function = self.steps[self.index % 8]  # On prend l'étape actuelle
        success = step_function()  # Appel de la fonction (ex: step_1, step_2, ...)

        if success:
            self.index += 1  # On avance vers l'énigme suivante
        
        return self.tai_game_loop(self.index)  # Appel récursif avec la mise à jour de l'index
    
    def draw_button(self, screen, x, y, width, height, button_color, text_color, text, font_size=40):

        # WHITE = (255, 255, 255)
        # BLUE = (0, 122, 255)
        # BLACK = (0, 0, 0)

        # # Position et dimensions du bouton
        # button_x = 180
        # button_y = 609
        # button_width = 421 - 180  # Calcul de la largeur
        # button_height = 682 - 609  # Calcul de la hauteur

        button_rect = pygame.draw.rect(screen, button_color, (x, y, width, height), border_radius=10)
        # ✅ Créer une police de caractères
        font = pygame.font.SysFont('Times', font_size)  # Taille 40
        text = font.render(text, True, text_color)  # Texte en blanc

        # ✅ Centrer le texte dans le bouton
        text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text, text_rect)  # Affiche le texte

        return button_rect
    
    def draw_banner(self, screen, message, banner_color=(0, 122, 255), text_color=(255, 255, 255), banner_height=50, font_size=40):
        """
        Fonction pour dessiner une bannière avec un message au centre de l'écran.

        Arguments :
        
        screen : La surface pygame sur laquelle dessiner la bannière.
        message : Le texte à afficher au centre de la bannière.
        banner_color : La couleur de la bannière (par défaut bleu).
        text_color : La couleur du texte (par défaut blanc).
        banner_height : La hauteur de la bannière (par défaut 50px).
        font_size : La taille de la police du texte (par défaut 40px).
        """
        # ✅ Calculer la largeur et la hauteur de la bannière
        banner_width = screen.get_width()  # La largeur de la bannière est égale à la largeur de l'écran
        banner_rect = pygame.Rect(0, 0, banner_width, banner_height)  # Rectangle de la bannière

        # ✅ Dessiner la bannière
        pygame.draw.rect(screen, banner_color, banner_rect)

        # ✅ Afficher le texte au centre de la bannière
        font = pygame.font.SysFont(None, font_size)  # Police par défaut de Pygame
        text_surface = font.render(message, True, text_color)  # Texte rendu
        text_rect = text_surface.get_rect(center=(banner_width // 2, banner_height // 2))  # Centré dans la bannière
        screen.blit(text_surface, text_rect)  # Afficher le texte sur l'écran

    def repeat_function(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle click on sound button
                if self.game.sound_button_rect.collidepoint(event.pos):
                    self.game.music_muted = not self.game.music_muted
                    if self.game.music_muted:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                # Handle click on validation button
                if self.game.validate_button_rect.collidepoint(event.pos):
                    print(f"Input validated: {self.game.input_text}")
                    self.game.quack_sound.play()  # self.game the quack sound
                    self.game.input_text = ""  # Clear input text
                
                if self.index == 3 and self.button2.collidepoint(event.pos):
                    return True
                
                if self.index == 4 and self.button1.collidepoint(event.pos):
                    return True
                
                if self.index == 5 and self.button1.collidepoint(event.pos):
                    return True
                
                if self.index == 6 and self.button3.collidepoint(event.pos):
                    return True
                
                if self.index == 7:
                    pygame.time.wait(3000)
                    return True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(f"Input validated: {self.game.input_text}")
                    self.game.quack_sound.play()  # self.game the quack sound
                    self.game.input_text = ""  # Clear input text

                elif event.key == pygame.K_BACKSPACE:
                    self.game.input_text = self.game.input_text[:-1]

                elif event.key == pygame.K_a:
                        return True

                else:
                    self.game.input_text += event.unicode

    def step_1(self):
        """ Énigme 1 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success
            
            self.game.draw_background(self.backgrounds[self.index])
            pygame.display.update()

    def step_2(self):
        """ Énigme 2 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success
                
            self.game.draw_background(self.backgrounds[self.index])
            pygame.display.update()

    def step_3(self):
        """ Énigme 3 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success
                    
            self.game.draw_background(self.backgrounds[self.index])
            pygame.display.update()

    def step_4(self):
        """ Énigme 4 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success
            
            self.game.draw_background(self.backgrounds[self.index])
            self.button1 = self.draw_button(self.game.screen, 180, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "network.exe")
            self.button2 = self.draw_button(self.game.screen, 430, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "cmd.exe")
            self.button3 = self.draw_button(self.game.screen, 680, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "config.exe")
            self.draw_banner(self.game.screen, "Oh ! On dirait que vous n'arrivez pas à accéder au site...")
            pygame.display.update()

    def step_5(self):
        """ Énigme 5 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success

            self.game.draw_background(self.backgrounds[self.index])
            self.button1 = self.draw_button(self.game.screen, 180, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "ping mns")
            self.button2 = self.draw_button(self.game.screen, 430, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "ipconfig")
            self.button3 = self.draw_button(self.game.screen, 680, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "netstat -an")
            self.draw_banner(self.game.screen, "Vous vous retrouver sur votre invite de commande Windows...")
            pygame.display.update()

    def step_6(self):
        """ Énigme 6 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success

            self.button1 = self.draw_button(self.game.screen, 114, 213, 136, 29, (0, 122, 255), (255, 255, 255), "")
            self.game.draw_background(self.backgrounds[self.index])
            self.draw_banner(self.game.screen, "Cliquez sur la bonne carte réseau.")
            pygame.display.update()

    def step_7(self):
        """ Énigme 7 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success

            self.game.draw_background(self.backgrounds[self.index])
            self.button1 = self.draw_button(self.game.screen, 320, 609, 450, 682 - 609, (0, 122, 255), (255, 255, 255), "metz-numeric.school.fr")
            self.button2 = self.draw_button(self.game.screen, 320, 530, 450, 682 - 609, (0, 122, 255), (255, 255, 255), "metz.numeric-school.fr")
            self.button3 = self.draw_button(self.game.screen, 320, 451, 450, 682 - 609, (0, 122, 255), (255, 255, 255), "metz-numeric-school.fr")
            self.draw_banner(self.game.screen, "Essayer d'aller vérifier si votre connexion est rétabli")
            pygame.display.update()

    def step_8(self):
        """ Énigme 8 """
        while True:
            success = self.repeat_function()
             
            if success:
                return success

            self.game.draw_background(self.backgrounds[self.index])
            self.button1 = self.draw_button(self.game.screen, 180, self.game.SCREEN_HEIGHT // 2, 720, 682 - 609, (0, 240, 0), (255, 255, 255), "Félicitation vous obtenez votre Canard Vert!")
            pygame.display.update()

