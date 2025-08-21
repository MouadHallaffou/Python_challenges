# Challenge 4.1 - Classes et objets
# Votre code ici...
# challenge A:
# Créer une classe `Personne` et manipuler ses instances
class Personne :
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    def afficher_info(self): # Méthode publique
        print(f"Nom: {self.__nom}, Age: {self.__age}")

    def _get_nom(self): # Utilisation d'un underscore pour indiquer que c'est une méthode protégée
        return f"je m'appelle: {self.__nom}"

    def __get_age(self): # Utilisation de deux underscores pour indiquer que c'est une méthode privée
        return "je suis age de: " + str(self.__age)

personne1 = Personne("Mouad", 25)
personne1.afficher_info()
print(personne1._get_nom())
print(personne1._Personne__get_age()) # Utilisation de la méthode privée 

# challenge B:
# Gérer un compte bancaire avec des attributs privés et validation.
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0): 
        self.__titulaire = titulaire
        self.__solde = solde_initial

    def deposer(self, titulaire, montant):
        if titulaire != self.__titulaire:
            print("Titulaire incorrect.")
            return 
        if montant > 0:
            self.__solde += montant
            print(f"Dépôt de {montant} effectué.")
        else:
            print("Montant invalide.")

    def retirer(self, titulaire, montant):
        if titulaire != self.__titulaire:
            print("Titulaire incorrect.")
            return
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué.")
        else:
            if montant <= 0:
                print("Montant invalide.")
            else:
                print("votre solde est insuffisant.")

    def afficher_solde(self):
        print(f"Solde de {self.__titulaire}: {self.__solde}")

compte1 = CompteBancaire("Alice", 1000)
compte1.afficher_solde()
compte1.deposer("Alice", 500) # Dépôt de 500 effectué.
compte1.retirer("Mouad", 200) # Titulaire incorrect.
compte1.retirer("Alice", 2200) # votre solde est insuffisant.
compte1.afficher_solde() # Solde de Alice: 1300

# Challenge C:
#  Utiliser les méthodes spéciales pour une classe `Produit`.
class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def __str__(self):
        return f"Produit: {self.__nom}, Prix: {self.__prix}"

    def __eq__(self, autre):
        if isinstance(autre, Produit):
            return self.__nom == autre.__nom and self.__prix == autre.__prix
        return False

produit1 = Produit("Laptop", 1200)
produit2 = Produit("Laptop", 1200)
produit3 = Produit("Smartphone", 800)

print(produit1)  # Utilise __str__
print(produit1 == produit2)  # Utilise __eq__
print(produit1 == produit3)  # Utilise __eq__

# Challenge D:
# Créer un système de gestion de bibliothèque.
class Livre: 
    catalogue = []  # Attribut de classe pour stocker tous les livres

    def __init__(self, titre, auteur, annee, prix, quantite):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee = annee
        self.__prix = prix
        self.__quantite = quantite

    def __ajouter_au_catalogue(self):
        Livre.catalogue.append(self)

    def __vendre(self, quantite):
        if quantite > self.__quantite:
            print("Quantité demandée supérieure à la quantité en stock.")
        else:
            self.__quantite -= quantite
            if self.__quantite == 0:
                Livre.catalogue.remove(self)
            print(f"{quantite} exemplaires de '{self.__titre}' vendus.")

    def __edit_quantite(self, nouvelle_quantite):
        self.__quantite = nouvelle_quantite

    def __edit_prix(self, nouveau_prix):
        self.__prix = nouveau_prix

    def __delete_livre(self, titre):
        for livre in Livre.catalogue:
            if livre.__titre == titre:
                Livre.catalogue.remove(livre) and livre.__quantite == 0 
                break

    def afficher_info(self):
            print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Année: {self.__annee}, Prix: {self.__prix}, Quantité: {self.__quantite}")

    def afficher_catalogue(cls):
        for livre in cls.catalogue:
            livre.afficher_info()
    

    
livre1 = Livre("1984", "George Orwell", 1949, 9.99, 5)
livre1._Livre__ajouter_au_catalogue()
livre1.afficher_info()
livre1._Livre__vendre(2)
livre1._Livre__edit_quantite(10)
livre1._Livre__edit_prix(8.99)
livre1.afficher_info()


livre2 = Livre("Brave New World", "Aldous Huxley", 1932, 12.99, 3)
livre2._Livre__ajouter_au_catalogue()
livre2.afficher_info()
livre2._Livre__vendre(4) # Quantité demandée supérieure à la quantité en stock.
livre2._Livre__edit_quantite(5)
livre2._Livre__edit_prix(11.99)
livre2.afficher_info() 
