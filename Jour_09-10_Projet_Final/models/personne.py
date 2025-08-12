"""
Module des classes de personnes pour le système de gestion d'école.

Ce module définit :
- Personne : Classe de base pour toutes les personnes
- Etudiant : Classe pour les étudiants avec gestion des notes
- Professeur : Classe pour les professeurs avec gestion des cours
"""

from datetime import datetime, date
from typing import List, Dict, Optional
import re


class ValidationError(Exception):
    """Exception levée lors d'erreurs de validation des données."""

    pass


class Personne:
    """
    Classe de base représentant une personne dans le système scolaire.

    Attributes:
        id_personne (str): Identifiant unique de la personne
        nom (str): Nom de famille
        prenom (str): Prénom
        date_naissance (date): Date de naissance
        email (str): Adresse email
        telephone (str): Numéro de téléphone
        adresse (str): Adresse postale
    """

    _compteur_id = 1

    def __init__(
        self,
        nom: str,
        prenom: str,
        date_naissance: str,
        email: str,
        telephone: str = "",
        adresse: str = "",
    ):
        """
        Initialise une nouvelle personne.

        Args:
            nom: Nom de famille
            prenom: Prénom
            date_naissance: Date de naissance (format YYYY-MM-DD)
            email: Adresse email
            telephone: Numéro de téléphone (optionnel)
            adresse: Adresse postale (optionnelle)

        Raises:
            ValidationError: Si les données sont invalides
        """
        self.id_personne = f"PER{Personne._compteur_id:04d}"
        Personne._compteur_id += 1

        self.nom = self._valider_nom(nom)
        self.prenom = self._valider_nom(prenom)
        self.date_naissance = self._valider_date_naissance(date_naissance)
        self.email = self._valider_email(email)
        self.telephone = self._valider_telephone(telephone) if telephone else ""
        self.adresse = adresse.strip()

        self.date_creation = datetime.now()
        self.date_modification = datetime.now()

    def _valider_nom(self, nom: str) -> str:
        """Valide et normalise un nom."""
        if not nom or not nom.strip():
            raise ValidationError("Le nom ne peut pas être vide")

        nom_clean = nom.strip()
        if len(nom_clean) < 2:
            raise ValidationError("Le nom doit contenir au moins 2 caractères")

        if not re.match(r"^[a-zA-ZÀ-ÿ\s\-']+$", nom_clean):
            raise ValidationError(
                "Le nom ne peut contenir que des lettres, espaces, tirets et apostrophes"
            )

        return nom_clean.title()

    def _valider_date_naissance(self, date_str: str) -> date:
        """Valide et convertit une date de naissance."""
        try:
            if isinstance(date_str, str):
                naissance = datetime.strptime(date_str, "%Y-%m-%d").date()
            elif isinstance(date_str, date):
                naissance = date_str
            else:
                raise ValueError("Format de date invalide")

            # Vérifier que la personne n'est pas née dans le futur
            if naissance > date.today():
                raise ValidationError(
                    "La date de naissance ne peut pas être dans le futur"
                )

            # Vérifier un âge raisonnable (entre 3 et 100 ans)
            age = (date.today() - naissance).days // 365
            if age < 3 or age > 100:
                raise ValidationError("L'âge doit être entre 3 et 100 ans")

            return naissance

        except ValueError:
            raise ValidationError("Format de date invalide. Utilisez YYYY-MM-DD")

    def _valider_email(self, email: str) -> str:
        """Valide un email."""
        if not email or not email.strip():
            raise ValidationError("L'email est obligatoire")

        email_clean = email.strip().lower()

        # Pattern regex pour validation email basique
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email_clean):
            raise ValidationError("Format d'email invalide")

        return email_clean

    def _valider_telephone(self, telephone: str) -> str:
        """Valide et formate un numéro de téléphone."""
        if not telephone:
            return ""

        # Nettoyer le numéro (enlever espaces, points, tirets)
        tel_clean = re.sub(r"[\s\.\-]", "", telephone)

        # Vérifier le format français (10 chiffres commençant par 0)
        if re.match(r"^0[1-9]\d{8}$", tel_clean):
            # Formater : 01.23.45.67.89
            return f"{tel_clean[:2]}.{tel_clean[2:4]}.{tel_clean[4:6]}.{tel_clean[6:8]}.{tel_clean[8:]}"

        # Vérifier le format international
        if re.match(r"^\+33[1-9]\d{8}$", tel_clean):
            return tel_clean

        raise ValidationError("Format de téléphone invalide (format français attendu)")

    @property
    def age(self) -> int:
        """Calcule et retourne l'âge de la personne."""
        return (date.today() - self.date_naissance).days // 365

    @property
    def nom_complet(self) -> str:
        """Retourne le nom complet (prénom nom)."""
        return f"{self.prenom} {self.nom}"

    def mettre_a_jour(self, **kwargs):
        """
        Met à jour les informations de la personne.

        Args:
            **kwargs: Attributs à mettre à jour
        """
        attributs_modifiables = {"nom", "prenom", "email", "telephone", "adresse"}

        for attr, valeur in kwargs.items():
            if attr in attributs_modifiables and hasattr(self, attr):
                if attr in ["nom", "prenom"]:
                    setattr(self, attr, self._valider_nom(valeur))
                elif attr == "email":
                    setattr(self, attr, self._valider_email(valeur))
                elif attr == "telephone":
                    setattr(self, attr, self._valider_telephone(valeur))
                else:
                    setattr(self, attr, valeur)

        self.date_modification = datetime.now()

    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire pour sérialisation."""
        return {
            "id_personne": self.id_personne,
            "type": self.__class__.__name__,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance.isoformat(),
            "email": self.email,
            "telephone": self.telephone,
            "adresse": self.adresse,
            "date_creation": self.date_creation.isoformat(),
            "date_modification": self.date_modification.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Crée une instance à partir d'un dictionnaire."""
        return cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data["date_naissance"],
            email=data["email"],
            telephone=data.get("telephone", ""),
            adresse=data.get("adresse", ""),
        )

    def __str__(self) -> str:
        return f"{self.nom_complet} ({self.email})"

    def __repr__(self) -> str:
        return f"Personne('{self.nom}', '{self.prenom}', '{self.email}')"


