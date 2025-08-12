# Challenge Jour 3-4 - Collections et Structures de Données
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Listes (60min)
# =============================================================================

print("=== PARTIE A - Listes ===")

# 1. Manipulation de base
films = ["Matrix", "Inception", "Interstellar"]
print(f"Films initiaux : {films}")

# Ajout de films
films.extend(["Blade Runner", "Dune"])
print(f"Après ajout : {films}")

# Suppression du premier film
premier_film = films.pop(0)
print(f"Film supprimé : {premier_film}")
print(f"Après suppression : {films}")

# Tri alphabétique
films.sort()
print(f"Films triés : {films}")

# 2. Calculs sur listes de notes
notes = [15, 12, 18, 9, 16, 14, 11, 17]
print(f"Notes : {notes}")

# Calculs sur les notes
moyenne = sum(notes) / len(notes)
note_min = min(notes)
note_max = max(notes)
notes_superieures_15 = len([note for note in notes if note > 15])
notes_paires = [note for note in notes if note % 2 == 0]

print(f"Moyenne : {moyenne:.2f}")
print(f"Note minimum : {note_min}")
print(f"Note maximum : {note_max}")
print(f"Notes > 15 : {notes_superieures_15}")
print(f"Notes paires : {notes_paires}")

# 3. Filtrage et transformation
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Nombres : {nombres}")

# Création des nouvelles listes
carres = [n**2 for n in nombres]
pairs = [n for n in nombres if n % 2 == 0]
multiples_3 = [n for n in nombres if n % 3 == 0]

print(f"Carrés : {carres}")
print(f"Nombres pairs : {pairs}")
print(f"Multiples de 3 : {multiples_3}")

# =============================================================================
# PARTIE B - Dictionnaires (60min)
# =============================================================================

print("\n=== PARTIE B - Dictionnaires ===")

# 1. Profil utilisateur
utilisateur = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(f"Utilisateur initial : {utilisateur}")

# Modification du profil utilisateur
utilisateur["email"] = "alice@email.com"
utilisateur["age"] = 26

print(f"Utilisateur modifié : {utilisateur}")
print(f"Clés : {list(utilisateur.keys())}")
print(f"Valeurs : {list(utilisateur.values())}")

# Vérification de l'existence d'une clé
if "telephone" in utilisateur:
    print("Le téléphone existe")
else:
    print("Le téléphone n'existe pas")

# 2. Inventaire de magasin
inventaire = {
    "pommes": {"prix": 2.5, "stock": 50},
    "oranges": {"prix": 3.0, "stock": 30},
}
print(f"Inventaire initial : {inventaire}")

# Gestion de l'inventaire
inventaire["bananes"] = {"prix": 2.8, "stock": 40}
print(f"Inventaire avec bananes : {inventaire}")

# Calcul de la valeur totale
valeur_totale = 0
for produit, infos in inventaire.items():
    valeur = infos["prix"] * infos["stock"]
    valeur_totale += valeur
    print(f"{produit}: {infos['stock']} × {infos['prix']}€ = {valeur}€")

print(f"Valeur totale du stock : {valeur_totale}€")

# Produits avec stock < 35
print("Produits avec stock < 35 :")
for produit, infos in inventaire.items():
    if infos["stock"] < 35:
        print(f"- {produit}: {infos['stock']} unités")

# Augmentation du stock des pommes
inventaire["pommes"]["stock"] += 20
print(f"Stock pommes après augmentation : {inventaire['pommes']['stock']}")

# 3. Compteur de fréquence des mots
texte = "python est fantastique python est puissant python est facile"
mots = texte.split()  # Divise le texte en liste de mots
print(f"Mots : {mots}")

# Comptage de fréquence des mots
frequence_mots = {}
for mot in mots:
    if mot in frequence_mots:
        frequence_mots[mot] += 1
    else:
        frequence_mots[mot] = 1

print(f"Fréquence des mots : {frequence_mots}")

# Mot le plus fréquent
mot_plus_frequent = max(frequence_mots.keys(), key=lambda mot: frequence_mots[mot])
print(
    f"Mot le plus fréquent : '{mot_plus_frequent}' ({frequence_mots[mot_plus_frequent]} fois)"
)

