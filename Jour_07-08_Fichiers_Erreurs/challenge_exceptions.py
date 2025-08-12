# Challenge Jour 7 - Gestion des Erreurs et Exceptions
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Exceptions de Base (45min)
# =============================================================================

print("=== PARTIE A - Exceptions de Base ===")


# 1. Gestion d'erreurs simples
def division_securisee(a, b):
    """Division avec gestion d'erreur"""
    try:
        resultat = a / b
        return f"✅ {a} ÷ {b} = {resultat}"
    except ZeroDivisionError:
        return "❌ Erreur: Division par zéro impossible"
    except TypeError:
        return "❌ Erreur: Les arguments doivent être des nombres"


# Tests de division sécurisée
print("1. Tests division sécurisée :")
print(division_securisee(10, 2))
print(division_securisee(10, 0))
print(division_securisee("10", 2))


# 2. Gestion de conversion de types
def convertir_en_entier(valeur):
    """Convertir une valeur en entier avec gestion d'erreur"""
    try:
        nombre = int(valeur)
        return f"✅ Conversion réussie: {nombre}"
    except ValueError:
        return f"❌ Impossible de convertir '{valeur}' en entier"
    except TypeError:
        return f"❌ Type '{type(valeur).__name__}' non convertible"


# Tests de conversion
print("\n2. Tests conversion :")
print(convertir_en_entier("123"))
print(convertir_en_entier("abc"))
print(convertir_en_entier(12.5))
print(convertir_en_entier([1, 2, 3]))


# 3. Gestion d'accès aux éléments
def obtenir_element(liste, index):
    """Obtenir un élément de liste avec gestion d'erreur"""
    try:
        element = liste[index]
        return f"✅ Élément à l'index {index}: {element}"
    except IndexError:
        return f"❌ Index {index} hors des limites (taille: {len(liste)})"
    except TypeError:
        return f"❌ L'objet n'est pas indexable"


# Tests d'accès aux éléments
print("\n3. Tests accès éléments :")
ma_liste = ["a", "b", "c"]
print(obtenir_element(ma_liste, 1))
print(obtenir_element(ma_liste, 5))
print(obtenir_element("pas une liste", 0))

# =============================================================================
# PARTIE B - Try/Except/Finally/Else (45min)
# =============================================================================

print("\n=== PARTIE B - Try/Except/Finally/Else ===")


# 1. Utilisation complète de try/except/else/finally
def traiter_fichier_demo(nom_fichier):
    """Démonstration complète de gestion d'erreurs"""
    print(f"\n🔄 Traitement du fichier: {nom_fichier}")
    fichier = None

    try:
        # Tentative d'ouverture du fichier
        print("  📂 Tentative d'ouverture...")
        fichier = open(nom_fichier, "r", encoding="utf-8")
        contenu = fichier.read()
        print(f"  ✅ Fichier lu avec succès ({len(contenu)} caractères)")

    except FileNotFoundError:
        print(f"  ❌ Fichier '{nom_fichier}' non trouvé")
        return False

    except PermissionError:
        print(f"  ❌ Pas d'autorisation pour lire '{nom_fichier}'")
        return False

    except UnicodeDecodeError:
        print(f"  ❌ Erreur d'encodage du fichier '{nom_fichier}'")
        return False

    else:
        # Exécuté seulement si aucune exception
        print("  🎉 Lecture terminée sans erreur")
        return True

    finally:
        # Exécuté dans tous les cas
        if fichier and not fichier.closed:
            fichier.close()
            print("  🔒 Fichier fermé")
        print("  ⏹️ Traitement terminé")


# Tests de traitement de fichier
print("4. Tests traitement fichier :")

# Créons d'abord un fichier de test
try:
    with open("test_fichier.txt", "w", encoding="utf-8") as f:
        f.write("Contenu de test pour la démonstration")
    print("📝 Fichier de test créé")
except Exception as e:
    print(f"❌ Erreur création fichier test: {e}")

