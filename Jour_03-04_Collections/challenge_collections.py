# Challenge Jour 3-4 - Collections et Structures de Données
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Listes (60min)
# =============================================================================

print("=== PARTIE A - Listes ===")

# 1. Manipulation de base
films = ["Matrix", "Inception", "Interstellar"]
print(f"Films initiaux : {films}")

# TODO:
# - Ajoutez "Blade Runner" et "Dune" à la fin
# - Supprimez le premier film
# - Triez la liste par ordre alphabétique
# - Affichez le résultat final

# 2. Calculs sur listes de notes
notes = [15, 12, 18, 9, 16, 14, 11, 17]
print(f"Notes : {notes}")

# TODO: Calculez et affichez :
# - La moyenne des notes
# - La note minimum et maximum
# - Le nombre de notes supérieures à 15
# - La liste des notes paires uniquement

# 3. Filtrage et transformation
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Nombres : {nombres}")

# TODO: Créez ces nouvelles listes :
# - Liste des carrés de tous les nombres
# - Liste des nombres pairs uniquement
# - Liste des multiples de 3 uniquement

# =============================================================================
# PARTIE B - Dictionnaires (60min)
# =============================================================================

print("\n=== PARTIE B - Dictionnaires ===")

# 1. Profil utilisateur
utilisateur = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(f"Utilisateur initial : {utilisateur}")

# TODO:
# - Ajoutez l'email "alice@email.com"
# - Modifiez l'âge à 26
# - Affichez toutes les clés et valeurs séparément
# - Vérifiez si la clé "telephone" existe

# 2. Inventaire de magasin
inventaire = {
    "pommes": {"prix": 2.5, "stock": 50},
    "oranges": {"prix": 3.0, "stock": 30},
}
print(f"Inventaire initial : {inventaire}")

# TODO:
# - Ajoutez les bananes (prix: 2.8, stock: 40)
# - Calculez la valeur totale du stock (prix * stock pour chaque produit)
# - Affichez les produits dont le stock est inférieur à 35
# - Augmentez le stock des pommes de 20

# 3. Compteur de fréquence des mots
texte = "python est fantastique python est puissant python est facile"
mots = texte.split()  # Divise le texte en liste de mots
print(f"Mots : {mots}")

# TODO:
# - Créez un dictionnaire qui compte la fréquence de chaque mot
# - Affichez le mot le plus fréquent
# - Affichez tous les mots avec leur nombre d'occurrences

# =============================================================================
# PARTIE C - Tuples et Sets (30min)
# =============================================================================

print("\n=== PARTIE C - Tuples et Sets ===")

# 1. Coordonnées GPS et calcul de distance
paris = (48.8566, 2.3522)
london = (51.5074, -0.1278)
print(f"Paris : {paris}")
print(f"London : {london}")

# TODO:
# - Extrayez les latitudes et longitudes dans des variables séparées
# - Calculez la différence de latitude et longitude
# - Calculez une distance approximative (différence absolue)

# 2. Opérations sur les sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1 : {set1}")
print(f"Set 2 : {set2}")

# TODO: Calculez et affichez :
# - L'intersection (éléments communs)
# - L'union (tous les éléments)
# - La différence (éléments dans set1 mais pas dans set2)
# - La différence symétrique (éléments dans un seul des deux sets)

# 3. Suppression de doublons avec des sets
nombres_avec_doublons = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"Avec doublons : {nombres_avec_doublons}")

# TODO: Utilisez un set pour supprimer les doublons et reconvertir en liste

# =============================================================================
# MINI-PROJETS
# =============================================================================


