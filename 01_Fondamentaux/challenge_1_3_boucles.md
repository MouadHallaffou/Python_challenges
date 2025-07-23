# 🎯 Challenge 1.3 : Boucles - for et while

## 📚 Objectif
Maîtriser les boucles pour répéter des actions et traiter des séquences de données.

## 🔧 Ce que vous devez apprendre
- La boucle `for` avec `range()`
- La boucle `while` 
- Les mots-clés `break` et `continue`
- L'itération sur des chaînes et listes
- Les boucles imbriquées

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
