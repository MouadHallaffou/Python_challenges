# Challenge 1.3 - Boucles
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Boucle for basique
# Votre code ici...
# - Affichent les nombres de 1 à 10
for i in range(1,11) :
    print(f"number: {i}")
# - Affichent les nombres pairs de 0 à 20
for i in range (1,21) :
    if i%2 == 0 :
        print(i)
    else :
        continue
# - Affichent les nombres de 10 à 1 (compte à rebours)
for i in range (10,0,-1) : 
    print(i)
# - Calculez la somme des nombres de 1 à 100
j = 0
for i in range (100) :
    j += i
print(j)

# Challenge B - Boucle while
# Votre code ici...
# - Demandent un mot de passe jusqu'à ce que l'utilisateur tape "secret"
alternative =""
password = "s"
while password != alternative :
    alternative = str(input("entre le password: "))
    if alternative != password:
       print("Mot de passe incorrect, essayez encore!")
print(" access autorise")

# - Comptent de 0 à 50 par pas de 5
nmbr = 50
while i < nmbr :
    if i%5 == 0 :
        print(i)
        continue

# - Calculent la factorielle d'un nombre (ex: 5! = 5×4×3×2×1)
nubr = int(input("entre le nmbr: "))
fact = 1
compt = nubr
while compt > 0 :
    fact *= compt
    compt -= 1
print(nubr,"!","=", fact)

# Challenge C - Boucles avec break et continue
# Votre code ici...
# - Affichez les nombres de 1 à 20, mais :
#   - Sautez les multiples de 3 (continue)
#   - Arrêtez si vous atteignez 15 (break)
for i in range(1,21):
    if i%3==0:
        print(i)
        continue
    elif i>=15 :
        break

# - Créez un menu qui tourne jusqu'à ce que l'utilisateur choisisse "Quitter"
print("="*10,"menu","="*10)
print("1-acceuil")
print("2-contact")
print("0-quitter")
for choix in range(3) :
    choix = int(input("choisir votre choix (ex: 1, 2, 0): "))
    if choix == 0 :
        print("au revoir!")
        break
    else :
        print("try again")
        continue

# Challenge D - Itération sur chaînes
# Votre code ici...
# - Comptent le nombre de voyelles dans une phrase
voiyelle = ["a","u","e","i","o","y"]
phrase = input("entre votre phrase ici: ")
compteur = sum(1 for lettre in phrase.lower() if lettre in voiyelle)
print("le numbre de voiyelle dans cette phrase est: ", compteur)

# - Inversent une chaîne caractère par caractère
chaine = input('entre your chaine ici : ')
converting = chaine[::-1]
print(converting)

# - Trouvent la position de chaque lettre 'a' dans un texte
texte = input("Entrez un texte : ")
lettre_searched = input("entre le lettre : ")
positions = [i+1 for i, lettre in enumerate(texte) if lettre == lettre_searched]
print("Positions de ", lettre_searched,":", positions)

# - Remplacent tous les espaces par des tirets
phrase = input("entre votre text : ")
phrase_tired = "-".join(phrase.split())
print(phrase_tired)

# Challenge E - Boucles imbriquées et patterns
# Votre code ici...
# 1. Triangle de nombres :
for i in range (1, 6):
    for j in range (i, i+1):
        print(i)
    print("")

# 2. Pyramide d'étoiles :
hauteur = int(input("entre la hauteur du pyramide: "))
for i in range(1, hauteur + 1):
    print(("*" * (2*i - 1)).center(2*hauteur - 1))

# 3. Table de multiplication (de 1 à 10)
nbr = int(input("entre le nbr de multiplucation: "))
for i in range (1, 11):
        print(nbr, "X", i, "=", nbr*i)

# 4. Créez un jeu de "Plus ou Moins" :
#    - L'ordinateur choisit un nombre entre 1 et 100
#    - L'utilisateur devine jusqu'à ce qu'il trouve
#    - Comptez le nombre de tentatives
#    - Proposez de rejouer
import random

while True:
    nbr = random.randint(1, 100)
    nbr_tentatives = 0
    while True:
        inputs = int(input("Entrez le nombre : "))
        nbr_tentatives += 1
        if nbr == inputs:
            print("Bravo ! Vous avez réussi en", nbr_tentatives, "tentatives.")
            break
        elif nbr > inputs:
            print("Votre choix est trop petit.")
        else:
            print("Votre choix est trop grand.")
    rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
    if rejouer != "o":
        print("Merci d'avoir joué !")
        break
