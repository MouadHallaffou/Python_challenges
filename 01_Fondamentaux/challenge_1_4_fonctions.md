# 🎯 Challenge 1.4 : Fonctions - Modularité et Réutilisation

## 📚 Objectif

Apprendre à créer et utiliser des fonctions pour organiser et réutiliser le code.

## 🔧 Ce que vous devez apprendre

- Définir une fonction avec `def`
- Paramètres et arguments
- Valeurs de retour avec `return`
- Portée des variables (scope)
- Arguments par défaut
- Arguments nommés

---

## 📖 **EXPLICATIONS DÉTAILLÉES AVEC EXEMPLES**

### 🏗️ **1. Qu'est-ce qu'une Fonction ?**

Une fonction est un **bloc de code réutilisable** qui effectue une tâche spécifique. C'est comme une **machine** : vous lui donnez des ingrédients (paramètres), elle fait son travail, et vous renvoie un résultat.

#### **Pourquoi utiliser des fonctions ?**

- ✅ **Réutilisabilité** : Éviter de répéter le même code
- ✅ **Organisation** : Découper le code en blocs logiques
- ✅ **Lisibilité** : Code plus facile à comprendre
- ✅ **Maintenance** : Plus facile de corriger/modifier
- ✅ **Test** : Tester chaque fonction séparément

---

### 🔧 **2. Définir une Fonction Simple**

#### **Syntaxe de base :**

```python
def nom_fonction():
    # Code de la fonction
    return resultat  # Optionnel
```

#### **Exemple 1 - Fonction sans paramètre :**

```python
def dire_bonjour():
    print("Bonjour tout le monde !")

# Appeler la fonction
dire_bonjour()  # Affiche : Bonjour tout le monde !
dire_bonjour()  # Peut être appelée plusieurs fois
```

#### **Exemple 2 - Fonction avec return :**

```python
def obtenir_salutation():
    return "Bonjour depuis la fonction !"

# Utiliser la valeur retournée
message = obtenir_salutation()
print(message)  # Affiche : Bonjour depuis la fonction !
```

---

### 📥 **3. Fonctions avec Paramètres**

Les paramètres permettent de **personnaliser** le comportement de la fonction.

#### **Exemple 1 - Un paramètre :**

```python
def saluer_personne(nom):
    print(f"Bonjour {nom} !")

# Appels avec différents arguments
saluer_personne("Alice")    # Affiche : Bonjour Alice !
saluer_personne("Bob")      # Affiche : Bonjour Bob !
saluer_personne("Charlie")  # Affiche : Bonjour Charlie !
```

#### **Exemple 2 - Plusieurs paramètres :**

```python
def additionner(a, b):
    resultat = a + b
    return resultat

# Utilisation
somme1 = additionner(5, 3)      # somme1 = 8
somme2 = additionner(10, 20)    # somme2 = 30
print(f"5 + 3 = {somme1}")      # Affiche : 5 + 3 = 8
print(f"10 + 20 = {somme2}")    # Affiche : 10 + 20 = 30
```

#### **Exemple 3 - Fonction plus complexe :**

```python
def calculer_aire_rectangle(longueur, largeur):
    """
    Calcule l'aire d'un rectangle

    Args:
        longueur: La longueur du rectangle
        largeur: La largeur du rectangle

    Returns:
        L'aire du rectangle (longueur × largeur)
    """
    aire = longueur * largeur
    return aire

# Utilisation
aire1 = calculer_aire_rectangle(5, 3)
aire2 = calculer_aire_rectangle(10, 7)
print(f"Rectangle 5×3 = {aire1} m²")   # Affiche : Rectangle 5×3 = 15 m²
print(f"Rectangle 10×7 = {aire2} m²")  # Affiche : Rectangle 10×7 = 70 m²
```

---

### 🎯 **4. Arguments par Défaut**

Les arguments par défaut permettent de rendre certains paramètres **optionnels**.

#### **Exemple 1 - Argument par défaut simple :**

