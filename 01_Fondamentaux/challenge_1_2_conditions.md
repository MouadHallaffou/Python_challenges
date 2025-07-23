# 🎯 Challenge 1.2 : Structures de Contrôle - if/elif/else

## 📚 Objectif
Maîtriser les structures conditionnelles pour créer des programmes qui prennent des décisions.

## 🔧 Ce que vous devez apprendre
- La syntaxe if/elif/else
- Les opérateurs de comparaison (==, !=, <, >, <=, >=)
- Les opérateurs logiques (and, or, not)
- L'indentation en Python
- Les conditions imbriquées

## 💪 Challenges

### Challenge A - Conditions simples (Facile)
Écrivez un programme qui :
- Demande l'âge de l'utilisateur
- Affiche "Mineur" si l'âge est inférieur à 18
- Affiche "Majeur" si l'âge est supérieur ou égal à 18

### Challenge B - Conditions multiples (Facile)
Créez un système de notes :
- Demandez une note entre 0 et 20
- Affichez la mention correspondante :
  - 16-20 : "Très bien"
  - 14-15 : "Bien" 
  - 12-13 : "Assez bien"
  - 10-11 : "Passable"
  - 0-9 : "Insuffisant"

### Challenge C - Opérateurs logiques (Moyen)
Créez un système d'accès à un club :
- Demandez l'âge et si la personne a une carte de membre
- Conditions d'entrée :
  - Âge >= 18 ET carte de membre : "Accès autorisé"
  - Âge >= 21 : "Accès autorisé" (même sans carte)
  - Sinon : "Accès refusé"

### Challenge D - Conditions imbriquées (Moyen)
Créez un calculateur d'IMC (Indice de Masse Corporelle) :
- Demandez le poids (kg) et la taille (m)
- Calculez l'IMC = poids / (taille²)
- Affichez la catégorie :
  - IMC < 18.5 : "Maigreur"
  - 18.5 ≤ IMC < 25 : "Normal"
  - 25 ≤ IMC < 30 : "Surpoids"
  - IMC ≥ 30 : "Obésité"
- Ajoutez des sous-catégories pour l'obésité si IMC ≥ 30

### Challenge E - Logique complexe (Difficile)
Créez un jeu de devinette amélioré :
- L'ordinateur choisit un nombre aléatoire entre 1 et 100
- L'utilisateur a 3 tentatives maximum
- Après chaque tentative :
  - Si correct : "Bravo ! Trouvé en X tentatives"
  - Si trop grand : "Trop grand, essayez plus petit"
  - Si trop petit : "Trop petit, essayez plus grand"
- Après 3 tentatives ratées : "Perdu ! Le nombre était X"
- Ajoutez des indices spéciaux :
  - Si très proche (±5) : "Vous êtes très proche !"
  - Si très loin (±50) : "Vous êtes très loin !"

## 💡 Conseils
- Attention à l'indentation : utilisez 4 espaces
- Testez tous les cas possibles
- Utilisez `import random` et `random.randint(1, 100)` pour générer un nombre aléatoire
- Pensez à valider les entrées utilisateur

## 🎯 Points clés à retenir
- L'indentation définit les blocs de code en Python
- `elif` permet de tester plusieurs conditions
- Les opérateurs logiques permettent de combiner des conditions
- Il faut toujours tester les cas limites
