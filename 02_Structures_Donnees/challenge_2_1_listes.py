# Challenge 2.1 - Listes
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Bases des listes
# Votre code ici...
# - Créent une liste de vos 5 films préférés
mes_films = ['preason break', 'the walking dead', 'game of tronze', 'squed game', 'la casa de papel']
# print(mes_films)
# - Ajoutent 2 nouveaux films à la fin
mes_films.append('film 1 a la fin')
mes_films.append('film 2 a la fin')
# print(mes_films)
# - Insèrent un film au début de la liste
mes_films.insert(0,'film 3 au debut')
# print(mes_films)
# - Supprimez le 3ème film de la liste
del mes_films[2]
del_film = mes_films.pop(2)
# print(del_film)
# print(mes_films)
# - Affichez la liste triée alphabétiquement
mes_films.sort()
sorted_films = sorted(mes_films)
# print(mes_films)
# print(sorted_films)

# Challenge B - Manipulation de listes
# Votre code ici...
# Avec une liste de nombres [10, 25, 5, 80, 3, 15, 42] :
test_liste = [10, 25, 5, 80, 3, 15, 42] 
# - Trouvez le plus grand et le plus petit nombre
le_plus_grand = max(test_liste)
le_plus_petit = min(test_liste)
# print(le_plus_grand)
# print(le_plus_petit)
# - Calculez la moyenne
la_moyenne = round((sum(test_liste))/(len(test_liste)),2)
# print(la_moyenne)
# - Comptez combien de nombres sont supérieurs à 20
def compteur(liste):
    compteur = 0
    for i in liste:
        if i > 20:
            compteur += 1
    return compteur
# print("les nombres supérieurs à 20 :", compteur(test_liste))
plus_de_20 = sum(1 for i in test_liste if i > 20)
# print("les nombres supérieurs à 20 :", plus_de_20)
# - Créez une nouvelle liste avec seulement les nombres pairs
nombres_pairs = [i for i in test_liste if i % 2 == 0]
# print("les nombres pairs :", nombres_pairs)
# - Inversez l'ordre de la liste originale
test_liste.reverse()
# print("la liste inversée :",test_liste)

# Challenge C - Listes et boucles
# Votre code ici...

# - Un gestionnaire de courses : ajoutez/supprimez des articles
courses = []
def gerer_courses(action, article=None):
    if action == "ajouter" and article:
        courses.append(article)
    elif action == "supprimer" and article in courses:
        courses.remove(article)
    return courses
# print(gerer_courses("ajouter", "Pommes"))
# print(gerer_courses("ajouter", "Bananes"))
# print(gerer_courses("supprimer", "Pommes"))
# print(gerer_courses("ajouter", "Oranges"))
# - Un calculateur de notes : stockez les notes et calculez la moyenne
notes = []
def gerer_notes(action, note=None):
    if action == "ajouter" and note is not None:
        notes.append(note)
    return round(sum(notes) / len(notes), 2) if notes else 0
# print(gerer_notes("ajouter", 15))
# print(gerer_notes("ajouter", 20))
# print(gerer_notes("ajouter", 10))
# - Un jeu "Pierre, Papier, Ciseaux" qui garde l'historique des parties
import random
historique = []
def jouer_pierre_papier_ciseaux(choix_joueur):
    choix_ordinateur = random.choice(["Pierre", "Papier", "Ciseaux"])
    if choix_joueur == choix_ordinateur:
        resultat = "Égalité"
    elif (choix_joueur == "Pierre" and choix_ordinateur == "Ciseaux") or \
         (choix_joueur == "Papier" and choix_ordinateur == "Pierre") or \
         (choix_joueur == "Ciseaux" and choix_ordinateur == "Papier"):
        resultat = "Vous gagnez!"
    else:
        resultat = "Vous perdez!"
    historique.append((choix_joueur, choix_ordinateur, resultat))
    return resultat, choix_ordinateur