```python
def presenter_personne(nom, age=0, ville="Inconnue"):
    print(f"Nom: {nom}")
    print(f"Âge: {age} ans")
    print(f"Ville: {ville}")
    print("-" * 20)

# Différentes façons d'appeler la fonction
presenter_personne("Alice")                    # Utilise les valeurs par défaut
presenter_personne("Bob", 25)                  # Spécifie l'âge
presenter_personne("Charlie", 30, "Paris")     # Spécifie tout
presenter_personne("Diana", ville="Lyon")      # Utilise l'argument nommé
```

#### **Exemple 2 - Calcul de prix avec TVA :**

```python
def calculer_prix_ttc(prix_ht, taux_tva=20):
    """
    Calcule le prix TTC à partir du prix HT

    Args:
        prix_ht: Prix hors taxes
        taux_tva: Taux de TVA en pourcentage (défaut: 20%)

    Returns:
        Le prix TTC
    """
    prix_ttc = prix_ht * (1 + taux_tva / 100)
    return prix_ttc

# Utilisation
print(f"100€ HT = {calculer_prix_ttc(100)}€ TTC")           # TVA 20%
print(f"100€ HT = {calculer_prix_ttc(100, 10)}€ TTC")       # TVA 10%
print(f"100€ HT = {calculer_prix_ttc(100, taux_tva=5.5)}€ TTC")  # TVA 5.5%
```

---

### 🔍 **5. Portée des Variables (Scope)**

Les variables ont une **portée** : elles n'existent que dans certaines parties du code.

#### **Exemple - Variables locales vs globales :**

```python
# Variable globale
message_global = "Je suis globale"

def ma_fonction():
    # Variable locale
    message_local = "Je suis locale"
    print(f"Dans la fonction: {message_global}")  # Accès à la variable globale
    print(f"Dans la fonction: {message_local}")   # Accès à la variable locale

# Appel de la fonction
ma_fonction()

# En dehors de la fonction
print(f"Hors fonction: {message_global}")  # ✅ Fonctionne
# print(f"Hors fonction: {message_local}")  # ❌ ERREUR ! Variable locale non accessible
```

#### **Exemple - Paramètres sont locaux :**

```python
def doubler_nombre(nombre):
    nombre = nombre * 2  # Modifie la copie locale
    print(f"Dans la fonction: {nombre}")
    return nombre

# Variable externe
mon_nombre = 5
resultat = doubler_nombre(mon_nombre)
print(f"Nombre original: {mon_nombre}")  # Reste 5 (inchangé)
print(f"Résultat: {resultat}")           # 10
```

---

### 🚀 **6. Fonctions Avancées**

#### **Exemple 1 - Validation dans les fonctions :**

```python
def diviser(a, b):
    """
    Division sécurisée avec gestion d'erreur
    """
    if b == 0:
        print("Erreur: Division par zéro impossible!")
        return None
    return a / b

# Utilisation
print(diviser(10, 2))   # Affiche : 5.0
print(diviser(10, 0))   # Affiche : Erreur: Division par zéro impossible! et None
```

#### **Exemple 2 - Fonction récursive (Fibonacci) :**

```python
def fibonacci(n):
    """
    Calcule le nième nombre de Fibonacci
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Utilisation
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
```

#### **Exemple 3 - Fonction qui retourne plusieurs valeurs :**

```python
def analyser_nombre(nombre):
    """
    Analyse un nombre et retourne plusieurs informations
    """
    est_pair = nombre % 2 == 0
    est_positif = nombre > 0
    carre = nombre ** 2

    return est_pair, est_positif, carre

# Utilisation
pair, positif, carre = analyser_nombre(4)
print(f"4 est pair: {pair}")        # True
print(f"4 est positif: {positif}")  # True
print(f"4 au carré: {carre}")       # 16
```

---

### 🎯 **7. Exemple Pratique Complet - Calculatrice**

