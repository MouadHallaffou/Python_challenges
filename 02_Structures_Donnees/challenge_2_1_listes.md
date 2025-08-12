# 🎯 Challenge 2.1 : Listes - Collections Dynamiques

## 📚 Objectif

Maîtriser les listes Python pour stocker et manipuler des collections de données.

## 🔧 Ce que vous devez apprendre

- Création et initialisation de listes
- Accès aux éléments (indexation et slicing)
- Méthodes de listes : append, insert, remove, pop, sort
- Parcours de listes
- Listes en compréhension

---

## 📖 **EXPLICATIONS DÉTAILLÉES AVEC EXEMPLES**

### 📋 **1. Qu'est-ce qu'une Liste ?**

Une liste est une **collection ordonnée et modifiable** d'éléments. C'est comme un **panier** où vous pouvez mettre différents objets, les réorganiser, en ajouter ou en retirer.

#### **Caractéristiques des listes :**

- ✅ **Ordonnées** : Les éléments ont une position fixe
- ✅ **Modifiables** : On peut changer, ajouter, supprimer des éléments
- ✅ **Permettent les doublons** : Le même élément peut apparaître plusieurs fois
- ✅ **Hétérogènes** : Peuvent contenir différents types de données

---

### 🏗️ **2. Création et Initialisation de Listes**

#### **Exemple 1 - Différentes façons de créer des listes :**

```python
# Liste vide
ma_liste_vide = []
autre_liste_vide = list()

# Liste avec des éléments
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["Alice", 25, True, 3.14]

# Liste avec répétition
zeros = [0] * 5  # [0, 0, 0, 0, 0]
lettres = ["A"] * 3  # ["A", "A", "A"]

print(f"Fruits: {fruits}")          # ['pomme', 'banane', 'orange']
print(f"Nombres: {nombres}")        # [1, 2, 3, 4, 5]
print(f"Mixte: {mixte}")           # ['Alice', 25, True, 3.14]
print(f"Zéros: {zeros}")           # [0, 0, 0, 0, 0]
```

#### **Exemple 2 - Création avec range() :**

```python
# Créer une liste de nombres avec range()
nombres_1_10 = list(range(1, 11))      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = list(range(0, 21, 2))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
compte_rebours = list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"1 à 10: {nombres_1_10}")
print(f"Pairs: {nombres_pairs}")
print(f"Rebours: {compte_rebours}")
```

---

### 🎯 **3. Accès aux Éléments - Indexation**

#### **Indexation positive et négative :**

```python
fruits = ["pomme", "banane", "orange", "kiwi", "mangue"]

# Indexation positive (commence à 0)
print(f"Premier fruit: {fruits[0]}")     # pomme
print(f"Deuxième fruit: {fruits[1]}")    # banane
print(f"Dernier fruit: {fruits[4]}")     # mangue

# Indexation négative (commence à -1 pour le dernier)
print(f"Dernier fruit: {fruits[-1]}")    # mangue
print(f"Avant-dernier: {fruits[-2]}")    # kiwi
print(f"Premier fruit: {fruits[-5]}")    # pomme

# Vérification de la longueur
print(f"Nombre de fruits: {len(fruits)}")  # 5
```

#### **Exemple pratique - Accès sécurisé :**

```python
def obtenir_element_securise(liste, index):
    """Obtient un élément de la liste sans risquer d'erreur"""
    if 0 <= index < len(liste):
        return liste[index]
    else:
        return "Index invalide"

fruits = ["pomme", "banane", "orange"]
print(obtenir_element_securise(fruits, 1))   # banane
print(obtenir_element_securise(fruits, 10))  # Index invalide
```

---

### ✂️ **4. Slicing - Découpage de Listes**

Le slicing permet d'extraire des portions de listes avec la syntaxe `[start:end:step]`.

