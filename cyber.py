import pygame
import sys
import cyber

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1024
dark_blue = (13,26,61)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("Pygame Background Example")

# Load background image
# Replace 'background.jpg' with the path to your image file
path_file = './assets/'
background_image = pygame.image.load('./assets/img/background.png')

# Scale the image to cover the screen while maintaining its aspect ratio
image_rect = background_image.get_rect()

def draw_background():
    # Scale the image to cover the screen
    scale = max(SCREEN_WIDTH / image_rect.width, SCREEN_HEIGHT / image_rect.height)
    scaled_width = int(image_rect.width * scale)
    scaled_height = int(image_rect.height * scale)
    scaled_image = pygame.transform.scale(background_image, (scaled_width, scaled_height))

    # Center the image on the screen
    offset_x = (scaled_width - SCREEN_WIDTH) // 2
    offset_y = (scaled_height - SCREEN_HEIGHT) // 2
    screen.blit(scaled_image, (-offset_x, -offset_y))

# Load and play background music
# Replace 'background.mp3' with the path to your audio file
pygame.mixer.music.load('./assets/sounds/background.mp3')
pygame.mixer.music.play(-1)  # Play the music in a loop

# Load quack sound effect
quack_sound = pygame.mixer.Sound('./assets/sounds/quack.mp3')

# Load images for sound on, sound off, and duck icon
sound_on_image = pygame.image.load('./assets/img/sound_on.png')
sound_off_image = pygame.image.load('./assets/img/sound_off.png')
duck_image = pygame.image.load('./assets/img/duck.png')
# duck_image = pygame.transform.scale(duck_image, (60, 60))  # Resize duck image

# Resize images if necessary
sound_on_image = pygame.transform.scale(sound_on_image, (64, 64))
sound_off_image = pygame.transform.scale(sound_off_image, (64, 64))

# Button variables
sound_button_rect = pygame.Rect(SCREEN_WIDTH - 80, 20, 64, 64)
music_muted = False

# Input field variables
input_rect = pygame.Rect((SCREEN_WIDTH // 2) - 300, SCREEN_HEIGHT - 80, 600, 60)
input_color = (0, 0, 0)  # Black border
input_text = ""
font = pygame.font.Font(None, 36)

# Validation button variables
validate_button_rect = pygame.Rect((SCREEN_WIDTH // 2) + 320, SCREEN_HEIGHT - 80, 60, 60)


def draw_rounded_rect(surface, rect, color, radius):
    # Draw a rounded rectangle with transparency
    pygame.draw.rect(surface, color, rect, border_radius=radius)


def draw_sound_button():
    if music_muted:
        screen.blit(sound_off_image, sound_button_rect.topleft)
    else:
        screen.blit(sound_on_image, sound_button_rect.topleft)


def draw_input_field():
    # Bottom bar spanning the full width of the screen
    bar_rect = pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100)

    # Top bar spanning the full width of the screen
    bar_rect_top = pygame.Rect(0, 0, SCREEN_WIDTH, 100)

    # Left bar spanning the full height of the screen
    bar_rect_left = pygame.Rect(0, 0, 100, SCREEN_HEIGHT)

    # Right bar spanning the full height of the screen
    bar_rect_right = pygame.Rect(SCREEN_WIDTH - 100, 0, 100, SCREEN_HEIGHT)

    pygame.draw.rect(screen, dark_blue, bar_rect, border_radius=0)  # Dark blue bar
    pygame.draw.rect(screen, dark_blue, bar_rect_top, border_radius=0)  # Dark blue bar
    pygame.draw.rect(screen, dark_blue, bar_rect_left, border_radius=0)  # Dark blue bar
    pygame.draw.rect(screen, dark_blue, bar_rect_right, border_radius=0)  # Dark blue bar

    # Create a surface for the input field with transparency
    input_surface = pygame.Surface((input_rect.width, input_rect.height), pygame.SRCALPHA)
    input_surface.fill((0, 0, 0, 0))  # Fully transparent background

    # Draw the rounded background on the input surface
    draw_rounded_rect(input_surface, input_surface.get_rect(), (255, 255, 255), 30)  # ,128) for 50% transparent white

    # Blit the input surface onto the main screen
    screen.blit(input_surface, input_rect.topleft)

    # Draw the black border with rounded corners on the main screen
    pygame.draw.rect(screen, input_color, input_rect, 4, border_radius=30)

    # Render text and center it vertically in the input field
    text_surface = font.render(input_text, True, dark_blue)  # Color text
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)

    # Draw the validation button as a circle with a black border and duck icon
    screen.blit(duck_image, validate_button_rect.topleft)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle click on sound button
            if sound_button_rect.collidepoint(event.pos):
                music_muted = not music_muted
                if music_muted:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            # Handle click on validation button
            if validate_button_rect.collidepoint(event.pos):
                print(f"Input validated: {input_text}")
                quack_sound.play()  # Play the quack sound
                input_text = ""  # Clear input text

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(f"Input validated: {input_text}")
                quack_sound.play()  # Play the quack sound
                input_text = ""  # Clear input text
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Draw the background image
    draw_background()

    # Draw the input field
    draw_input_field()

    # Draw the sound button
    draw_sound_button()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

