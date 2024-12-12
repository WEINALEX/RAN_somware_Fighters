import pygame
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 1000
hauteur_ecran = 700

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Chargement de l'image de fond
image_fond = pygame.image.load("./assets/img/hub_hub.png")  # Remplacez "background.jpg" par votre image

# Définir la taille de l'image de fond pour qu'elle remplisse l'écran
image_fond = pygame.transform.scale(image_fond, (largeur_ecran, hauteur_ecran)) #changer la taille par la taille de la petite fenetre.

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Interface avec boutons")

# Définir les boutons
largeur_bouton = 250 #quand on change la largeur il faut aussi gérer l'espacement pour que ca reste centrer
hauteur_bouton = 50
espacement = 20
font = pygame.font.Font(None, 25)

# Fonction des boutons
def fonction_bouton_1():
    print("Entrée dans la salle 101, renvoie vers Cyber. ")

def fonction_bouton_2():
    print("Entrée dans la salle 103, renvoie vers Dev. ")

def fonction_bouton_3():
    print("Entrée dans la salle 202, renvoie vers Tai. ")

# Liste des boutons et de leurs fonctions
boutons = [
    {"rect": pygame.Rect((largeur_ecran - largeur_bouton * 3 - espacement * 2) // 2, hauteur_ecran - hauteur_bouton - 10, largeur_bouton, hauteur_bouton), "label": "Entrer dans la salle 101", "fonction": fonction_bouton_1},
    {"rect": pygame.Rect((largeur_ecran - largeur_bouton * 3 - espacement * 2) // 2 + largeur_bouton + espacement, hauteur_ecran - hauteur_bouton - 10, largeur_bouton, hauteur_bouton), "label": "Entrer dans la salle 103", "fonction": fonction_bouton_2},
    {"rect": pygame.Rect((largeur_ecran - largeur_bouton * 3 - espacement * 2) // 2 + 2 * (largeur_bouton + espacement), hauteur_ecran - hauteur_bouton - 10, largeur_bouton, hauteur_bouton), "label": "Entrer dans la salle 202", "fonction": fonction_bouton_3},
]

# Fonction pour dessiner les boutons
def dessiner_boutons():
    for bouton in boutons:
        pygame.draw.rect(ecran, (30, 36, 64), bouton["rect"]) #couleur du bouton
        texte = font.render(bouton["label"], True, BLANC) #couleur du texte
        ecran.blit(texte, (bouton["rect"].x + (bouton["rect"].width - texte.get_width()) // 2, bouton["rect"].y + (bouton["rect"].height - texte.get_height()) // 2))

# Boucle principale du programme
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                for bouton in boutons:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f'posX: {mouse_x}, posY: {mouse_y}')

                    if bouton["rect"].collidepoint(event.pos):
                        bouton["fonction"]()  # Appel de la fonction associée au bouton

    # Affichage du fond et des éléments
    ecran.blit(image_fond, (0, 0))  # Affiche l'image de fond
    dessiner_boutons()  # Dessine les boutons

    # Actualiser l'écran
    pygame.display.flip()
