# 📚 Ressources et Références Python

## 🌐 Documentation Officielle
- **Python.org** : https://docs.python.org/3/
- **Tutorial officiel** : https://docs.python.org/3/tutorial/
- **Bibliothèque standard** : https://docs.python.org/3/library/

## 📖 Livres Recommandés (Français)
- **"Apprendre à programmer avec Python"** - Gérard Swinnen
- **"Python pour les Nuls"** - John Paul Mueller
- **"Programmation efficace en Python"** - Brett Slatkin

## 🎥 Chaînes YouTube (Français)
- **Graven - Développement** : Tutoriels Python complets
- **FormationVidéo** : Cours structurés
- **Docstring** : Concepts avancés

## 🛠️ Outils de Développement
- **IDE recommandés** : VS Code, PyCharm, Sublime Text
- **Interpréteur en ligne** : Replit, CodePen
- **Jupyter Notebooks** : Pour l'expérimentation

## 🧪 Plateformes d'Exercices
- **Codingame** : Jeux de programmation
- **HackerRank** : Challenges algorithmiques
- **LeetCode** : Préparation aux entretiens
- **Codewars** : Kata de programmation

## 🏗️ Frameworks Populaires à Découvrir Plus Tard
- **Web** : Django, Flask, FastAPI
- **Data Science** : Pandas, NumPy, Matplotlib
- **Machine Learning** : Scikit-learn, TensorFlow
- **GUI** : Tkinter, PyQt, Kivy

## 🔧 Commandes Python Utiles

### Installation de packages
```bash
pip install nom_package
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Exécution de scripts
```bash
python script.py
python -m module_name
python -i script.py  # Mode interactif après exécution
```

### Environnements virtuels
```bash
python -m venv mon_env
# Windows
mon_env\Scripts\activate
# Linux/Mac
source mon_env/bin/activate
deactivate
```

## 🐛 Debugging et Aide
```python
# Aide intégrée
help(fonction)
dir(objet)  # Liste les attributs
type(variable)  # Type de la variable

# Debugging
import pdb
pdb.set_trace()  # Point d'arrêt

# Timing
import time
start = time.time()
# ... code ...
print(f"Temps: {time.time() - start:.2f}s")
```

## ⚡ Snippets Code Utiles

### Template de script principal
```python
def main():
    """Fonction principale du programme"""
    pass

if __name__ == "__main__":
    main()
```

### Lecture de fichier sécurisée
```python
try:
    with open("fichier.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier non trouvé")
```

### Menu interactif
```python
def afficher_menu():
    print("\n=== MENU ===")
    print("1. Option 1")
    print("2. Option 2")
    print("0. Quitter")
    
def main():
    while True:
        afficher_menu()
        choix = input("Votre choix: ")
        if choix == "0":
            break
        # Traiter les autres choix...
```

## 🎯 Bonnes Pratiques

### Nommage
- **Variables** : `ma_variable` (snake_case)
- **Fonctions** : `ma_fonction()` (snake_case)
- **Classes** : `MaClasse` (PascalCase)
- **Constants** : `MA_CONSTANTE` (UPPER_CASE)

### Structure de projet
```
mon_projet/
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   └── test_module1.py
└── docs/
```

### Style de code (PEP 8)
- **Indentation** : 4 espaces
- **Longueur ligne** : max 79 caractères
- **Imports** : en haut du fichier
- **Espaces** : autour des opérateurs

## 🚨 Erreurs Courantes à Éviter

1. **Mutation de listes pendant itération**
```python
# ❌ Mauvais
for item in ma_liste:
    if condition:
        ma_liste.remove(item)

# ✅ Bon
ma_liste = [item for item in ma_liste if not condition]
```

2. **Variables mutables comme valeurs par défaut**
```python
# ❌ Mauvais
def ma_fonction(liste=[]):
    liste.append(1)
    return liste

# ✅ Bon
def ma_fonction(liste=None):
    if liste is None:
        liste = []
    liste.append(1)
    return liste
```

3. **Comparaison avec None**
```python
# ❌ Mauvais
if variable == None:

# ✅ Bon
if variable is None:
```

## 🎉 Motivation
- **Patience** : La programmation s'apprend progressivement
- **Pratique** : Codez tous les jours, même 15 minutes
- **Projets** : Créez des choses qui vous passionnent
- **Communauté** : Rejoignez des forums Python français

**Remember** : Chaque expert était un débutant un jour ! 🌟
