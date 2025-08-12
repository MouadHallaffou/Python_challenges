# Challenge Jour 7-8 - Manipulation de Fichiers
# Complétez tous les exercices ci-dessous

import os
import json
import csv
from datetime import datetime
import shutil
import glob

# =============================================================================
# PARTIE A - Lecture et Écriture de Fichiers Texte (45min)
# =============================================================================

print("=== PARTIE A - Fichiers Texte ===")


# 1. Écriture de fichier simple
def creer_fichier_journal(nom_fichier="journal.txt"):
    """Créer un fichier journal avec horodatage"""
    try:
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.write("=== JOURNAL D'ACTIVITÉS ===\n")
            fichier.write(
                f"Créé le: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}\n"
            )
            fichier.write("-" * 40 + "\n\n")

        print(f"✅ Fichier journal créé: {nom_fichier}")
        return True

    except Exception as e:
        print(f"❌ Erreur création fichier: {e}")
        return False


# 2. Ajout de contenu à un fichier
def ajouter_entree_journal(message, nom_fichier="journal.txt"):
    """Ajouter une entrée au journal"""
    try:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(nom_fichier, "a", encoding="utf-8") as fichier:
            fichier.write(f"[{timestamp}] {message}\n")

        print(f"✅ Entrée ajoutée: {message}")
        return True

    except Exception as e:
        print(f"❌ Erreur ajout entrée: {e}")
        return False


# 3. Lecture de fichier avec différentes méthodes
def lire_fichier_complet(nom_fichier):
    """Lire un fichier entièrement"""
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()

        print(f"📖 Contenu de {nom_fichier}:")
        print("-" * 50)
        print(contenu)
        print("-" * 50)
        return contenu

    except FileNotFoundError:
        print(f"❌ Fichier {nom_fichier} non trouvé")
        return None
    except Exception as e:
        print(f"❌ Erreur lecture: {e}")
        return None


def lire_fichier_ligne_par_ligne(nom_fichier):
    """Lire un fichier ligne par ligne"""
    try:
        lignes = []
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for numero, ligne in enumerate(fichier, 1):
                ligne_clean = ligne.rstrip("\n")
                lignes.append(ligne_clean)
                print(f"Ligne {numero:2d}: {ligne_clean}")

        return lignes

    except FileNotFoundError:
        print(f"❌ Fichier {nom_fichier} non trouvé")
        return []
    except Exception as e:
        print(f"❌ Erreur lecture: {e}")
        return []


# Tests des fonctions de fichiers texte
print("1. Création et manipulation du journal :")
creer_fichier_journal()
ajouter_entree_journal("Application démarrée")
ajouter_entree_journal("Utilisateur connecté")
ajouter_entree_journal("Traitement des données en cours")

print("\n2. Lecture du journal :")
lire_fichier_complet("journal.txt")

print("\n3. Lecture ligne par ligne :")
lire_fichier_ligne_par_ligne("journal.txt")

# =============================================================================
# PARTIE B - Fichiers CSV (45min)
# =============================================================================

print("\n=== PARTIE B - Fichiers CSV ===")


# 1. Création d'un fichier CSV
def creer_csv_etudiants(nom_fichier="etudiants.csv"):
    """Créer un fichier CSV avec des données d'étudiants"""
    etudiants = [
        ["ID", "Nom", "Prénom", "Âge", "Note", "Spécialité"],
        [1, "Dupont", "Alice", 20, 15.5, "Informatique"],
        [2, "Martin", "Bob", 19, 14.0, "Mathématiques"],
        [3, "Durand", "Claire", 21, 16.5, "Informatique"],
        [4, "Moreau", "David", 20, 13.5, "Physique"],
        [5, "Bernard", "Emma", 22, 17.0, "Informatique"],
        [6, "Petit", "François", 19, 12.0, "Mathématiques"],
        [7, "Robert", "Grace", 21, 18.0, "Physique"],
        [8, "Richard", "Hugo", 20, 15.0, "Informatique"],
    ]

    try:
        with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier, delimiter=";")
            writer.writerows(etudiants)

        print(f"✅ Fichier CSV créé: {nom_fichier}")
        return True

    except Exception as e:
        print(f"❌ Erreur création CSV: {e}")
        return False