# print(jouer_pierre_papier_ciseaux("Pierre"))
# - Un analyseur de mots : comptez la fréquence de chaque mot dans un texte
def analyser_mots(texte):
    mots = texte.split()
    frequence = {}
    for mot in mots:
        frequence[mot] = frequence.get(mot, 0) + 1
    return frequence
# print(analyser_mots("Bonjour le monde Bonjour tout le monde"))

# Challenge D - Listes avancées
# Votre code ici...
# - `fusionner_listes(liste1, liste2)` : fusionne deux listes triées  
liste1 = [1, 3, 5, 7]
liste2 = [2, 4, 6, 8]
def fusionner_listes(liste1, liste2):
    return liste1 + liste2
# print("Liste fusionnée :", fusionner_listes(liste1, liste2))
# - `supprimer_doublons(liste)` : supprime les éléments en double   
def supprimer_doublons(liste): 
    return list(set(liste))
# print("Liste sans doublons :", supprimer_doublons([1, 2, 2, 3, 4, 4, 5]))   
# - `rotation_liste(liste, n)` : fait une rotation de n positions
def rotation_liste(liste, n):
    n = n % len(liste)  # Pour gérer les rotations plus grandes que la liste
    return liste[-n:] + liste[:-n]
# print("Liste après rotation :", rotation_liste([1, 2, 3, 4, 5], 2))
# - `sous_liste_max(liste)` : trouve la sous-liste avec la somme maximale
def sous_liste_max(liste):
    max_somme = 0
    sous_liste = []
    for i in range(len(liste)):
        for j in range(i + 1, len(liste) + 1):
            curr_sous_liste = liste[i:j]
            curr_somme = sum(curr_sous_liste)
            if curr_somme > max_somme:
                max_somme = curr_somme
                sous_liste = curr_sous_liste
    return sous_liste
# print("Sous-liste avec la somme maximale :", sous_liste_max([1, -2, 3, 4, -1, 2, 1, -5, 4]))
# Challenge E - Projet : Système de gestion d'étudiants
# Votre code ici...
# - Liste d'étudiants avec [nom, notes, moyenne]
# - Ajouter/supprimer des étudiants
# - Ajouter des notes à un étudiant
# - Calculer automatiquement les moyennes
# - Trier les étudiants par moyenne
# - Afficher les statistiques de la classe :
#   - Moyenne générale
#   - Meilleure et pire note
#   - Nombre d'étudiants au-dessus de la moyenne
# - Rechercher un étudiant par nom
# - Exporter les données en format texte
# Bonus :
# - Sauvegarde/chargement depuis un fichier
# - Interface menu interactive
# - Validation des entrées utilisateur
# Pour gérer plusieurs notes par étudiant, il faut stocker chaque étudiant comme un dictionnaire :
# Exemple : {"nom": "Alice", "notes": [15, 18, 12], "moyenne": 15.0}
etudiants = []

def ajouter_etudiant(nom):
    # Ajoute un nouvel étudiant avec une liste de notes vide
    etudiants.append({"nom": nom, "notes": [], "moyenne": 0})

def supprimer_etudiant(nom):
    # Supprime l'étudiant par son nom
    global etudiants
    etudiants = [e for e in etudiants if e["nom"] != nom]

def ajouter_note(nom, note):
    # Ajoute une note à l'étudiant et met à jour la moyenne
    for e in etudiants:
        if e["nom"] == nom:
            e["notes"].append(note)
            e["moyenne"] = round(sum(e["notes"]) / len(e["notes"]), 2)
            break

def trier_par_moyenne():
    # Trie les étudiants par moyenne décroissante
    return sorted(etudiants, key=lambda x: x["moyenne"], reverse=True)

def rechercher_etudiant(nom):
    # Recherche un étudiant par nom
    for e in etudiants:
        if e["nom"] == nom:
            return e
    return None

