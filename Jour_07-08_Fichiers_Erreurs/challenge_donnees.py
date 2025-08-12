# Challenge Jour 8 - Données Structurées et APIs
# Complétez tous les exercices ci-dessous

import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import urllib.request
import urllib.parse
import http.client
import os
import re

# =============================================================================
# PARTIE A - Traitement Avancé de Données CSV (45min)
# =============================================================================

print("=== PARTIE A - Traitement Avancé CSV ===")


# 1. Lecture et nettoyage de données CSV sales
def nettoyer_donnees_csv(nom_fichier_entree, nom_fichier_sortie):
    """Nettoyer un fichier CSV avec des données sales"""

    # Créer d'abord un fichier CSV sale pour la démonstration
    donnees_sales = [
        ["nom", "age", "email", "salaire", "ville"],
        ["  DUPONT, Alice  ", "25", "alice@email.com", "35000.50", "Paris"],
        ["martin bob", "TRENTE", "bob@invalid", "45000", "lyon"],
        ["", "22", "claire@email.com", "38000.75", ""],
        ["DURAND Claire", "-5", "claire.durand@email.com", "ABC", "Marseille"],
        ["Bernard Emma", "28", "emma@email.com", "42000", "toulouse"],
        ["  ", "35", "", "55000", "Nice"],
        ["ROBERT Grace", "24", "grace@email.com", "39500.25", "BORDEAUX"],
        ["petit françois", "29", "francois@email.com", "48000", "lille"],
    ]

    try:
        # Créer le fichier sale
        with open(nom_fichier_entree, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(donnees_sales)

        donnees_nettoyees = []

        with open(nom_fichier_entree, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for ligne in reader:
                ligne_nettoyee = {}

                # Nettoyer le nom
                nom = ligne["nom"].strip()
                if nom and nom != "":
                    # Capitaliser correctement
                    nom = " ".join(word.capitalize() for word in nom.split())
                    ligne_nettoyee["nom"] = nom
                else:
                    continue  # Ignorer les lignes sans nom

                # Nettoyer l'âge
                age_str = ligne["age"].strip()
                try:
                    age = int(age_str)
                    if 18 <= age <= 65:  # Âge valide pour un employé
                        ligne_nettoyee["age"] = age
                    else:
                        continue  # Ignorer les âges invalides
                except ValueError:
                    continue  # Ignorer les âges non numériques

                # Nettoyer l'email
                email = ligne["email"].strip().lower()
                if email and "@" in email and "." in email.split("@")[1]:
                    ligne_nettoyee["email"] = email
                else:
                    ligne_nettoyee["email"] = "email_manquant@example.com"

                # Nettoyer le salaire
                salaire_str = ligne["salaire"].strip()
                try:
                    salaire = float(salaire_str)
                    if salaire > 0:
                        ligne_nettoyee["salaire"] = round(salaire, 2)
                    else:
                        continue  # Ignorer les salaires négatifs
                except ValueError:
                    continue  # Ignorer les salaires non numériques

                # Nettoyer la ville
                ville = ligne["ville"].strip()
                if ville:
                    ligne_nettoyee["ville"] = ville.capitalize()
                else:
                    ligne_nettoyee["ville"] = "Non spécifiée"

                donnees_nettoyees.append(ligne_nettoyee)

        # Sauvegarder les données nettoyées
        if donnees_nettoyees:
            with open(nom_fichier_sortie, "w", newline="", encoding="utf-8") as f:
                fieldnames = ["nom", "age", "email", "salaire", "ville"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(donnees_nettoyees)

        print(
            f"✅ Données nettoyées: {len(donnees_nettoyees)} lignes valides sauvegardées"
        )
        return donnees_nettoyees

    except Exception as e:
        print(f"❌ Erreur nettoyage CSV: {e}")
        return []


# 2. Agrégation et calculs sur données CSV
def analyser_donnees_employees(donnees):
    """Analyser les données d'employés"""
    if not donnees:
        print("❌ Aucune donnée à analyser")
        return

    print("\n📊 ANALYSE DES DONNÉES EMPLOYÉS")
    print("=" * 40)

    # Statistiques générales
    salaires = [emp["salaire"] for emp in donnees]
    ages = [emp["age"] for emp in donnees]

    print(f"Nombre d'employés: {len(donnees)}")
    print(f"Âge moyen: {sum(ages)/len(ages):.1f} ans")
    print(f"Âge minimum: {min(ages)} ans")
    print(f"Âge maximum: {max(ages)} ans")
    print(f"Salaire moyen: {sum(salaires)/len(salaires):,.2f} €")
    print(f"Salaire minimum: {min(salaires):,.2f} €")
    print(f"Salaire maximum: {max(salaires):,.2f} €")

    # Analyse par ville
    villes = {}
    for emp in donnees:
        ville = emp["ville"]
        if ville not in villes:
            villes[ville] = {"count": 0, "salaires": [], "ages": []}
        villes[ville]["count"] += 1
        villes[ville]["salaires"].append(emp["salaire"])
        villes[ville]["ages"].append(emp["age"])

    print(f"\nRépartition par ville:")
    for ville, stats in sorted(villes.items()):
        salaire_moyen = sum(stats["salaires"]) / len(stats["salaires"])
        age_moyen = sum(stats["ages"]) / len(stats["ages"])
        print(
            f"  {ville}: {stats['count']} employés, "
            f"salaire moyen: {salaire_moyen:,.2f} €, "
            f"âge moyen: {age_moyen:.1f} ans"
        )

    # Tranches de salaires
    tranches = {"< 30k": 0, "30k-40k": 0, "40k-50k": 0, "> 50k": 0}

    for salaire in salaires:
        if salaire < 30000:
            tranches["< 30k"] += 1
        elif salaire < 40000:
            tranches["30k-40k"] += 1
        elif salaire < 50000:
            tranches["40k-50k"] += 1
        else:
            tranches["> 50k"] += 1

    print(f"\nRépartition par tranche de salaire:")
    for tranche, count in tranches.items():
        pourcentage = (count / len(donnees)) * 100
        print(f"  {tranche}: {count} employés ({pourcentage:.1f}%)")


# 3. Fusion de plusieurs fichiers CSV
def fusionner_csv(fichiers_entree, fichier_sortie, cle_unique="email"):
    """Fusionner plusieurs fichiers CSV en évitant les doublons"""
    try:
        donnees_fusionnees = {}

        for fichier in fichiers_entree:
            if not os.path.exists(fichier):
                print(f"⚠️ Fichier non trouvé: {fichier}")
                continue

            with open(fichier, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for ligne in reader:
                    cle = ligne.get(cle_unique)
                    if cle and cle not in donnees_fusionnees:
                        donnees_fusionnees[cle] = ligne
                    elif cle:
                        # Mise à jour avec les nouvelles données
                        donnees_fusionnees[cle].update(
                            {k: v for k, v in ligne.items() if v}
                        )

        # Sauvegarder les données fusionnées
        if donnees_fusionnees:
            donnees_liste = list(donnees_fusionnees.values())

            with open(fichier_sortie, "w", newline="", encoding="utf-8") as f:
                if donnees_liste:
                    fieldnames = donnees_liste[0].keys()
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(donnees_liste)

        print(f"✅ Fusion terminée: {len(donnees_fusionnees)} enregistrements uniques")
        return len(donnees_fusionnees)

    except Exception as e:
        print(f"❌ Erreur fusion CSV: {e}")
        return 0


# Tests des fonctions CSV avancées
print("1. Nettoyage de données CSV :")
donnees_propres = nettoyer_donnees_csv("donnees_sales.csv", "donnees_propres.csv")
analyser_donnees_employees(donnees_propres)

# =============================================================================
# PARTIE B - Traitement de Données XML (45min)
# =============================================================================

print("\n=== PARTIE B - Traitement XML ===")


# 1. Création et écriture de fichiers XML
def creer_xml_bibliotheque(nom_fichier="bibliotheque.xml"):
    """Créer un fichier XML de bibliothèque"""
    try:
        # Création de l'élément racine
        bibliotheque = ET.Element("bibliotheque")
        bibliotheque.set("nom", "Bibliothèque Municipale")
        bibliotheque.set("ville", "Paris")

        # Informations générales
        infos = ET.SubElement(bibliotheque, "informations")

        adresse = ET.SubElement(infos, "adresse")
        adresse.text = "123 Rue des Livres, 75001 Paris"

        telephone = ET.SubElement(infos, "telephone")
        telephone.text = "01.23.45.67.89"

        email = ET.SubElement(infos, "email")
        email.text = "contact@bibliotheque-municipale.fr"

        # Section des livres
        livres = ET.SubElement(bibliotheque, "livres")

        donnees_livres = [
            {
                "id": "1",
                "titre": "Le Petit Prince",
                "auteur": "Antoine de Saint-Exupéry",
                "isbn": "978-2-07-040818-9",
                "genre": "Fiction",
                "annee": "1943",
                "pages": "96",
                "disponible": "true",
                "emplacement": "A-01-15",
            },
            {
                "id": "2",
                "titre": "1984",
                "auteur": "George Orwell",
                "isbn": "978-2-07-036822-5",
                "genre": "Science-fiction",
                "annee": "1949",
                "pages": "376",
                "disponible": "false",
                "emplacement": "B-03-22",
            },
            {
                "id": "3",
                "titre": "Python pour les nuls",
                "auteur": "Stef Maruch",
                "isbn": "978-2-412-05976-8",
                "genre": "Informatique",
                "annee": "2019",
                "pages": "512",
                "disponible": "true",
                "emplacement": "C-05-08",
            },
        ]

        for donnees_livre in donnees_livres:
            livre = ET.SubElement(livres, "livre")
            livre.set("id", donnees_livre["id"])

            for cle, valeur in donnees_livre.items():
                if cle != "id":
                    element = ET.SubElement(livre, cle)
                    element.text = valeur

        # Section des emprunts
        emprunts = ET.SubElement(bibliotheque, "emprunts")

        emprunt1 = ET.SubElement(emprunts, "emprunt")
        emprunt1.set("id", "1")

        ET.SubElement(emprunt1, "livre_id").text = "2"
        ET.SubElement(emprunt1, "emprunteur").text = "Alice Dupont"
        ET.SubElement(emprunt1, "date_emprunt").text = "2024-01-15"
        ET.SubElement(emprunt1, "date_retour_prevue").text = "2024-02-15"

        # Sauvegarde du fichier
        tree = ET.ElementTree(bibliotheque)
        tree.write(nom_fichier, encoding="utf-8", xml_declaration=True)

        print(f"✅ Fichier XML créé: {nom_fichier}")
        return True

    except Exception as e:
        print(f"❌ Erreur création XML: {e}")
        return False


# 2. Lecture et parsing de fichiers XML
def lire_xml_bibliotheque(nom_fichier="bibliotheque.xml"):
    """Lire et parser le fichier XML de bibliothèque"""
    try:
        tree = ET.parse(nom_fichier)
        root = tree.getroot()

        print(f"📚 Bibliothèque: {root.get('nom')} ({root.get('ville')})")

        # Informations générales
        infos = root.find("informations")
        if infos is not None:
            print(f"Adresse: {infos.find('adresse').text}")
            print(f"Téléphone: {infos.find('telephone').text}")
            print(f"Email: {infos.find('email').text}")

        # Liste des livres
        livres = root.find("livres")
        if livres is not None:
            print(f"\n📖 Livres disponibles: {len(livres.findall('livre'))}")

            for livre in livres.findall("livre"):
                livre_id = livre.get("id")
                titre = livre.find("titre").text
                auteur = livre.find("auteur").text
                genre = livre.find("genre").text
                disponible = livre.find("disponible").text == "true"
                emplacement = livre.find("emplacement").text

                statut = "✅ Disponible" if disponible else "❌ Emprunté"
                print(
                    f"  [{livre_id}] {titre} - {auteur} ({genre}) - {statut} - {emplacement}"
                )

        # Emprunts en cours
        emprunts = root.find("emprunts")
        if emprunts is not None:
            print(f"\n📋 Emprunts en cours: {len(emprunts.findall('emprunt'))}")

            for emprunt in emprunts.findall("emprunt"):
                emprunt_id = emprunt.get("id")
                livre_id = emprunt.find("livre_id").text
                emprunteur = emprunt.find("emprunteur").text
                date_emprunt = emprunt.find("date_emprunt").text
                date_retour = emprunt.find("date_retour_prevue").text

                print(
                    f"  [{emprunt_id}] Livre {livre_id} - {emprunteur} - {date_emprunt} → {date_retour}"
                )

        return root

    except FileNotFoundError:
        print(f"❌ Fichier {nom_fichier} non trouvé")
        return None
    except ET.ParseError as e:
        print(f"❌ Erreur parsing XML: {e}")
        return None
    except Exception as e:
        print(f"❌ Erreur lecture XML: {e}")
        return None


# 3. Recherche et modification dans XML
def rechercher_livres_xml(root, critere, valeur):
    """Rechercher des livres dans le XML selon un critère"""
    if root is None:
        return []

    resultats = []
    livres = root.find("livres")

    if livres is not None:
        for livre in livres.findall("livre"):
            element = livre.find(critere)
            if element is not None and valeur.lower() in element.text.lower():
                resultats.append(
                    {
                        "id": livre.get("id"),
                        "titre": livre.find("titre").text,
                        "auteur": livre.find("auteur").text,
                        "genre": livre.find("genre").text,
                        "disponible": livre.find("disponible").text == "true",
                    }
                )

    return resultats


def ajouter_livre_xml(root, nouveau_livre, nom_fichier="bibliotheque.xml"):
    """Ajouter un livre au fichier XML"""
    try:
        if root is None:
            return False

        livres = root.find("livres")
        if livres is None:
            livres = ET.SubElement(root, "livres")

        # Générer un nouvel ID
        ids_existants = [int(livre.get("id")) for livre in livres.findall("livre")]
        nouvel_id = max(ids_existants) + 1 if ids_existants else 1

        # Créer le nouvel élément livre
        livre = ET.SubElement(livres, "livre")
        livre.set("id", str(nouvel_id))

        for cle, valeur in nouveau_livre.items():
            element = ET.SubElement(livre, cle)
            element.text = str(valeur)

        # Sauvegarder
        tree = ET.ElementTree(root)
        tree.write(nom_fichier, encoding="utf-8", xml_declaration=True)

        print(
            f"✅ Livre ajouté avec ID {nouvel_id}: {nouveau_livre.get('titre', 'Sans titre')}"
        )
        return True

    except Exception as e:
        print(f"❌ Erreur ajout livre XML: {e}")
        return False


# Tests des fonctions XML
print("2. Création et manipulation XML :")
creer_xml_bibliotheque()
root = lire_xml_bibliotheque()

print("\n3. Recherche dans XML :")
livres_fiction = rechercher_livres_xml(root, "genre", "Fiction")
print(f"Livres de fiction trouvés: {len(livres_fiction)}")
for livre in livres_fiction:
    statut = "Disponible" if livre["disponible"] else "Emprunté"
    print(f"  - {livre['titre']} par {livre['auteur']} ({statut})")

print("\n4. Ajout de livre en XML :")
nouveau_livre = {
    "titre": "Clean Code",
    "auteur": "Robert C. Martin",
    "isbn": "978-0-13-235088-4",
    "genre": "Informatique",
    "annee": "2008",
    "pages": "464",
    "disponible": "true",
    "emplacement": "C-05-09",
}
ajouter_livre_xml(root, nouveau_livre)

# =============================================================================
# PARTIE C - APIs et Données Web (Simulation) (45min)
# =============================================================================

print("\n=== PARTIE C - APIs et Données Web (Simulation) ===")

# Note: Pour éviter les dépendances externes, nous simulons les appels API


class SimulateurAPI:
    """Simulateur d'API pour les exercices"""

    def __init__(self):
        # Données simulées pour l'API météo
        self.donnees_meteo = {
            "Paris": {
                "temperature": 15.5,
                "humidite": 65,
                "description": "Nuageux",
                "vent": 12,
                "pression": 1013,
            },
            "Londres": {
                "temperature": 12.3,
                "humidite": 78,
                "description": "Pluvieux",
                "vent": 18,
                "pression": 998,
            },
            "New York": {
                "temperature": 22.1,
                "humidite": 55,
                "description": "Ensoleillé",
                "vent": 8,
                "pression": 1021,
            },
        }

        # Données simulées pour l'API de taux de change
        self.taux_change = {
            "EUR": 1.0,
            "USD": 1.08,
            "GBP": 0.87,
            "JPY": 162.45,
            "CAD": 1.46,
        }

        # Données simulées pour l'API de nouvelles
        self.nouvelles = [
            {
                "id": 1,
                "titre": "Nouvelle découverte en IA",
                "auteur": "Tech News",
                "date": "2024-01-20",
                "categorie": "Technologie",
                "contenu": "Une nouvelle avancée majeure dans l'intelligence artificielle...",
            },
            {
                "id": 2,
                "titre": "Climat : rapport alarmant",
                "auteur": "Science Today",
                "date": "2024-01-19",
                "categorie": "Environnement",
                "contenu": "Les dernières études climatiques révèlent...",
            },
            {
                "id": 3,
                "titre": "Marché financier en hausse",
                "auteur": "Finance Daily",
                "date": "2024-01-18",
                "categorie": "Finance",
                "contenu": "Les marchés financiers affichent une tendance positive...",
            },
        ]

    def obtenir_meteo(self, ville):
        """Simuler un appel API météo"""
        try:
            # Simulation d'un délai de réseau
            import time

            time.sleep(0.1)

            if ville in self.donnees_meteo:
                donnees = self.donnees_meteo[ville].copy()
                donnees["ville"] = ville
                donnees["timestamp"] = datetime.now().isoformat()
                return donnees
            else:
                return {"erreur": f"Ville {ville} non trouvée"}

        except Exception as e:
            return {"erreur": f"Erreur API: {e}"}

    def convertir_devise(self, montant, devise_source, devise_cible):
        """Simuler un appel API de conversion de devise"""
        try:
            import time

            time.sleep(0.1)

            if (
                devise_source not in self.taux_change
                or devise_cible not in self.taux_change
            ):
                return {"erreur": "Devise non supportée"}

            # Conversion via EUR comme devise de base
            montant_eur = montant / self.taux_change[devise_source]
            montant_final = montant_eur * self.taux_change[devise_cible]

            return {
                "montant_source": montant,
                "devise_source": devise_source,
                "montant_cible": round(montant_final, 2),
                "devise_cible": devise_cible,
                "taux": round(montant_final / montant, 4),
                "timestamp": datetime.now().isoformat(),
            }

        except Exception as e:
            return {"erreur": f"Erreur conversion: {e}"}

    def obtenir_nouvelles(self, categorie=None, limite=10):
        """Simuler un appel API de nouvelles"""
        try:
            import time

            time.sleep(0.1)

            nouvelles_filtrees = self.nouvelles

            if categorie:
                nouvelles_filtrees = [
                    n
                    for n in self.nouvelles
                    if n["categorie"].lower() == categorie.lower()
                ]

            return {
                "total": len(nouvelles_filtrees),
                "articles": nouvelles_filtrees[:limite],
            }

        except Exception as e:
            return {"erreur": f"Erreur nouvelles: {e}"}


# 1. Classe pour gérer les appels API
class GestionnaireAPI:
    """Gestionnaire centralisé pour les appels API"""

    def __init__(self):
        self.api = SimulateurAPI()
        self.cache = {}
        self.historique = []

    def appel_avec_cache(self, methode, *args, duree_cache=300):
        """Effectuer un appel API avec mise en cache"""
        try:
            # Créer une clé de cache
            cle_cache = f"{methode.__name__}_{hash(str(args))}"

            # Vérifier le cache
            if cle_cache in self.cache:
                donnees_cache, timestamp = self.cache[cle_cache]
                age_cache = (datetime.now() - timestamp).total_seconds()

                if age_cache < duree_cache:
                    print(f"📋 Données récupérées du cache (âge: {age_cache:.1f}s)")
                    return donnees_cache

            # Appel API réel
            print(f"🌐 Appel API: {methode.__name__}")
            resultat = methode(*args)

            # Mise en cache
            if "erreur" not in resultat:
                self.cache[cle_cache] = (resultat, datetime.now())

            # Historique
            self.historique.append(
                {
                    "methode": methode.__name__,
                    "args": args,
                    "timestamp": datetime.now().isoformat(),
                    "succes": "erreur" not in resultat,
                }
            )

            return resultat

        except Exception as e:
            return {"erreur": f"Erreur gestionnaire API: {e}"}

    def obtenir_meteo_ville(self, ville):
        """Obtenir la météo avec cache"""
        return self.appel_avec_cache(self.api.obtenir_meteo, ville)

    def convertir_devise(self, montant, source, cible):
        """Convertir devise avec cache"""
        return self.appel_avec_cache(self.api.convertir_devise, montant, source, cible)

    def obtenir_nouvelles(self, categorie=None):
        """Obtenir nouvelles avec cache"""
        return self.appel_avec_cache(self.api.obtenir_nouvelles, categorie)

    def afficher_historique(self):
        """Afficher l'historique des appels API"""
        print(f"\n📊 HISTORIQUE DES APPELS API ({len(self.historique)} appels)")
        print("=" * 50)

        for i, appel in enumerate(self.historique[-10:], 1):  # Derniers 10 appels
            timestamp = datetime.fromisoformat(appel["timestamp"])
            statut = "✅" if appel["succes"] else "❌"
            print(
                f"{i:2d}. {statut} {appel['methode']} - {timestamp.strftime('%H:%M:%S')}"
            )


# 2. Traitement et analyse de données API
def analyser_donnees_meteo(donnees_meteo_list):
    """Analyser plusieurs données météo"""
    if not donnees_meteo_list:
        print("❌ Aucune donnée météo à analyser")
        return

    print(f"\n🌤️ ANALYSE MÉTÉO - {len(donnees_meteo_list)} villes")
    print("=" * 40)

    temperatures = []
    humidites = []
    pressions = []

    for donnees in donnees_meteo_list:
        if "erreur" not in donnees:
            print(
                f"{donnees['ville']}: {donnees['temperature']}°C, "
                f"{donnees['description']}, Humidité: {donnees['humidite']}%"
            )

            temperatures.append(donnees["temperature"])
            humidites.append(donnees["humidite"])
            pressions.append(donnees["pression"])

    if temperatures:
        print(f"\nStatistiques globales:")
        print(f"  Température moyenne: {sum(temperatures)/len(temperatures):.1f}°C")
        print(
            f"  Température min/max: {min(temperatures):.1f}°C / {max(temperatures):.1f}°C"
        )
        print(f"  Humidité moyenne: {sum(humidites)/len(humidites):.1f}%")
        print(f"  Pression moyenne: {sum(pressions)/len(pressions):.1f} hPa")


def sauvegarder_donnees_api(donnees, nom_fichier, format_fichier="json"):
    """Sauvegarder des données API dans différents formats"""
    try:
        if format_fichier.lower() == "json":
            with open(nom_fichier, "w", encoding="utf-8") as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False, default=str)

        elif format_fichier.lower() == "csv":
            # Convertir en format tabulaire
            if isinstance(donnees, list) and donnees:
                if isinstance(donnees[0], dict):
                    with open(nom_fichier, "w", newline="", encoding="utf-8") as f:
                        fieldnames = donnees[0].keys()
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(donnees)
                else:
                    print("❌ Format non compatible avec CSV")
                    return False

        print(f"✅ Données sauvegardées: {nom_fichier} (format: {format_fichier})")
        return True

    except Exception as e:
        print(f"❌ Erreur sauvegarde: {e}")
        return False


# Tests des fonctions API
print("5. Test des appels API avec cache :")
gestionnaire = GestionnaireAPI()

# Tests météo
villes = ["Paris", "Londres", "New York", "Tokyo"]
donnees_meteo = []

for ville in villes:
    donnees = gestionnaire.obtenir_meteo_ville(ville)
    donnees_meteo.append(donnees)

# Deuxième appel pour tester le cache
print("\nDeuxième appel (avec cache) :")
donnees_paris = gestionnaire.obtenir_meteo_ville("Paris")

analyser_donnees_meteo(donnees_meteo)

print("\n6. Test conversion de devises :")
conversions = [(100, "EUR", "USD"), (500, "USD", "EUR"), (1000, "EUR", "JPY")]

resultats_conversion = []
for montant, source, cible in conversions:
    resultat = gestionnaire.convertir_devise(montant, source, cible)
    if "erreur" not in resultat:
        print(
            f"{resultat['montant_source']} {resultat['devise_source']} = "
            f"{resultat['montant_cible']} {resultat['devise_cible']} "
            f"(taux: {resultat['taux']})"
        )
        resultats_conversion.append(resultat)

gestionnaire.afficher_historique()

# =============================================================================
# MINI-PROJET - Agrégateur de Données Multi-Sources (60min)
# =============================================================================

print("\n=== MINI-PROJET - Agrégateur de Données ===")


class AgregateurDonnees:
    """Agrégateur de données provenant de multiples sources"""

    def __init__(self):
        self.gestionnaire_api = GestionnaireAPI()
        self.donnees_agregees = {
            "meteo": {},
            "finance": {},
            "actualites": {},
            "timestamp": None,
        }

    def collecter_donnees_complete(self, villes, devises_base="EUR"):
        """Collecter toutes les données pour un rapport complet"""
        print("🔄 Collecte des données en cours...")

        # Données météo
        print("📡 Collecte des données météo...")
        for ville in villes:
            donnees = self.gestionnaire_api.obtenir_meteo_ville(ville)
            if "erreur" not in donnees:
                self.donnees_agregees["meteo"][ville] = donnees

        # Données financières
        print("💰 Collecte des taux de change...")
        devises_cibles = ["USD", "GBP", "JPY", "CAD"]
        for devise in devises_cibles:
            if devise != devises_base:
                conversion = self.gestionnaire_api.convertir_devise(
                    1, devises_base, devise
                )
                if "erreur" not in conversion:
                    self.donnees_agregees["finance"][
                        f"{devises_base}_{devise}"
                    ] = conversion

        # Données d'actualités
        print("📰 Collecte des actualités...")
        categories = ["Technologie", "Environnement", "Finance"]
        for categorie in categories:
            nouvelles = self.gestionnaire_api.obtenir_nouvelles(categorie)
            if "erreur" not in nouvelles:
                self.donnees_agregees["actualites"][categorie] = nouvelles

        self.donnees_agregees["timestamp"] = datetime.now().isoformat()
        print("✅ Collecte terminée")

    def generer_rapport_html(self, nom_fichier="rapport_donnees.html"):
        """Générer un rapport HTML des données collectées"""
        try:
            html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de Données Agrégées</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; text-align: center; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
        h2 {{ color: #4CAF50; border-left: 4px solid #4CAF50; padding-left: 10px; }}
        .section {{ margin: 20px 0; }}
        .meteo-card {{ background: linear-gradient(135deg, #74b9ff, #0984e3); color: white; padding: 15px; margin: 10px 0; border-radius: 8px; }}
        .finance-card {{ background: linear-gradient(135deg, #00b894, #00a085); color: white; padding: 15px; margin: 10px 0; border-radius: 8px; }}
        .news-card {{ background: #f8f9fa; border-left: 4px solid #6c757d; padding: 15px; margin: 10px 0; border-radius: 0 8px 8px 0; }}
        .timestamp {{ text-align: center; color: #666; font-style: italic; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Rapport de Données Agrégées</h1>
        <p class="timestamp">Généré le: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
"""

            # Section météo
            if self.donnees_agregees["meteo"]:
                html_content += """
        <div class="section">
            <h2>🌤️ Données Météorologiques</h2>
"""
                for ville, donnees in self.donnees_agregees["meteo"].items():
                    html_content += f"""
            <div class="meteo-card">
                <h3>{ville}</h3>
                <p><strong>Température:</strong> {donnees['temperature']}°C</p>
                <p><strong>Description:</strong> {donnees['description']}</p>
                <p><strong>Humidité:</strong> {donnees['humidite']}%</p>
                <p><strong>Vent:</strong> {donnees['vent']} km/h</p>
                <p><strong>Pression:</strong> {donnees['pression']} hPa</p>
            </div>
"""
                html_content += "        </div>"

            # Section finance
            if self.donnees_agregees["finance"]:
                html_content += """
        <div class="section">
            <h2>💰 Taux de Change</h2>
            <table>
                <tr><th>Conversion</th><th>Taux</th><th>Exemple (100 unités)</th></tr>
"""
                for cle, donnees in self.donnees_agregees["finance"].items():
                    exemple = 100 * donnees["taux"]
                    html_content += f"""
                <tr>
                    <td>{donnees['devise_source']} → {donnees['devise_cible']}</td>
                    <td>{donnees['taux']}</td>
                    <td>100 {donnees['devise_source']} = {exemple:.2f} {donnees['devise_cible']}</td>
                </tr>
"""
                html_content += """
            </table>
        </div>
"""

            # Section actualités
            if self.donnees_agregees["actualites"]:
                html_content += """
        <div class="section">
            <h2>📰 Actualités</h2>
"""
                for categorie, donnees_news in self.donnees_agregees[
                    "actualites"
                ].items():
                    html_content += f"            <h3>{categorie}</h3>"
                    for article in donnees_news.get("articles", [])[
                        :3
                    ]:  # 3 premiers articles
                        html_content += f"""
            <div class="news-card">
                <h4>{article['titre']}</h4>
                <p><strong>Auteur:</strong> {article['auteur']} | <strong>Date:</strong> {article['date']}</p>
                <p>{article['contenu'][:150]}...</p>
            </div>
"""
                html_content += "        </div>"

            html_content += """
    </div>
</body>
</html>
"""

            # Sauvegarder le fichier HTML
            with open(nom_fichier, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"✅ Rapport HTML généré: {nom_fichier}")
            return True

        except Exception as e:
            print(f"❌ Erreur génération rapport: {e}")
            return False

    def exporter_donnees_json(self, nom_fichier="donnees_agregees.json"):
        """Exporter toutes les données en JSON"""
        return sauvegarder_donnees_api(self.donnees_agregees, nom_fichier, "json")

    def analyser_tendances(self):
        """Analyser les tendances dans les données collectées"""
        print("\n📈 ANALYSE DES TENDANCES")
        print("=" * 40)

        # Analyse météo
        if self.donnees_agregees["meteo"]:
            temperatures = [
                d["temperature"] for d in self.donnees_agregees["meteo"].values()
            ]
            temp_moy = sum(temperatures) / len(temperatures)

            print(f"🌡️ Météo globale:")
            print(f"  Température moyenne: {temp_moy:.1f}°C")

            ville_plus_chaude = max(
                self.donnees_agregees["meteo"].items(),
                key=lambda x: x[1]["temperature"],
            )
            ville_plus_froide = min(
                self.donnees_agregees["meteo"].items(),
                key=lambda x: x[1]["temperature"],
            )

            print(
                f"  Plus chaude: {ville_plus_chaude[0]} ({ville_plus_chaude[1]['temperature']}°C)"
            )
            print(
                f"  Plus froide: {ville_plus_froide[0]} ({ville_plus_froide[1]['temperature']}°C)"
            )

        # Analyse finance
        if self.donnees_agregees["finance"]:
            print(f"\n💱 Tendances financières:")
            for cle, donnees in self.donnees_agregees["finance"].items():
                devise_cible = donnees["devise_cible"]
                taux = donnees["taux"]

                if taux > 1:
                    print(f"  1 EUR = {taux:.4f} {devise_cible} (EUR fort)")
                else:
                    print(f"  1 EUR = {taux:.4f} {devise_cible} (EUR faible)")

        # Analyse actualités
        if self.donnees_agregees["actualites"]:
            print(f"\n📊 Répartition des actualités:")
            for categorie, donnees_news in self.donnees_agregees["actualites"].items():
                nb_articles = len(donnees_news.get("articles", []))
                print(f"  {categorie}: {nb_articles} articles")


# Test du mini-projet
print("7. Test de l'agrégateur de données :")

agregateur = AgregateurDonnees()

# Collecte des données
villes_test = ["Paris", "Londres", "New York"]
agregateur.collecter_donnees_complete(villes_test)

# Analyse des tendances
agregateur.analyser_tendances()

# Export des données
print("\n8. Export des données :")
agregateur.exporter_donnees_json()
agregateur.generer_rapport_html()

print("\n🎉 Traitement de données terminé !")
print("📁 Fichiers générés: donnees_agregees.json, rapport_donnees.html")
print("⏭️ Passez maintenant au projet final !")
