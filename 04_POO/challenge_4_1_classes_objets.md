# 🎯 Challenge 4.1 : Classes et Objets - Introduction à la POO

## 📚 Objectif
Comprendre les concepts fondamentaux de la Programmation Orientée Objet (POO) en Python à travers des exemples concrets.

## 🔧 Ce que vous devez apprendre

### 1. Définition de classes avec `class`
```python
class Personne:
    pass  # Une classe vide pour commencer
```

### 2. Méthode `__init__` (constructeur)
```python
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
```

### 3. Attributs d'instance et de classe
```python
class Personne:
    espece = "Humain"  # Attribut de classe
    def __init__(self, nom):
        self.nom = nom  # Attribut d'instance
```

### 4. Méthodes d'instance
```python
class Personne:
    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom}")
```

### 5. Encapsulation et attributs privés
```python
class CompteBancaire:
    def __init__(self, numero, solde):
        self.__numero = numero      # Attribut privé
        self.__solde = solde        # Attribut privé
```

### 6. Méthodes spéciales (`__str__`, `__repr__`)
```python
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} coûte {self.prix}€"

    def __repr__(self):
        return f"Produit('{self.nom}', {self.prix})"
```

---

## 💪 Challenges avec exemples

### Challenge A - Première classe (Facile)

**Objectif :** Créer une classe `Personne` et manipuler ses instances.

```python
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans, mon email est {self.email}")

    def avoir_anniversaire(self):
        self.age += 1
        print(f"Joyeux anniversaire {self.nom} ! Tu as maintenant {self.age} ans.")

# Exemple d'utilisation
alice = Personne("Alice", 30, "alice@email.com")
bob = Personne("Bob", 25, "bob@email.com")

alice.se_presenter()
bob.se_presenter()
alice.avoir_anniversaire()
```

---

### Challenge B - Classe avec validation (Moyen)

**Objectif :** Gérer un compte bancaire avec des attributs privés et validation.

```python
class CompteBancaire:
    def __init__(self, numero_compte, solde, titulaire):
        self.__numero_compte = numero_compte
        self.__solde = solde
        self.__titulaire = titulaire

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if montant > self.__solde:
            print("Solde insuffisant !")
        else:
            self.__solde -= montant

    def consulter_solde(self):
        print(f"Solde du compte {self.__numero_compte}: {self.__solde}€")

# Exemple d'utilisation
compte = CompteBancaire("123ABC", 100, "Alice")
compte.deposer(50)
compte.retirer(200)  # Affiche "Solde insuffisant !"
compte.consulter_solde()
```

---

### Challenge C - Méthodes spéciales (Moyen)

**Objectif :** Utiliser les méthodes spéciales pour une classe `Produit`.

```python
class Produit:
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def __str__(self):
        return f"{self.nom} ({self.stock} en stock) - {self.prix}€"

    def __repr__(self):
        return f"Produit('{self.nom}', {self.prix}, {self.stock})"

    def __eq__(self, other):
        return self.nom == other.nom and self.prix == other.prix

    def valeur_totale(self):
        return self.prix * self.stock

# Exemple d'utilisation
p1 = Produit("Livre", 15, 10)
p2 = Produit("Livre", 15, 5)
print(p1)  # Affiche: Livre (10 en stock) - 15€
print(repr(p1))
print(p1 == p2)  # True
print("Valeur totale:", p1.valeur_totale())
```

---

### Challenge D - Projet complet POO (Difficile)

**Objectif :** Créer un système de gestion de bibliothèque.

```python
class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

class Membre:
    def __init__(self, nom, numero_membre):
        self.nom = nom
        self.numero_membre = numero_membre
        self.livres_empruntes = []

class Bibliotheque:
    def __init__(self):
        self.catalogue = []
        self.membres = []

    def ajouter_livre(self, livre):
        self.catalogue.append(livre)

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def emprunter(self, numero_membre, isbn):
        membre = next((m for m in self.membres if m.numero_membre == numero_membre), None)
        livre = next((l for l in self.catalogue if l.isbn == isbn and l.disponible), None)
        if membre and livre:
            livre.disponible = False
            membre.livres_empruntes.append(livre)
            print(f"{membre.nom} a emprunté {livre.titre}")
        else:
            print("Emprunt impossible.")

    def rendre(self, numero_membre, isbn):
        membre = next((m for m in self.membres if m.numero_membre == numero_membre), None)
        if membre:
            livre = next((l for l in membre.livres_empruntes if l.isbn == isbn), None)
            if livre:
                livre.disponible = True
                membre.livres_empruntes.remove(livre)
                print(f"{membre.nom} a rendu {livre.titre}")

# Exemple d'utilisation
biblio = Bibliotheque()
livre1 = Livre("1984", "George Orwell", "123")
membre1 = Membre("Alice", "001")
biblio.ajouter_livre(livre1)
biblio.ajouter_membre(membre1)
biblio.emprunter("001", "123")
biblio.rendre("001", "123")
```

---

**N'hésitez pas à modifier les exemples et à expérimenter pour mieux comprendre la POO !**
