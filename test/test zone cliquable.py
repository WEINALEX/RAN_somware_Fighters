import pygame
import sys

# meme principe q'un bouton, un zone qu'on place ou on veut sans bouton 
# et plus bas ajout d'une petite icon qui remplace le cuseur quand il entre dans la zone + le clic qui fait quelque chose.



# Initialisation de pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 800
hauteur_ecran = 600

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Chargement de l'image de fond
image_fond = pygame.image.load("background.jpg")  # Remplacez par votre image de fond
image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Zone Cliquable et Curseur")

# Définir la zone cliquable (par exemple, un petit carré dans le coin supérieur gauche)
zone_cliquable = pygame.Rect(50, 50, 100, 100)  # Zone de 100x100 pixels à la position (50, 50)

# Chargement d'un curseur personnalisé (facultatif)
curseur_personnalise = pygame.image.load("curseur.png")  # Remplacez par le chemin de votre curseur personnalisé
curseur_personnalise = pygame.transform.scale(curseur_personnalise, (32, 32))  # Redimensionner le curseur si nécessaire

# Fonction pour changer l'image de fond
def fonction_zone_cliquable():
    print("Zone cliquée !")
    # Par exemple, vous pouvez changer l'image de fond ou exécuter d'autres actions
    global image_fond
    image_fond = pygame.image.load("nouveau_background.jpg")  # Change l'image de fond
    image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran))

# Boucle principale du programme
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                if zone_cliquable.collidepoint(event.pos):
                    fonction_zone_cliquable()  # Appeler la fonction lorsqu'on clique dans la zone

    # Gestion du curseur personnalisé
    souris_pos = pygame.mouse.get_pos()
    if zone_cliquable.collidepoint(souris_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Changer le curseur en main (pour la zone cliquable)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Retour au curseur par défaut

    # Affichage du fond et de la zone cliquable
    ecran.blit(image_fond, (0, 0))  # Affiche l'image de fond
    pygame.draw.rect(ecran, (255, 0, 0), zone_cliquable)  # Dessine la zone cliquable en rouge

    # Actualiser l'écran
    pygame.display.flip()
