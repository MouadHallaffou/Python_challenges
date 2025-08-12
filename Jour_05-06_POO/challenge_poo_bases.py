# Challenge Jour 5 - Bases de la POO
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Première Classe (45min)
# =============================================================================

print("=== PARTIE A - Première Classe ===")


# 1. Classe Personne simple
class Personne:
    def __init__(self, nom, age):
        """Constructeur de la classe Personne"""
        self.nom = nom
        self.age = age

    def se_presenter(self):
        """Méthode pour se présenter"""
        return f"Bonjour, je suis {self.nom} et j'ai {self.age} ans"

    def avoir_anniversaire(self):
        """Méthode pour vieillir d'un an"""
        self.age += 1
        return f"Joyeux anniversaire ! J'ai maintenant {self.age} ans"


# Tests de la classe Personne
print("1. Test classe Personne :")
personne1 = Personne("Alice", 25)
personne2 = Personne("Bob", 30)

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne1.avoir_anniversaire())

# =============================================================================
# PARTIE B - Classe avec Validation (45min)
# =============================================================================

print("\n=== PARTIE B - Classe avec Validation ===")


class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        """Constructeur du compte bancaire"""
        self.titulaire = titulaire
        self.__solde = solde_initial  # Attribut privé
        self.__historique = []
        self.__ajouter_transaction("Ouverture du compte", solde_initial)

    def __ajouter_transaction(self, type_operation, montant):
        """Méthode privée pour ajouter une transaction à l'historique"""
        import datetime

        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": type_operation,
            "montant": montant,
            "solde_apres": self.__solde,
        }
        self.__historique.append(transaction)

    def deposer(self, montant):
        """Déposer de l'argent sur le compte"""
        if montant <= 0:
            return "❌ Le montant doit être positif"

        self.__solde += montant
        self.__ajouter_transaction("Dépôt", montant)
        return f"✅ Dépôt de {montant}€ effectué. Nouveau solde: {self.__solde}€"

    def retirer(self, montant):
        """Retirer de l'argent du compte"""
        if montant <= 0:
            return "❌ Le montant doit être positif"

        if montant > self.__solde:
            return f"❌ Solde insuffisant. Solde actuel: {self.__solde}€"

        self.__solde -= montant
        self.__ajouter_transaction("Retrait", -montant)
        return f"✅ Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€"

    def consulter_solde(self):
        """Consulter le solde du compte"""
        return f"💰 Solde actuel: {self.__solde}€"

    def afficher_historique(self):
        """Afficher l'historique des transactions"""
        print(f"\n📊 Historique du compte de {self.titulaire}:")
        print("-" * 60)
        for transaction in self.__historique:
            print(
                f"{transaction['date']} | {transaction['operation']:15} | "
                f"{transaction['montant']:8.2f}€ | Solde: {transaction['solde_apres']:8.2f}€"
            )

    def __str__(self):
        """Représentation string du compte"""
        return f"Compte de {self.titulaire} - Solde: {self.__solde}€"


# Tests de la classe CompteBancaire
print("2. Test classe CompteBancaire :")
compte = CompteBancaire("Alice Dupont", 1000)
print(compte)
print(compte.consulter_solde())
print(compte.deposer(500))
print(compte.retirer(200))
print(compte.retirer(2000))  # Test solde insuffisant
compte.afficher_historique()

# =============================================================================
# PARTIE C - Classe avec Properties (45min)
# =============================================================================

print("\n=== PARTIE C - Classe avec Properties ===")


