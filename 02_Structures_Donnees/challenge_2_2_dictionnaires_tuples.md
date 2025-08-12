# 🎯 Challenge 2.2 : Dictionnaires et Tuples

## 📚 Objectif

Maîtriser les dictionnaires pour les données clé-valeur et les tuples pour les données immutables.

## 🔧 Ce que vous devez apprendre

- Création et manipulation de dictionnaires
- Accès, ajout, suppression d'éléments
- Méthodes : keys(), values(), items()
- Tuples : création, unpacking
- Différences mutables/immutables

---

## 📖 **EXPLICATIONS DÉTAILLÉES AVEC EXEMPLES**

### 📚 **1. Les Dictionnaires - Collections Clé-Valeur**

Un dictionnaire est une **collection non-ordonnée** d'éléments stockés sous forme de **paires clé-valeur**. C'est comme un **annuaire téléphonique** : vous cherchez par nom (clé) pour obtenir le numéro (valeur).

#### **Caractéristiques des dictionnaires :**

- ✅ **Clés uniques** : Chaque clé ne peut apparaître qu'une seule fois
- ✅ **Modifiables** : On peut ajouter, modifier, supprimer des éléments
- ✅ **Accès rapide** : Recherche très efficace par clé
- ✅ **Clés immutables** : Les clés doivent être des types immutables (str, int, tuple)

---

### 🏗️ **2. Création et Initialisation de Dictionnaires**

#### **Exemple 1 - Différentes façons de créer des dictionnaires :**

```python
# Dictionnaire vide
mon_dict_vide = {}
autre_dict_vide = dict()

# Dictionnaire avec des éléments
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "profession": "Développeuse"
}

# Création avec dict()
coordonnees = dict(x=10, y=20, z=5)

# Création à partir de listes
cles = ["nom", "age", "ville"]
valeurs = ["Bob", 30, "Lyon"]
personne2 = dict(zip(cles, valeurs))

print(f"Personne: {personne}")
print(f"Coordonnées: {coordonnees}")
print(f"Personne2: {personne2}")
```

#### **Exemple 2 - Dictionnaires avec différents types de données :**

```python
# Dictionnaire complexe
etudiant = {
    "nom": "Charlie",
    "age": 20,
    "notes": [15, 18, 12, 16],
    "actif": True,
    "adresse": {
        "rue": "123 Rue de la Paix",
        "ville": "Marseille",
        "code_postal": "13000"
    }
}

print(f"Étudiant: {etudiant}")
print(f"Notes: {etudiant['notes']}")
print(f"Ville: {etudiant['adresse']['ville']}")
```

---

### 🎯 **3. Accès aux Éléments**

#### **Exemple 1 - Accès par clé :**

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

# Accès direct par clé
print(f"Nom: {personne['nom']}")          # Alice
print(f"Âge: {personne['age']}")          # 25

# Accès sécurisé avec get()
print(f"Ville: {personne.get('ville')}")         # Paris
print(f"Profession: {personne.get('profession', 'Non spécifiée')}")  # Non spécifiée

# Vérifier l'existence d'une clé
print(f"'nom' existe: {'nom' in personne}")        # True
print(f"'salaire' existe: {'salaire' in personne}")  # False
```

#### **Exemple 2 - Gestion des erreurs :**

```python
def obtenir_valeur_securisee(dictionnaire, cle):
    """Obtient une valeur du dictionnaire sans risquer d'erreur"""
    try:
        return dictionnaire[cle]
    except KeyError:
        return f"La clé '{cle}' n'existe pas"

personne = {"nom": "Alice", "age": 25}
print(obtenir_valeur_securisee(personne, "nom"))     # Alice
print(obtenir_valeur_securisee(personne, "salaire")) # La clé 'salaire' n'existe pas
```

---

### 🔧 **4. Modification des Dictionnaires**

#### **Ajouter et modifier des éléments :**

```python
personne = {"nom": "Alice", "age": 25}
print(f"Dictionnaire initial: {personne}")

# Ajouter un nouvel élément
personne["ville"] = "Paris"
print(f"Après ajout ville: {personne}")

# Modifier un élément existant
personne["age"] = 26
print(f"Après modification âge: {personne}")

# Ajouter plusieurs éléments avec update()
personne.update({"profession": "Développeuse", "salaire": 45000})
print(f"Après update: {personne}")

# Fusion de dictionnaires (Python 3.9+)
infos_supplementaires = {"hobbies": ["lecture", "natation"], "nationalité": "française"}
personne_complete = personne | infos_supplementaires
print(f"Fusion: {personne_complete}")
```

#### **Supprimer des éléments :**

```python
personne = {
    "nom": "Alice",
    "age": 26,
    "ville": "Paris",
    "profession": "Développeuse",
    "salaire": 45000
}

