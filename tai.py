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
        if index == 8:
            return index

        # Dessiner le fond de l'énigme actuelle
        self.game.draw_background(self.backgrounds[index])
        pygame.display.update() 

        # On appelle l'étape correspondante
        step_function = self.steps[index % 8] 
        success = step_function(index) 

        if success:
            index += 1
        
        return self.tai_game_loop(index) 

    def draw_button(self, screen, x, y, width, height, button_color, text_color, text, font_size=40):
        
        button_rect = pygame.draw.rect(screen, button_color, (x, y, width, height), border_radius=10)
        # ✅ Créer une police de caractères
        font = pygame.font.SysFont('Times', font_size)
        text = font.render(text, True, text_color) 

        # ✅ Centrer le texte dans le bouton
        text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text, text_rect)

        return button_rect

    def draw_banner(self, screen, message, banner_color=(0, 122, 255), text_color=(255, 255, 255), banner_height=50, font_size=40):
        """
        Fonction pour dessiner une bannière avec un message au centre de l'écran.

        Arguments :
        - screen : La surface pygame sur laquelle dessiner la bannière.
        - message : Le texte à afficher au centre de la bannière.
        - banner_color : La couleur de la bannière (par défaut bleu).
        - text_color : La couleur du texte (par défaut blanc).
        - banner_height : La hauteur de la bannière (par défaut 50px).
        - font_size : La taille de la police du texte (par défaut 40px).
        """
        # ✅ Calculer la largeur et la hauteur de la bannière
        banner_width = screen.get_width()
        banner_rect = pygame.Rect(0, 0, banner_width, banner_height)
        
        # ✅ Dessiner la bannière
        pygame.draw.rect(screen, banner_color, banner_rect)
        
        # ✅ Afficher le texte au centre de la bannière
        font = pygame.font.SysFont(None, font_size) 
        text_surface = font.render(message, True, text_color) 
        text_rect = text_surface.get_rect(center=(banner_width // 2, banner_height // 2))
        screen.blit(text_surface, text_rect) 



    def step_1(self, index):
        """ Énigme 1 """
        button = self.draw_button(self.game.screen, 180, 609, 421 - 180, 682 - 609, (0, 122, 255), (255, 255, 255), "Cliquez ici")
        self.draw_banner(self.game.screen, "Bienvenue au cours de TAI")
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button.collidepoint(mouse_x, mouse_y): 
                        print(f"Le bouton a été cliqué ! Énigme terminée.")
                        return True
        

    def step_2(self, index):
        """ Énigme 2 """
        button = self.draw_button(self.game.screen, 550, 741, 900 - 550, 832 - 741, (0, 122, 255), (255, 255, 255), "Allumez le PC")
        self.draw_banner(self.game.screen, "Veuillez démarrer votre ordinateur")

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button.collidepoint(mouse_x, mouse_y):  # ✅ Si le bouton est cliqué
                        print(f"Le bouton a été cliqué ! Énigme terminée. {mouse_x}:{mouse_y}")
                        self.draw_banner(self.game.screen, "Démarrage de l'ordinateur en cours...", banner_color=(255, 0, 0))
                        pygame.display.update()
                        
                        # ⏳ Attendre 5 secondes (5000 ms)
                        pygame.time.wait(5000)
                        return True
            

    def step_3(self, index):
        """ Énigme 3 avec des inputs à des positions précises """
        
        # ✅ Position et taille des inputs (x, y, largeur, hauteur)
        input_positions = [
            pygame.Rect(791, 517, 998-791, 560-517),  # la ram
            pygame.Rect(675, 300, 150, 40),   # le processeur
            pygame.Rect(1042, 553, 1218-1042, 599-553),   # le hdd
            pygame.Rect(658, 670, 830-658, 709-670),   # ssd
        ]

        # ✅ Les bonnes réponses associées à chaque input
        correct_answers = ["ram", "processeur", "disque dur", "ssd"]  # Les réponses correctes à entrer

        # ✅ Contenu des inputs (texte que l'utilisateur a saisi)
        input_texts = ["", "","",""]  # Contenu de chaque input (vide au départ)

        # ✅ Index de l'input actif (celui en train de recevoir la saisie)
        active_input_index = None

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # ✅ Clic sur un input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    for i, input_rect in enumerate(input_positions):
                        if input_rect.collidepoint(mouse_x, mouse_y):
                            active_input_index = i  # On rend l'input actif
                            print(f"Input {i} activé")
                            break
                    
                    if button.collidepoint(mouse_x, mouse_y):  # ✅ Si le bouton est cliqué
                        print(f"Le bouton a été cliqué! Énigme terminée. {mouse_x}:{mouse_y}")

                        if input_texts == correct_answers:
                            return True
                        else:
                            self.draw_banner(self.game.screen, "Vous avez une ou plusieurs réponses fausses", banner_color=(255, 0, 0))
                            pygame.display.update()
                            
                            pygame.time.wait(5000)

                # ✅ Saisie de texte dans l'input actif
                if event.type == pygame.KEYDOWN and active_input_index is not None:
                    if event.key == pygame.K_BACKSPACE:  # Efface le dernier caractère
                        input_texts[active_input_index] = input_texts[active_input_index][:-1]
                    else:
                        # Ajouter la lettre à l'input actif
                        input_texts[active_input_index] += event.unicode

            # ✅ Affichage du background
            self.game.draw_background(self.backgrounds[index])

            button = self.draw_button(self.game.screen, 0, self.game.screen.get_height() - 100, self.game.screen.get_width(), 80, (0, 122, 255), (255, 255, 255), "Valider")

            self.draw_banner(self.game.screen, "Votre ordinateur n'a pas démarré. Veuillez entrer le nom des composants")

            # ✅ Dessiner tous les inputs
            for i, input_rect in enumerate(input_positions):
                # Couleur de l'input (bleu s'il est actif, blanc sinon)
                color = (0, 122, 255) if i == active_input_index else (255, 255, 255)
                
                # Dessiner l'input (boîte rectangulaire)
                pygame.draw.rect(self.game.screen, color, input_rect, border_radius=5)
                
                # Ajouter le texte de l'input
                font = pygame.font.SysFont(None, 30)
                text_surface = font.render(input_texts[i], True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=input_rect.center)
                self.game.screen.blit(text_surface, text_rect)
            
            pygame.display.update()
        

    def step_4(self, index):
        """ Énigme 4 """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A pressed, step 4 complete")
                        return True
        
    def step_5(self, index):
        """ Énigme 4 """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A pressed, step 4 complete")
                        return True
        
    def step_6(self, index):
        """ Énigme 4 """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A pressed, step 4 complete")
                        return True
        
    def step_7(self, index):
        """ Énigme 4 """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A pressed, step 4 complete")
                        return True
        
    def step_8(self, index):
        """ Énigme 4 """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(f"Key A pressed, step 4 complete")
                        return True
        
