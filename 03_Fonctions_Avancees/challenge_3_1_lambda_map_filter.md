# 🎯 Challenge 3.1 : Fonctions Lambda et Fonctions d'Ordre Supérieur

## 📚 Objectif

Découvrir la programmation fonctionnelle avec lambda, map, filter, reduce.

## 🔧 Ce que vous devez apprendre

- Fonctions lambda (fonctions anonymes)
- map() : transformer des données
- filter() : filtrer des données
- reduce() : agréger des données
- Composition de fonctions

---

## 📖 **EXPLICATIONS DÉTAILLÉES AVEC EXEMPLES**

### ⚡ **1. Programmation Fonctionnelle - Introduction**

La **programmation fonctionnelle** est un paradigme qui traite les fonctions comme des **citoyens de première classe**. Cela signifie qu'on peut :

- Passer des fonctions comme arguments
- Retourner des fonctions depuis d'autres fonctions
- Stocker des fonctions dans des variables
- Créer des fonctions à la volée (lambda)

#### **Avantages de la programmation fonctionnelle :**

- ✅ **Code plus concis** : Moins de lignes, plus expressif
- ✅ **Moins d'effets de bord** : Fonctions pures, prévisibles
- ✅ **Réutilisabilité** : Fonctions génériques et composables
- ✅ **Lisibilité** : Code déclaratif plutôt qu'impératif

---

### 🎯 **2. Fonctions Lambda - Fonctions Anonymes**

Les fonctions **lambda** sont des **fonctions courtes et anonymes** définies en une seule ligne. Elles sont parfaites pour des opérations simples qu'on utilise une seule fois.

#### **Syntaxe :**

```python
lambda arguments: expression
```

#### **Exemple 1 - Comparaison fonction normale vs lambda :**

```python
# Fonction normale
def carre_normal(x):
    return x ** 2

# Fonction lambda équivalente
carre_lambda = lambda x: x ** 2

# Utilisation
print(f"Normal: {carre_normal(5)}")    # 25
print(f"Lambda: {carre_lambda(5)}")    # 25

# Utilisation directe (sans variable)
resultat = (lambda x: x ** 2)(5)
print(f"Direct: {resultat}")           # 25
```

#### **Exemple 2 - Lambda avec plusieurs paramètres :**

```python
# Addition de deux nombres
addition = lambda a, b: a + b
print(f"Addition: {addition(3, 7)}")   # 10

# Calcul d'aire d'un rectangle
aire = lambda longueur, largeur: longueur * largeur
print(f"Aire: {aire(5, 3)}")          # 15

# Condition avec lambda
est_majeur = lambda age: "Majeur" if age >= 18 else "Mineur"
print(f"Statut: {est_majeur(20)}")    # Majeur
print(f"Statut: {est_majeur(16)}")    # Mineur

# Lambda plus complexe
prix_ttc = lambda prix_ht, tva=20: prix_ht * (1 + tva/100)
print(f"Prix TTC: {prix_ttc(100)}€")  # 120.0€
print(f"Prix TTC: {prix_ttc(100, 10)}€")  # 110.0€
```

#### **Exemple 3 - Lambda dans les structures de données :**

```python
# Dictionnaire de fonctions mathématiques
operations = {
    'addition': lambda a, b: a + b,
    'soustraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b if b != 0 else "Division par zéro"
}

# Utilisation
print(f"3 + 5 = {operations['addition'](3, 5)}")        # 8
print(f"10 - 4 = {operations['soustraction'](10, 4)}")  # 6
print(f"7 * 8 = {operations['multiplication'](7, 8)}")  # 56
print(f"15 / 3 = {operations['division'](15, 3)}")      # 5.0

# Liste de transformations
transformations = [
    lambda x: x ** 2,      # Carré
    lambda x: x ** 3,      # Cube
    lambda x: x * 2,       # Double
    lambda x: x / 2        # Moitié
]

nombre = 4
for i, transform in enumerate(transformations):
    print(f"Transformation {i+1}: {nombre} → {transform(nombre)}")
```

---

