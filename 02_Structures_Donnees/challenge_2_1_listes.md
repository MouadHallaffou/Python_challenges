# 🎯 Challenge 2.1 : Listes - Collections Dynamiques

## 📚 Objectif
Maîtriser les listes Python pour stocker et manipuler des collections de données.

## 🔧 Ce que vous devez apprendre
- Création et initialisation de listes
- Accès aux éléments (indexation et slicing)
- Méthodes de listes : append, insert, remove, pop, sort
- Parcours de listes
- Listes en compréhension

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
