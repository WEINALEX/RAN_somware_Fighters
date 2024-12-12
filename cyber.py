import pygame, sys
from start import EscapeGame
import re


# pygame.init()

class Cybersecurite:
  def __init__(self):
    self.enigme_cyber_1 = False
    self.enigme_cyber_2 = False
    self.enigme_cyber_3 = False
    self.enigme_cyber_4 = False
    self.password = ""
    self.font = pygame.font.Font(None, 36)
    self.background_image = pygame.image.load('./assets/img/salle_cyber.png')
    self.usb_rect = pygame.Rect(400, 500, 120, 120)  # Example rectangle dimensions
    self.pc_rect = pygame.Rect(600, 250, 260, 160)  # Example rectangle dimensions
    self.red_rect_border_thickness = 3  # Thickness of the yellow border
    self.start = EscapeGame()

  def draw_rectangle_with_border(self, dimentions):
    # Create a surface for the rectangle with transparency
    rect_surface = pygame.Surface((dimentions.width, dimentions.height), pygame.SRCALPHA)
    rect_surface.fill((0, 0, 0, 0))  # transparent (RGBA)

    # Blit the surface onto the main screen
    self.start.screen.blit(rect_surface, dimentions.topleft)

    # Draw the yellow border around the rectangle
    pygame.draw.rect(self.start.screen, (255, 193, 7, 128), dimentions, self.red_rect_border_thickness)

  def draw_text_with_background(self, text, position, text_color=(0, 0, 0), bg_color=(255, 255, 255),
                                border_color=(0, 0, 0), padding=20, border_radius=10, border_width=3):
    """Draw text with a rounded background and border."""
    # Render the text surface
    text_surface = self.font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=position)

    # Calculate the background rectangle dimensions with padding
    bg_rect = pygame.Rect(
      text_rect.left - padding,
      text_rect.top - padding,
      text_rect.width + 2 * padding,
      text_rect.height + 2 * padding
    )

    # Draw the border
    pygame.draw.rect(self.start.screen, border_color, bg_rect, border_width, border_radius)

    # Draw the background rectangle
    pygame.draw.rect(self.start.screen, bg_color, bg_rect.inflate(-border_width * 2, -border_width * 2), 0,
                     border_radius)

    # Draw the text on top
    self.start.screen.blit(text_surface, text_rect)

  def handle_usb_choice(self):
    response = self.start.input_text.lower()

    if response == "oui":

      # Draw the background image
      self.start.draw_background(self.background_image)

      # Draw the red rectangle with a yellow border
      self.draw_rectangle_with_border(dimentions=self.usb_rect)
      self.draw_rectangle_with_border(dimentions=self.pc_rect)

      self.draw_text_with_background(
        f"""Les clés USB peuvent contenir des virus et des logiciels malveillants.""",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )
      self.draw_text_with_background(
        f"""Erreur : ne branchez jamais une clé USB inconnue sur votre ordinateur.""",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 300),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )
      pygame.display.flip()
      pygame.time.wait(2000)
      self.start.draw_background(self.background_image)
      self.draw_text_with_background(
        f"Vous avez trouvé une clé USB. Voulez-vous brancher la clé USB ? (oui/non)",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )



      return False

    elif response == "non":
      # self.start.draw_background(self.background_image)
      self.draw_text_with_background(
        f"Félicitations ! Vous avez fait preuve de prudence. Les clés USB peuvent contenir des virus et des logiciels malveillants.",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )
      pygame.display.flip()
      pygame.time.wait(2000)
      self.start.draw_background(self.background_image)
      # Draw the red rectangle with a yellow border
      self.draw_rectangle_with_border(dimentions=self.usb_rect)
      self.draw_rectangle_with_border(dimentions=self.pc_rect)

      return True


  def usb_cyber(self):
    """Display the USB message with styled background."""
    self.draw_text_with_background(
      f"Vous avez trouvé une clé USB. Voulez-vous brancher la clé USB ? (oui/non)",
      (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
      text_color=(0, 0, 0),
      bg_color=(255, 255, 255),
      border_color=(0, 0, 0),
      padding=20,
      border_radius=30,
      border_width=3
    )
    # self.start.draw_input_field()
    pygame.display.flip()

    running = True

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          # Handle click on sound button
          if self.start.sound_button_rect.collidepoint(event.pos):
            self.start.music_muted = not self.start.music_muted
            if self.start.music_muted:
              pygame.mixer.music.pause()
            else:
              pygame.mixer.music.unpause()

          # Handle click on validation button
          if self.start.validate_button_rect.collidepoint(event.pos):
            print(f"Input validated: {self.start.input_text}")
            self.start.quack_sound.play()  # Play the quack sound
            self.handle_usb_choice()
            self.start.input_text = ""  # Clear input text


        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            print(f"Input validated: {self.start.input_text}")
            self.start.quack_sound.play()  # Play the quack sound
            if self.handle_usb_choice():
              return
            self.start.input_text = ""  # Clear input text


          elif event.key == pygame.K_BACKSPACE:
            self.start.input_text = self.start.input_text[:-1]
          else:
            self.start.input_text += event.unicode


      self.start.draw_input_field()
      pygame.display.flip()


  def check_password(self, password):
    if len(password) < 10 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[!@#$%^&*()_+=\[\]{};':\"\\|,.<>\/?-]", password):
      # Draw the background image
      self.start.draw_background(self.background_image)

      # Draw the red rectangle with a yellow border
      self.draw_rectangle_with_border(dimentions=self.usb_rect)
      self.draw_rectangle_with_border(dimentions=self.pc_rect)

      self.draw_text_with_background(
        f"""Votre mot de passe n'est pas sécurisé.""",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )

      pygame.display.flip()
      pygame.time.wait(2000)
      self.start.draw_background(self.background_image)
      self.draw_text_with_background(
        f"Créer un mot de passe sécurisé",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3)

      return False
    else:
      self.draw_text_with_background(
        f"""Votre mot de passe est assez sécurisé.""",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )
      pygame.display.update()
      self.enigme_cyber_2 = True
      return True

  def change_password_cyber(self):
    self.start.input_text = ""  # Reset input text for password input
    while True:
      # You can draw a prompt for the user on the screen here
      self.start.draw_input_field()
      self.draw_text_with_background(
        f"""Créer un nouveau mot de passe sécurisé.""",
        (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
        text_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        border_color=(0, 0, 0),
        padding=20,
        border_radius=30,
        border_width=3
      )
      pygame.display.update()

      running = True

      while running:

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
              self.start.quack_sound.play()
              if self.check_password(self.start.input_text):
                break
              else:
                self.draw_text_with_background(
                  f"""Votre mot de passe n'est pas sécurisé.""",
                  (self.start.SCREEN_WIDTH / 2, self.start.SCREEN_HEIGHT - 200),
                  text_color=(0, 0, 0),
                  bg_color=(255, 255, 255),
                  border_color=(0, 0, 0),
                  padding=20,
                  border_radius=30,
                  border_width=3
                )
                pygame.display.update()
                self.start.input_text = ""  # Reset password input
            elif event.key == pygame.K_BACKSPACE:
              self.start.input_text = self.start.input_text[:-1]
            else:
              self.start.input_text += event.unicode

  def load_cyber(self):
    cyber_on = True

    # Draw the background image
    self.start.draw_background(self.background_image)

    # Draw the red rectangle with a yellow border
    self.draw_rectangle_with_border(dimentions=self.usb_rect)
    self.draw_rectangle_with_border(dimentions=self.pc_rect)

    while cyber_on:
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
        #
        #   # Handle click on validation button
        #   if self.start.validate_button_rect.collidepoint(event.pos):
        #     print(f"Input validated: {self.start.input_text}")
        #     self.start.quack_sound.play()  # Play the quack sound
        #     self.start.input_text = ""  # Clear input text

          # Handle click on sound button
          # Draw the sound button
          self.start.draw_sound_button()
          if self.start.sound_button_rect.collidepoint(event.pos):
            self.start.music_muted = not self.start.music_muted
            if self.start.music_muted:
              pygame.mixer.music.pause()
              self.start.draw_sound_button()
            else:
              pygame.mixer.music.unpause()
              self.start.draw_sound_button()

          # Handle USB click
          if self.usb_rect.collidepoint(event.pos):
            self.start.quack_sound.play()
            self.usb_cyber()

          # Handle PC click
          if self.pc_rect.collidepoint(event.pos):
            self.start.quack_sound.play()
            self.change_password_cyber()

      # # Draw the background image
      # self.start.draw_background(self.background_image)
      #
      # # Draw the red rectangle with a yellow border
      # self.draw_rectangle_with_border(dimentions=self.usb_rect)
      # self.draw_rectangle_with_border(dimentions=self.pc_rect)


      # # Draw the input field
      # EscapeGame().draw_input_field()
      #
      # Draw the sound button
      self.start.draw_sound_button()

      # Update the display
      pygame.display.flip()