class Produit:
    def __init__(self, nom, prix, stock=0):
        """Constructeur du produit"""
        self._nom = nom
        self._prix = prix
        self._stock = stock

    @property
    def nom(self):
        """Getter pour le nom"""
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        """Setter pour le nom avec validation"""
        if not nouveau_nom or not isinstance(nouveau_nom, str):
            raise ValueError("Le nom doit être une chaîne non vide")
        self._nom = nouveau_nom.strip().title()

    @property
    def prix(self):
        """Getter pour le prix"""
        return self._prix

    @prix.setter
    def prix(self, nouveau_prix):
        """Setter pour le prix avec validation"""
        if nouveau_prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self._prix = nouveau_prix

    @property
    def stock(self):
        """Getter pour le stock"""
        return self._stock

    @stock.setter
    def stock(self, nouveau_stock):
        """Setter pour le stock avec validation"""
        if nouveau_stock < 0:
            raise ValueError("Le stock ne peut pas être négatif")
        self._stock = nouveau_stock

    @property
    def valeur_stock(self):
        """Propriété calculée : valeur totale du stock"""
        return self._prix * self._stock

    @property
    def disponible(self):
        """Propriété calculée : produit disponible ou non"""
        return self._stock > 0

    def ajouter_stock(self, quantite):
        """Ajouter du stock"""
        if quantite <= 0:
            raise ValueError("La quantité à ajouter doit être positive")
        self._stock += quantite
        return f"✅ Stock ajouté. Nouveau stock: {self._stock}"

    def vendre(self, quantite):
        """Vendre une quantité du produit"""
        if quantite <= 0:
            raise ValueError("La quantité à vendre doit être positive")
        if quantite > self._stock:
            raise ValueError(f"Stock insuffisant. Stock disponible: {self._stock}")

        self._stock -= quantite
        total = quantite * self._prix
        return f"✅ Vente effectuée: {quantite} unités pour {total}€. Stock restant: {self._stock}"

    def __str__(self):
        """Représentation string du produit"""
        statut = "✅ Disponible" if self.disponible else "❌ Rupture de stock"
        return f"{self.nom} - {self.prix}€ - Stock: {self.stock} - {statut}"

    def __repr__(self):
        """Représentation pour debugging"""
        return f"Produit('{self.nom}', {self.prix}, {self.stock})"


# Tests de la classe Produit
print("3. Test classe Produit :")
produit = Produit("ordinateur portable", 899.99, 10)
print(produit)
print(f"Valeur du stock: {produit.valeur_stock}€")
print(f"Disponible: {produit.disponible}")

# Test des setters avec validation
try:
    produit.prix = -100  # Doit lever une erreur
except ValueError as e:
    print(f"Erreur attendue: {e}")

print(produit.vendre(3))
print(produit.ajouter_stock(5))
print(produit)

# =============================================================================
# PARTIE D - Méthodes de Classe et Statiques (30min)
# =============================================================================

print("\n=== PARTIE D - Méthodes de Classe et Statiques ===")


class Voiture:
    # Attribut de classe
    nombre_voitures = 0
    marques_autorisees = ["Peugeot", "Renault", "Citroën", "Toyota", "Honda"]

    def __init__(self, marque, modele, annee):
        """Constructeur de la voiture"""
        if not self.marque_valide(marque):
            raise ValueError(
                f"Marque non autorisée. Marques autorisées: {', '.join(self.marques_autorisees)}"
            )

        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0

        # Incrémenter le compteur de voitures
        Voiture.nombre_voitures += 1

    @staticmethod
    def marque_valide(marque):
        """Méthode statique pour valider une marque"""
        return marque in Voiture.marques_autorisees

    @classmethod
    def creer_voiture_occasion(cls, marque, modele, annee, kilometrage):
        """Méthode de classe pour créer une voiture d'occasion"""
        voiture = cls(marque, modele, annee)
        voiture.kilometrage = kilometrage
        return voiture

    @classmethod
    def get_nombre_voitures(cls):
        """Méthode de classe pour obtenir le nombre total de voitures"""
        return cls.nombre_voitures

    @classmethod
    def ajouter_marque(cls, nouvelle_marque):
        """Méthode de classe pour ajouter une marque autorisée"""
        if nouvelle_marque not in cls.marques_autorisees:
            cls.marques_autorisees.append(nouvelle_marque)
            return f"✅ Marque '{nouvelle_marque}' ajoutée"
        return f"❌ Marque '{nouvelle_marque}' déjà autorisée"

    def rouler(self, distance):
        """Faire rouler la voiture"""
        self.kilometrage += distance
        return f"🚗 {self.marque} {self.modele} a roulé {distance}km. Kilométrage total: {self.kilometrage}km"

    @property
    def age(self):
        """Propriété calculée : âge de la voiture"""
        import datetime

        return datetime.datetime.now().year - self.annee

    def __str__(self):
        """Représentation string de la voiture"""
        return f"{self.marque} {self.modele} ({self.annee}) - {self.kilometrage}km - {self.age} ans"