### 🗂️ **3. La Fonction MAP() - Transformer des Données**

`map()` applique une fonction à **chaque élément** d'un itérable et retourne un objet map (qu'on convertit généralement en liste).

#### **Syntaxe :**

```python
map(fonction, itérable)
```

#### **Exemple 1 - Map avec lambda :**

```python
# Transformer une liste de nombres
nombres = [1, 2, 3, 4, 5]

# Calculer les carrés
carres = list(map(lambda x: x ** 2, nombres))
print(f"Nombres: {nombres}")         # [1, 2, 3, 4, 5]
print(f"Carrés: {carres}")          # [1, 4, 9, 16, 25]

# Convertir en Fahrenheit
celsius = [0, 20, 30, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")        # [0, 20, 30, 37, 100]
print(f"Fahrenheit: {fahrenheit}")  # [32.0, 68.0, 86.0, 98.6, 212.0]

# Mettre en majuscules
mots = ["python", "java", "javascript"]
mots_majuscules = list(map(lambda mot: mot.upper(), mots))
print(f"Original: {mots}")                    # ['python', 'java', 'javascript']
print(f"Majuscules: {mots_majuscules}")       # ['PYTHON', 'JAVA', 'JAVASCRIPT']
```

#### **Exemple 2 - Map avec fonctions normales :**

```python
def formater_nom(nom):
    """Formate un nom : première lettre majuscule, reste minuscule"""
    return nom.strip().title()

def calculer_tva(prix, taux=20):
    """Calcule le prix TTC"""
    return prix * (1 + taux/100)

# Application sur des listes
noms_bruts = ["  alice  ", "BOB", "cHaRlIe"]
noms_formates = list(map(formater_nom, noms_bruts))
print(f"Noms formatés: {noms_formates}")  # ['Alice', 'Bob', 'Charlie']

prix_ht = [100, 50, 200, 25]
prix_ttc = list(map(calculer_tva, prix_ht))
print(f"Prix HT: {prix_ht}")              # [100, 50, 200, 25]
print(f"Prix TTC: {prix_ttc}")            # [120.0, 60.0, 240.0, 30.0]
```

#### **Exemple 3 - Map avec plusieurs itérables :**

```python
# Map peut prendre plusieurs itérables
nombres1 = [1, 2, 3, 4]
nombres2 = [10, 20, 30, 40]

# Addition élément par élément
sommes = list(map(lambda a, b: a + b, nombres1, nombres2))
print(f"Sommes: {sommes}")  # [11, 22, 33, 44]

# Calculer des distances (théorème de Pythagore)
x_coords = [3, 5, 8]
y_coords = [4, 12, 15]
distances = list(map(lambda x, y: (x**2 + y**2)**0.5, x_coords, y_coords))
print(f"Distances: {[round(d, 2) for d in distances]}")  # [5.0, 13.0, 17.0]

# Créer des coordonnées
coordonnees = list(map(lambda x, y: (x, y), x_coords, y_coords))
print(f"Coordonnées: {coordonnees}")  # [(3, 4), (5, 12), (8, 15)]
```

---

### 🔍 **4. La Fonction FILTER() - Filtrer des Données**

`filter()` **sélectionne les éléments** d'un itérable qui satisfont une condition (fonction qui retourne True/False).

#### **Syntaxe :**

```python
filter(fonction_condition, itérable)
```

#### **Exemple 1 - Filter avec lambda :**

```python
# Filtrer les nombres pairs
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"Nombres: {nombres}")           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Pairs: {pairs}")              # [2, 4, 6, 8, 10]

# Filtrer les nombres positifs
nombres_mixtes = [-5, -2, 0, 3, 7, -1, 4]
positifs = list(filter(lambda x: x > 0, nombres_mixtes))
print(f"Positifs: {positifs}")        # [3, 7, 4]

# Filtrer les mots longs
mots = ["chat", "elephant", "souris", "hippopotame", "rat"]
mots_longs = list(filter(lambda mot: len(mot) > 5, mots))
print(f"Mots longs: {mots_longs}")    # ['elephant', 'hippopotame']
```

