import pygame, sys
from start import EscapeGame
# from tai_enigme2 import TaiEnigme2
from tai import tai_enigme_1

pygame.init()

def main():

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle click on sound button
                    if play.sound_button_rect.collidepoint(event.pos):
                        play.music_muted = not play.music_muted
                        if play.music_muted:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                    # Handle click on validation button
                    if play.validate_button_rect.collidepoint(event.pos):
                        print(f"Input validated: {play.input_text}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text

                    # if play.image_rect.collidepoint(event.pos):
                    #     tai_2.load_enigme()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(f"Input validated: {play.input_text}")
                        play.quack_sound.play()  # Play the quack sound
                        play.input_text = ""  # Clear input text

                    elif event.key == pygame.K_BACKSPACE:
                        play.input_text = play.input_text[:-1]

                    elif event.key == pygame.K_b:
                        tai.load_enigme()
                        
                    else:
                        play.input_text += event.unicode

            # Draw the background image
            play.draw_background(play.background_image)

            # Draw the input field
            play.draw_input_field()

            # Draw the sound button
            play.draw_sound_button()

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    play = EscapeGame()
    # tai_2 = TaiEnigme2()
    tai = tai_enigme_1()
    main()