# Challenge Jour 1-2 - Fondamentaux Python
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Variables et Types (30min)
# =============================================================================

from datetime import date


print("=== PARTIE A - Variables et Types ===")

# 1. Créez ces variables et affichez leurs types
nom = "Python"
version = 3.11
est_gratuit = True
prix = 0.0

# TODO: Affichez le nom et le type de chaque variable
print(f"Nom: {nom} (Type: {type(nom)})")
print(f"Version: {version} (Type: {type(version)})")
print(f"Est gratuit: {est_gratuit} (Type: {type(est_gratuit)})")
print(f"Prix: {prix} (Type: {type(prix)})")

# 2. Calculs rapides
a, b = 15, 4

# TODO: Calculez et affichez :
# - somme
somme = a + b
print(f"Somme: {somme}")
# - différence
difference = a - b
print(f"Différence: {difference}")
# - produit
produit = a * b
print(f"Produit: {produit}")
# - division
division = a / b
print(f"Division: {division}")
# - modulo (reste)
modulo = a % b
print(f"Modulo: {modulo}")
# - puissance
puissance = a ** b
print(f"Puissance: {puissance}")

# 3. Chaînes de caractères
phrase = "Apprendre Python en 10 jours"

# TODO: Affichez :
# - longueur de la phrase
longueur = len(phrase)
print(f"Longueur de la phrase: {longueur}")
# - phrase en majuscules
majuscule = phrase.upper()
print(f"Phrase en majuscules: {majuscule}")
# - phrase en minuscules
minuscule = phrase.lower()
print(f"Phrase en minuscules: {minuscule}")
# - premier caractère
premier_caractere = phrase[0]
print(f"Premier caractère: {premier_caractere}")
# - dernier caractère
dernier_caractere = phrase[-1]
print(f"Dernier caractère: {dernier_caractere}")

# =============================================================================
# PARTIE B - Conditions (45min)
# =============================================================================

print("\n=== PARTIE B - Conditions ===")

# 1. Système de notes
# TODO: Demandez une note à l'utilisateur et affichez la mention
# A: 16-20, B: 14-15, C: 12-13, D: 10-11, F: <10
note = float(input("Entrez une note (0-20): "))

if 16 <= note <= 20:
    mention = "A"
elif 14 <= note < 16:
    mention = "B"
elif 12 <= note < 14:
    mention = "C"
elif 10 <= note < 12:
    mention = "D"
else:
    mention = "F"

print(f"Mention: {mention}")

# 2. Calculateur d'âge
# TODO: Demandez l'année de naissance et déterminez la catégorie
# enfant (<13), ado (13-17), adulte (18-64), senior (65+)

annee_naissance = int(input("Entrez votre année de naissance: "))
age = date.today().year - annee_naissance

if age < 13:
    categorie = "enfant"
elif 13 <= age <= 17:
    categorie = "ado"
elif 18 <= age <= 64:
    categorie = "adulte"
else:
    categorie = "senior"

print(f"Catégorie: {categorie}")

# 3. Vérificateur de mot de passe
# TODO: Vérifiez si un mot de passe respecte les critères :
# - au moins 8 caractères
# - contient au moins une majuscule
# - contient au moins un chiffre
mot_de_passe = input("Entrez un mot de passe (min 8 caractères, 1 majuscule, 1 chiffre): ")

if (len(mot_de_passe) >= 8 and
        any(c.isupper() for c in mot_de_passe) and
        any(c.isdigit() for c in mot_de_passe)):
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")

# =============================================================================
# PARTIE C - Boucles (45min)
# =============================================================================

print("\n=== PARTIE C - Boucles ===")

# 1. Table de multiplication
# TODO: Demandez un nombre et affichez sa table de multiplication (1 à 10)
nombre = int(input("Entrez un nombre pour sa table de multiplication: "))

for i in range(1, 11):
    print(f"{nombre} x {i} = {nombre * i}")