# Tests de la classe Voiture
print("4. Test classe Voiture :")
print(f"Marques autorisées: {Voiture.marques_autorisees}")
print(f"Nombre de voitures créées: {Voiture.get_nombre_voitures()}")

voiture1 = Voiture("Peugeot", "308", 2020)
voiture2 = Voiture.creer_voiture_occasion("Renault", "Clio", 2018, 45000)

print(voiture1)
print(voiture2)
print(voiture1.rouler(150))
print(f"Nombre total de voitures: {Voiture.get_nombre_voitures()}")

# Test ajout de marque
print(Voiture.ajouter_marque("BMW"))
voiture3 = Voiture("BMW", "X3", 2022)
print(voiture3)

# =============================================================================
# MINI-PROJET - Bibliothèque (45min)
# =============================================================================

print("\n=== MINI-PROJET - Bibliothèque ===")


class Livre:
    def __init__(self, titre, auteur, isbn, nombre_pages):
        """Constructeur du livre"""
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nombre_pages = nombre_pages
        self.emprunte = False
        self.emprunteur = None
        self.date_emprunt = None

    def emprunter(self, nom_emprunteur):
        """Emprunter le livre"""
        if self.emprunte:
            return f"❌ Le livre '{self.titre}' est déjà emprunté par {self.emprunteur}"

        self.emprunte = True
        self.emprunteur = nom_emprunteur
        import datetime

        self.date_emprunt = datetime.datetime.now()
        return f"✅ Livre '{self.titre}' emprunté par {nom_emprunteur}"

    def retourner(self):
        """Retourner le livre"""
        if not self.emprunte:
            return f"❌ Le livre '{self.titre}' n'est pas emprunté"

        emprunteur = self.emprunteur
        self.emprunte = False
        self.emprunteur = None
        self.date_emprunt = None
        return f"✅ Livre '{self.titre}' retourné par {emprunteur}"

    @property
    def statut(self):
        """Propriété pour le statut du livre"""
        if self.emprunte:
            import datetime

            duree = (datetime.datetime.now() - self.date_emprunt).days
            return f"Emprunté par {self.emprunteur} depuis {duree} jours"
        return "Disponible"

    def __str__(self):
        """Représentation string du livre"""
        return f"'{self.titre}' par {self.auteur} - {self.statut}"