#### **Exemple 2 - Filter avec fonctions personnalisées :**

```python
def est_adulte(personne):
    """Vérifie si une personne est adulte"""
    return personne['age'] >= 18

def a_bonne_note(etudiant):
    """Vérifie si un étudiant a une bonne moyenne"""
    return etudiant['moyenne'] >= 15

# Données de test
personnes = [
    {'nom': 'Alice', 'age': 25},
    {'nom': 'Bob', 'age': 17},
    {'nom': 'Charlie', 'age': 30},
    {'nom': 'Diana', 'age': 16}
]

etudiants = [
    {'nom': 'Alice', 'moyenne': 18},
    {'nom': 'Bob', 'moyenne': 12},
    {'nom': 'Charlie', 'moyenne': 16},
    {'nom': 'Diana', 'moyenne': 14}
]

# Filtrage
adultes = list(filter(est_adulte, personnes))
bons_etudiants = list(filter(a_bonne_note, etudiants))

print("Adultes:")
for adulte in adultes:
    print(f"  {adulte['nom']} ({adulte['age']} ans)")

print("Bons étudiants:")
for etudiant in bons_etudiants:
    print(f"  {etudiant['nom']} (moyenne: {etudiant['moyenne']})")
```

#### **Exemple 3 - Filter avec None (filtrer les valeurs "falsy") :**

```python
# Filter avec None supprime les valeurs "falsy"
valeurs_mixtes = [1, 0, "hello", "", None, "world", False, 42, [], [1, 2]]
valeurs_vraies = list(filter(None, valeurs_mixtes))
print(f"Valeurs vraies: {valeurs_vraies}")  # [1, 'hello', 'world', 42, [1, 2]]

# Filtrer les chaînes non vides
textes = ["Python", "", "Java", "   ", "C++", None, "JavaScript"]
textes_valides = list(filter(lambda x: x and x.strip(), textes))
print(f"Textes valides: {textes_valides}")  # ['Python', 'Java', 'C++', 'JavaScript']
```

---

### 🔄 **5. La Fonction REDUCE() - Agréger des Données**

`reduce()` applique une fonction de manière **cumulative** aux éléments d'un itérable pour le réduire à une seule valeur.

#### **Import nécessaire :**

```python
from functools import reduce
```

#### **Syntaxe :**

```python
reduce(fonction, itérable, valeur_initiale)
```

#### **Exemple 1 - Reduce basique :**

```python
from functools import reduce

# Calculer la somme (équivalent à sum())
nombres = [1, 2, 3, 4, 5]
somme = reduce(lambda a, b: a + b, nombres)
print(f"Somme: {somme}")  # 15 (1+2+3+4+5)

# Calculer le produit
produit = reduce(lambda a, b: a * b, nombres)
print(f"Produit: {produit}")  # 120 (1*2*3*4*5)

# Trouver le maximum (équivalent à max())
maximum = reduce(lambda a, b: a if a > b else b, nombres)
print(f"Maximum: {maximum}")  # 5

# Avec valeur initiale
somme_avec_100 = reduce(lambda a, b: a + b, nombres, 100)
print(f"Somme + 100: {somme_avec_100}")  # 115 (100+1+2+3+4+5)
```

#### **Exemple 2 - Reduce avec des chaînes :**

```python
# Concaténer des mots
mots = ["Python", "est", "un", "langage", "formidable"]
phrase = reduce(lambda a, b: a + " " + b, mots)
print(f"Phrase: {phrase}")  # Python est un langage formidable

# Trouver le mot le plus long
mot_le_plus_long = reduce(
    lambda a, b: a if len(a) > len(b) else b,
    mots
)
print(f"Mot le plus long: {mot_le_plus_long}")  # formidable

# Construire un dictionnaire des longueurs
def ajouter_longueur(dictionnaire, mot):
    dictionnaire[mot] = len(mot)
    return dictionnaire

longueurs = reduce(ajouter_longueur, mots, {})
print(f"Longueurs: {longueurs}")
```

#### **Exemple 3 - Reduce avec des structures complexes :**

