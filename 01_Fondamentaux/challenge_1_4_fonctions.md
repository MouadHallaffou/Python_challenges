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
