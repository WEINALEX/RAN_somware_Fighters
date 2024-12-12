import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 1440
screen_height = 1024

# Couleurs (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (70, 130, 180)

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouton avec texte indenté")

# Choisir une police d'écriture
font = pygame.font.SysFont('Times', 10)  # On utilise une police de type "code" comme Consolas ou Courier New

def draw_button(x, y, width, height, text_lines, color_normal, color_hover):
    """
    Cette fonction dessine un bouton et affiche du texte multi-lignes à l'intérieur.
    - (x, y) = position du bouton
    - (width, height) = dimensions du bouton
    - text_lines = liste des lignes de texte
    - color_normal = couleur par défaut
    - color_hover = couleur au survol
    """
    # Position actuelle de la souris
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    
    # Change la couleur du bouton si la souris le survole
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, color_hover, button_rect)  # Couleur au survol
    else:
        pygame.draw.rect(screen, color_normal, button_rect)  # Couleur normale
    
    # Afficher chaque ligne de texte avec une indentation respectée
    for i, line in enumerate(text_lines):
        # Crée une surface de texte
        text_surface = font.render(line, True, WHITE)
        # Position du texte à l'intérieur du bouton (petit décalage de 10px sur la gauche et espacement vertical)
        text_rect = text_surface.get_rect(topleft=(x + 10, y + 10 + i * 30))
        screen.blit(text_surface, text_rect)  # Affiche la ligne de texte
    
    return button_rect

# Contenu du "pseudo-code" à afficher dans le bouton
code_lines = [
    "def age():",
    "    age = 20",
    "    if age < 18:",
    "        print(\"Vous ne pouvez pas étudier à MNS car vous êtes mineur\")",
    "    else:",
    "        print(\"Bienvenue à MNS\")",
    "",
    "age()"
]

# Boucle principale
running = True
while running:
    screen.fill(WHITE)  # Nettoie l'écran
    
    # 🟦 Dessiner un bouton (position x=300, y=200, largeur=400, hauteur=300)
    button_rect = draw_button(300, 150, 400, 150, code_lines, BLUE, LIGHT_BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Ferme la fenêtre
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie le clic de la souris
            if button_rect.collidepoint(event.pos):  # Si la position du clic est dans le bouton
                print("Le bouton contenant le code a été cliqué ! 🚀")
    
    pygame.display.update()  # Met à jour l'affichage

# Quitte Pygame proprement
pygame.quit()
sys.exit()
