import pygame

# Initialize Pygame
pygame.init()

class EscapeGame:

    def __init__(self):
        # Set screen dimensions
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        self.dark_blue = (13,26,61)
        self.input_text = ""
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Set window title
        pygame.display.set_caption("Pygame Background Example")

        # Load background image
        # Replace 'background.jpg' with the path to your image file
        # path_file = './assets/'
        self.background_image = pygame.image.load('./assets/img/hub_door.png')

        self.load_music_assets()

    def load_music_assets(self):
        # Load and play background music
        # Replace 'background.mp3' with the path to your audio file
        pygame.mixer.music.load('./assets/sounds/background.mp3')
        # pygame.mixer.music.play(-1)  # Play the music in a loop

        # Load quack sound effect
        self.quack_sound = pygame.mixer.Sound('./assets/sounds/quack.mp3')

        # Load images for sound on, sound off, and duck icon
        self.sound_on_image = pygame.image.load('./assets/img/sound_on.png')
        self.sound_off_image = pygame.image.load('./assets/img/sound_off.png')
        self.duck_image = pygame.image.load('./assets/img/duck.png')
        # duck_image = pygame.transform.scale(duck_image, (60, 60))  # Resize duck image

        # Resize images if necessary
        self.sound_on_image = pygame.transform.scale(self.sound_on_image, (64, 64))
        self.sound_off_image = pygame.transform.scale(self.sound_off_image, (64, 64))

        # Button variables
        self.sound_button_rect = pygame.Rect(self.SCREEN_WIDTH - 80, 20, 64, 64)
        self.music_muted = False

        # Input field variables
        self.input_rect = pygame.Rect((self.SCREEN_WIDTH // 2) - 300, self.SCREEN_HEIGHT - 80, 600, 60)
        self.input_color = (0, 0, 0)  # Black border

        # Validation button variables
        self.validate_button_rect = pygame.Rect((self.SCREEN_WIDTH // 2) + 320, self.SCREEN_HEIGHT - 80, 60, 60)

    def draw_background(self, image):
        # Scale the image to cover the screen
        self.image = pygame.transform.scale(image, (self.screen.get_width() - 200, self.screen.get_height() - 300))
        self.image_rect = self.image.get_rect()
        # self.scale = max(self.SCREEN_WIDTH / self.image_rect.width, self.SCREEN_HEIGHT / self.image_rect.height)
        # self.scaled_width = int(self.image_rect.width * self.scale)
        # self.scaled_height = int(self.image_rect.height * self.scale)
        # self.scaled_image = pygame.transform.scale(self.background_image, (self.scaled_width, self.scaled_height))

        # Center the image on the screen
        # self.offset_x = (self.scaled_width - self.SCREEN_WIDTH) // 2
        # self.offset_y = (self.scaled_height - self.SCREEN_HEIGHT) // 2
        self.screen.fill(self.dark_blue)
        self.screen.blit(self.image, (100, 100))

    def draw_rounded_rect(self, surface, rect, color, radius):
        # Draw a rounded rectangle with transparency
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def draw_sound_button(self):
        if self.music_muted:
            self.screen.blit(self.sound_off_image, self.sound_button_rect.topleft)
        else:
            self.screen.blit(self.sound_on_image, self.sound_button_rect.topleft)

    def draw_input_field(self):
        # Bottom bar spanning the full width of the screen
        # bar_rect = pygame.Rect(0, self.SCREEN_HEIGHT - 100, self.SCREEN_WIDTH, 100)

        # Top bar spanning the full width of the screen
        # bar_rect_top = pygame.Rect(0, 0, self.SCREEN_WIDTH, 100)

        # Left bar spanning the full height of the screen
        # bar_rect_left = pygame.Rect(0, 0, 100, self.SCREEN_HEIGHT)

        # Right bar spanning the full height of the screen
        # bar_rect_right = pygame.Rect(self.SCREEN_WIDTH - 100, 0, 100, self.SCREEN_HEIGHT)

        # pygame.draw.rect(self.screen, self.dark_blue, bar_rect, border_radius=0)  # Dark blue bar
        # pygame.draw.rect(self.screen, self.dark_blue, bar_rect_top, border_radius=0)  # Dark blue bar
        # pygame.draw.rect(self.screen, self.dark_blue, bar_rect_left, border_radius=0)  # Dark blue bar
        # pygame.draw.rect(self.screen, self.dark_blue, bar_rect_right, border_radius=0)  # Dark blue bar

        # Create a surface for the input field with transparency
        self.input_surface = pygame.Surface((self.input_rect.width, self.input_rect.height), pygame.SRCALPHA)
        self.input_surface.fill((0, 0, 0, 0))  # Fully transparent background

        # Draw the rounded background on the input surface
        self.draw_rounded_rect(self.input_surface, self.input_surface.get_rect(), (255, 255, 255), 30)  # ,128) for 50% transparent white

        # Blit the input surface onto the main screen
        self.screen.blit(self.input_surface, self.input_rect.topleft)

        # Draw the black border with rounded corners on the main screen
        pygame.draw.rect(self.screen, self.input_color, self.input_rect, 4, border_radius=30)

        # Render text and center it vertically in the input field
        text_surface = self.font.render(self.input_text, True, self.dark_blue)  # Color text
        text_rect = text_surface.get_rect(center=self.input_rect.center)
        self.screen.blit(text_surface, text_rect)

        # Draw the validation button as a circle with a black border and duck icon
        self.screen.blit(self.duck_image, self.validate_button_rect.topleft)

EscapeGame()