# 🚀 Jour 3-4 : Collections et Structures de Données

## ⏰ Durée : 2 jours (4-6 heures total)

## 🎯 Objectifs
Maîtriser les collections Python pour organiser et manipuler des données.

## 📋 Programme

### **Jour 3 (2-3h) : Listes et Tuples**
- ✅ Listes : création, modification, méthodes (60min)
- ✅ Indexation et slicing (30min)
- ✅ Tuples et unpacking (30min)
- ✅ Mini-projet : Gestionnaire de courses (60min)

### **Jour 4 (2-3h) : Dictionnaires et Sets**
- ✅ Dictionnaires : clés-valeurs (60min)
- ✅ Sets et opérations (30min)
- ✅ Compréhensions de base (30min)
- ✅ Mini-projet : Carnet d'adresses (60min)

## 💪 Challenge Intensif

### Partie A - Listes (60min)
```python
# 1. Manipulation de base
films = ["Matrix", "Inception", "Interstellar"]
# Ajoutez 2 films, supprimez le premier, triez alphabétiquement

# 2. Calculs sur listes
notes = [15, 12, 18, 9, 16, 14, 11, 17]
# Calculez : moyenne, min, max, notes >15, notes paires

# 3. Filtrage et transformation
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Créez : carrés, nombres pairs, multiples de 3
```

### Partie B - Dictionnaires (60min)
```python
# 1. Profil utilisateur
utilisateur = {"nom": "Alice", "age": 25, "ville": "Paris"}
# Ajoutez email, modifiez l'âge, affichez toutes les informations

# 2. Inventaire magasin
inventaire = {
    "pommes": {"prix": 2.5, "stock": 50},
    "oranges": {"prix": 3.0, "stock": 30}
}
# Ajoutez des bananes, calculez la valeur totale du stock

# 3. Compteur de mots
texte = "python est fantastique python est puissant"
# Comptez la fréquence de chaque mot
```

### Partie C - Tuples et Sets (30min)
```python
# 1. Coordonnées GPS
paris = (48.8566, 2.3522)
london = (51.5074, -0.1278)
# Calculez la distance approximative

# 2. Opérations sur sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Trouvez : intersection, union, différence
```

## 🏆 Mini-Projets

### Projet Jour 3 : Gestionnaire de Courses
```python
def gestionnaire_courses():
    courses = []
    
    while True:
        print("\n=== LISTE DE COURSES ===")
        print("1. Ajouter article")
        print("2. Supprimer article") 
        print("3. Afficher liste")
        print("4. Marquer comme acheté")
        print("0. Quitter")
        
        # Implémentez toutes les fonctionnalités
        pass
```

### Projet Jour 4 : Carnet d'Adresses
```python
def carnet_adresses():
    contacts = {}
    
    # Structure : {nom: {"tel": "...", "email": "...", "ville": "..."}}
    
    while True:
        print("\n=== CARNET D'ADRESSES ===")
        print("1. Ajouter contact")
        print("2. Rechercher contact")
        print("3. Modifier contact")
        print("4. Supprimer contact")
        print("5. Lister tous les contacts")
        print("6. Contacts par ville")
        print("0. Quitter")
        
        # Implémentez toutes les fonctionnalités
        pass
```

## ✅ Validation des Acquis

Après ces 2 jours, vous devez savoir :
- ✅ Manipuler des listes efficacement
- ✅ Utiliser des dictionnaires pour structurer des données
- ✅ Choisir la bonne collection selon le besoin
- ✅ Filtrer et transformer des données
- ✅ Créer des applications avec plusieurs collections

## ⏭️ Prochaine Étape
**Jour 5-6** : Programmation Orientée Objet

---
💡 **Conseil** : Maîtrisez bien les collections, elles sont la base de tout programme Python !