# Affichage de tous les mots avec occurrences
print("Tous les mots avec leurs occurrences :")
for mot, count in frequence_mots.items():
    print(f"- '{mot}': {count} fois")

# =============================================================================
# PARTIE C - Tuples et Sets (30min)
# =============================================================================

print("\n=== PARTIE C - Tuples et Sets ===")

# 1. Coordonnées GPS et calcul de distance
paris = (48.8566, 2.3522)
london = (51.5074, -0.1278)
print(f"Paris : {paris}")
print(f"London : {london}")

# Extraction des coordonnées
lat_paris, lon_paris = paris
lat_london, lon_london = london

print(f"Paris - Latitude: {lat_paris}, Longitude: {lon_paris}")
print(f"London - Latitude: {lat_london}, Longitude: {lon_london}")

# Calcul des différences
diff_lat = abs(lat_paris - lat_london)
diff_lon = abs(lon_paris - lon_london)
distance_approximative = (diff_lat**2 + diff_lon**2) ** 0.5

print(f"Différence latitude: {diff_lat:.4f}")
print(f"Différence longitude: {diff_lon:.4f}")
print(f"Distance approximative: {distance_approximative:.4f}")

# 2. Opérations sur les sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1 : {set1}")
print(f"Set 2 : {set2}")

# Opérations sur les sets
intersection = set1 & set2  # ou set1.intersection(set2)
union = set1 | set2  # ou set1.union(set2)
difference = set1 - set2  # ou set1.difference(set2)
diff_symetrique = set1 ^ set2  # ou set1.symmetric_difference(set2)

print(f"Intersection (éléments communs): {intersection}")
print(f"Union (tous les éléments): {union}")
print(f"Différence (dans set1 mais pas set2): {difference}")
print(f"Différence symétrique (dans un seul des deux): {diff_symetrique}")

# 3. Suppression de doublons avec des sets
nombres_avec_doublons = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"Avec doublons : {nombres_avec_doublons}")

# Suppression des doublons avec set
nombres_uniques = list(set(nombres_avec_doublons))
nombres_uniques.sort()  # Pour garder l'ordre
print(f"Sans doublons : {nombres_uniques}")

# Alternative qui préserve l'ordre original
nombres_uniques_ordre = []
for nombre in nombres_avec_doublons:
    if nombre not in nombres_uniques_ordre:
        nombres_uniques_ordre.append(nombre)
