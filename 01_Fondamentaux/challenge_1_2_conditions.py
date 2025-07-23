# Challenge 1.2 - Structures de Contrôle
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Conditions simples
# Votre code ici...

print("=" * 10, "Test de l'âge:", "=" * 10)
while True:
    try:
        age = int(input("Entrez votre âge ici: "))
        if age < 0:
            print("L'âge ne peut pas être négatif!")
            continue
        elif age < 18:
            print("Vous êtes mineur")
        else:
            print("Vous êtes majeur")
        break
    except ValueError:
        print("Il faut entrer un âge correct, sous forme de nombre!!")

# Challenge B - Conditions multiples
# Votre code ici...
print("=" * 10, "test de la note:", "=" * 10)
while True:
    try:
        note = float(input("entre la note ici (entre 0 et 20): "))
        if note < 0 or note > 20:
            print("La note doit être entre 0 et 20.")
            continue
        if note >= 16:
            print("Très bien")
        elif note >= 14:
            print("Bien")
        elif note >= 12:
            print("Assez bien")
        elif note >= 10:
            print("Passable")
        else:
            print("Insuffisant")
        break
    except ValueError:
        print("La note doit être un nombre entre 0 et 20.")

# Challenge C - Opérateurs logiques
# Votre code ici...
print("=" * 10, "Test du club:", "=" * 10)
while True:
    try:
        age = int(input("Entrez votre âge ici : "))
        if age < 0:
            print("L'âge ne peut pas être négatif!")
            continue

        if age >= 21:
            print("Accès autorisé (21 ans ou plus)")
            break
        elif age >= 18:
            carte = input("Avez-vous une carte de membre ? (oui/non): ").lower()
            if carte in ["oui", "o", "yes", "y"]:
                print("Accès autorisé (18+ avec carte)")
                break
            else:
                print("Accès refusé (18+ mais sans carte)")
                break
        else:
            print("Accès refusé (moins de 18 ans)")
            break
    except ValueError:
        print("Il faut respecter le type de l'âge !!")

# Challenge D - Conditions imbriquées
# Votre code ici...
print("=" * 10, "Test de l'IMC:", "=" * 10)
while True:
    try:
        poids = float(input("Entrez votre poids (kg): "))
        if poids <= 0:
            print("Le poids doit être positif!")
            continue

        taille = float(input("Entrez votre taille (m): "))
        if taille <= 0:
            print("La taille doit être positive!")
            continue

        # CORRECTION: IMC = poids / (taille²)
        IMC = poids / (taille**2)
        print(f"Votre IMC est: {IMC:.2f}")

        if IMC < 18.5:
            print("Catégorie: Maigreur")
        elif 18.5 <= IMC < 25:  # CORRECTION: utiliser 'and' au lieu de 'or'
            print("Catégorie: Normal")
        elif 25 <= IMC < 30:
            print("Catégorie: Surpoids")
        else:  # IMC >= 30
            print("Catégorie: Obésité")
            # Sous-catégories d'obésité
            if IMC >= 40:
                print("Sous-catégorie: Obésité morbide")
            elif IMC >= 35:
                print("Sous-catégorie: Obésité sévère")
            else:
                print("Sous-catégorie: Obésité modérée")
        break

    except ValueError:
        print("Vous devez entrer des nombres valides!")

# Challenge E - Logique complexe
# Votre code ici...
print("=" * 10, "Bienvenue dans votre jeu", "=" * 10)

import random

nombre_secret = random.randint(1, 100)
tentatives = 3

for essai in range(1, tentatives + 1):
    try:
        guess = int(
            input(f"Tentative {essai}/{tentatives} - Devinez le nombre (1-100): ")
        )

        if guess < 1 or guess > 100:
            print("Le nombre doit être entre 1 et 100!")
            continue

        difference = abs(nombre_secret - guess)

        if guess == nombre_secret:
            print(f"🎉 Bravo ! Trouvé en {essai} tentative(s) !")
            print(f"Le nombre secret était: {nombre_secret}")
            break
        elif guess < nombre_secret:
            if difference <= 5:
                print("Trop petit, mais vous êtes très proche !")
            elif difference >= 50:
                print("Trop petit, et vous êtes très loin !")
            else:
                print("Trop petit, essayez plus grand")
        else:  # guess > nombre_secret
            if difference <= 5:
                print("Trop grand, mais vous êtes très proche !")
            elif difference >= 50:
                print("Trop grand, et vous êtes très loin !")
            else:
                print("Trop grand, essayez plus petit")

    except ValueError:
        print("Veuillez entrer un nombre valide.")

else:
    print(f"😞 Dommage ! Le nombre secret était {nombre_secret}.")