# 2. Lecture d'un fichier CSV
def lire_csv_etudiants(nom_fichier="etudiants.csv"):
    """Lire et analyser le fichier CSV des étudiants"""
    try:
        etudiants = []

        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier, delimiter=";")

            for ligne in reader:
                # Conversion des types
                ligne["ID"] = int(ligne["ID"])
                ligne["Âge"] = int(ligne["Âge"])
                ligne["Note"] = float(ligne["Note"])
                etudiants.append(ligne)

        print(f"📊 Données lues: {len(etudiants)} étudiants")
        return etudiants

    except FileNotFoundError:
        print(f"❌ Fichier {nom_fichier} non trouvé")
        return []
    except Exception as e:
        print(f"❌ Erreur lecture CSV: {e}")
        return []


# 3. Analyse des données CSV
def analyser_donnees_etudiants(etudiants):
    """Analyser les données des étudiants"""
    if not etudiants:
        print("❌ Aucune donnée à analyser")
        return

    print("\n📈 ANALYSE DES DONNÉES ÉTUDIANTS")
    print("=" * 40)

    # Statistiques générales
    notes = [etudiant["Note"] for etudiant in etudiants]
    ages = [etudiant["Âge"] for etudiant in etudiants]

    print(f"Nombre total d'étudiants: {len(etudiants)}")
    print(f"Note moyenne: {sum(notes)/len(notes):.2f}")
    print(f"Note minimale: {min(notes)}")
    print(f"Note maximale: {max(notes)}")
    print(f"Âge moyen: {sum(ages)/len(ages):.1f} ans")

    # Répartition par spécialité
    specialites = {}
    for etudiant in etudiants:
        specialite = etudiant["Spécialité"]
        if specialite not in specialites:
            specialites[specialite] = []
        specialites[specialite].append(etudiant)

    print(f"\nRépartition par spécialité:")
    for specialite, liste_etudiants in specialites.items():
        notes_specialite = [e["Note"] for e in liste_etudiants]
        moyenne_specialite = sum(notes_specialite) / len(notes_specialite)
        print(
            f"  {specialite}: {len(liste_etudiants)} étudiants (moyenne: {moyenne_specialite:.2f})"
        )

    # Top 3 des meilleures notes
    etudiants_tries = sorted(etudiants, key=lambda x: x["Note"], reverse=True)
    print(f"\nTop 3 des meilleures notes:")
    for i, etudiant in enumerate(etudiants_tries[:3], 1):
        print(f"  {i}. {etudiant['Prénom']} {etudiant['Nom']}: {etudiant['Note']}/20")


# 4. Modification et sauvegarde CSV
def ajouter_etudiant_csv(nouvel_etudiant, nom_fichier="etudiants.csv"):
    """Ajouter un étudiant au fichier CSV"""
    try:
        with open(nom_fichier, "a", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier, delimiter=";")
            writer.writerow(nouvel_etudiant)

        print(f"✅ Étudiant ajouté: {nouvel_etudiant[1]} {nouvel_etudiant[2]}")
        return True

    except Exception as e:
        print(f"❌ Erreur ajout étudiant: {e}")
        return False


def filtrer_et_sauvegarder_csv(etudiants, critere, valeur_min, nom_fichier_sortie):
    """Filtrer les étudiants et sauvegarder dans un nouveau fichier"""
    try:
        etudiants_filtres = [e for e in etudiants if e[critere] >= valeur_min]

        with open(nom_fichier_sortie, "w", newline="", encoding="utf-8") as fichier:
            if etudiants_filtres:
                writer = csv.DictWriter(
                    fichier, fieldnames=etudiants_filtres[0].keys(), delimiter=";"
                )
                writer.writeheader()
                writer.writerows(etudiants_filtres)

        print(
            f"✅ {len(etudiants_filtres)} étudiants sauvegardés dans {nom_fichier_sortie}"
        )
        return len(etudiants_filtres)

    except Exception as e:
        print(f"❌ Erreur filtrage: {e}")
        return 0


# Tests des fonctions CSV
print("4. Création et analyse CSV :")
creer_csv_etudiants()
etudiants = lire_csv_etudiants()
analyser_donnees_etudiants(etudiants)

print("\n5. Ajout d'étudiant :")
nouvel_etudiant = [9, "Leroy", "Isabelle", 23, 16.0, "Physique"]
ajouter_etudiant_csv(nouvel_etudiant)