# Tests avec différents scénarios
traiter_fichier_demo("test_fichier.txt")  # Fichier existant
traiter_fichier_demo("fichier_inexistant.txt")  # Fichier inexistant


# 2. Gestion de saisie utilisateur robuste
def demander_nombre(message, type_nombre=int, min_val=None, max_val=None):
    """Demander un nombre à l'utilisateur avec validation complète"""
    while True:
        try:
            # Demande de saisie
            saisie = input(f"{message}: ")

            # Conversion
            nombre = type_nombre(saisie)

            # Validation des limites
            if min_val is not None and nombre < min_val:
                print(f"❌ Le nombre doit être >= {min_val}")
                continue

            if max_val is not None and nombre > max_val:
                print(f"❌ Le nombre doit être <= {max_val}")
                continue

            # Si tout va bien
            return nombre

        except ValueError:
            type_nom = "entier" if type_nombre == int else "nombre décimal"
            print(f"❌ Veuillez entrer un {type_nom} valide")
        except KeyboardInterrupt:
            print("\n⚠️ Interruption utilisateur")
            return None
        except EOFError:
            print("\n⚠️ Fin de saisie détectée")
            return None


# Test interactif (décommenté pour tester)
# print("\n5. Test saisie sécurisée :")
# age = demander_nombre("Entrez votre âge", int, 0, 120)
# if age is not None:
#     print(f"✅ Âge saisi: {age} ans")

# =============================================================================
# PARTIE C - Exceptions Personnalisées (45min)
# =============================================================================

print("\n=== PARTIE C - Exceptions Personnalisées ===")


# 1. Définition d'exceptions personnalisées
class ErreurValidation(Exception):
    """Exception de base pour les erreurs de validation"""

    def __init__(self, message, code_erreur=None):
        super().__init__(message)
        self.code_erreur = code_erreur
        self.message = message

    def __str__(self):
        if self.code_erreur:
            return f"[{self.code_erreur}] {self.message}"
        return self.message


class ErreurMotDePasse(ErreurValidation):
    """Exception pour les erreurs de mot de passe"""

    def __init__(self, message):
        super().__init__(message, "PWD_001")


class ErreurEmail(ErreurValidation):
    """Exception pour les erreurs d'email"""

    def __init__(self, message):
        super().__init__(message, "EMAIL_001")


class ErreurAge(ErreurValidation):
    """Exception pour les erreurs d'âge"""

    def __init__(self, message, age_fourni=None):
        super().__init__(message, "AGE_001")
        self.age_fourni = age_fourni


# 2. Validateur avec exceptions personnalisées
class ValidateurUtilisateur:
    """Classe pour valider les données utilisateur"""

    @staticmethod
    def valider_mot_de_passe(mot_de_passe):
        """Valider un mot de passe"""
        if len(mot_de_passe) < 8:
            raise ErreurMotDePasse(
                "Le mot de passe doit contenir au moins 8 caractères"
            )

        if not any(c.isupper() for c in mot_de_passe):
            raise ErreurMotDePasse(
                "Le mot de passe doit contenir au moins une majuscule"
            )

        if not any(c.islower() for c in mot_de_passe):
            raise ErreurMotDePasse(
                "Le mot de passe doit contenir au moins une minuscule"
            )

        if not any(c.isdigit() for c in mot_de_passe):
            raise ErreurMotDePasse("Le mot de passe doit contenir au moins un chiffre")

        caracteres_speciaux = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in caracteres_speciaux for c in mot_de_passe):
            raise ErreurMotDePasse(
                "Le mot de passe doit contenir au moins un caractère spécial"
            )

        return True

    @staticmethod
    def valider_email(email):
        """Valider un email"""
        if "@" not in email:
            raise ErreurEmail("L'email doit contenir le symbole @")

        if email.count("@") != 1:
            raise ErreurEmail("L'email ne doit contenir qu'un seul symbole @")

        partie_locale, domaine = email.split("@")

        if not partie_locale:
            raise ErreurEmail("L'email doit avoir une partie avant le @")

        if not domaine:
            raise ErreurEmail("L'email doit avoir un domaine après le @")

        if "." not in domaine:
            raise ErreurEmail("Le domaine doit contenir au moins un point")

        return True

    @staticmethod
    def valider_age(age):
        """Valider un âge"""
        try:
            age_int = int(age)
        except (ValueError, TypeError):
            raise ErreurAge(f"L'âge doit être un nombre entier", age)

        if age_int < 0:
            raise ErreurAge(f"L'âge ne peut pas être négatif", age_int)

        if age_int > 150:
            raise ErreurAge(f"L'âge ne peut pas dépasser 150 ans", age_int)

        return age_int