print(f"Sans doublons (ordre préservé) : {nombres_uniques_ordre}")

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
            article = input("Article à ajouter : ").strip()
            if article:
                courses.append(article)
                print(f"✅ '{article}' ajouté à la liste!")
            else:
                print("❌ Article vide non ajouté")
        elif choix == "2":
            if not courses:
                print("❌ Liste vide, rien à supprimer")
            else:
                print("Articles actuels :")
                for i, article in enumerate(courses, 1):
                    print(f"  {i}. {article}")
                try:
                    index = int(input("Numéro de l'article à supprimer : ")) - 1
                    if 0 <= index < len(courses):
                        article_supprime = courses.pop(index)
                        print(f"✅ '{article_supprime}' supprimé!")
                    else:
                        print("❌ Numéro invalide")
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide")
        elif choix == "3":
            if not courses:
                print("📋 Liste vide")
            else:
                print("📋 Votre liste de courses :")
                for i, article in enumerate(courses, 1):
                    print(f"  {i}. {article}")
        elif choix == "4":
            if courses:
                courses.clear()
                print("✅ Liste vidée!")
            else:
                print("📋 Liste déjà vide")
        elif choix == "5":
            print(f"📊 Nombre d'articles : {len(courses)}")
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
            nom = input("Nom du contact : ").strip().title()
            if nom in contacts:
                print("❌ Contact déjà existant!")
            else:
                tel = input("Téléphone : ").strip()
                email = input("Email : ").strip()
                ville = input("Ville : ").strip().title()

                contacts[nom] = {"tel": tel, "email": email, "ville": ville}
                print(f"✅ Contact '{nom}' ajouté!")
        elif choix == "2":
            if not contacts:
                print("❌ Aucun contact enregistré")
            else:
                terme = input("Rechercher (nom) : ").strip().title()
                if terme in contacts:
                    contact = contacts[terme]
                    print(f"📞 {terme}:")
                    print(f"   Téléphone: {contact['tel']}")
                    print(f"   Email: {contact['email']}")
                    print(f"   Ville: {contact['ville']}")
                else:
                    print("❌ Contact non trouvé")
        elif choix == "3":
            if not contacts:
                print("❌ Aucun contact enregistré")
            else:
                nom = input("Nom du contact à modifier : ").strip().title()
                if nom in contacts:
                    print("Laissez vide pour conserver la valeur actuelle")
                    tel = input(
                        f"Nouveau téléphone ({contacts[nom]['tel']}) : "
                    ).strip()
                    email = input(f"Nouvel email ({contacts[nom]['email']}) : ").strip()
                    ville = (
                        input(f"Nouvelle ville ({contacts[nom]['ville']}) : ")
                        .strip()
                        .title()
                    )

                    if tel:
                        contacts[nom]["tel"] = tel
                    if email:
                        contacts[nom]["email"] = email
                    if ville:
                        contacts[nom]["ville"] = ville

                    print(f"✅ Contact '{nom}' modifié!")
                else:
                    print("❌ Contact non trouvé")
        elif choix == "4":
            if not contacts:
                print("❌ Aucun contact enregistré")
            else:
                nom = input("Nom du contact à supprimer : ").strip().title()
                if nom in contacts:
                    del contacts[nom]
                    print(f"✅ Contact '{nom}' supprimé!")
                else:
                    print("❌ Contact non trouvé")
        elif choix == "5":
            if not contacts:
                print("📋 Aucun contact enregistré")
            else:
                print("📋 Tous les contacts :")
                for nom, infos in sorted(contacts.items()):
                    print(f"  👤 {nom}")
                    print(f"     📞 {infos['tel']}")
                    print(f"     📧 {infos['email']}")
                    print(f"     🏙️ {infos['ville']}")
                    print()
        elif choix == "6":
            if not contacts:
                print("❌ Aucun contact enregistré")
            else:
                villes = {}
                for nom, infos in contacts.items():
                    ville = infos["ville"]
                    if ville not in villes:
                        villes[ville] = []
                    villes[ville].append(nom)

                print("📍 Contacts par ville :")
                for ville, noms in sorted(villes.items()):
                    print(f"  🏙️ {ville}: {', '.join(noms)}")
        elif choix == "7":
            print(f"📊 Nombre total de contacts : {len(contacts)}")
        else:
            print("Choix invalide !")


# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================


def analyser_liste(liste):
    """Analyse complète d'une liste de nombres"""
    if not liste:
        return {"erreur": "Liste vide"}

    pairs = [n for n in liste if n % 2 == 0]
    impairs = [n for n in liste if n % 2 != 0]

    return {
        "nombre_elements": len(liste),
        "somme": sum(liste),
        "moyenne": sum(liste) / len(liste),
        "minimum": min(liste),
        "maximum": max(liste),
        "nombres_pairs": pairs,
        "nombres_impairs": impairs,
        "count_pairs": len(pairs),
        "count_impairs": len(impairs),
    }


def fusionner_dictionnaires(dict1, dict2):
    """Fusionne deux dictionnaires"""
    resultat = dict1.copy()  # Copie du premier dictionnaire
    resultat.update(dict2)  # Ajout des éléments du second
    return resultat


def nettoyer_texte(texte):
    """Nettoie un texte et retourne les mots uniques"""
    import string

    # Convertir en minuscules
    texte_clean = texte.lower()

    # Supprimer la ponctuation
    for punct in string.punctuation:
        texte_clean = texte_clean.replace(punct, " ")

    # Diviser en mots et supprimer les doublons
    mots = texte_clean.split()
    mots_uniques = list(set(mots))
    mots_uniques.sort()  # Tri alphabétique

    return mots_uniques


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
        print(analyser_liste(test_liste))

        dict_a = {"a": 1, "b": 2}
        dict_b = {"c": 3, "d": 4}
        print(f"Fusion de {dict_a} et {dict_b} :")
        print(fusionner_dictionnaires(dict_a, dict_b))

        texte_test = "Python, c'est fantastique! Python est puissant."
        print(f"Nettoyage de '{texte_test}' :")
        print(nettoyer_texte(texte_test))

    print("\n🎉 Bravo ! Vous maîtrisez les collections Python !")
    print("⏭️ Passez maintenant aux Jour 5-6 : POO")
