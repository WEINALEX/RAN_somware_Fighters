import re
 #mot de passe de la salle 202
mdp_salle101="101"
#le code se déclenche si le mot de passe de la salle est correct

if mot_de_passe_salle_cyber==mdp_salle101:
    print("Bienvenue dans la salle 101")

def check_password(password):
  """
  Vérifie si un mot de passe est sécurisé.

  Un mot de passe sécurisé doit comporter au moins 10 caractères, une lettre majuscule, 
  une lettre minuscule, au moins un chiffre et un caractère spécial.

  Args:
    password: Le mot de passe à vérifier.

  Returns:
    True si le mot de passe est sécurisé, False sinon.
  """
  if len(password) < 10:
    return False
  if not re.search("[a-z]", password):
    return False
  if not re.search("[A-Z]", password):
    return False
  if not re.search("[0-9]", password):
    return False
  if not re.search("[!@#$%^&*()_+=\[\]{};':\"\\|,.<>\/?-]", password):
    return False
  return True


#pygame image d'accueil de la salle 202 : Taille 1440x1024px

enigme_cyber_1=False #USB
enigme_cyber_2=False #Mot de passe
enigme_cyber_3=False #Social Engineering
enigme_cyber_4=False #Phishing

#pygame clic sur le bloc mot de passe

#si clic sur l'ordinateur, pour changement de mdp : 
nb_text_mdp_cyber=0
while True:
  password = input("Entrez un nouveau mot de passe : ")
  if check_password(password):
    print("Mot de passe accepté.")
    enigme_cyber_2=True
    break
  else:
    print("Mot de passe non sécurisé. Veuillez réessayer.")
    nb_text_mdp_cyber+=1
    if nb_text_mdp_cyber>=3:
      print("Pour rappel, un mot de passe sécurisé doit comporter au moins 10 caractères, une lettre majuscule, une lettre minuscule, au moins un chiffre et un caractère spécial.")

#pygame clic sur le bloc USB

def usb_cyber():
    print("Vous avez trouvé une clé USB.")
  #choix multiple : si branchement de clef USB afficher un message d'erreur et des rappels sur la cybersécurité, si l'on choisit de laisser la clef USB sans la brancher, afficher un message de félicitations et des informations sur la cybersécurité
    choix_usb=input("Voulez-vous brancher la clé USB ? (oui/non)")
    if choix_usb=="oui":
        print("Erreur : ne branchez jamais une clé USB inconnue sur votre ordinateur.\nLes clés USB peuvent contenir des virus et des logiciels malveillants.")
    elif choix_usb=="non":
        print("Félicitations ! Vous avez fait preuve de prudence.\nLes clés USB peuvent contenir des virus et des logiciels malveillants.")
    enigme_cyber_1=True
    return

if enigme_cyber_1==True and enigme_cyber_2==True:

#Apparition du splash screen avec l'individu louche
#pygame clic sur le bloc Social Engineering

def social_engineering_cyber():
    error_social_engineering=0
    print("Élève MNS : Salut, je suis nouveau! Toi aussi tu es en cybersecurité?")
    print("user.name : Oui, je suis en cybersecurité.")
    print("Élève MNS : C'est pas super facile comme cours, tu ne trouves pas?")
    print("user.name : Si, c'est vrai que c'est un peu difficile.")
    print("Élève MNS : Je suis en réorientation, tu as fais quel lycée toi?")
    if input("Entrez une réponse")==reponse_nathalie_lycee:
        print("Élève MNS : Ah, moi aussi! On a dû se croiser là-bas.")
        error_social_engineering+=1
    else:
       print("Élève MNS : Ah, d'accord ! Je n'étais pas là-bas moi")
    print("Élève MNS : Tu habites dans le coin par hasard? J'ai l'impression de t'avoir déjà croisé")
    if input("Entrez une réponse")==reponse_nathalie_adresse:
        print("Élève MNS : Ah, c'est bien ce que je pensais! On habite dans le même quartier.")
        error_social_engineering+=1
    else: 
        print("Élève MNS : Ah, d'accord ! Je ne suis pas du coin.")
    print("Élève MNS : Tu as des frères et soeurs? Tu as l'air d'avoir une grande famille.")
    if input("Entrez une réponse")==reponse_nathalie_famille:
        print("Élève MNS : Ah, c'est bien ce que je pensais! Tu as une grande famille.")
        error_social_engineering+=1
    else:
        print("Élève MNS : Ah, d'accord ! Pas de soucis.")
    print("Élève MNS : Tu as des animaux ?")
    if input("Entrez une réponse")==reponse_nathalie_animaux:
        print("Élève MNS : Ah, c'est bien ce que je pensais!")
        error_social_engineering+=1
    else:
           print("Élève MNS : Ah, d'accord !")
    print("Élève MNS : Je n'arrive pas à accéder à mon PC, tu peux me donner ton ID s'il te plait pour que je puisse me connecter ?.")
    if input("Entrez une réponse")==reponse_nathalie_ID:
        print("Élève MNS : Merci beaucoup! Je vais pouvoir me connecter maintenant.")
        error_social_engineering+=1
    else:
       print("Élève MNS : D'accord, je vais demander à quelqu'un d'autre.")
    print("Élève MNS : Bon hé bien je te laisse")
    print("user.name : D'accord, à plus tard!")

    if error_social_engineering>=3:
       print("Vous avez donné trop d'informations personnelles. Attention au Social Engineering!")
    else:
       print("Vous avez fait preuve de prudence. Attention au Social Engineering!")
    enigme_cyber_3=True

if enigme_cyber_3==True:
   
#pygame clic sur le bloc Phishing

def phishing_cyber():
   #images des mails



  