# PROJET 1 - Gestionnaire de Courses (Jour 3)
def gestionnaire_courses():
    """Gestionnaire de liste de courses interactif"""
    courses = []

    while True:
        print("\n" + "=" * 30)
        print("    LISTE DE COURSES")
        print("=" * 30)
        print("1. Ajouter un article")
        print("2. Supprimer un article")
        print("3. Afficher la liste")
        print("4. Vider la liste")
        print("5. Nombre d'articles")
        print("0. Quitter")
        print("-" * 30)

        choix = input("Votre choix : ")

        if choix == "0":
            print("Au revoir !")
            break
        elif choix == "1":
            # TODO: Demander un article et l'ajouter à la liste
            pass
        elif choix == "2":
            # TODO: Demander quel article supprimer
            pass
        elif choix == "3":
            # TODO: Afficher tous les articles avec des numéros
            pass
        elif choix == "4":
            # TODO: Vider complètement la liste
            pass
        elif choix == "5":
            # TODO: Afficher le nombre total d'articles
            pass
        else:
            print("Choix invalide !")


# PROJET 2 - Carnet d'Adresses (Jour 4)
def carnet_adresses():
    """Carnet d'adresses avec dictionnaires"""
    contacts = {}
    # Structure : {nom: {"tel": "...", "email": "...", "ville": "..."}}

    while True:
        print("\n" + "=" * 35)
        print("     CARNET D'ADRESSES")
        print("=" * 35)
        print("1. Ajouter un contact")
        print("2. Rechercher un contact")
        print("3. Modifier un contact")
        print("4. Supprimer un contact")
        print("5. Lister tous les contacts")
        print("6. Contacts par ville")
        print("7. Nombre total de contacts")
        print("0. Quitter")
        print("-" * 35)

        choix = input("Votre choix : ")

        if choix == "0":
            print("Au revoir !")
            break
        elif choix == "1":
            # TODO: Demander nom, téléphone, email, ville et ajouter au dictionnaire
            pass
        elif choix == "2":
            # TODO: Rechercher un contact par nom
            pass
        elif choix == "3":
            # TODO: Modifier les informations d'un contact existant
            pass
        elif choix == "4":
            # TODO: Supprimer un contact
            pass
        elif choix == "5":
            # TODO: Afficher tous les contacts de manière formatée
            pass
        elif choix == "6":
            # TODO: Grouper et afficher les contacts par ville
            pass
        elif choix == "7":
            # TODO: Afficher le nombre total de contacts
            pass
        else:
            print("Choix invalide !")


# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================


def analyser_liste(liste):
    """Analyse complète d'une liste de nombres"""
    # TODO: Retournez un dictionnaire avec :
    # - nombre d'éléments
    # - somme, moyenne, min, max
    # - nombres pairs et impairs
    pass


def fusionner_dictionnaires(dict1, dict2):
    """Fusionne deux dictionnaires"""
    # TODO: Retournez un nouveau dictionnaire avec tous les éléments
    pass


def nettoyer_texte(texte):
    """Nettoie un texte et retourne les mots uniques"""
    # TODO:
    # - Convertir en minuscules
    # - Supprimer la ponctuation
    # - Retourner la liste des mots uniques
    pass


# =============================================================================
# TESTS ET EXÉCUTION
# =============================================================================

if __name__ == "__main__":
    print("🎯 Choisissez un projet à tester :")
    print("1. Gestionnaire de courses")
    print("2. Carnet d'adresses")
    print("3. Tests des fonctions utilitaires")

    choix = input("\nVotre choix (1-3) : ")

    if choix == "1":
        gestionnaire_courses()
    elif choix == "2":
        carnet_adresses()
    elif choix == "3":
        # Tests des fonctions utilitaires
        test_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"Analyse de {test_liste} :")
        # print(analyser_liste(test_liste))

        dict_a = {"a": 1, "b": 2}
        dict_b = {"c": 3, "d": 4}
        print(f"Fusion de {dict_a} et {dict_b} :")
        # print(fusionner_dictionnaires(dict_a, dict_b))

        texte_test = "Python, c'est fantastique! Python est puissant."
        print(f"Nettoyage de '{texte_test}' :")
        # print(nettoyer_texte(texte_test))

    print("\n🎉 Bravo ! Vous maîtrisez les collections Python !")
    print("⏭️ Passez maintenant aux Jour 5-6 : POO")
