# 🎯 Challenge 1.3 : Boucles - for et while

## 📚 Objectif

Maîtriser les boucles pour répéter des actions et traiter des séquences de données.

## 🔧 Ce que vous devez apprendre

- La boucle `for` avec `range()`
- La boucle `while`
- Les mots-clés `break` et `continue`
- L'itération sur des chaînes et listes
- Les boucles imbriquées

---

## 📖 **EXPLICATIONS DÉTAILLÉES AVEC EXEMPLES**

### 🔄 **1. La Boucle FOR - Répétition Contrôlée**

La boucle `for` est utilisée quand vous savez **combien de fois** vous voulez répéter une action.

#### **Syntaxe de base :**

```python
for variable in sequence:
    # Code à répéter
```

#### **Exemple 1 - Boucle for simple :**

```python
# Afficher les nombres de 1 à 5
for i in range(1, 6):  # range(début, fin_exclue)
    print(f"Nombre : {i}")

# Résultat :
# Nombre : 1
# Nombre : 2
# Nombre : 3
# Nombre : 4
# Nombre : 5
```

#### **Exemple 2 - range() avec différents paramètres :**

```python
# range(stop) - de 0 à stop-1
for i in range(5):
    print(i)  # Affiche : 0, 1, 2, 3, 4

# range(start, stop) - de start à stop-1
for i in range(2, 7):
    print(i)  # Affiche : 2, 3, 4, 5, 6

# range(start, stop, step) - avec un pas
for i in range(0, 10, 2):
    print(i)  # Affiche : 0, 2, 4, 6, 8

# range inversé (compte à rebours)
for i in range(10, 0, -1):
    print(i)  # Affiche : 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

#### **Exemple 3 - Itération sur des chaînes :**

```python
mot = "Python"
for lettre in mot:
    print(f"Lettre : {lettre}")

# Résultat :
# Lettre : P
# Lettre : y
# Lettre : t
# Lettre : h
# Lettre : o
# Lettre : n
```

#### **Exemple 4 - Accumulation avec for :**

```python
# Calculer la somme de 1 à 10
somme = 0
for i in range(1, 11):
    somme += i  # somme = somme + i
print(f"Somme : {somme}")  # Résultat : 55
```

---

### 🔄 **2. La Boucle WHILE - Répétition Conditionnelle**

La boucle `while` est utilisée quand vous ne savez pas **combien de fois** répéter, mais vous avez une **condition** à respecter.

#### **Syntaxe de base :**

```python
while condition:
    # Code à répéter
    # IMPORTANT : modifier la condition pour éviter une boucle infinie
```

#### **Exemple 1 - While simple :**

```python
# Compter de 1 à 5
compteur = 1
while compteur <= 5:
    print(f"Compteur : {compteur}")
    compteur += 1  # CRUCIAL : incrémenter pour sortir de la boucle

# Résultat :
# Compteur : 1
# Compteur : 2
# Compteur : 3
# Compteur : 4
# Compteur : 5
```

#### **Exemple 2 - While avec entrée utilisateur :**

```python
# Demander un mot de passe jusqu'à ce qu'il soit correct
mot_de_passe_correct = "secret"
tentative = ""

while tentative != mot_de_passe_correct:
    tentative = input("Entrez le mot de passe : ")
    if tentative != mot_de_passe_correct:
        print("Mot de passe incorrect, essayez encore!")

print("Accès autorisé !")
```

#### **Exemple 3 - While avec compteur :**

```python
# Calculer la factorielle de 5 (5! = 5×4×3×2×1)
nombre = 5
factorielle = 1
compteur = nombre

while compteur > 0:
    factorielle *= compteur  # factorielle = factorielle * compteur
    compteur -= 1

print(f"{nombre}! = {factorielle}")  # Résultat : 5! = 120
```

---

### ⚡ **3. BREAK et CONTINUE - Contrôle de Flux**

#### **BREAK - Sortir de la boucle :**

```python
# Chercher un nombre spécifique
for i in range(1, 11):
    if i == 7:
        print(f"Trouvé {i} ! On arrête.")
        break  # Sort de la boucle immédiatement
    print(f"Nombre : {i}")

# Résultat :
# Nombre : 1
# Nombre : 2
# Nombre : 3
# Nombre : 4
# Nombre : 5
# Nombre : 6
# Trouvé 7 ! On arrête.
```

#### **CONTINUE - Passer à l'itération suivante :**

```python
# Afficher seulement les nombres pairs
for i in range(1, 11):
    if i % 2 != 0:  # Si le nombre est impair
        continue    # Passer à l'itération suivante
    print(f"Nombre pair : {i}")