print("\n6. Filtrage des données :")
etudiants_mis_a_jour = lire_csv_etudiants()
nb_excellents = filtrer_et_sauvegarder_csv(
    etudiants_mis_a_jour, "Note", 15.0, "etudiants_excellents.csv"
)

# =============================================================================
# PARTIE C - Fichiers JSON (45min)
# =============================================================================

print("\n=== PARTIE C - Fichiers JSON ===")


# 1. Création d'un fichier JSON
def creer_json_bibliotheque(nom_fichier="bibliotheque.json"):
    """Créer un fichier JSON pour une bibliothèque"""
    bibliotheque = {
        "nom": "Bibliothèque Municipale",
        "adresse": "123 Rue des Livres, 75001 Paris",
        "telephone": "01.23.45.67.89",
        "horaires": {
            "lundi": "9h-18h",
            "mardi": "9h-18h",
            "mercredi": "9h-20h",
            "jeudi": "9h-18h",
            "vendredi": "9h-18h",
            "samedi": "10h-17h",
            "dimanche": "Fermé",
        },
        "collections": {
            "livres": [
                {
                    "id": 1,
                    "titre": "Le Petit Prince",
                    "auteur": "Antoine de Saint-Exupéry",
                    "isbn": "978-2-07-040818-9",
                    "genre": "Fiction",
                    "annee": 1943,
                    "disponible": True,
                    "emprunts": 245,
                },
                {
                    "id": 2,
                    "titre": "1984",
                    "auteur": "George Orwell",
                    "isbn": "978-2-07-036822-5",
                    "genre": "Science-fiction",
                    "annee": 1949,
                    "disponible": False,
                    "emprunts": 189,
                },
                {
                    "id": 3,
                    "titre": "Python pour les nuls",
                    "auteur": "Stef Maruch",
                    "isbn": "978-2-412-05976-8",
                    "genre": "Informatique",
                    "annee": 2019,
                    "disponible": True,
                    "emprunts": 156,
                },
                {
                    "id": 4,
                    "titre": "Les Misérables",
                    "auteur": "Victor Hugo",
                    "isbn": "978-2-07-041104-2",
                    "genre": "Classique",
                    "annee": 1862,
                    "disponible": True,
                    "emprunts": 302,
                },
            ],
            "dvd": [
                {
                    "id": 1,
                    "titre": "Inception",
                    "realisateur": "Christopher Nolan",
                    "annee": 2010,
                    "genre": "Science-fiction",
                    "duree": 148,
                    "disponible": True,
                },
                {
                    "id": 2,
                    "titre": "Amélie",
                    "realisateur": "Jean-Pierre Jeunet",
                    "annee": 2001,
                    "genre": "Romance",
                    "duree": 122,
                    "disponible": False,
                },
            ],
        },
        "statistiques": {
            "total_livres": 4,
            "total_dvd": 2,
            "adherents": 1247,
            "emprunts_mois": 89,
            "derniere_mise_a_jour": datetime.now().isoformat(),
        },
    }

    try:
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            json.dump(bibliotheque, fichier, indent=2, ensure_ascii=False)

        print(f"✅ Fichier JSON créé: {nom_fichier}")
        return True

    except Exception as e:
        print(f"❌ Erreur création JSON: {e}")
        return False


# 2. Lecture et analyse d'un fichier JSON
def lire_json_bibliotheque(nom_fichier="bibliotheque.json"):
    """Lire et analyser le fichier JSON de la bibliothèque"""
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            bibliotheque = json.load(fichier)

        print(f"📚 Données bibliothèque chargées")
        return bibliotheque

    except FileNotFoundError:
        print(f"❌ Fichier {nom_fichier} non trouvé")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erreur format JSON: {e}")
        return None
    except Exception as e:
        print(f"❌ Erreur lecture: {e}")
        return None


def afficher_info_bibliotheque(bibliotheque):
    """Afficher les informations de la bibliothèque"""
    if not bibliotheque:
        print("❌ Aucune donnée à afficher")
        return

    print(f"\n📚 {bibliotheque['nom']}")
    print("=" * 50)
    print(f"Adresse: {bibliotheque['adresse']}")
    print(f"Téléphone: {bibliotheque['telephone']}")

    print(f"\nHoraires d'ouverture:")
    for jour, horaire in bibliotheque["horaires"].items():
        print(f"  {jour.capitalize()}: {horaire}")

    stats = bibliotheque["statistiques"]
    print(f"\nStatistiques:")
    print(f"  Livres: {stats['total_livres']}")
    print(f"  DVD: {stats['total_dvd']}")
    print(f"  Adhérents: {stats['adherents']}")
    print(f"  Emprunts ce mois: {stats['emprunts_mois']}")