#### **Exemple 1 - Slicing de base :**

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntaxe: [start:end:step] - end est exclu
print(f"Éléments 2 à 5: {nombres[2:6]}")        # [2, 3, 4, 5]
print(f"3 premiers: {nombres[:3]}")             # [0, 1, 2]
print(f"3 derniers: {nombres[-3:]}")            # [7, 8, 9]
print(f"Tous sauf premiers et derniers: {nombres[1:-1]}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# Avec un pas (step)
print(f"Un élément sur deux: {nombres[::2]}")   # [0, 2, 4, 6, 8]
print(f"Éléments pairs positions: {nombres[1::2]}")  # [1, 3, 5, 7, 9]
print(f"Liste inversée: {nombres[::-1]}")       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### **Exemple 2 - Slicing pour extraire des données :**

```python
phrase = "Bonjour Python"
lettres = list(phrase)  # Convertit en liste de caractères

print(f"Premières 7 lettres: {''.join(lettres[:7])}")    # Bonjour
print(f"Dernières 6 lettres: {''.join(lettres[-6:])}")   # Python
print(f"Une lettre sur deux: {''.join(lettres[::2])}")   # BnorPto
```

---

### 🔧 **5. Méthodes de Modification des Listes**

#### **Ajouter des éléments :**

```python
ma_liste = ["a", "b", "c"]
print(f"Liste initiale: {ma_liste}")

# append() - ajoute à la fin
ma_liste.append("d")
print(f"Après append('d'): {ma_liste}")  # ['a', 'b', 'c', 'd']

# insert() - ajoute à une position spécifique
ma_liste.insert(1, "X")  # Insère "X" à l'index 1
print(f"Après insert(1, 'X'): {ma_liste}")  # ['a', 'X', 'b', 'c', 'd']

# extend() - ajoute plusieurs éléments
ma_liste.extend(["e", "f"])
print(f"Après extend(['e', 'f']): {ma_liste}")  # ['a', 'X', 'b', 'c', 'd', 'e', 'f']
```

#### **Supprimer des éléments :**

```python
ma_liste = ["a", "b", "c", "b", "d"]
print(f"Liste initiale: {ma_liste}")

# remove() - supprime la première occurrence
ma_liste.remove("b")  # Supprime le premier "b"
print(f"Après remove('b'): {ma_liste}")  # ['a', 'c', 'b', 'd']

# pop() - supprime et retourne un élément
element_supprime = ma_liste.pop()  # Supprime le dernier
print(f"Élément supprimé: {element_supprime}")  # d
print(f"Liste après pop(): {ma_liste}")  # ['a', 'c', 'b']

# pop(index) - supprime à un index spécifique
element_supprime = ma_liste.pop(1)  # Supprime l'élément à l'index 1
print(f"Élément supprimé à l'index 1: {element_supprime}")  # c
print(f"Liste finale: {ma_liste}")  # ['a', 'b']

# del - supprime par index ou slice
del ma_liste[0]  # Supprime le premier élément
print(f"Après del ma_liste[0]: {ma_liste}")  # ['b']
```

#### **Modifier et organiser :**

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Liste originale: {nombres}")

# sort() - trie la liste (modifie l'originale)
nombres.sort()
print(f"Après sort(): {nombres}")  # [1, 1, 2, 3, 4, 5, 6, 9]

# reverse() - inverse l'ordre
nombres.reverse()
print(f"Après reverse(): {nombres}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - retourne une nouvelle liste triée (n'affecte pas l'originale)
nombres_originaux = [3, 1, 4, 1, 5, 9, 2, 6]
nombres_tries = sorted(nombres_originaux)
print(f"Originaux: {nombres_originaux}")  # [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Triés: {nombres_tries}")          # [1, 1, 2, 3, 4, 5, 6, 9]
```

---

### 🔄 **6. Parcours de Listes**

#### **Exemple 1 - Parcours simple :**

```python
fruits = ["pomme", "banane", "orange"]

# Parcours des éléments
print("=== Parcours des éléments ===")
for fruit in fruits:
    print(f"J'aime les {fruit}s")

# Parcours avec index
print("\n=== Parcours avec index ===")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Parcours avec enumerate() (plus pythonique)
print("\n=== Parcours avec enumerate ===")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### **Exemple 2 - Parcours avec conditions :**

```python
notes = [12, 18, 8, 15, 9, 17, 11]

# Compter les bonnes notes
bonnes_notes = 0
for note in notes:
    if note >= 15:
        bonnes_notes += 1
        print(f"Excellente note: {note}")

print(f"Nombre de bonnes notes: {bonnes_notes}")

# Trouver la position de la meilleure note
meilleure_note = max(notes)
position = notes.index(meilleure_note)
print(f"Meilleure note: {meilleure_note} à la position {position}")
```

---

### ⚡ **7. Listes en Compréhension**

Les listes en compréhension permettent de créer des listes de manière concise et élégante.

#### **Syntaxe de base :**

```python
# [expression for item in iterable if condition]
```

#### **Exemple 1 - Compréhensions simples :**

```python
# Créer une liste de carrés
nombres = [1, 2, 3, 4, 5]
carres = [x**2 for x in nombres]
print(f"Carrés: {carres}")  # [1, 4, 9, 16, 25]

# Même chose avec boucle classique (plus verbeux)
carres_classique = []
for x in nombres:
    carres_classique.append(x**2)
print(f"Carrés (méthode classique): {carres_classique}")

# Filtrer les nombres pairs
pairs = [x for x in range(1, 11) if x % 2 == 0]
print(f"Nombres pairs: {pairs}")  # [2, 4, 6, 8, 10]
```

#### **Exemple 2 - Compréhensions avancées :**

```python
# Transformer des strings
mots = ["python", "java", "javascript"]
mots_majuscules = [mot.upper() for mot in mots]
print(f"Majuscules: {mots_majuscules}")  # ['PYTHON', 'JAVA', 'JAVASCRIPT']

# Extraire les premières lettres
premieres_lettres = [mot[0] for mot in mots]
print(f"Premières lettres: {premieres_lettres}")  # ['p', 'j', 'j']

# Filtrer et transformer
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres_pairs = [x**2 for x in nombres if x % 2 == 0]
print(f"Carrés des nombres pairs: {carres_pairs}")  # [4, 16, 36, 64, 100]
```

---

### 🎯 **8. Fonctions Utiles avec les Listes**

#### **Fonctions built-in :**

```python
nombres = [3, 7, 2, 9, 1, 5]

print(f"Liste: {nombres}")
print(f"Longueur: {len(nombres)}")        # 6
print(f"Minimum: {min(nombres)}")         # 1
print(f"Maximum: {max(nombres)}")         # 9
print(f"Somme: {sum(nombres)}")           # 27
print(f"Moyenne: {sum(nombres)/len(nombres):.2f}")  # 4.50

# Compter les occurrences
notes = [12, 15, 12, 18, 12, 16]
print(f"Nombre de 12: {notes.count(12)}")  # 3

# Trouver la position
print(f"Position du 18: {notes.index(18)}")  # 3
```

#### **Opérations sur les listes :**

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Concaténation
fusion = liste1 + liste2
print(f"Fusion: {fusion}")  # [1, 2, 3, 4, 5, 6]

# Répétition
repetition = liste1 * 3
print(f"Répétition: {repetition}")  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Vérification d'appartenance
print(f"2 dans liste1: {2 in liste1}")      # True
print(f"10 dans liste1: {10 in liste1}")    # False
```

---

### 🚀 **9. Exemples Pratiques Complets**

#### **Exemple 1 - Gestionnaire de tâches :**

```python
def gestionnaire_taches():
    """Gestionnaire simple de tâches"""
    taches = []

    while True:
        print(f"\n=== GESTIONNAIRE DE TÂCHES ===")
        print(f"Tâches actuelles: {len(taches)}")
        print("1. Ajouter une tâche")
        print("2. Voir toutes les tâches")
        print("3. Marquer une tâche comme terminée")
        print("0. Quitter")

        choix = input("Votre choix: ")

        if choix == "1":
            tache = input("Nouvelle tâche: ")
            taches.append(tache)
            print(f"Tâche '{tache}' ajoutée!")

        elif choix == "2":
            if taches:
                print("\n=== VOS TÂCHES ===")
                for i, tache in enumerate(taches, 1):
                    print(f"{i}. {tache}")
            else:
                print("Aucune tâche!")

        elif choix == "3":
            if taches:
                print("\n=== TÂCHES À TERMINER ===")
                for i, tache in enumerate(taches, 1):
                    print(f"{i}. {tache}")
                try:
                    index = int(input("Numéro de la tâche terminée: ")) - 1
                    if 0 <= index < len(taches):
                        tache_terminee = taches.pop(index)
                        print(f"Tâche '{tache_terminee}' terminée!")
                    else:
                        print("Numéro invalide!")
                except ValueError:
                    print("Veuillez entrer un nombre!")
            else:
                print("Aucune tâche à terminer!")

        elif choix == "0":
            print("Au revoir!")
            break

# gestionnaire_taches()  # Décommentez pour tester
```

#### **Exemple 2 - Analyse de données :**

```python
def analyser_notes(notes):
    """Analyse un ensemble de notes"""
    if not notes:
        return "Aucune note à analyser"

    # Statistiques de base
    moyenne = sum(notes) / len(notes)
    note_min = min(notes)
    note_max = max(notes)

    # Répartition par catégorie
    excellentes = [note for note in notes if note >= 16]
    bonnes = [note for note in notes if 14 <= note < 16]
    moyennes = [note for note in notes if 10 <= note < 14]
    faibles = [note for note in notes if note < 10]

    # Affichage des résultats
    print(f"=== ANALYSE DES NOTES ===")
    print(f"Nombre total: {len(notes)}")
    print(f"Moyenne: {moyenne:.2f}")
    print(f"Note minimum: {note_min}")
    print(f"Note maximum: {note_max}")
    print(f"Excellentes (≥16): {len(excellentes)} notes")
    print(f"Bonnes (14-15): {len(bonnes)} notes")
    print(f"Moyennes (10-13): {len(moyennes)} notes")
    print(f"Faibles (<10): {len(faibles)} notes")

    return {
        'moyenne': moyenne,
        'min': note_min,
        'max': note_max,
        'excellentes': len(excellentes),
        'bonnes': len(bonnes),
        'moyennes': len(moyennes),
        'faibles': len(faibles)
    }

# Test de la fonction
notes_classe = [12, 18, 14, 16, 8, 15, 19, 11, 17, 13, 9, 20]
resultats = analyser_notes(notes_classe)
```

---

## 💪 Challenges

### Challenge A - Bases des listes (Facile)

Créez des programmes qui :

- Créent une liste de vos 5 films préférés
- Ajoutent 2 nouveaux films à la fin
- Insèrent un film au début de la liste
- Supprimez le 3ème film de la liste
- Affichez la liste triée alphabétiquement

### Challenge B - Manipulation de listes (Facile)

Avec une liste de nombres [10, 25, 5, 80, 3, 15, 42] :

- Trouvez le plus grand et le plus petit nombre
- Calculez la moyenne
- Comptez combien de nombres sont supérieurs à 20
- Créez une nouvelle liste avec seulement les nombres pairs
- Inversez l'ordre de la liste originale

### Challenge C - Listes et boucles (Moyen)

Créez ces programmes :

- Un gestionnaire de courses : ajoutez/supprimez des articles
- Un calculateur de notes : stockez les notes et calculez la moyenne
- Un jeu "Pierre, Papier, Ciseaux" qui garde l'historique des parties
- Un analyseur de mots : comptez la fréquence de chaque mot dans un texte

### Challenge D - Listes avancées (Moyen)

Implémentez ces fonctions :

- `fusionner_listes(liste1, liste2)` : fusionne deux listes triées
- `supprimer_doublons(liste)` : supprime les éléments en double
- `rotation_liste(liste, n)` : fait une rotation de n positions
- `sous_liste_max(liste)` : trouve la sous-liste avec la somme maximale

### Challenge E - Projet : Système de gestion d'étudiants (Difficile)

Créez un système complet avec ces fonctionnalités :

- Liste d'étudiants avec [nom, notes, moyenne]
- Ajouter/supprimer des étudiants
- Ajouter des notes à un étudiant
- Calculer automatiquement les moyennes
- Trier les étudiants par moyenne
- Afficher les statistiques de la classe :
  - Moyenne générale
  - Meilleure et pire note
  - Nombre d'étudiants au-dessus de la moyenne
- Rechercher un étudiant par nom
- Exporter les données en format texte

Bonus :

- Sauvegarde/chargement depuis un fichier
- Interface menu interactive
- Validation des entrées utilisateur

## 💡 Conseils

- Les listes sont modifiables (mutables)
- L'indexation commence à 0
- Les indices négatifs comptent depuis la fin
- Le slicing [start:end:step] est très puissant
- Attention aux références lors de la copie de listes

## 🎯 Points clés à retenir

- append() ajoute à la fin, insert() à une position donnée
- remove() supprime par valeur, pop() par index
- sort() modifie la liste, sorted() retourne une nouvelle liste
- Les listes en compréhension sont concises et efficaces
- len(), min(), max(), sum() sont vos amis pour les listes
