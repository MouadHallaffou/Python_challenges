# Challenge Jour 1-2 - Fondamentaux Python
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Variables et Types (30min)
# =============================================================================

print("=== PARTIE A - Variables et Types ===")

# 1. Créez ces variables et affichez leurs types
nom = "Python"
version = 3.11
est_gratuit = True
prix = 0.0

# TODO: Affichez le nom et le type de chaque variable

# 2. Calculs rapides
a, b = 15, 4

# TODO: Calculez et affichez :
# - somme
# - différence
# - produit
# - division
# - modulo (reste)
# - puissance

# 3. Chaînes de caractères
phrase = "Apprendre Python en 10 jours"

# TODO: Affichez :
# - longueur de la phrase
# - phrase en majuscules
# - phrase en minuscules
# - premier caractère
# - dernier caractère

# =============================================================================
# PARTIE B - Conditions (45min)
# =============================================================================

print("\n=== PARTIE B - Conditions ===")

# 1. Système de notes
# TODO: Demandez une note à l'utilisateur et affichez la mention
# A: 16-20, B: 14-15, C: 12-13, D: 10-11, F: <10

# 2. Calculateur d'âge
# TODO: Demandez l'année de naissance et déterminez la catégorie
# enfant (<13), ado (13-17), adulte (18-64), senior (65+)

# 3. Vérificateur de mot de passe
# TODO: Vérifiez si un mot de passe respecte les critères :
# - au moins 8 caractères
# - contient au moins une majuscule
# - contient au moins un chiffre

# =============================================================================
# PARTIE C - Boucles (45min)
# =============================================================================

print("\n=== PARTIE C - Boucles ===")

# 1. Table de multiplication
# TODO: Demandez un nombre et affichez sa table de multiplication (1 à 10)

# 2. Compteur de voyelles
# TODO: Comptez les voyelles dans une phrase donnée par l'utilisateur

# 3. Suite de Fibonacci
# TODO: Affichez les 10 premiers termes de la suite de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# =============================================================================
# PARTIE D - Fonctions (45min)
# =============================================================================

print("\n=== PARTIE D - Fonctions ===")


# 1. Fonctions de calcul d'aire
def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle"""
    # TODO: Retournez l'aire
    pass


def aire_cercle(rayon):
    """Calcule l'aire d'un cercle"""
    # TODO: Retournez l'aire (π ≈ 3.14159)
    pass


# 2. Fonctions de validation
def est_email_valide(email):
    """Vérifie si un email est valide (contient @ et .)"""
    # TODO: Retournez True/False
    pass


def est_nombre_premier(n):
    """Vérifie si un nombre est premier"""
    # TODO: Retournez True/False
    pass


# 3. Fonction avec paramètre par défaut
def salutation(nom, titre="Monsieur/Madame"):
    """Génère une salutation"""
    # TODO: Retournez "Bonjour [titre] [nom]"
    pass


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
    # - Demander l'opération (+, -, *, /)
    # - Calculer et afficher le résultat
    # - Gérer la division par zéro
    pass


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
    # - Demander un nombre à l'utilisateur
    # - Comparer avec le nombre secret
    # - Donner des indices (plus grand/plus petit)
    # - Compter les tentatives
    # - Afficher victoire ou défaite

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