class Etudiant(Personne):
    """
    Classe représentant un étudiant.

    Hérite de Personne et ajoute :
    - Numéro étudiant
    - Classe/niveau
    - Liste des cours suivis
    - Notes et moyennes
    """

    _compteur_etudiant = 1

    def __init__(
        self,
        nom: str,
        prenom: str,
        date_naissance: str,
        email: str,
        classe: str,
        telephone: str = "",
        adresse: str = "",
    ):
        """
        Initialise un nouvel étudiant.

        Args:
            nom: Nom de famille
            prenom: Prénom
            date_naissance: Date de naissance
            email: Adresse email
            classe: Classe ou niveau de l'étudiant
            telephone: Numéro de téléphone (optionnel)
            adresse: Adresse postale (optionnelle)
        """
        super().__init__(nom, prenom, date_naissance, email, telephone, adresse)

        self.numero_etudiant = f"ETU{Etudiant._compteur_etudiant:04d}"
        Etudiant._compteur_etudiant += 1

        self.classe = self._valider_classe(classe)
        self.cours_inscrits: List[str] = []  # IDs des cours
        self.notes: Dict[str, List[float]] = {}  # cours_id: [notes]
        self.absences: Dict[str, int] = {}  # cours_id: nombre d'absences
        self.statut = "Actif"  # Actif, Suspendu, Diplômé, Exclu

    def _valider_classe(self, classe: str) -> str:
        """Valide le nom de classe."""
        if not classe or not classe.strip():
            raise ValidationError("La classe est obligatoire")

        classe_clean = classe.strip().upper()

        # Exemple de validation pour classes françaises
        patterns_valides = [
            r"^[0-9]{1,2}[A-Z]{1,2}$",  # 6A, 5B, 1STI2D, etc.
            r"^CP|CE[12]|CM[12]$",  # Primaire
            r"^TERM[A-Z]*$",  # Terminale
            r"^BTS|DUT|L[123]|M[12]$",  # Supérieur
        ]

        if not any(re.match(pattern, classe_clean) for pattern in patterns_valides):
            # Accepter tout format si pas de correspondance exacte
            pass

        return classe_clean

    def inscrire_cours(self, cours_id: str):
        """
        Inscrit l'étudiant à un cours.

        Args:
            cours_id: Identifiant du cours
        """
        if cours_id not in self.cours_inscrits:
            self.cours_inscrits.append(cours_id)
            self.notes[cours_id] = []
            self.absences[cours_id] = 0
            self.date_modification = datetime.now()

    def desinscrire_cours(self, cours_id: str):
        """
        Désinscrit l'étudiant d'un cours.

        Args:
            cours_id: Identifiant du cours
        """
        if cours_id in self.cours_inscrits:
            self.cours_inscrits.remove(cours_id)
            if cours_id in self.notes:
                del self.notes[cours_id]
            if cours_id in self.absences:
                del self.absences[cours_id]
            self.date_modification = datetime.now()

    def ajouter_note(self, cours_id: str, note: float, coefficient: float = 1.0):
        """
        Ajoute une note pour un cours.

        Args:
            cours_id: Identifiant du cours
            note: Note obtenue (0-20)
            coefficient: Coefficient de la note

        Raises:
            ValidationError: Si la note est invalide
        """
        if cours_id not in self.cours_inscrits:
            raise ValidationError("L'étudiant n'est pas inscrit à ce cours")

        if not 0 <= note <= 20:
            raise ValidationError("La note doit être entre 0 et 20")

        if not 0 < coefficient <= 5:
            raise ValidationError("Le coefficient doit être entre 0.1 et 5")

        # Stocker la note avec son coefficient
        self.notes[cours_id].append({"note": note, "coefficient": coefficient})
        self.date_modification = datetime.now()

    def calculer_moyenne_cours(self, cours_id: str) -> Optional[float]:
        """
        Calcule la moyenne pour un cours donné.

        Args:
            cours_id: Identifiant du cours

        Returns:
            Moyenne du cours ou None si pas de notes
        """
        if cours_id not in self.notes or not self.notes[cours_id]:
            return None

        notes_cours = self.notes[cours_id]

        # Si les notes sont des nombres simples (compatibilité)
        if isinstance(notes_cours[0], (int, float)):
            return sum(notes_cours) / len(notes_cours)

        # Si les notes ont des coefficients
        total_points = sum(note["note"] * note["coefficient"] for note in notes_cours)
        total_coefficients = sum(note["coefficient"] for note in notes_cours)

        return total_points / total_coefficients if total_coefficients > 0 else None

    def calculer_moyenne_generale(self) -> Optional[float]:
        """
        Calcule la moyenne générale de l'étudiant.

        Returns:
            Moyenne générale ou None si pas de notes
        """
        moyennes_cours = []

        for cours_id in self.cours_inscrits:
            moyenne = self.calculer_moyenne_cours(cours_id)
            if moyenne is not None:
                moyennes_cours.append(moyenne)

        if not moyennes_cours:
            return None

        return sum(moyennes_cours) / len(moyennes_cours)

    def ajouter_absence(self, cours_id: str, nombre: int = 1):
        """
        Ajoute des absences pour un cours.

        Args:
            cours_id: Identifiant du cours
            nombre: Nombre d'absences à ajouter
        """
        if cours_id in self.absences:
            self.absences[cours_id] += nombre
        else:
            self.absences[cours_id] = nombre

        self.date_modification = datetime.now()

    def obtenir_bulletin(self) -> Dict:
        """
        Génère le bulletin de notes de l'étudiant.

        Returns:
            Dictionnaire contenant toutes les informations du bulletin
        """
        bulletin = {
            "etudiant": {
                "numero": self.numero_etudiant,
                "nom_complet": self.nom_complet,
                "classe": self.classe,
                "age": self.age,
            },
            "periode": {
                "debut": self.date_creation.strftime("%Y-%m-%d"),
                "fin": datetime.now().strftime("%Y-%m-%d"),
            },
            "notes_par_cours": {},
            "moyenne_generale": self.calculer_moyenne_generale(),
            "total_absences": sum(self.absences.values()),
            "statut": self.statut,
        }

        for cours_id in self.cours_inscrits:
            moyenne = self.calculer_moyenne_cours(cours_id)
            bulletin["notes_par_cours"][cours_id] = {
                "notes": self.notes.get(cours_id, []),
                "moyenne": moyenne,
                "absences": self.absences.get(cours_id, 0),
            }

        return bulletin

    def changer_statut(self, nouveau_statut: str):
        """
        Change le statut de l'étudiant.

        Args:
            nouveau_statut: Nouveau statut (Actif, Suspendu, Diplômé, Exclu)
        """
        statuts_valides = ["Actif", "Suspendu", "Diplômé", "Exclu"]

        if nouveau_statut not in statuts_valides:
            raise ValidationError(
                f"Statut invalide. Statuts valides: {statuts_valides}"
            )

        self.statut = nouveau_statut
        self.date_modification = datetime.now()

    def to_dict(self) -> Dict:
        """Convertit l'étudiant en dictionnaire."""
        data = super().to_dict()
        data.update(
            {
                "numero_etudiant": self.numero_etudiant,
                "classe": self.classe,
                "cours_inscrits": self.cours_inscrits,
                "notes": self.notes,
                "absences": self.absences,
                "statut": self.statut,
            }
        )
        return data

    @classmethod
    def from_dict(cls, data: Dict):
        """Crée un étudiant à partir d'un dictionnaire."""
        etudiant = cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data["date_naissance"],
            email=data["email"],
            classe=data["classe"],
            telephone=data.get("telephone", ""),
            adresse=data.get("adresse", ""),
        )

        # Restaurer les données spécifiques
        etudiant.numero_etudiant = data.get("numero_etudiant", etudiant.numero_etudiant)
        etudiant.cours_inscrits = data.get("cours_inscrits", [])
        etudiant.notes = data.get("notes", {})
        etudiant.absences = data.get("absences", {})
        etudiant.statut = data.get("statut", "Actif")

        return etudiant

    def __str__(self) -> str:
        return f"Étudiant {self.numero_etudiant}: {self.nom_complet} ({self.classe})"