class Bibliotheque:
    def __init__(self, nom):
        """Constructeur de la bibliothèque"""
        self.nom = nom
        self.livres = []
        self.membres = set()

    def ajouter_livre(self, livre):
        """Ajouter un livre à la bibliothèque"""
        self.livres.append(livre)
        return f"✅ Livre '{livre.titre}' ajouté à la bibliothèque"

    def ajouter_membre(self, nom):
        """Ajouter un membre à la bibliothèque"""
        if nom in self.membres:
            return f"❌ {nom} est déjà membre"
        self.membres.add(nom)
        return f"✅ {nom} ajouté comme membre"

    def chercher_livre(self, titre):
        """Chercher un livre par titre"""
        for livre in self.livres:
            if titre.lower() in livre.titre.lower():
                return livre
        return None

    def emprunter_livre(self, titre, emprunteur):
        """Emprunter un livre"""
        if emprunteur not in self.membres:
            return f"❌ {emprunteur} n'est pas membre de la bibliothèque"

        livre = self.chercher_livre(titre)
        if not livre:
            return f"❌ Livre '{titre}' non trouvé"

        return livre.emprunter(emprunteur)

    def retourner_livre(self, titre):
        """Retourner un livre"""
        livre = self.chercher_livre(titre)
        if not livre:
            return f"❌ Livre '{titre}' non trouvé"

        return livre.retourner()

    def livres_disponibles(self):
        """Lister les livres disponibles"""
        disponibles = [livre for livre in self.livres if not livre.emprunte]
        return disponibles

    def livres_empruntes(self):
        """Lister les livres empruntés"""
        empruntes = [livre for livre in self.livres if livre.emprunte]
        return empruntes

    def afficher_catalogue(self):
        """Afficher tout le catalogue"""
        print(f"\n📚 Catalogue de la bibliothèque {self.nom}:")
        print("-" * 60)
        if not self.livres:
            print("Aucun livre dans la bibliothèque")
        else:
            for i, livre in enumerate(self.livres, 1):
                print(f"{i:2d}. {livre}")

    def afficher_statistiques(self):
        """Afficher les statistiques de la bibliothèque"""
        total = len(self.livres)
        disponibles = len(self.livres_disponibles())
        empruntes = len(self.livres_empruntes())

        print(f"\n📊 Statistiques de {self.nom}:")
        print(f"Total de livres: {total}")
        print(f"Livres disponibles: {disponibles}")
        print(f"Livres empruntés: {empruntes}")
        print(f"Membres inscrits: {len(self.membres)}")


# Tests du système de bibliothèque
print("5. Test système de bibliothèque :")

# Création de la bibliothèque
biblio = Bibliotheque("Bibliothèque Municipale")

# Ajout de livres
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789", 96)
livre2 = Livre("1984", "George Orwell", "987654321", 328)
livre3 = Livre("Les Misérables", "Victor Hugo", "456789123", 1232)

print(biblio.ajouter_livre(livre1))
print(biblio.ajouter_livre(livre2))
print(biblio.ajouter_livre(livre3))

# Ajout de membres
print(biblio.ajouter_membre("Alice"))
print(biblio.ajouter_membre("Bob"))
print(biblio.ajouter_membre("Charlie"))

# Test d'emprunt
print(biblio.emprunter_livre("1984", "Alice"))
print(biblio.emprunter_livre("Le Petit Prince", "Bob"))

# Affichage du catalogue
biblio.afficher_catalogue()
biblio.afficher_statistiques()

# Test de retour
print(biblio.retourner_livre("1984"))
biblio.afficher_statistiques()

# =============================================================================
# EXERCICES PRATIQUES
# =============================================================================

print("\n=== EXERCICES PRATIQUES ===")


# Exercice 1: Créez une classe Rectangle
class Rectangle:
    def __init__(self, longueur, largeur):
        """TODO: Initialisez longueur et largeur avec validation (>0)"""
        pass

    @property
    def aire(self):
        """TODO: Calculez et retournez l'aire"""
        pass

    @property
    def perimetre(self):
        """TODO: Calculez et retournez le périmètre"""
        pass

    def est_carre(self):
        """TODO: Retournez True si c'est un carré"""
        pass


# Exercice 2: Créez une classe Etudiant
class Etudiant:
    def __init__(self, nom, prenom, numero_etudiant):
        """TODO: Initialisez les attributs"""
        pass

    def ajouter_note(self, matiere, note):
        """TODO: Ajoutez une note dans une matière (note entre 0 et 20)"""
        pass

    def calculer_moyenne(self):
        """TODO: Calculez la moyenne générale"""
        pass

    def obtenir_mention(self):
        """TODO: Retournez la mention selon la moyenne"""
        # Passable: 10-12, Assez bien: 12-14, Bien: 14-16, Très bien: 16+
        pass


print("🎯 Complétez les exercices ci-dessus !")
print("⏭️ Passez ensuite au challenge POO avancée !")