def rechercher_livres(bibliotheque, critere, valeur):
    """Rechercher des livres selon un critère"""
    if not bibliotheque:
        return []

    livres = bibliotheque["collections"]["livres"]
    resultats = []

    for livre in livres:
        if critere in livre:
            if isinstance(livre[critere], str):
                if valeur.lower() in livre[critere].lower():
                    resultats.append(livre)
            elif livre[critere] == valeur:
                resultats.append(livre)

    return resultats


# 3. Modification et sauvegarde JSON
def ajouter_livre_json(bibliotheque, nouveau_livre, nom_fichier="bibliotheque.json"):
    """Ajouter un livre à la bibliothèque"""
    try:
        # Générer un nouvel ID
        livres = bibliotheque["collections"]["livres"]
        nouvel_id = max(livre["id"] for livre in livres) + 1
        nouveau_livre["id"] = nouvel_id

        # Ajouter le livre
        livres.append(nouveau_livre)

        # Mettre à jour les statistiques
        bibliotheque["statistiques"]["total_livres"] += 1
        bibliotheque["statistiques"][
            "derniere_mise_a_jour"
        ] = datetime.now().isoformat()

        # Sauvegarder
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            json.dump(bibliotheque, fichier, indent=2, ensure_ascii=False)

        print(f"✅ Livre ajouté: {nouveau_livre['titre']}")
        return True

    except Exception as e:
        print(f"❌ Erreur ajout livre: {e}")
        return False


def emprunter_livre(bibliotheque, livre_id, nom_fichier="bibliotheque.json"):
    """Emprunter un livre"""
    try:
        livres = bibliotheque["collections"]["livres"]

        for livre in livres:
            if livre["id"] == livre_id:
                if not livre["disponible"]:
                    print(f"❌ Le livre '{livre['titre']}' n'est pas disponible")
                    return False

                livre["disponible"] = False
                livre["emprunts"] += 1
                bibliotheque["statistiques"]["emprunts_mois"] += 1
                bibliotheque["statistiques"][
                    "derniere_mise_a_jour"
                ] = datetime.now().isoformat()

                # Sauvegarder
                with open(nom_fichier, "w", encoding="utf-8") as fichier:
                    json.dump(bibliotheque, fichier, indent=2, ensure_ascii=False)

                print(f"✅ Livre emprunté: {livre['titre']}")
                return True

        print(f"❌ Livre avec ID {livre_id} non trouvé")
        return False

    except Exception as e:
        print(f"❌ Erreur emprunt: {e}")
        return False


# Tests des fonctions JSON
print("7. Création et gestion JSON :")
creer_json_bibliotheque()
bibliotheque = lire_json_bibliotheque()
afficher_info_bibliotheque(bibliotheque)

print("\n8. Recherche de livres :")
livres_fiction = rechercher_livres(bibliotheque, "genre", "Fiction")
print(f"Livres de fiction trouvés: {len(livres_fiction)}")
for livre in livres_fiction:
    print(f"  - {livre['titre']} par {livre['auteur']}")

livres_python = rechercher_livres(bibliotheque, "titre", "Python")
print(f"Livres contenant 'Python': {len(livres_python)}")
for livre in livres_python:
    print(f"  - {livre['titre']}")

print("\n9. Ajout et emprunt :")
nouveau_livre = {
    "titre": "Clean Code",
    "auteur": "Robert C. Martin",
    "isbn": "978-0-13-235088-4",
    "genre": "Informatique",
    "annee": 2008,
    "disponible": True,
    "emprunts": 0,
}
ajouter_livre_json(bibliotheque, nouveau_livre)

# Recharger les données mises à jour
bibliotheque = lire_json_bibliotheque()
emprunter_livre(bibliotheque, 1)  # Emprunter "Le Petit Prince"

# =============================================================================
# PARTIE D - Gestion de Fichiers et Dossiers (45min)
# =============================================================================

print("\n=== PARTIE D - Gestion de Fichiers et Dossiers ===")