print(f"Dictionnaire initial: {personne}")

# del - supprime une clé
del personne["salaire"]
print(f"Après del salaire: {personne}")

# pop() - supprime et retourne la valeur
profession = personne.pop("profession")
print(f"Profession supprimée: {profession}")
print(f"Après pop profession: {personne}")

# pop() avec valeur par défaut
hobby = personne.pop("hobby", "Aucun hobby défini")
print(f"Hobby: {hobby}")

# popitem() - supprime et retourne le dernier élément (Python 3.7+)
dernier_element = personne.popitem()
print(f"Dernier élément supprimé: {dernier_element}")
print(f"Dictionnaire final: {personne}")
```

---

### 🔍 **5. Méthodes Importantes des Dictionnaires**

#### **Exemple - keys(), values(), items() :**

```python
notes_etudiants = {
    "Alice": [15, 18, 16],
    "Bob": [12, 14, 13],
    "Charlie": [17, 19, 18],
    "Diana": [11, 15, 12]
}

# keys() - obtient toutes les clés
print("=== ÉTUDIANTS ===")
for etudiant in notes_etudiants.keys():
    print(f"- {etudiant}")

# values() - obtient toutes les valeurs
print("\n=== TOUTES LES NOTES ===")
for notes in notes_etudiants.values():
    print(f"Notes: {notes}")

# items() - obtient les paires clé-valeur
print("\n=== DÉTAIL PAR ÉTUDIANT ===")
for etudiant, notes in notes_etudiants.items():
    moyenne = sum(notes) / len(notes)
    print(f"{etudiant}: {notes} → Moyenne: {moyenne:.2f}")
```

#### **Exemple - Méthodes de copie :**

```python
original = {"a": 1, "b": 2, "c": 3}

# Copie superficielle
copie = original.copy()
copie["d"] = 4

print(f"Original: {original}")    # {'a': 1, 'b': 2, 'c': 3}
print(f"Copie: {copie}")         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Attention avec les références !
original_avec_liste = {"nums": [1, 2, 3]}
copie_superficielle = original_avec_liste.copy()
copie_superficielle["nums"].append(4)  # Modifie aussi l'original !

print(f"Original avec liste: {original_avec_liste}")  # {'nums': [1, 2, 3, 4]}
```

---

### 📦 **6. Les Tuples - Collections Immutables**

Un tuple est une **collection ordonnée et immutable** d'éléments. C'est comme une **boîte fermée** : une fois créée, on ne peut plus modifier son contenu.

#### **Caractéristiques des tuples :**

- ✅ **Ordonnés** : Les éléments ont une position fixe
- ✅ **Immutables** : On ne peut pas modifier le contenu après création
- ✅ **Permettent les doublons** : Le même élément peut apparaître plusieurs fois
- ✅ **Indexables** : Accès par index comme les listes
- ✅ **Plus rapides** : Plus efficaces que les listes pour l'accès en lecture

---

### 🏗️ **7. Création et Utilisation des Tuples**

#### **Exemple 1 - Création de tuples :**

```python
# Tuple vide
tuple_vide = ()
autre_tuple_vide = tuple()

# Tuple avec éléments
coordonnees = (10, 20)
couleur_rgb = (255, 128, 0)
personne = ("Alice", 25, "Paris")

# Tuple d'un seul élément (attention à la virgule !)
single_element = (42,)  # Sans virgule, ce serait juste des parenthèses
single_element2 = 42,   # Virgule suffisante

# Tuple sans parenthèses (packing)
point = 5, 10, 15

print(f"Coordonnées: {coordonnees}")        # (10, 20)
print(f"RGB: {couleur_rgb}")                # (255, 128, 0)
print(f"Personne: {personne}")              # ('Alice', 25, 'Paris')
print(f"Single: {single_element}")          # (42,)
print(f"Point: {point}")                    # (5, 10, 15)
```

#### **Exemple 2 - Accès aux éléments des tuples :**

```python
personne = ("Alice", 25, "Paris", "Développeuse")

# Accès par index
print(f"Nom: {personne[0]}")               # Alice
print(f"Âge: {personne[1]}")               # 25
print(f"Dernier élément: {personne[-1]}")  # Développeuse

# Slicing
print(f"Infos de base: {personne[:3]}")    # ('Alice', 25, 'Paris')
print(f"Âge et après: {personne[1:]}")     # (25, 'Paris', 'Développeuse')

