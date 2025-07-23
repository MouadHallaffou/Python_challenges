#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple de script Python bien structuré
Démontre les bonnes pratiques de programmation
"""


def main():
    """
    Fonction principale - point d'entrée du programme
    Démontre l'utilisation des concepts de base Python
    """
    print("🐍 Bienvenue dans votre formation Python !")
    print("=" * 50)

    # Démonstration des concepts de base
    demonstrer_variables()
    demonstrer_structures_controle()
    demonstrer_fonctions()
    demonstrer_collections()

    print("\n🎯 Vous êtes prêt à commencer les challenges !")
    print("📁 Commencez par le dossier 01_Fondamentaux")


def demonstrer_variables():
    """Démontre l'utilisation des variables et types de base"""
    print("\n📌 1. Variables et Types de Données")

    # Différents types de variables
    nom = "Python"
    version = 3.11
    est_awesome = True

    print(f"Langage: {nom} (type: {type(nom).__name__})")
    print(f"Version: {version} (type: {type(version).__name__})")
    print(f"Est génial: {est_awesome} (type: {type(est_awesome).__name__})")


def demonstrer_structures_controle():
    """Démontre les structures de contrôle"""
    print("\n📌 2. Structures de Contrôle")

    # Condition
    age = 25
    if age >= 18:
        print(f"Vous avez {age} ans - Vous êtes majeur")
    else:
        print(f"Vous avez {age} ans - Vous êtes mineur")

    # Boucle
    print("Compte à rebours:", end=" ")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print("🚀")


def demonstrer_fonctions():
    """Démontre la création et l'utilisation de fonctions"""
    print("\n📌 3. Fonctions")

    def saluer(nom, age=None):
        """Fonction de salutation avec paramètre optionnel"""
        if age:
            return f"Salut {nom}, tu as {age} ans !"
        return f"Salut {nom} !"

    # Test de la fonction
    message1 = saluer("Alice")
    message2 = saluer("Bob", 30)

    print(message1)
    print(message2)


def demonstrer_collections():
    """Démontre l'utilisation des collections Python"""
    print("\n📌 4. Collections de Données")

    # Liste
    langages = ["Python", "JavaScript", "Java", "C++"]
    print(f"Langages de programmation: {langages}")
    print(f"Mon préféré: {langages[0]}")

    # Dictionnaire
    personne = {
        "nom": "Alice",
        "age": 25,
        "ville": "Paris",
        "langages": langages[:2],  # Les 2 premiers
    }
    print(f"Profil: {personne['nom']}, {personne['age']} ans, {personne['ville']}")
    print(f"Compétences: {', '.join(personne['langages'])}")

    # Compréhension de liste (bonus)
    langages_courts = [lang for lang in langages if len(lang) <= 6]
    print(f"Langages courts: {langages_courts}")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