# Résultat :
# Nombre pair : 2
# Nombre pair : 4
# Nombre pair : 6
# Nombre pair : 8
# Nombre pair : 10
```

---

### 🔗 **4. Boucles Imbriquées - Boucles dans des Boucles**

#### **Exemple 1 - Table de multiplication :**

```python
# Table de multiplication de 1 à 3
for i in range(1, 4):  # Boucle externe
    print(f"Table de {i} :")
    for j in range(1, 4):  # Boucle interne
        resultat = i * j
        print(f"  {i} × {j} = {resultat}")
    print()  # Ligne vide

# Résultat :
# Table de 1 :
#   1 × 1 = 1
#   1 × 2 = 2
#   1 × 3 = 3
#
# Table de 2 :
#   2 × 1 = 2
#   2 × 2 = 4
#   2 × 3 = 6
# ...
```

#### **Exemple 2 - Dessiner un triangle :**

```python
# Triangle de nombres
for ligne in range(1, 6):  # 5 lignes
    for colonne in range(1, ligne + 1):  # Colonnes selon la ligne
        print(colonne, end="")  # end="" évite le retour à la ligne
    print()  # Retour à la ligne après chaque ligne

# Résultat :
# 1
# 12
# 123
# 1234
# 12345
```

---

### 🎯 **5. Exemples Pratiques Complets**

#### **Exemple 1 - Compter les voyelles :**

```python
phrase = "Bonjour Python"
voyelles = "aeiouAEIOU"
compteur = 0

for lettre in phrase:
    if lettre in voyelles:
        compteur += 1
        print(f"Voyelle trouvée : {lettre}")

print(f"Total voyelles : {compteur}")
```

#### **Exemple 2 - Menu interactif :**

```python
while True:
    print("\n=== MENU ===")
    print("1. Option 1")
    print("2. Option 2")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Vous avez choisi l'option 1")
    elif choix == "2":
        print("Vous avez choisi l'option 2")
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide !")
```

---

## 💪 Challenges

### Challenge A - Boucle for basique (Facile)

Écrivez des programmes qui :

- Affichent les nombres de 1 à 10
- Affichent les nombres pairs de 0 à 20
- Affichent les nombres de 10 à 1 (compte à rebours)
- Calculez la somme des nombres de 1 à 100

### Challenge B - Boucle while (Facile)

Créez des programmes qui :

- Demandent un mot de passe jusqu'à ce que l'utilisateur tape "secret"
- Comptent de 0 à 50 par pas de 5
- Calculent la factorielle d'un nombre (ex: 5! = 5×4×3×2×1)

### Challenge C - Boucles avec break et continue (Moyen)

- Affichez les nombres de 1 à 20, mais :
  - Sautez les multiples de 3 (continue)
  - Arrêtez si vous atteignez 15 (break)
- Créez un menu qui tourne jusqu'à ce que l'utilisateur choisisse "Quitter"

### Challenge D - Itération sur chaînes (Moyen)

Créez des programmes qui :

- Comptent le nombre de voyelles dans une phrase
- Inversent une chaîne caractère par caractère
- Trouvent la position de chaque lettre 'a' dans un texte
- Remplacent tous les espaces par des tirets

### Challenge E - Boucles imbriquées et patterns (Difficile)

Dessinez ces patterns avec des boucles :

1. Triangle de nombres :

```
1
12
123
1234
12345
```

2. Pyramide d'étoiles :

```
    *
   ***
  *****
 *******
*********
```

3. Table de multiplication (de 1 à 10)

4. Créez un jeu de "Plus ou Moins" :
   - L'ordinateur choisit un nombre entre 1 et 100
   - L'utilisateur devine jusqu'à ce qu'il trouve
   - Comptez le nombre de tentatives
   - Proposez de rejouer

## 💡 Conseils

- `range(start, stop, step)` pour contrôler les boucles for
- Attention aux boucles infinites avec while
- Utilisez des variables pour compter et accumuler
- Testez avec des print() pour déboguer

## 🎯 Points clés à retenir

- `for` est idéal quand on connaît le nombre d'itérations
- `while` est parfait pour les conditions dynamiques
- `break` sort de la boucle, `continue` passe à l'itération suivante
- Les boucles imbriquées permettent de traiter des structures 2D