# Opérations
print(f"Longueur: {len(personne)}")        # 4
print(f"'Alice' dans tuple: {'Alice' in personne}")  # True
```

---

### 📤 **8. Unpacking (Déballage) de Tuples**

L'unpacking permet d'extraire les éléments d'un tuple dans des variables séparées.

#### **Exemple 1 - Unpacking simple :**

```python
# Tuple de coordonnées
point = (10, 20, 5)

# Unpacking dans des variables
x, y, z = point
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=5

# Unpacking avec échange de variables
a = 5
b = 10
print(f"Avant: a={a}, b={b}")

a, b = b, a  # Échange élégant !
print(f"Après: a={a}, b={b}")

# Unpacking partiel avec *
nombres = (1, 2, 3, 4, 5)
premier, *milieu, dernier = nombres
print(f"Premier: {premier}")      # 1
print(f"Milieu: {milieu}")        # [2, 3, 4]
print(f"Dernier: {dernier}")      # 5
```

#### **Exemple 2 - Unpacking en fonction :**

```python
def calculer_statistiques(notes):
    """Retourne plusieurs statistiques sous forme de tuple"""
    moyenne = sum(notes) / len(notes)
    minimum = min(notes)
    maximum = max(notes)
    return moyenne, minimum, maximum  # Retourne un tuple

# Utilisation avec unpacking
notes_etudiant = [15, 18, 12, 16, 14]
moy, mini, maxi = calculer_statistiques(notes_etudiant)

print(f"Moyenne: {moy:.2f}")    # Moyenne: 15.00
print(f"Minimum: {mini}")       # Minimum: 12
print(f"Maximum: {maxi}")       # Maximum: 18
```

---

### 🔄 **9. Tuples vs Listes - Quand Utiliser Quoi ?**

#### **Utilisez des TUPLES quand :**

- ✅ Les données ne changent pas (coordonnées, couleurs RGB)
- ✅ Vous voulez garantir l'immutabilité
- ✅ Vous utilisez comme clé de dictionnaire
- ✅ Vous retournez plusieurs valeurs d'une fonction
- ✅ Performance importante (tuples plus rapides)

#### **Utilisez des LISTES quand :**

- ✅ Les données peuvent changer (ajouter/supprimer des éléments)
- ✅ Vous avez besoin des méthodes de modification
- ✅ La taille de la collection varie
- ✅ Vous travaillez avec des données homogènes

#### **Exemple comparatif :**

```python
# TUPLE pour des données fixes
coordonnee_gps = (48.8566, 2.3522)  # Latitude, longitude de Paris
couleur_rouge = (255, 0, 0)         # RGB fixe

# LISTE pour des données variables
courses = ["pain", "lait", "œufs"]   # On peut ajouter/retirer des articles
notes = [15, 18, 12]                # Les notes peuvent changer

# Tuple comme clé de dictionnaire
positions = {
    (0, 0): "origine",
    (1, 1): "diagonale",
    (0, 1): "haut"
}

print(f"Position (0,0): {positions[(0, 0)]}")
```

---

### 🚀 **10. Exemples Pratiques Complets**

#### **Exemple 1 - Système de gestion d'inventaire :**

```python
def gestion_inventaire():
    """Système de gestion d'inventaire avec dictionnaires"""
    inventaire = {}

    def afficher_inventaire():
        if not inventaire:
            print("Inventaire vide!")
            return

        print("\n=== INVENTAIRE ===")
        total_valeur = 0
        for produit, infos in inventaire.items():
            prix, stock = infos  # Unpacking du tuple
            valeur = prix * stock
            total_valeur += valeur
            print(f"{produit}: {stock} unités × {prix}€ = {valeur}€")
        print(f"Valeur totale: {total_valeur}€")

    def ajouter_produit():
        nom = input("Nom du produit: ")
        try:
            prix = float(input("Prix unitaire: "))
            stock = int(input("Stock initial: "))
            inventaire[nom] = (prix, stock)  # Stockage en tuple
            print(f"Produit '{nom}' ajouté!")
        except ValueError:
            print("Erreur: Prix et stock doivent être des nombres!")

    def vendre_produit():
        if not inventaire:
            print("Aucun produit en stock!")
            return

        nom = input("Produit à vendre: ")
        if nom not in inventaire:
            print("Produit introuvable!")
            return

        prix, stock = inventaire[nom]
        try:
            quantite = int(input(f"Quantité (stock: {stock}): "))
            if quantite <= stock:
                nouveau_stock = stock - quantite
                inventaire[nom] = (prix, nouveau_stock)
                total = prix * quantite
                print(f"Vente: {quantite} × {nom} = {total}€")
                if nouveau_stock == 0:
                    print("⚠️ Stock épuisé!")
            else:
                print("Stock insuffisant!")
        except ValueError:
            print("Quantité invalide!")

    # Boucle principale
    while True:
        print("\n=== GESTION INVENTAIRE ===")
        print("1. Afficher inventaire")
        print("2. Ajouter produit")
        print("3. Vendre produit")
        print("0. Quitter")

        choix = input("Choix: ")

        if choix == "1":
            afficher_inventaire()
        elif choix == "2":
            ajouter_produit()
        elif choix == "3":
            vendre_produit()
        elif choix == "0":
            break
        else:
            print("Choix invalide!")

