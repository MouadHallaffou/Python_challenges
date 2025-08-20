# Challenge 2.2 - Dictionnaires et Tuples
# Votre code ici...
    # - Créez un dictionnaire "personne" avec nom, âge, ville
personne = {
    "nom": "mouad",
    "age": 30,
    "ville": "rabat"
}
    # - Modifiez l'âge et ajoutez la profession
personne["age"] = 32
personne["profession"] = "Ingénieur"
    # - Affichez toutes les clés et valeurs
def afficher_dictionnaire(personne):
    for cle, valeur in personne.items():
        print(f"{cle}: {valeur}")
afficher_dictionnaire(personne)
    # - Vérifiez si une clé existe
def verifier_cle_existe(personne):
    for cle in ["nom", "age", "profession", "ville"]:
        if cle in personne:
            print(f"La clé '{cle}' existe avec la valeur: {personne[cle]}")
        else:
            print(f"La clé '{cle}' n'existe pas.")
verifier_cle_existe(personne)

# Challenge 3.1 - Lambda et fonctions d'ordre supérieur
# Votre code ici...
    # Créez un système d'inventaire de magasin :
        # - Dictionnaire produits : {"nom": {"prix": X, "stock": Y}}
        # - Fonctions : ajouter_produit, vendre_produit, restock
        # - Calcul de la valeur totale du stock

def ajouter_produit(inventaire, nom, prix, stock):
    inventaire[nom] = {"prix": prix, "stock": stock}

def vendre_produit(inventaire, nom, quantite):
    if nom in inventaire and inventaire[nom]["stock"] >= quantite:
        inventaire[nom]["stock"] -= quantite
        print(f"Vente de {quantite} unités de {nom}.")
    else:
        print(f"Produit non disponible ou stock insuffisant.")

def restock(inventaire, nom, quantite):
    if nom in inventaire:
        inventaire[nom]["stock"] += quantite
        print(f"Restock de {quantite} unités de {nom}.")
    else:
        print(f"Produit {nom} non trouvé dans l'inventaire.")

def calculer_valeur_totale(inventaire):
    return sum(item["prix"] * item["stock"] for item in inventaire.values())

# Initialiser l'inventaire
inventaire = {}

print("*" * 20)
print("========= système d'inventaire =========")
print("*" * 20)

while True:
    print("sélectionnez une action")
    print("1. Ajouter un produit")
    print("2. Vendre un produit")
    print("3. Restocker un produit")
    print("4. Afficher la valeur totale du stock")
    print("5. Quitter")
    choix = input("Entrez votre choix (1-5): ")
    if choix == "1":
        nom = input("Nom du produit: ")
        prix = float(input("Prix du produit: "))
        stock = int(input("Quantité en stock: "))
        ajouter_produit(inventaire, nom, prix, stock)
    elif choix == "2":
        nom = input("Nom du produit à vendre: ")
        quantite = int(input("Quantité à vendre: "))
        vendre_produit(inventaire, nom, quantite)
    elif choix == "3":
        nom = input("Nom du produit à restocker: ")
        quantite = int(input("Quantité à ajouter: "))
        restock(inventaire, nom, quantite)
    elif choix == "4":
        print(f"Valeur totale du stock: {calculer_valeur_totale(inventaire)}")
    elif choix == "5":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

# Challenge 4.1 - Classes et objets
# Votre code ici...
# - Créez des tuples coordonnées (x, y)      
tuple_coordonnees = (10, 20)
# - Fonction distance entre deux points
def calculer_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print(f"Distance entre {tuple_coordonnees} et (0, 0): {calculer_distance(tuple_coordonnees, (0, 0))} unité(s)")  
# - Liste d'étudiants avec (nom, note1, note2, note3)
etudiants = [
    ("Alice", 15, 14, 13),
    ("Bob", 12, 16, 14),
    ("Charlie", 18, 17, 19)
]
# - Calcul automatique des moyennes
def calculer_moyenne(etudiant):
    return sum(etudiant[1:]) / len(etudiant[1:])
moyennes = {etudiant[0]: calculer_moyenne(etudiant) for etudiant in etudiants}
print("Moyennes des étudiants:")
for nom, moyenne in moyennes.items():
    print(f"{nom}: {moyenne:.2f}")

# Challenge 5.1 - Gestion des exceptions
# Votre code ici...
    # Système complet avec dictionnaires imbriqués :

    # - Structure : {nom: {"tel": X, "email": Y, "adresse": Z}}
    # - Recherche par nom, téléphone
    # - Groupement par ville
    # - Export/import CSV
import csv 

def exporter_contacts(annuaire, fichier):
    with open(fichier, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Nom", "Téléphone", "Email", "Adresse"])
        for nom, infos in annuaire.items():
            writer.writerow([nom, infos["tel"], infos["email"], infos["adresse"]])

def importer_contacts(fichier):
    annuaire = {}
    with open(fichier, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            nom = row["Nom"]
            annuaire[nom] = {
                "tel": row["Téléphone"],
                "email": row["Email"],
                "adresse": row["Adresse"]
            }
    return annuaire 

def ajouter_contact(annuaire, nom, tel, email, adresse):
    annuaire[nom] = {
        "tel": tel,
        "email": email,
        "adresse": adresse
    }
    return annuaire

def rechercher_contact(annuaire, nom):
    return annuaire.get(nom)

def afficher_contacts(annuaire): 
    for nom, infos in annuaire.items():
        print(f"Nom: {nom}, Infos: {infos}")

print("*" * 20)
print("========= Système d'annuaire =========")
print("*" * 20)

while True:
    print("1. Ajouter un contact")
    print("2. Rechercher un contact")
    print("3. Afficher tous les contacts")
    print("4. Exporter les contacts")
    print("5. Importer les contacts")
    print("6. Quitter")
    choix = input("Entrez votre choix (1-6): ")
    if choix == "1":
        nom = input("Nom du contact: ")
        tel = input("Téléphone du contact: ")
        email = input("Email du contact: ")
        adresse = input("Adresse du contact: ")
        ajouter_contact(annuaire, nom, tel, email, adresse)
    elif choix == "2":
        nom = input("Nom du contact à rechercher: ")
        contact = rechercher_contact(annuaire, nom)
        if contact:
            print(f"Contact trouvé: {contact}")
        else:
            print("Contact non trouvé.")
    elif choix == "3":
        afficher_contacts(annuaire)
    elif choix == "4":
        fichier = input("Nom du fichier d'export (CSV): ")
        exporter_contacts(annuaire, fichier)
    elif choix == "5":
        fichier = input("Nom du fichier d'import (CSV): ")
        annuaire = importer_contacts(fichier)
    elif choix == "6":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")