```python
# Calculer le total des ventes
ventes = [
    {'produit': 'A', 'quantite': 10, 'prix': 5},
    {'produit': 'B', 'quantite': 5, 'prix': 15},
    {'produit': 'C', 'quantite': 8, 'prix': 7.5}
]

def calculer_chiffre_affaires(total, vente):
    return total + (vente['quantite'] * vente['prix'])

chiffre_affaires = reduce(calculer_chiffre_affaires, ventes, 0)
print(f"Chiffre d'affaires: {chiffre_affaires}€")  # 185.0€

# Compter les occurrences de lettres
texte = "programmation python"
def compter_lettres(compteur, lettre):
    if lettre.isalpha():
        compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur

occurrences = reduce(compter_lettres, texte.lower(), {})
print(f"Occurrences: {dict(sorted(occurrences.items()))}")
```

---

### 🔗 **6. Composition de Fonctions - Chaîner les Opérations**

La vraie puissance vient de la **combinaison** de map, filter et reduce !

#### **Exemple 1 - Pipeline de transformation :**

```python
# Données : notes d'étudiants
notes_brutes = [12, 18, 8, 15, 9, 17, 11, 19, 6, 14]

# Pipeline : filtrer les bonnes notes, les transformer, calculer la moyenne
bonnes_notes = list(filter(lambda note: note >= 15, notes_brutes))
notes_sur_100 = list(map(lambda note: note * 5, bonnes_notes))
moyenne = reduce(lambda a, b: a + b, notes_sur_100) / len(notes_sur_100)

print(f"Notes brutes: {notes_brutes}")
print(f"Bonnes notes (≥15): {bonnes_notes}")          # [18, 15, 17, 19]
print(f"Sur 100: {notes_sur_100}")                    # [90, 75, 85, 95]
print(f"Moyenne des bonnes notes: {moyenne}")         # 86.25

# Version plus concise en une ligne
moyenne_concise = reduce(lambda a, b: a + b,
                        map(lambda note: note * 5,
                           filter(lambda note: note >= 15, notes_brutes))) / len(list(filter(lambda note: note >= 15, notes_brutes)))
```

#### **Exemple 2 - Analyse de texte complète :**

```python
# Texte d'exemple
texte = "Python est un langage de programmation puissant et élégant"

# Pipeline d'analyse
mots = texte.lower().split()

# 1. Filtrer les mots longs (>3 lettres)
mots_longs = list(filter(lambda mot: len(mot) > 3, mots))

# 2. Transformer : compter les voyelles dans chaque mot
def compter_voyelles(mot):
    return sum(1 for lettre in mot if lettre in 'aeiou')

voyelles_par_mot = list(map(compter_voyelles, mots_longs))

# 3. Réduire : total des voyelles
total_voyelles = reduce(lambda a, b: a + b, voyelles_par_mot)

print(f"Texte original: {texte}")
print(f"Mots longs: {mots_longs}")
print(f"Voyelles par mot: {voyelles_par_mot}")
print(f"Total voyelles dans mots longs: {total_voyelles}")
```

#### **Exemple 3 - Traitement de données de ventes :**

```python
# Données de ventes
ventes = [
    {'vendeur': 'Alice', 'produit': 'Laptop', 'prix': 1200, 'quantite': 2},
    {'vendeur': 'Bob', 'produit': 'Mouse', 'prix': 25, 'quantite': 10},
    {'vendeur': 'Alice', 'produit': 'Keyboard', 'prix': 80, 'quantite': 5},
    {'vendeur': 'Charlie', 'produit': 'Monitor', 'prix': 300, 'quantite': 3},
    {'vendeur': 'Bob', 'produit': 'Laptop', 'prix': 1200, 'quantite': 1}
]

# Pipeline d'analyse :
# 1. Filtrer les grosses ventes (>500€)
grosses_ventes = list(filter(
    lambda vente: vente['prix'] * vente['quantite'] > 500,
    ventes
))

# 2. Transformer : calculer le chiffre d'affaires par vente
ca_par_vente = list(map(
    lambda vente: {
        'vendeur': vente['vendeur'],
        'produit': vente['produit'],
        'ca': vente['prix'] * vente['quantite']
    },
    grosses_ventes
))

# 3. Réduire : chiffre d'affaires total des grosses ventes
ca_total = reduce(
    lambda total, vente: total + vente['ca'],
    ca_par_vente,
    0
)

print("=== ANALYSE DES GROSSES VENTES ===")
print(f"Nombre de grosses ventes: {len(grosses_ventes)}")
for vente in ca_par_vente:
    print(f"{vente['vendeur']} - {vente['produit']}: {vente['ca']}€")
print(f"Chiffre d'affaires total: {ca_total}€")
```