```python
def afficher_menu():
    """Affiche le menu de la calculatrice"""
    print("\n=== CALCULATRICE ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Quitter")

def obtenir_nombres():
    """Demande deux nombres à l'utilisateur"""
    try:
        a = float(input("Premier nombre: "))
        b = float(input("Deuxième nombre: "))
        return a, b
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides!")
        return None, None

def calculer(operation, a, b):
    """Effectue le calcul selon l'opération choisie"""
    if operation == "1":
        return a + b, "+"
    elif operation == "2":
        return a - b, "-"
    elif operation == "3":
        return a * b, "×"
    elif operation == "4":
        if b != 0:
            return a / b, "÷"
        else:
            print("Erreur: Division par zéro!")
            return None, None
    else:
        print("Opération invalide!")
        return None, None

def calculatrice():
    """Fonction principale de la calculatrice"""
    while True:
        afficher_menu()
        choix = input("Votre choix: ")

        if choix == "0":
            print("Au revoir!")
            break

        a, b = obtenir_nombres()
        if a is not None and b is not None:
            resultat, symbole = calculer(choix, a, b)
            if resultat is not None:
                print(f"Résultat: {a} {symbole} {b} = {resultat}")

# Lancer la calculatrice
# calculatrice()
```

---

## 💪 Challenges

### Challenge A - Fonctions simples (Facile)

Créez ces fonctions :

- `saluer(nom)` : affiche "Bonjour [nom] !"
- `additionner(a, b)` : retourne la somme de a et b
- `est_pair(nombre)` : retourne True si le nombre est pair
- `calculer_aire_rectangle(longueur, largeur)` : retourne l'aire

### Challenge B - Fonctions avec validation (Facile)

Créez ces fonctions :

- `diviser(a, b)` : division sécurisée (gérer division par zéro)
- `age_en_jours(age_annees)` : convertit l'âge en jours (approximation)
- `note_en_lettre(note)` : convertit une note (0-20) en lettre (A, B, C, D, F)
- `temperature_celsius_fahrenheit(celsius)` : convertit les températures

### Challenge C - Fonctions avec arguments par défaut (Moyen)

Créez ces fonctions :

- `present_personne(nom, age=0, ville="Inconnue")` : présente une personne
- `calculer_prix_ttc(prix_ht, taux_tva=20)` : calcule le prix TTC
- `generer_mot_de_passe(longueur=8, inclure_chiffres=True, inclure_majuscules=True)`
- `afficher_menu(titre, options, separator="*")` : affiche un joli menu

### Challenge D - Fonctions avancées (Moyen)

Créez ces fonctions :

- `fibonacci(n)` : retourne le nième nombre de Fibonacci
- `est_premier(nombre)` : vérifie si un nombre est premier
- `compter_mots(texte)` : compte les mots dans un texte
- `inverser_mots(phrase)` : inverse l'ordre des mots dans une phrase

### Challenge E - Mini-projet avec fonctions (Difficile)

Créez un calculateur scientifique avec ces fonctions :

- `menu_principal()` : affiche le menu et gère les choix
- `addition(a, b)`, `soustraction(a, b)`, `multiplication(a, b)`, `division(a, b)`
- `puissance(base, exposant)`, `racine_carree(nombre)`
- `factorielle(n)`, `pourcentage(valeur, total)`
- `historique` : stocke les derniers calculs
- `afficher_historique()` : montre les derniers calculs
- Le programme doit tourner en boucle jusqu'à ce que l'utilisateur quitte

Fonctionnalités bonus :

- Sauvegarde de l'historique dans un fichier
- Fonctions trigonométriques (sin, cos, tan)
- Gestion des erreurs pour toutes les opérations

## 💡 Conseils

- Une fonction doit avoir une responsabilité claire
- Utilisez des noms de fonctions descriptifs
- Documentez vos fonctions avec des docstrings
- Testez chaque fonction séparément
- Gérez les cas d'erreur

## 🎯 Points clés à retenir

- Les fonctions permettent de découper le code en blocs réutilisables
- `return` renvoie une valeur et termine la fonction
- Les variables locales n'existent que dans la fonction
- Les arguments par défaut rendent les fonctions plus flexibles
- Une bonne fonction fait une seule chose, mais la fait bien
