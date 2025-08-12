# models/__init__.py
"""
Module des modèles de données pour le système de gestion d'école.

Ce module contient toutes les classes principales :
- Personne, Etudiant, Professeur
- Cours, Matiere
- Note, Evaluation
- Ecole (gestionnaire principal)
"""

from .personne import Personne, Etudiant, Professeur
from .cours import Cours, Matiere
from .note import Note, Evaluation
from .ecole import Ecole

__all__ = [
    "Personne",
    "Etudiant",
    "Professeur",
    "Cours",
    "Matiere",
    "Note",
    "Evaluation",
    "Ecole",
]

__version__ = "1.0.0"
__author__ = "École Python Formation"