class Professeur(Personne):
    """
    Classe représentant un professeur.

    Hérite de Personne et ajoute :
    - Numéro de professeur
    - Spécialités enseignées
    - Liste des cours assignés
    - Statut d'emploi
    """

    _compteur_professeur = 1

    def __init__(
        self,
        nom: str,
        prenom: str,
        date_naissance: str,
        email: str,
        specialites: List[str],
        telephone: str = "",
        adresse: str = "",
    ):
        """
        Initialise un nouveau professeur.

        Args:
            nom: Nom de famille
            prenom: Prénom
            date_naissance: Date de naissance
            email: Adresse email
            specialites: Liste des matières enseignées
            telephone: Numéro de téléphone (optionnel)
            adresse: Adresse postale (optionnelle)
        """
        super().__init__(nom, prenom, date_naissance, email, telephone, adresse)

        self.numero_professeur = f"PROF{Professeur._compteur_professeur:04d}"
        Professeur._compteur_professeur += 1

        self.specialites = self._valider_specialites(specialites)
        self.cours_assignes: List[str] = []  # IDs des cours
        self.statut_emploi = "Actif"  # Actif, Congé, Retraité, Licencié
        self.date_embauche = datetime.now().date()
        self.salaire_mensuel: Optional[float] = None

    def _valider_specialites(self, specialites: List[str]) -> List[str]:
        """
        Valide et normalise les spécialités.

        Args:
            specialites: Liste des spécialités

        Returns:
            Liste des spécialités validées
        """
        if not specialites:
            raise ValidationError("Au moins une spécialité est requise")

        specialites_valides = []
        for spec in specialites:
            if isinstance(spec, str) and spec.strip():
                specialites_valides.append(spec.strip().title())

        if not specialites_valides:
            raise ValidationError("Aucune spécialité valide fournie")

        return list(set(specialites_valides))  # Éliminer les doublons

    def ajouter_specialite(self, specialite: str):
        """
        Ajoute une spécialité au professeur.

        Args:
            specialite: Nouvelle spécialité
        """
        if specialite and specialite.strip():
            spec_clean = specialite.strip().title()
            if spec_clean not in self.specialites:
                self.specialites.append(spec_clean)
                self.date_modification = datetime.now()

    def retirer_specialite(self, specialite: str):
        """
        Retire une spécialité du professeur.

        Args:
            specialite: Spécialité à retirer
        """
        if len(self.specialites) <= 1:
            raise ValidationError("Un professeur doit avoir au moins une spécialité")

        spec_clean = specialite.strip().title()
        if spec_clean in self.specialites:
            self.specialites.remove(spec_clean)
            self.date_modification = datetime.now()

    def assigner_cours(self, cours_id: str):
        """
        Assigne un cours au professeur.

        Args:
            cours_id: Identifiant du cours
        """
        if cours_id not in self.cours_assignes:
            self.cours_assignes.append(cours_id)
            self.date_modification = datetime.now()

    def retirer_cours(self, cours_id: str):
        """
        Retire un cours du professeur.

        Args:
            cours_id: Identifiant du cours
        """
        if cours_id in self.cours_assignes:
            self.cours_assignes.remove(cours_id)
            self.date_modification = datetime.now()

    def definir_salaire(self, salaire: float):
        """
        Définit le salaire mensuel du professeur.

        Args:
            salaire: Salaire mensuel en euros
        """
        if salaire <= 0:
            raise ValidationError("Le salaire doit être positif")

        self.salaire_mensuel = salaire
        self.date_modification = datetime.now()

    def changer_statut_emploi(self, nouveau_statut: str):
        """
        Change le statut d'emploi du professeur.

        Args:
            nouveau_statut: Nouveau statut
        """
        statuts_valides = ["Actif", "Congé", "Retraité", "Licencié"]

        if nouveau_statut not in statuts_valides:
            raise ValidationError(
                f"Statut invalide. Statuts valides: {statuts_valides}"
            )

        self.statut_emploi = nouveau_statut
        self.date_modification = datetime.now()

    @property
    def anciennete_annees(self) -> float:
        """Calcule l'ancienneté en années."""
        return (date.today() - self.date_embauche).days / 365.25

    def obtenir_rapport_activite(self) -> Dict:
        """
        Génère un rapport d'activité du professeur.

        Returns:
            Dictionnaire avec les informations d'activité
        """
        return {
            "professeur": {
                "numero": self.numero_professeur,
                "nom_complet": self.nom_complet,
                "specialites": self.specialites,
                "statut": self.statut_emploi,
            },
            "emploi": {
                "date_embauche": self.date_embauche.isoformat(),
                "anciennete_annees": round(self.anciennete_annees, 1),
                "salaire_mensuel": self.salaire_mensuel,
            },
            "cours": {
                "nombre_cours_assignes": len(self.cours_assignes),
                "cours_assignes": self.cours_assignes,
            },
            "periode": {
                "debut": self.date_creation.strftime("%Y-%m-%d"),
                "fin": datetime.now().strftime("%Y-%m-%d"),
            },
        }

    def to_dict(self) -> Dict:
        """Convertit le professeur en dictionnaire."""
        data = super().to_dict()
        data.update(
            {
                "numero_professeur": self.numero_professeur,
                "specialites": self.specialites,
                "cours_assignes": self.cours_assignes,
                "statut_emploi": self.statut_emploi,
                "date_embauche": self.date_embauche.isoformat(),
                "salaire_mensuel": self.salaire_mensuel,
            }
        )
        return data

    @classmethod
    def from_dict(cls, data: Dict):
        """Crée un professeur à partir d'un dictionnaire."""
        professeur = cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data["date_naissance"],
            email=data["email"],
            specialites=data["specialites"],
            telephone=data.get("telephone", ""),
            adresse=data.get("adresse", ""),
        )

        # Restaurer les données spécifiques
        professeur.numero_professeur = data.get(
            "numero_professeur", professeur.numero_professeur
        )
        professeur.cours_assignes = data.get("cours_assignes", [])
        professeur.statut_emploi = data.get("statut_emploi", "Actif")
        professeur.salaire_mensuel = data.get("salaire_mensuel")

        if "date_embauche" in data:
            professeur.date_embauche = datetime.fromisoformat(
                data["date_embauche"]
            ).date()

        return professeur

    def __str__(self) -> str:
        specialites_str = ", ".join(self.specialites[:2])
        if len(self.specialites) > 2:
            specialites_str += "..."
        return f"Professeur {self.numero_professeur}: {self.nom_complet} ({specialites_str})"