def statistiques_classe():
    # Affiche les statistiques de la classe
    toutes_les_notes = [note for e in etudiants for note in e["notes"]]
    if not toutes_les_notes:
        return {}
    moyenne_generale = round(sum(toutes_les_notes) / len(toutes_les_notes), 2)
    meilleure_note = max(toutes_les_notes)
    pire_note = min(toutes_les_notes)
    nb_etudiants_above_moyenne = sum(1 for e in etudiants if e["moyenne"] > moyenne_generale)
    return {
        "moyenne_generale": moyenne_generale,
        "meilleure_note": meilleure_note,
        "pire_note": pire_note,
        "nb_etudiants_above_moyenne": nb_etudiants_above_moyenne
    }

def exporter_donnees(nom_fichier):
    # Exporte les données en format texte
    with open(nom_fichier, 'w') as f:
        f.write("RAPPORT DES ÉTUDIANTS\n")
        f.write("=" * 50 + "\n")
        for e in etudiants:
            f.write(f"Nom: {e['nom']}\n")
            f.write(f"Notes: {e['notes']}\n")
            f.write(f"Moyenne: {e['moyenne']}\n")
            f.write("-" * 30 + "\n")

def sauvegarder_fichier(nom_fichier):
    # Sauvegarde les données dans un fichier
    with open(nom_fichier, 'w') as f:
        for e in etudiants:
            f.write(f"{e['nom']},{','.join(map(str, e['notes']))}\n")

def charger_fichier(nom_fichier):
    # Charge les données depuis un fichier
    global etudiants
    etudiants = []
    try:
        with open(nom_fichier, 'r') as f:
            for ligne in f:
                donnees = ligne.strip().split(',')
                nom = donnees[0]
                notes = [float(note) for note in donnees[1:] if note]
                moyenne = round(sum(notes) / len(notes), 2) if notes else 0
                etudiants.append({"nom": nom, "notes": notes, "moyenne": moyenne})
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} non trouvé.")

def menu_interactif():
    # Interface menu interactive
    while True:
        print("\n=== GESTIONNAIRE D'ÉTUDIANTS ===")
        print("1. Ajouter un étudiant")
        print("2. Supprimer un étudiant")
        print("3. Ajouter une note")
        print("4. Rechercher un étudiant")
        print("5. Afficher statistiques")
        print("6. Trier par moyenne")
        print("7. Exporter données")
        print("8. Sauvegarder")
        print("9. Charger")
        print("0. Quitter")
        
        choix = input("Votre choix: ")
        
        if choix == '1':
            nom = input("Nom de l'étudiant: ")
            ajouter_etudiant(nom)
            print(f"Étudiant {nom} ajouté.")
        elif choix == '2':
            nom = input("Nom de l'étudiant à supprimer: ")
            supprimer_etudiant(nom)
            print(f"Étudiant {nom} supprimé.")
        elif choix == '3':
            nom = input("Nom de l'étudiant: ")
            try:
                note = float(input("Note (0-20): "))
                if 0 <= note <= 20:
                    ajouter_note(nom, note)
                    print(f"Note {note} ajoutée à {nom}.")
                else:
                    print("Note invalide (0-20).")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        elif choix == '4':
            nom = input("Nom à rechercher: ")
            etudiant = rechercher_etudiant(nom)
            if etudiant:
                print(f"Trouvé: {etudiant}")
            else:
                print("Étudiant non trouvé.")
        elif choix == '5':
            stats = statistiques_classe()
            if stats:
                print(f"Statistiques: {stats}")
            else:
                print("Aucune donnée disponible.")
        elif choix == '6':
            tries = trier_par_moyenne()
            for e in tries:
                print(f"{e['nom']}: {e['moyenne']}")
        elif choix == '7':
            fichier = input("Nom du fichier: ")
            exporter_donnees(fichier)
            print(f"Données exportées vers {fichier}.")
        elif choix == '8':
            fichier = input("Nom du fichier: ")
            sauvegarder_fichier(fichier)
            print(f"Données sauvegardées dans {fichier}.")
        elif choix == '9':
            fichier = input("Nom du fichier: ")
            charger_fichier(fichier)
            print(f"Données chargées depuis {fichier}.")
        elif choix == '0':
            print("Au revoir!")
            break
        else:
            print("Choix invalide.")

# Test du système
menu_interactif()