# Tests des validateurs
print("6. Tests validateurs avec exceptions personnalisées :")

# Test mots de passe
mots_de_passe_test = [
    "123456",  # Trop court
    "motdepasse",  # Pas de majuscule/chiffre
    "MOTDEPASSE",  # Pas de minuscule/chiffre
    "MotDePasse",  # Pas de chiffre/caractère spécial
    "MotDePasse123",  # Pas de caractère spécial
    "MotDePasse123!",  # Valide
]

for mdp in mots_de_passe_test:
    try:
        ValidateurUtilisateur.valider_mot_de_passe(mdp)
        print(f"✅ Mot de passe valide: {mdp}")
    except ErreurMotDePasse as e:
        print(f"❌ {e}")

# Test emails
emails_test = [
    "email",  # Pas de @
    "email@@domain.com",  # Plusieurs @
    "@domain.com",  # Pas de partie locale
    "email@",  # Pas de domaine
    "email@domain",  # Pas de point dans domaine
    "email@domain.com",  # Valide
]

print("\nTests emails :")
for email in emails_test:
    try:
        ValidateurUtilisateur.valider_email(email)
        print(f"✅ Email valide: {email}")
    except ErreurEmail as e:
        print(f"❌ {e}")

# Test âges
ages_test = ["25", "-5", "200", "abc", "25.5"]

print("\nTests âges :")
for age in ages_test:
    try:
        age_valide = ValidateurUtilisateur.valider_age(age)
        print(f"✅ Âge valide: {age_valide} ans")
    except ErreurAge as e:
        print(f"❌ {e}")

# =============================================================================
# PARTIE D - Gestion d'Erreurs dans les Fonctions (30min)
# =============================================================================

print("\n=== PARTIE D - Gestion d'Erreurs dans les Fonctions ===")


def calculatrice_robuste():
    """Calculatrice avec gestion complète des erreurs"""
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "**": lambda a, b: a**b,
        "%": lambda a, b: a % b,
    }

    while True:
        try:
            print("\n🔢 CALCULATRICE ROBUSTE")
            print("Opérations disponibles:", ", ".join(operations.keys()))
            print("Tapez 'quit' pour quitter")

            # Saisie de l'opération
            operation = input("Opération: ").strip()
            if operation.lower() == "quit":
                break

            if operation not in operations:
                print(f"❌ Opération '{operation}' non reconnue")
                continue

            # Saisie des nombres
            a = float(input("Premier nombre: "))
            b = float(input("Deuxième nombre: "))

            # Calcul
            resultat = operations[operation](a, b)
            print(f"✅ {a} {operation} {b} = {resultat}")

        except ValueError:
            print("❌ Veuillez entrer des nombres valides")
        except ZeroDivisionError:
            print("❌ Division par zéro impossible")
        except OverflowError:
            print("❌ Résultat trop grand pour être calculé")
        except KeyboardInterrupt:
            print("\n⚠️ Calculatrice interrompue")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")


# Test calculatrice (décommenté pour tester)
# calculatrice_robuste()

# =============================================================================
# PARTIE E - Logging et Debugging (30min)
# =============================================================================

print("\n=== PARTIE E - Logging et Debugging ===")