# 1. Exploration de dossiers
def explorer_dossier(chemin, niveau=0, max_niveau=2):
    """Explorer récursivement un dossier"""
    if niveau > max_niveau:
        return

    try:
        indent = "  " * niveau
        items = os.listdir(chemin)

        for item in sorted(items):
            chemin_complet = os.path.join(chemin, item)

            if os.path.isdir(chemin_complet):
                print(f"{indent}📁 {item}/")
                explorer_dossier(chemin_complet, niveau + 1, max_niveau)
            else:
                taille = os.path.getsize(chemin_complet)
                print(f"{indent}📄 {item} ({taille} octets)")

    except PermissionError:
        print(f"{indent}❌ Accès refusé")
    except Exception as e:
        print(f"{indent}❌ Erreur: {e}")


def obtenir_info_fichier(chemin_fichier):
    """Obtenir des informations détaillées sur un fichier"""
    try:
        if not os.path.exists(chemin_fichier):
            return f"❌ Le fichier {chemin_fichier} n'existe pas"

        stats = os.stat(chemin_fichier)

        info = {
            "nom": os.path.basename(chemin_fichier),
            "chemin": os.path.abspath(chemin_fichier),
            "taille": stats.st_size,
            "creation": datetime.fromtimestamp(stats.st_ctime),
            "modification": datetime.fromtimestamp(stats.st_mtime),
            "est_fichier": os.path.isfile(chemin_fichier),
            "est_dossier": os.path.isdir(chemin_fichier),
            "extension": os.path.splitext(chemin_fichier)[1],
        }

        return info

    except Exception as e:
        return f"❌ Erreur lecture info: {e}"


# 2. Création et organisation de dossiers
def creer_structure_projet(nom_projet):
    """Créer une structure de projet organisée"""
    try:
        # Dossier principal
        os.makedirs(nom_projet, exist_ok=True)

        # Sous-dossiers
        dossiers = ["src", "data", "docs", "tests", "config", "logs", "backup"]

        for dossier in dossiers:
            chemin_dossier = os.path.join(nom_projet, dossier)
            os.makedirs(chemin_dossier, exist_ok=True)

        # Fichiers de base
        fichiers = {
            "README.md": f"# {nom_projet}\n\nDescription du projet...\n",
            "main.py": "# Point d'entrée principal\n\nif __name__ == '__main__':\n    print('Hello World!')\n",
            "requirements.txt": "# Dépendances Python\n# requests==2.28.1\n",
            "config/settings.py": "# Configuration de l'application\n\nDEBUG = True\nVERSION = '1.0.0'\n",
        }

        for fichier, contenu in fichiers.items():
            chemin_fichier = os.path.join(nom_projet, fichier)
            os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

            with open(chemin_fichier, "w", encoding="utf-8") as f:
                f.write(contenu)

        print(f"✅ Structure de projet créée: {nom_projet}")
        return True

    except Exception as e:
        print(f"❌ Erreur création structure: {e}")
        return False


# 3. Opérations sur fichiers
def copier_fichier(source, destination):
    """Copier un fichier avec gestion d'erreurs"""
    try:
        # Créer le dossier de destination si nécessaire
        dossier_dest = os.path.dirname(destination)
        if dossier_dest:
            os.makedirs(dossier_dest, exist_ok=True)

        shutil.copy2(source, destination)
        print(f"✅ Fichier copié: {source} → {destination}")
        return True

    except FileNotFoundError:
        print(f"❌ Fichier source non trouvé: {source}")
        return False
    except Exception as e:
        print(f"❌ Erreur copie: {e}")
        return False


def rechercher_fichiers(dossier, motif="*", extension=None):
    """Rechercher des fichiers selon un motif"""
    try:
        if extension:
            motif = f"*.{extension.lstrip('.')}"

        chemin_recherche = os.path.join(dossier, "**", motif)
        fichiers = glob.glob(chemin_recherche, recursive=True)

        # Filtrer seulement les fichiers (pas les dossiers)
        fichiers = [f for f in fichiers if os.path.isfile(f)]

        return fichiers

    except Exception as e:
        print(f"❌ Erreur recherche: {e}")
        return []


