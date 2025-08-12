# Challenge 1.3 - Boucles

# Challenge A - Boucle for basique

# Affiche les nombres de 1 à 10
for nombre in range(1, 11):
    print(f"number: {nombre}")

# Affiche les nombres pairs de 0 à 20
for nombre in range(0, 21):
    if nombre % 2 == 0:
        print(nombre)

# Affiche les nombres de 10 à 1 (compte à rebours)
for nombre in range(10, 0, -1):
    print(nombre)

# Calcule la somme des nombres de 1 à 100
somme = 0
for nombre in range(1, 101):
    somme += nombre
print("la somme des nombres de 1 à 100 est: ",somme)

# Challenge B - Boucle while

# Demande un mot de passe jusqu'à ce que l'utilisateur tape "secret"
mot_de_passe = "secret"
saisie = ""
while saisie != mot_de_passe:
    saisie = input("Entrez le mot de passe : ")
    if saisie != mot_de_passe:
        print("Mot de passe incorrect, essayez encore !")
print("Accès autorisé")

# Compte de 0 à 50 par pas de 5
compteur = 0
while compteur <= 50:
    print(compteur)
    compteur += 5

# Calcule la factorielle d'un nombre
nombre = int(input("Entrez un nombre : "))
factorielle = 1
compteur = nombre
while compteur > 0:
    factorielle *= compteur
    compteur -= 1
print(f"{nombre}! = {factorielle}")

# Challenge C - Boucles avec break et continue

# Affiche les nombres de 1 à 20, saute les multiples de 3, arrête à 15
for nombre in range(1, 21):
    if nombre % 3 == 0:
        continue
    if nombre >= 15:
        break
    print(nombre)

# Menu qui tourne jusqu'à ce que l'utilisateur choisisse "Quitter"
while True:
    print("="*10, "Menu", "="*10)
    print("1 - Accueil")
    print("2 - Contact")
    print("0 - Quitter")
    choix = int(input("Choisissez une option (ex: 1, 2, 0): "))
    if choix == 0:
        print("Au revoir !")
        break
    else:
        print("Option invalide, essayez encore.")

# Challenge D - Itération sur chaînes

# Compte le nombre de voyelles dans une phrase
voyelles = "aeiouy"
phrase = input("Entrez votre phrase ici : ")
compteur_voyelles = sum(1 for lettre in phrase.lower() if lettre in voyelles)
print("Le nombre de voyelles dans cette phrase est :", compteur_voyelles)

# Inverse une chaîne caractère par caractère
chaine = input('Entrez votre chaîne ici : ')
chaine_inversee = chaine[::-1]
print(chaine_inversee)

# Trouve la position de chaque lettre choisie dans un texte
texte = input("Entrez un texte : ")
lettre_recherchee = input("Entrez la lettre à rechercher : ")
positions = [i + 1 for i, lettre in enumerate(texte) if lettre == lettre_recherchee]
print(f"Positions de '{lettre_recherchee}'est :", positions)

# Remplace tous les espaces par des tirets
phrase = input("Entrez votre texte : ")
phrase_tirets = "-".join(phrase.split())
print(phrase_tirets)

# Challenge E - Boucles imbriquées et patterns

# 1. Triangle de nombres
for ligne in range(1, 6):
    print(str(ligne) * ligne)

# 2. Pyramide d'étoiles
hauteur = int(input("Entrez la hauteur de la pyramide : "))
for i in range(1, hauteur + 1):
    print(("*" * (2 * i - 1)).center(2 * hauteur - 1))

# 3. Table de multiplication (de 1 à 10)
nombre = int(input("Entrez le nombre pour la table de multiplication : "))
for multiplicateur in range(1, 11):
    print(f"{nombre} x {multiplicateur} = {nombre * multiplicateur}")

# 4. Jeu de 'Plus ou Moins'
import random

while True:
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    while True:
        proposition = int(input("Entrez le nombre : "))
        tentatives += 1
        if proposition == nombre_secret:
            print(f"Bravo ! Vous avez réussi en {tentatives} tentatives.")
            break
        elif proposition < nombre_secret:
            print("Votre choix est trop petit.")
        else:
            print("Votre choix est trop grand.")
    rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
    if rejouer != "o":
        print("Merci d'avoir joué !")
        break