# 2. Compteur de voyelles
# TODO: Comptez les voyelles dans une phrase donnée par l'utilisateur
phrase = input("Entrez une phrase: ")
voyelles = "aeiouyAEIOUY"
compteur = sum(1 for c in phrase if c in voyelles)
print(f"Nombre de voyelles: {compteur}")

# 3. Suite de Fibonacci
# TODO: Affichez les 10 premiers termes de la suite de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(f"Suite de Fibonacci: {fibonacci}")

# =============================================================================
# PARTIE D - Fonctions (45min)
# =============================================================================

print("\n=== PARTIE D - Fonctions ===")


# 1. Fonctions de calcul d'aire
def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle"""
    # TODO: Retournez l'aire
    return longueur * largeur

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle"""
    # TODO: Retournez l'aire (π ≈ 3.14159)
    return 3.14159 * rayon**2

# 2. Fonctions de validation
def est_email_valide(email):
    """Vérifie si un email est valide (contient @ et .)"""
    # TODO: Retournez True/False
    return "@" in email and "." in email
print("Exemple d'email valide:", est_email_valide("exemple@domaine.com")) # True
print("Exemple d'email invalide:", est_email_valide("exemple@domaine")) # False

def est_nombre_premier(n):
    """Vérifie si un nombre est premier"""
    # TODO: Retournez True/False
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Fonction avec paramètre par défaut
def salutation(nom, titre="Monsieur/Madame"):
    """Génère une salutation"""
    # TODO: Retournez "Bonjour [titre] [nom]"
    return f"Bonjour {titre} {nom}"

# TODO: Testez toutes vos fonctions

# =============================================================================
# MINI-PROJETS
# =============================================================================


# PROJET 1 - Calculatrice Interactive
def calculatrice():
    """Calculatrice simple avec 4 opérations"""
    print("\n=== CALCULATRICE ===")

    # TODO: Implémentez la calculatrice
    # - Demander deux nombres
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))
    # - Demander l'opération (+, -, *, /)
    operation = input("Entrez l'opération (+, -, *, /): ")      
    # - Calculer et afficher le résultat
    # - Gérer la division par zéro
    if operation == "+":
        print(f"Résultat: {nombre1 + nombre2}")
    elif operation == "-":
        print(f"Résultat: {nombre1 - nombre2}")
    elif operation == "*":
        print(f"Résultat: {nombre1 * nombre2}")
    elif operation == "/":
        if nombre2 != 0:
            print(f"Résultat: {nombre1 / nombre2}")
        else:
            print("Erreur: Division par zéro non permise.")
    else:
        print("Opération invalide.")

# PROJET 2 - Jeu de Devinette
def jeu_devinette():
    """Jeu de devinette de nombre"""
    import random

    secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 7

    print("\n=== JEU DE DEVINETTE ===")
    print("Devinez un nombre entre 1 et 100!")
    print(f"Vous avez {max_tentatives} tentatives.")

    # TODO: Implémentez le jeu
    # - Boucle pour les tentatives
    while tentatives < max_tentatives:
        # - Demander un nombre à l'utilisateur
        proposition = int(input("Entrez votre proposition: "))
        tentatives += 1

        # - Comparer avec le nombre secret
        if proposition == secret:
            print("Félicitations! Vous avez deviné le nombre.")
            break
        elif proposition < secret:
            print("C'est plus grand!")
        else:
            print("C'est plus petit!")

    # - Afficher victoire ou défaite
    if tentatives == max_tentatives:
        print(f"Vous avez épuisé vos tentatives. Le nombre secret était {secret}.")

    pass


# =============================================================================
# TESTS ET EXÉCUTION
# =============================================================================

if __name__ == "__main__":
    # Décommentez les parties que vous voulez tester :

    # calculatrice()
    # jeu_devinette()

    print("\n🎉 Bravo ! Vous avez terminé les fondamentaux Python !")
    print("⏭️ Passez maintenant aux Jour 3-4 : Collections")
