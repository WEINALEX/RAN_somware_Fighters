import pygame, sys
from start import EscapeGame


def main():
        # Couleurs
    BLANC = (255, 255, 255)

    # Police
    font = pygame.font.SysFont('Arial', 30)

    texte = font.render("Bonjour, bienvenue à Metz Numeric School, Vous pouvez entrer.", True, BLANC)
    texte_2 = font.render("", True, BLANC)
    texte_2_1 = font.render("", True, BLANC)
    fin_sequence = 0
    # Main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle click on sound button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f'posX: {mouse_x}, posY: {mouse_y}')
                if play.sound_button_rect.collidepoint(event.pos):
                    play.music_muted = not play.music_muted
                    if play.music_muted:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                
                if event.button == 1 and fin_sequence == 0:
                    play.background_image = pygame.image.load('./assets/img/hub_hub.png')
                    texte = font.render("", True, BLANC)
                    texte_2 = font.render("Oh bonjour bienvenue,", True, BLANC)
                    texte_2_1 = font.render("approchez on va procéder à votre enregistrement", True, BLANC)
                    event.button = 0
                    fin_sequence += 1


                if event.button == 1 and fin_sequence == 1:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Tout d'abord quel est votre prenom ?", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 2:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Maintenant j'ai besoin de savoir, dans quel lycée à tu étudié ? ", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 3:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Ok, tu as des frères et soeurs ? ", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 4:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Très bien, pour finir j'ai besoin de ton adresse s'il te plait. ", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 5:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Super, je vous donne votre ID : MNS2911 ne le divulgez pas ! ", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 6:
                    play.background_image = pygame.image.load('./assets/img/hub_desk.png')
                    texte_2 = font.render("Votre but est de récupérer les 3 canards.", True, BLANC)
                    texte_2_1 = font.render("Il y a un canard par salle, bon courage !", True, BLANC)
                    event.button = 0
                    fin_sequence += 1

                if event.button == 1 and fin_sequence == 7: 
                    play.background_image = pygame.image.load('./assets/img/hub_hub.png')
                    texte_2 = font.render("", True, BLANC)
                    texte_2_1 = font.render("", True, BLANC)
                    event.button = 0
                    fin_sequence += 1
                
                    # Handle click on validation button
                # if play.validate_button_rect.collidepoint(event.pos):
                #     reponse = play.input_text
                #     print(f"votre nom est : {reponse}")
                #     play.quack_sound.play()  # Play the quack sound
                #     play.input_text = ""  # Clear input text

                # if play.image_rect.collidepoint(event.pos):
            if event.type == pygame.KEYDOWN:
                if fin_sequence == 2:
                    if event.key == pygame.K_RETURN:
                        reponse_nathalie_nom = play.input_text
                        print(f"votre nom est : {reponse_nathalie_nom}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text
                    elif event.key == pygame.K_BACKSPACE:
                        play.input_text = play.input_text[:-1]
                    else:
                        play.input_text += event.unicode

                if fin_sequence == 3:
                    if event.key == pygame.K_RETURN:
                        reponse_nathalie_lycee = play.input_text
                        print(f"votre lycee est : {reponse_nathalie_lycee}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text
                    elif event.key == pygame.K_BACKSPACE:
                        play.input_text = play.input_text[:-1]
                    else:
                        play.input_text += event.unicode

                if fin_sequence == 4:
                    if event.key == pygame.K_RETURN:
                        reponse_nathalie_famille = play.input_text
                        print(f"votre famille est : {reponse_nathalie_famille}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text
                    elif event.key == pygame.K_BACKSPACE:
                        play.input_text = play.input_text[:-1]
                    else:
                        play.input_text += event.unicode

                if fin_sequence == 5:
                    if event.key == pygame.K_RETURN:
                        reponse_nathalie_adresse = play.input_text
                        print(f"votre adresse est : {reponse_nathalie_adresse}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text
                    elif event.key == pygame.K_BACKSPACE:
                        play.input_text = play.input_text[:-1]
                    else:
                        play.input_text += event.unicode

            

        # Draw the background image
        play.draw_background(play.background_image)

        # Draw the input field
        play.draw_input_field()

        # Draw the sound button
        play.draw_sound_button()

        play.screen.blit(texte,(75, 575))
        play.screen.blit(texte_2,(75, 535))
        play.screen.blit(texte_2_1,(75, 575))
        

        # Update the display
        pygame.display.flip()


    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    play = EscapeGame()

    main()