# gestion_inventaire()  # Décommentez pour tester
```

#### **Exemple 2 - Carnet d'adresses avec recherche :**

```python
def carnet_adresses():
    """Carnet d'adresses avec fonctionnalités de recherche"""
    contacts = {}

    def ajouter_contact():
        nom = input("Nom: ").strip().title()
        if nom in contacts:
            print("Contact déjà existant!")
            return

        telephone = input("Téléphone: ").strip()
        email = input("Email: ").strip()
        ville = input("Ville: ").strip().title()

        contacts[nom] = {
            "telephone": telephone,
            "email": email,
            "ville": ville
        }
        print(f"Contact '{nom}' ajouté!")

    def chercher_contact():
        terme = input("Rechercher (nom ou téléphone): ").strip()
        resultats = []

        for nom, infos in contacts.items():
            if (terme.lower() in nom.lower() or
                terme in infos["telephone"]):
                resultats.append((nom, infos))

        if resultats:
            print(f"\n=== {len(resultats)} RÉSULTAT(S) ===")
            for nom, infos in resultats:
                print(f"{nom}: {infos['telephone']} | {infos['email']} | {infos['ville']}")
        else:
            print("Aucun contact trouvé!")

    def contacts_par_ville():
        if not contacts:
            print("Aucun contact!")
            return

        villes = {}
        for nom, infos in contacts.items():
            ville = infos["ville"]
            if ville not in villes:
                villes[ville] = []
            villes[ville].append(nom)

        print("\n=== CONTACTS PAR VILLE ===")
        for ville, noms in sorted(villes.items()):
            print(f"{ville}: {', '.join(noms)}")

    def statistiques():
        if not contacts:
            print("Aucun contact!")
            return

        total = len(contacts)
        villes = set(infos["ville"] for infos in contacts.values())
        domaines_email = {}

        for infos in contacts.values():
            if "@" in infos["email"]:
                domaine = infos["email"].split("@")[1]
                domaines_email[domaine] = domaines_email.get(domaine, 0) + 1

        print(f"\n=== STATISTIQUES ===")
        print(f"Total contacts: {total}")
        print(f"Nombre de villes: {len(villes)}")
        print(f"Villes: {', '.join(sorted(villes))}")

        if domaines_email:
            print("Domaines email les plus fréquents:")
            for domaine, count in sorted(domaines_email.items(),
                                       key=lambda x: x[1], reverse=True):
                print(f"  {domaine}: {count}")

    # Menu principal
    while True:
        print("\n=== CARNET D'ADRESSES ===")
        print("1. Ajouter contact")
        print("2. Chercher contact")
        print("3. Contacts par ville")
        print("4. Statistiques")
        print("0. Quitter")

        choix = input("Choix: ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            chercher_contact()
        elif choix == "3":
            contacts_par_ville()
        elif choix == "4":
            statistiques()
        elif choix == "0":
            break
        else:
            print("Choix invalide!")

# carnet_adresses()  # Décommentez pour tester
```

---

## 💪 Challenges

### Challenge A - Dictionnaires de base (Facile)

- Créez un dictionnaire "personne" avec nom, âge, ville
- Modifiez l'âge et ajoutez la profession
- Affichez toutes les clés et valeurs
- Vérifiez si une clé existe

### Challenge B - Gestion d'inventaire (Moyen)

Créez un système d'inventaire de magasin :

- Dictionnaire produits : {"nom": {"prix": X, "stock": Y}}
- Fonctions : ajouter_produit, vendre_produit, restock
- Calcul de la valeur totale du stock

### Challenge C - Tuples et unpacking (Moyen)

- Créez des tuples coordonnées (x, y)
- Fonction distance entre deux points
- Liste d'étudiants avec (nom, note1, note2, note3)
- Calcul automatique des moyennes

### Challenge D - Projet carnet d'adresses (Difficile)

Système complet avec dictionnaires imbriqués :

- Structure : {nom: {"tel": X, "email": Y, "adresse": Z}}
- Recherche par nom, téléphone
- Groupement par ville
- Export/import CSV