import logging
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("application.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


class CompteBancaireAvecLog:
    """Compte bancaire avec logging des opérations"""

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []

        logger.info(
            f"Création compte pour {titulaire} avec solde initial {solde_initial}€"
        )

    def deposer(self, montant):
        """Déposer de l'argent avec logging"""
        try:
            if montant <= 0:
                raise ValueError("Le montant doit être positif")

            self.solde += montant
            self.historique.append(f"Dépôt: +{montant}€")

            logger.info(
                f"Dépôt de {montant}€ sur le compte de {self.titulaire}. Nouveau solde: {self.solde}€"
            )
            return f"✅ Dépôt de {montant}€ effectué"

        except ValueError as e:
            logger.warning(f"Tentative de dépôt invalide pour {self.titulaire}: {e}")
            return f"❌ Erreur: {e}"
        except Exception as e:
            logger.error(f"Erreur inattendue lors du dépôt pour {self.titulaire}: {e}")
            return f"❌ Erreur système: {e}"

    def retirer(self, montant):
        """Retirer de l'argent avec logging"""
        try:
            if montant <= 0:
                raise ValueError("Le montant doit être positif")

            if montant > self.solde:
                raise ValueError(f"Solde insuffisant. Solde actuel: {self.solde}€")

            self.solde -= montant
            self.historique.append(f"Retrait: -{montant}€")

            logger.info(
                f"Retrait de {montant}€ du compte de {self.titulaire}. Nouveau solde: {self.solde}€"
            )
            return f"✅ Retrait de {montant}€ effectué"

        except ValueError as e:
            logger.warning(f"Tentative de retrait invalide pour {self.titulaire}: {e}")
            return f"❌ Erreur: {e}"
        except Exception as e:
            logger.error(
                f"Erreur inattendue lors du retrait pour {self.titulaire}: {e}"
            )
            return f"❌ Erreur système: {e}"


# Test du compte avec logging
print("7. Test compte bancaire avec logging :")
compte = CompteBancaireAvecLog("Alice Dupont", 1000)
print(compte.deposer(500))
print(compte.retirer(200))
print(compte.retirer(2000))  # Solde insuffisant
print(compte.deposer(-100))  # Montant négatif

# =============================================================================
# MINI-PROJET - Système de Validation de Formulaire (45min)
# =============================================================================

print("\n=== MINI-PROJET - Validation de Formulaire ===")


class ErreurFormulaire(Exception):
    """Exception de base pour les erreurs de formulaire"""

    pass


class ErreurChampObligatoire(ErreurFormulaire):
    """Exception pour les champs obligatoires manquants"""

    def __init__(self, nom_champ):
        self.nom_champ = nom_champ
        super().__init__(f"Le champ '{nom_champ}' est obligatoire")


class ErreurFormatChamp(ErreurFormulaire):
    """Exception pour les formats de champs invalides"""

    def __init__(self, nom_champ, format_attendu):
        self.nom_champ = nom_champ
        self.format_attendu = format_attendu
        super().__init__(
            f"Le champ '{nom_champ}' doit respecter le format: {format_attendu}"
        )


class FormulaireUtilisateur:
    """Classe pour gérer un formulaire d'inscription utilisateur"""

    def __init__(self):
        self.donnees = {}
        self.erreurs = []

    def ajouter_champ(self, nom_champ, valeur, obligatoire=False, validateur=None):
        """Ajouter un champ au formulaire"""
        try:
            # Vérifier si le champ est obligatoire
            if obligatoire and (not valeur or str(valeur).strip() == ""):
                raise ErreurChampObligatoire(nom_champ)

            # Appliquer le validateur si fourni
            if validateur and valeur:
                valeur_validee = validateur(valeur)
                self.donnees[nom_champ] = valeur_validee
            else:
                self.donnees[nom_champ] = valeur

            return True

        except ErreurFormulaire as e:
            self.erreurs.append(str(e))
            return False
        except Exception as e:
            self.erreurs.append(f"Erreur inattendue pour le champ '{nom_champ}': {e}")
            return False

    def valider_formulaire(self):
        """Valider l'ensemble du formulaire"""
        if self.erreurs:
            raise ErreurFormulaire(
                f"Formulaire invalide: {len(self.erreurs)} erreur(s) détectée(s)"
            )
        return True

    def afficher_erreurs(self):
        """Afficher toutes les erreurs"""
        if self.erreurs:
            print("❌ Erreurs de validation :")
            for i, erreur in enumerate(self.erreurs, 1):
                print(f"  {i}. {erreur}")
        else:
            print("✅ Aucune erreur de validation")

    def afficher_donnees(self):
        """Afficher les données validées"""
        if self.donnees:
            print("📋 Données du formulaire :")
            for champ, valeur in self.donnees.items():
                print(f"  {champ}: {valeur}")
        else:
            print("📋 Aucune donnée valide")


# Validateurs spécifiques
def validateur_telephone(telephone):
    """Valider un numéro de téléphone français"""
    # Nettoyer le numéro
    telephone_clean = "".join(c for c in telephone if c.isdigit())

    if len(telephone_clean) != 10:
        raise ErreurFormatChamp("telephone", "10 chiffres (ex: 0123456789)")

    if not telephone_clean.startswith("0"):
        raise ErreurFormatChamp("telephone", "doit commencer par 0")

    return f"{telephone_clean[:2]}.{telephone_clean[2:4]}.{telephone_clean[4:6]}.{telephone_clean[6:8]}.{telephone_clean[8:]}"


def validateur_date_naissance(date_str):
    """Valider une date de naissance"""
    try:
        jour, mois, annee = map(int, date_str.split("/"))

        if not (1 <= jour <= 31):
            raise ValueError("Jour invalide")
        if not (1 <= mois <= 12):
            raise ValueError("Mois invalide")
        if not (1900 <= annee <= 2024):
            raise ValueError("Année invalide")

        # Vérification d'âge
        age = 2024 - annee
        if age < 13:
            raise ValueError("Vous devez avoir au moins 13 ans")

        return f"{jour:02d}/{mois:02d}/{annee}"

    except (ValueError, AttributeError):
        raise ErreurFormatChamp("date_naissance", "JJ/MM/AAAA")


# Test du système de formulaire
print("8. Test système de formulaire :")

# Création du formulaire
formulaire = FormulaireUtilisateur()

# Ajout des champs avec validation
donnees_test = {
    "nom": ("Dupont", True, None),
    "prenom": ("Alice", True, None),
    "email": ("alice@email.com", True, ValidateurUtilisateur.valider_email),
    "telephone": ("01 23 45 67 89", False, validateur_telephone),
    "date_naissance": ("15/03/1990", True, validateur_date_naissance),
    "mot_de_passe": (
        "MotDePasse123!",
        True,
        ValidateurUtilisateur.valider_mot_de_passe,
    ),
}

# Test avec données valides
print("\nTest avec données valides :")
for nom_champ, (valeur, obligatoire, validateur) in donnees_test.items():
    succes = formulaire.ajouter_champ(nom_champ, valeur, obligatoire, validateur)
    print(f"  {nom_champ}: {'✅' if succes else '❌'}")

try:
    formulaire.valider_formulaire()
    print("✅ Formulaire valide !")
    formulaire.afficher_donnees()
except ErreurFormulaire as e:
    print(f"❌ {e}")
    formulaire.afficher_erreurs()

# Test avec données invalides
print("\nTest avec données invalides :")
formulaire_invalide = FormulaireUtilisateur()

donnees_invalides = {
    "nom": ("", True, None),  # Champ obligatoire vide
    "email": (
        "email_invalide",
        True,
        ValidateurUtilisateur.valider_email,
    ),  # Email invalide
    "telephone": ("123", False, validateur_telephone),  # Téléphone invalide
    "date_naissance": ("32/13/1800", True, validateur_date_naissance),  # Date invalide
}

for nom_champ, (valeur, obligatoire, validateur) in donnees_invalides.items():
    formulaire_invalide.ajouter_champ(nom_champ, valeur, obligatoire, validateur)

formulaire_invalide.afficher_erreurs()

print("\n🎉 Gestion d'erreurs terminée !")
print("⏭️ Passez maintenant aux fichiers et données !")