---

### 🚀 **7. Fonctions d'Ordre Supérieur Personnalisées**

Créons nos propres fonctions qui prennent d'autres fonctions en paramètres !

#### **Exemple 1 - Fonction générique d'application :**

```python
def appliquer_operation(liste, operation, condition=None):
    """
    Applique une opération sur les éléments d'une liste
    avec une condition optionnelle
    """
    if condition:
        elements_filtres = filter(condition, liste)
    else:
        elements_filtres = liste

    return list(map(operation, elements_filtres))

# Utilisation
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Carrés de tous les nombres
carres = appliquer_operation(nombres, lambda x: x**2)
print(f"Carrés: {carres}")

# Cubes des nombres pairs seulement
cubes_pairs = appliquer_operation(
    nombres,
    lambda x: x**3,
    lambda x: x % 2 == 0
)
print(f"Cubes des pairs: {cubes_pairs}")
```

#### **Exemple 2 - Décorateur de fonctions :**

```python
def mesurer_temps(func):
    """Décorateur pour mesurer le temps d'exécution"""
    import time

    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        print(f"Fonction {func.__name__} exécutée en {fin-debut:.4f}s")
        return resultat

    return wrapper

# Utilisation
@mesurer_temps
def calcul_intensif(n):
    return sum(x**2 for x in range(n))

# Test
resultat = calcul_intensif(100000)
print(f"Résultat: {resultat}")
```

---

### 💡 **8. Bonnes Pratiques et Conseils**

#### **Quand utiliser lambda vs fonction normale :**

```python
# ✅ BIEN : Lambda pour opérations simples
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))

# ❌ ÉVITER : Lambda trop complexe
# complique = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# ✅ MIEUX : Fonction normale pour logique complexe
def traiter_nombre(x):
    if x > 0:
        return x**2
    elif x < 0:
        return -x**2
    else:
        return 0

resultats = list(map(traiter_nombre, [-2, -1, 0, 1, 2]))
```

#### **Performance et lisibilité :**

```python
# Pour de gros volumes de données, les compréhensions peuvent être plus rapides
nombres = list(range(1000000))

# Map/filter/reduce (style fonctionnel)
import time
debut = time.time()
pairs_carres = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nombres)))
temps_fonctionnel = time.time() - debut

# Compréhension de liste (style pythonique)
debut = time.time()
pairs_carres_comp = [x**2 for x in nombres if x % 2 == 0]
temps_comprehension = time.time() - debut

print(f"Style fonctionnel: {temps_fonctionnel:.4f}s")
print(f"Compréhension: {temps_comprehension:.4f}s")
```

---

## 💪 Challenges

### Challenge A - Lambda basics (Facile)

- Créez des lambda pour : carré, cube, pair/impair
- Triez une liste de tuples par le 2ème élément
- Trouvez le maximum avec une fonction custom

### Challenge B - Map et Filter (Moyen)

- Convertissez des températures Celsius en Fahrenheit
- Filtrez les mots de plus de 5 lettres
- Extrayez les nombres d'un texte mixte

### Challenge C - Reduce et agrégation (Moyen)

- Calculez le produit de tous les éléments
- Trouvez le mot le plus long
- Comptez les occurrences de chaque lettre

### Challenge D - Projet analyse de données (Difficile)

Analysez un dataset de ventes avec les fonctions :

- Filtrage par critères multiples
- Calculs de statistiques
- Transformations de données
- Pipeline de traitement fonctionnel