def nettoyer_dossier(dossier, extensions_a_supprimer, simulation=True):
    """Nettoyer un dossier en supprimant certains types de fichiers"""
    try:
        fichiers_a_supprimer = []

        for extension in extensions_a_supprimer:
            fichiers = rechercher_fichiers(dossier, extension=extension)
            fichiers_a_supprimer.extend(fichiers)

        if simulation:
            print(f"🔍 SIMULATION - Fichiers qui seraient supprimés:")
            for fichier in fichiers_a_supprimer:
                taille = os.path.getsize(fichier)
                print(f"  - {fichier} ({taille} octets)")
            print(f"Total: {len(fichiers_a_supprimer)} fichiers")
        else:
            for fichier in fichiers_a_supprimer:
                os.remove(fichier)
                print(f"🗑️ Supprimé: {fichier}")
            print(f"✅ {len(fichiers_a_supprimer)} fichiers supprimés")

        return len(fichiers_a_supprimer)

    except Exception as e:
        print(f"❌ Erreur nettoyage: {e}")
        return 0


# Tests de gestion de fichiers
print("10. Exploration du dossier actuel :")
explorer_dossier(".", max_niveau=1)

print("\n11. Informations sur les fichiers :")
for fichier in ["journal.txt", "bibliotheque.json", "etudiants.csv"]:
    info = obtenir_info_fichier(fichier)
    if isinstance(info, dict):
        print(f"📄 {info['nom']}:")
        print(f"  Taille: {info['taille']} octets")
        print(f"  Modifié: {info['modification'].strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"  Extension: {info['extension'] or 'Aucune'}")

print("\n12. Création structure projet :")
creer_structure_projet("mon_projet_python")

print("\n13. Recherche de fichiers :")
fichiers_python = rechercher_fichiers(".", extension="py")
print(f"Fichiers Python trouvés: {len(fichiers_python)}")
for fichier in fichiers_python[:5]:  # Afficher les 5 premiers
    print(f"  - {fichier}")

# =============================================================================
# MINI-PROJET - Gestionnaire de Fichiers de Logs (60min)
# =============================================================================

print("\n=== MINI-PROJET - Gestionnaire de Logs ===")


class GestionnaireLogs:
    """Gestionnaire avancé de fichiers de logs"""

    def __init__(self, dossier_logs="logs"):
        self.dossier_logs = dossier_logs
        self.types_logs = {
            "INFO": "ℹ️",
            "WARNING": "⚠️",
            "ERROR": "❌",
            "DEBUG": "🐛",
            "SUCCESS": "✅",
        }

        # Créer le dossier de logs
        os.makedirs(self.dossier_logs, exist_ok=True)

    def ecrire_log(self, message, niveau="INFO", fichier_log=None):
        """Écrire un message de log"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if fichier_log is None:
                # Nom de fichier basé sur la date
                date_str = datetime.now().strftime("%Y-%m-%d")
                fichier_log = f"app_{date_str}.log"

            chemin_log = os.path.join(self.dossier_logs, fichier_log)

            # Format du message
            icone = self.types_logs.get(niveau, "📝")
            ligne_log = f"[{timestamp}] {niveau} {icone} {message}\n"

            # Écriture dans le fichier
            with open(chemin_log, "a", encoding="utf-8") as f:
                f.write(ligne_log)

            return True

        except Exception as e:
            print(f"❌ Erreur écriture log: {e}")
            return False

    def lire_logs_date(self, date_str):
        """Lire les logs d'une date spécifique"""
        try:
            fichier_log = f"app_{date_str}.log"
            chemin_log = os.path.join(self.dossier_logs, fichier_log)

            if not os.path.exists(chemin_log):
                return f"❌ Aucun log pour la date {date_str}"

            with open(chemin_log, "r", encoding="utf-8") as f:
                contenu = f.read()

            return contenu

        except Exception as e:
            return f"❌ Erreur lecture logs: {e}"

    def analyser_logs(self, date_str):
        """Analyser les logs d'une journée"""
        try:
            contenu = self.lire_logs_date(date_str)

            if contenu.startswith("❌"):
                return contenu

            lignes = contenu.strip().split("\n")

            # Comptage par niveau
            compteurs = {niveau: 0 for niveau in self.types_logs.keys()}

            for ligne in lignes:
                for niveau in self.types_logs.keys():
                    if f"] {niveau} " in ligne:
                        compteurs[niveau] += 1
                        break

            # Statistiques
            total = sum(compteurs.values())
            analyse = {
                "date": date_str,
                "total_messages": total,
                "repartition": compteurs,
                "pourcentages": {
                    niveau: (count / total * 100) if total > 0 else 0
                    for niveau, count in compteurs.items()
                },
            }

            return analyse

        except Exception as e:
            return f"❌ Erreur analyse: {e}"

    def nettoyer_anciens_logs(self, jours_retention=30, simulation=True):
        """Nettoyer les logs anciens"""
        try:
            from datetime import timedelta

            date_limite = datetime.now() - timedelta(days=jours_retention)
            fichiers_logs = rechercher_fichiers(self.dossier_logs, extension="log")

            fichiers_anciens = []

            for fichier in fichiers_logs:
                info = obtenir_info_fichier(fichier)
                if isinstance(info, dict):
                    if info["modification"] < date_limite:
                        fichiers_anciens.append(fichier)

            if simulation:
                print(f"🔍 SIMULATION - Logs anciens (>{jours_retention} jours):")
                for fichier in fichiers_anciens:
                    info = obtenir_info_fichier(fichier)
                    print(
                        f"  - {os.path.basename(fichier)} ({info['modification'].strftime('%d/%m/%Y')})"
                    )
                print(f"Total: {len(fichiers_anciens)} fichiers")
            else:
                for fichier in fichiers_anciens:
                    os.remove(fichier)
                print(f"🗑️ {len(fichiers_anciens)} logs anciens supprimés")

            return len(fichiers_anciens)

        except Exception as e:
            print(f"❌ Erreur nettoyage logs: {e}")
            return 0

    def generer_rapport_logs(self, periode_jours=7):
        """Générer un rapport sur plusieurs jours"""
        try:
            from datetime import timedelta

            rapport = {
                "periode": periode_jours,
                "donnees_par_jour": {},
                "totaux": {niveau: 0 for niveau in self.types_logs.keys()},
                "total_general": 0,
            }

            for i in range(periode_jours):
                date = datetime.now() - timedelta(days=i)
                date_str = date.strftime("%Y-%m-%d")

                analyse = self.analyser_logs(date_str)

                if isinstance(analyse, dict) and "total_messages" in analyse:
                    rapport["donnees_par_jour"][date_str] = analyse

                    # Accumulation des totaux
                    for niveau, count in analyse["repartition"].items():
                        rapport["totaux"][niveau] += count

                    rapport["total_general"] += analyse["total_messages"]

            return rapport

        except Exception as e:
            return f"❌ Erreur génération rapport: {e}"


# Test du gestionnaire de logs
print("14. Test gestionnaire de logs :")
gestionnaire = GestionnaireLogs()

# Génération de logs de test
messages_test = [
    ("Application démarrée", "INFO"),
    ("Connexion utilisateur réussie", "SUCCESS"),
    ("Configuration chargée", "INFO"),
    ("Tentative de connexion échouée", "WARNING"),
    ("Erreur base de données", "ERROR"),
    ("Mode debug activé", "DEBUG"),
    ("Sauvegarde effectuée", "SUCCESS"),
    ("Mémoire faible", "WARNING"),
    ("Traitement terminé", "INFO"),
]

print("Génération de logs de test...")
for message, niveau in messages_test:
    gestionnaire.ecrire_log(message, niveau)

# Analyse des logs du jour
date_aujourd_hui = datetime.now().strftime("%Y-%m-%d")
print(f"\n15. Analyse des logs du {date_aujourd_hui}:")
analyse = gestionnaire.analyser_logs(date_aujourd_hui)

if isinstance(analyse, dict):
    print(f"Total de messages: {analyse['total_messages']}")
    print("Répartition par niveau:")
    for niveau, count in analyse["repartition"].items():
        pourcentage = analyse["pourcentages"][niveau]
        icone = gestionnaire.types_logs[niveau]
        print(f"  {icone} {niveau}: {count} ({pourcentage:.1f}%)")

# Génération de rapport
print(f"\n16. Rapport sur 3 jours:")
rapport = gestionnaire.generer_rapport_logs(3)
if isinstance(rapport, dict):
    print(f"Messages total sur {rapport['periode']} jours: {rapport['total_general']}")
    print("Totaux par niveau:")
    for niveau, count in rapport["totaux"].items():
        icone = gestionnaire.types_logs[niveau]
        print(f"  {icone} {niveau}: {count}")

print("\n🎉 Manipulation de fichiers terminée !")
print("⏭️ Passez maintenant aux données structurées !")
