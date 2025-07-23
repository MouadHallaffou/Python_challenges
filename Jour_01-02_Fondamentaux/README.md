# 🚀 Jour 1-2 : Fondamentaux Python 

## ⏰ Durée : 2 jours (4-6 heures total)

## 🎯 Objectifs
Maîtriser les concepts de base indispensables de Python.

## 📋 Programme

### **Jour 1 (2-3h) : Variables et Contrôle**
- ✅ Variables et types de données (30min)
- ✅ Opérateurs et expressions (30min)
- ✅ Conditions if/elif/else (45min)
- ✅ Mini-projet : Calculatrice simple (45min)

### **Jour 2 (2-3h) : Boucles et Fonctions**
- ✅ Boucles for et while (45min)
- ✅ Fonctions de base (45min)
- ✅ Paramètres et return (30min)
- ✅ Mini-projet : Jeu de devinette (60min)

## 💪 Challenge Intensif

### Partie A - Variables et Types (30min)
```python
# 1. Créez ces variables et affichez leurs types :
nom = "Python"
version = 3.11
est_gratuit = True
prix = 0.0

# 2. Calculs rapides :
a, b = 15, 4
# Calculez : somme, différence, produit, division, modulo, puissance

# 3. Chaînes de caractères :
phrase = "Apprendre Python en 10 jours"
# Affichez : longueur, majuscules, minuscules, premier/dernier caractère
```

### Partie B - Conditions (45min)
```python
# 1. Système de notes :
note = int(input("Votre note /20: "))
# Affichez la mention (A: 16-20, B: 14-15, C: 12-13, D: 10-11, F: <10)

# 2. Calculateur d'âge :
annee_naissance = int(input("Année de naissance: "))
age = 2025 - annee_naissance
# Déterminez si: enfant (<13), ado (13-17), adulte (18-64), senior (65+)

# 3. Vérificateur de mot de passe :
mdp = input("Mot de passe: ")
# Critères: au moins 8 caractères, contient majuscule, chiffre
```

### Partie C - Boucles (45min)
```python
# 1. Tables de multiplication (choisir une table)
table = int(input("Table de multiplication: "))
# Affichez: 2 x 1 = 2, 2 x 2 = 4, etc. jusqu'à 10

# 2. Compteur de voyelles
texte = input("Entrez une phrase: ")
# Comptez le nombre de voyelles (a,e,i,o,u)

# 3. Suite de Fibonacci (10 premiers termes)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### Partie D - Fonctions (45min)
```python
# 1. Fonction de calcul d'aire
def aire_rectangle(longueur, largeur):
    # Retournez l'aire du rectangle
    pass

def aire_cercle(rayon):
    # Retournez l'aire du cercle (π ≈ 3.14159)
    pass

# 2. Fonction de validation
def est_email_valide(email):
    # Retournez True si contient "@" et "."
    pass

def est_nombre_premier(n):
    # Retournez True si n est premier
    pass

# 3. Fonction avec paramètres par défaut
def salutation(nom, titre="Monsieur/Madame"):
    # Retournez "Bonjour [titre] [nom]"
    pass
```

## 🏆 Mini-Projets

### Projet Jour 1 : Calculatrice Interactive
```python
def calculatrice():
    print("=== CALCULATRICE ===")
    a = float(input("Premier nombre: "))
    op = input("Opération (+, -, *, /): ")
    b = float(input("Second nombre: "))
    
    # Calculez et affichez le résultat
    # Gérez la division par zéro
    pass

calculatrice()
```

### Projet Jour 2 : Jeu de Devinette
```python
import random

def jeu_devinette():
    secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 7
    
    print("Devinez un nombre entre 1 et 100!")
    
    while tentatives < max_tentatives:
        # Votre code ici :
        # - Demander un nombre à l'utilisateur
        # - Comparer avec le secret
        # - Donner des indices (plus grand/plus petit)
        # - Compter les tentatives
        pass
    
    print(f"Le nombre était: {secret}")

jeu_devinette()
```

## ✅ Validation des Acquis

Après ces 2 jours, vous devez savoir :
- ✅ Déclarer et utiliser des variables
- ✅ Écrire des conditions complexes  
- ✅ Créer des boucles efficaces
- ✅ Définir et appeler des fonctions
- ✅ Résoudre des problèmes simples en Python

## ⏭️ Prochaine Étape
**Jour 3-4** : Collections et structures de données

---
💡 **Conseil** : Ne passez au jour suivant que si vous maîtrisez tous ces concepts !
