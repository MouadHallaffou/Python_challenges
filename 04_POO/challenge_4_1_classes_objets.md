# 🎯 Challenge 4.1 : Classes et Objets - Introduction à la POO

## 📚 Objectif
Comprendre les concepts fondamentaux de la Programmation Orientée Objet.

## 🔧 Ce que vous devez apprendre
- Définition de classes avec `class`
- Méthode `__init__` (constructeur)
- Attributs d'instance et de classe
- Méthodes d'instance
- Encapsulation et attributs privés
- Méthodes spéciales (__str__, __repr__)

## 💪 Challenges

### Challenge A - Première classe (Facile)
Créez une classe `Personne` avec :
- Attributs : nom, âge, email
- Méthodes : se_presenter(), avoir_anniversaire()
- Testez avec plusieurs instances

### Challenge B - Classe avec validation (Moyen)
Classe `CompteBancaire` :
- Attributs privés : numero_compte, solde, titulaire
- Méthodes : deposer(), retirer(), consulter_solde()
- Validation : pas de retrait si solde insuffisant

### Challenge C - Méthodes spéciales (Moyen)
Classe `Produit` pour e-commerce :
- Attributs : nom, prix, stock
- Implémentez __str__, __repr__, __eq__
- Méthode pour calculer valeur totale

### Challenge D - Projet complet POO (Difficile)
Système de gestion de bibliothèque :
- Classe `Livre` : titre, auteur, isbn, disponible
- Classe `Membre` : nom, numero_membre, livres_empruntes
- Classe `Bibliotheque` : catalogue, membres
- Fonctionnalités : emprunter, rendre, rechercher
- Interface utilisateur complète
