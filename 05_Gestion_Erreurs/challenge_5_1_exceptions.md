# 🎯 Challenge 5.1 : Gestion des Exceptions

## 📚 Objectif
Apprendre à gérer les erreurs de manière élégante et robuste.

## 🔧 Ce que vous devez apprendre

### 1. Try, except, else, finally

```python
try:
    x = int(input("Entrez un nombre : "))
    y = 10 / x
except ZeroDivisionError:
    print("Erreur : division par zéro !")
except ValueError:
    print("Erreur : entrée invalide !")
else:
    print(f"Résultat : {y}")
finally:
    print("Fin du programme.")
```
- **try** : Bloc où le code à risque est exécuté.
- **except** : Bloc qui gère l’erreur.
- **else** : S’exécute si aucune erreur.
- **finally** : S’exécute toujours (erreur ou non).

### 2. Types d'exceptions courantes

| Exception            | Exemple déclencheur                   |
|----------------------|---------------------------------------|
| ZeroDivisionError    | `10 / 0`                              |
| ValueError           | `int("abc")`                          |
| IndexError           | `liste[10]` si liste trop courte      |
| FileNotFoundError    | `open("fichier.txt")` si absent       |

### 3. Création d'exceptions personnalisées

```python
class SoldeInsuffisantError(Exception):
    pass

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError("Solde insuffisant !")
    return solde - montant

try:
    retirer(100, 200)
except SoldeInsuffisantError as e:
    print(e)
```

### 4. Bonnes pratiques de gestion d'erreurs

- Préciser le type d’exception à intercepter.
- Donner des messages clairs à l’utilisateur.
- Ne jamais masquer les erreurs silencieusement.
- Utiliser des exceptions personnalisées pour les cas métier.

### 5. Logging des erreurs

```python
import logging

logging.basicConfig(filename='erreurs.log', level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error(f"Erreur détectée : {e}")
```

---

## 💪 Challenges

### Challenge A - Exceptions de base (Facile)

- **Division sécurisée**
    ```python
    try:
        a = int(input("Numérateur : "))
        b = int(input("Dénominateur : "))
        print(a / b)
    except ZeroDivisionError:
        print("Impossible de diviser par zéro.")
    ```
- **Conversion sécurisée**
    ```python
    try:
        age = int(input("Votre âge : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
    ```
- **Accès liste sécurisé**
    ```python
    liste = [1, 2, 3]
    try:
        print(liste[5])
    except IndexError:
        print("Index hors limites.")
    ```
- **Ouverture fichier sécurisée**
    ```python
    try:
        with open("data.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("Fichier introuvable.")
    ```

### Challenge B - Validation d'entrées (Moyen)

- **Âge**
    ```python
    try:
        age = int(input("Âge : "))
        if not (0 <= age <= 120):
            raise ValueError("Âge hors limites.")
    except ValueError as e:
        print(e)
    ```
- **Email**
    ```python
    import re
    email = input("Email : ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Format d'email invalide.")
    ```
- **Téléphone**
    ```python
    tel = input("Téléphone : ")
    if not re.match(r"^0[1-9]\d{8}$", tel):
        print("Format de téléphone français invalide.")
    ```
- **Code postal**
    ```python
    cp = input("Code postal : ")
    if not re.match(r"^\d{5}$", cp):
        print("Code postal invalide.")
    ```

### Challenge C - Exceptions personnalisées (Moyen)

```python
class CompteInexistantError(Exception): pass
class MontantInvalideError(Exception): pass

def virement(compte, montant):
    if compte not in comptes:
        raise CompteInexistantError("Compte non trouvé.")
    if montant <= 0:
        raise MontantInvalideError("Montant invalide.")
    # etc.
```

### Challenge D - Projet robuste (Difficile)

- **Calculatrice scientifique ultra-robuste**
    ```python
    import logging

    logging.basicConfig(filename='calc.log', level=logging.ERROR)

    def calculatrice():
        while True:
            try:
                expr = input("Expression : ")
                if expr == "exit":
                    break
                print(eval(expr))
            except Exception as e:
                logging.error(f"Erreur : {e}")
                print("Erreur détectée, veuillez réessayer.")
    calculatrice()
    ```
- **Recovery automatique** : Boucle qui ne s’arrête jamais sur erreur.
- **Tests unitaires** : Créez des tests pour chaque cas d’erreur.

---

**Astuce** : Testez chaque exemple pour bien comprendre le comportement des exceptions !
