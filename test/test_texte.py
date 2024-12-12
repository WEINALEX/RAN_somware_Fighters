import pygame
import sys

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
largeur_fenetre = 1000
hauteur_fenetre = 700
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Demander un Input")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (30, 36, 64)

# Police
font = pygame.font.SysFont('Arial', 30)
font_input = pygame.font.SysFont('Arial', 40)

# Charger l'image de fond
image_fond = pygame.image.load('./assets/img/door.png')  # Remplacez par le chemin de votre image
image_fond = pygame.transform.scale(image_fond, (largeur_fenetre, hauteur_fenetre))  # Redimensionner l'image pour qu'elle couvre l'écran

# Variables de texte
input_text = ''
max_input_length = 20  # Longueur maximale de l'input

# Fonction pour afficher le texte sur l'écran
def afficher_texte(texte, taille_font, y_position):
    text_surface = taille_font.render(texte, True, NOIR)
    text_rect = text_surface.get_rect(center=(largeur_fenetre // 2, y_position))

# Fonction principale du jeu
def boucle_principale(): # def pour un ecran ?
    
    global input_text
    clock = pygame.time.Clock()  # L'horloge est bien utilisée ici pour limiter les FPS

    while True:
        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Lorsque l'utilisateur appuie sur Entrée, afficher ce qu'il a entré
                    print(f"Donc votre nom est {input_text}")
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    # Supprimer un caractère si Backspace est pressé
                    input_text = input_text[:-1]
                else:
                    # Ajouter les caractères tapés (limité à une certaine longueur)
                    if len(input_text) < max_input_length:
                        input_text += event.unicode

        # Remplir l'écran avec l'image de fond
        fenetre.blit(image_fond, (0, 0))

        # Afficher le texte demandant un input
        afficher_texte("Bon, tout d'abord quel est votre nom ? :", font, hauteur_fenetre - 150)

        # Afficher l'input de l'utilisateur
        afficher_texte(input_text, font_input, hauteur_fenetre - 50)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter les images par seconde à 60
        clock.tick(60)

# Lancer la boucle principale
boucle_principale()
