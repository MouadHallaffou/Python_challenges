# Challenge 1.4 - Fonctions
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Fonctions simples
# Votre code ici...
# - `saluer(nom)` : affiche "Bonjour [nom] !"
def saluer(nom:str="user"):
    print("bonsoir",nom)
saluer("mouad")
saluer()
# - `additionner(a, b)` : retourne la somme de a et b
def addition(a,b):
    return  a + b
print(addition(1,2)) 
# - `est_pair(nombre)` : retourne True si le nombre est pair
def est_pair(number):
    if number%2==0 and number!=0:
        return True
    else:
        return False
print(est_pair(0))
# - `calculer_aire_rectangle(longueur, largeur)` : retourne l'aire
longueur  = float(input("entre la longueur ici : "))
largeur  = float(input("entre la largeur ici : "))
def aire_rectangle(longueur, largeur):
    aire:float = round((longueur*largeur)/2,2)
    print(aire, "cm²")
aire_rectangle(longueur, largeur)

# Challenge B - Fonctions avec validation
# Votre code ici...
# - `diviser(a, b)` : division sécurisée (gérer division par zéro)
def devision(a,b):
    if b!=0:
        print(round(a/b, 2))
    else:
        print("n'a pas devise sur zero!!")
devision(2,3)
# - `age_en_jours(age_annees)` : convertit l'âge en jours (approximation)
def convertir_age(age_annee):
    return age_annee*365
print(convertir_age(25), "jours")
# - `note_en_lettre(note)` : convertit une note (0-20) en lettre (A, B, C, D, F)
def note_en_lettre(note):
    if note>=16 and note <=20:
        print("A")
    elif note>=10 and note <=15:
        print("B")
    elif note>=8 and note <=9:
        print("C")
    elif note>=5 and note <=7:
        print("D")
    else:
        print("F")
note_en_lettre(15)
# - `temperature_celsius_fahrenheit(celsius)` : convertit les températures
def temperature_celsius_fahrenheit(temperature, unite="C"):
    if unite == "C":
        return (temperature * 9/5) + 32
    elif unite == "F":
        return (temperature - 32) * 5/9
    else:
        return "Unité inconnue"
print(temperature_celsius_fahrenheit(25, "C"))
print(temperature_celsius_fahrenheit(77, "F"))
# Challenge C - Fonctions avec arguments par défaut
# Votre code ici...
# - `present_personne(nom, age=0, ville="Inconnue")` : présente une personne
def present_personne(nom, age=0, ville="Inconnue"):
    return f"bonjour {nom}, votre age est de {age} ans, vous etes habite à {ville}"
print(present_personne("mouad", 25, "casablanca"))
print(present_personne("mouad", 25))
print(present_personne("mouad"))
# - `calculer_prix_ttc(prix_ht, taux_tva=20)` : calcule le prix TTC
def calculer_prix_ttc(prix_ht, taux_tva=20):
    return round(prix_ht * (1 + taux_tva / 100), 2)
print(calculer_prix_ttc(100))  # Prix HT de 100€ avec TVA par défaut
print(calculer_prix_ttc(100, 10))  # Prix HT de 100€ avec TVA de 10%
# - `generer_mot_de_passe(longueur=8, inclure_chiffres=True, inclure_majuscules=True)`
import random
import string
def generer_mot_de_passe(longueur=8, inclure_chiffres=True, inclure_majuscules=True):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    if inclure_chiffres:
        caracteres += "0123456789"
    if inclure_majuscules:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(caracteres) for _ in range(longueur))
print(generer_mot_de_passe())  # Mot de passe par défaut
# - `afficher_menu(titre, options, separator="*")` : affiche un joli menu
def afficher_menu(titre, options, separator="*"):
    print(separator * 10)
    print(titre)
    print(separator * 10)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print(separator * 10) 
afficher_menu("Menu Principal", ["Option 1", "Option 2", "Quitter"])

# Challenge D - Fonctions avancées
# Votre code ici...
# - `fibonacci(n)` : retourne le nième nombre de Fibonacci  
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))  # Affiche le 8ème nombre de Fibonacci
# - `est_premier(nombre)` : vérifie si un nombre est premier  
def est_premier(nombre):
    """
    Un nombre premier est un entier naturel supérieur à 1
    qui n'a que deux diviseurs : 1 et lui-même.
    Cette fonction retourne True si 'nombre' est premier, sinon False.
    """
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True 
print(est_premier(7))  # Affiche True pour 7 
# - `compter_mots(texte)` : compte les mots dans un texte
def compter_mots(texte):
    mots = texte.split()
    mots_nettoyes = [mot.strip(string.punctuation) for mot in mots if mot.strip(string.punctuation) and not mot.strip(string.punctuation).isdigit()]
    return len(mots_nettoyes)
print(compter_mots("Bonjour, comment ça va ?"))  # Affiche 4
# - `inverser_mots(phrase)` : inverse l'ordre des mots dans une phrase
def inverser_mots(phrase):
    mots = phrase.split()
    mots_inverses = mots[::-1]
    return " ".join(mots_inverses)
print(inverser_mots("Bonjour, comment ça va ?"))  # Affiche "? va ça comment Bonjour,"
# Challenge E - Mini-projet avec fonctions
# Votre code ici...
# - `menu_principal()` : affiche le menu et gère les choix
# - `addition(a, b)`, `soustraction(a, b)`, `multiplication(a, b)`, `division(a, b)`
# - `puissance(base, exposant)`, `racine_carree(nombre)`
# - `factorielle(n)`, `pourcentage(valeur, total)`
# - `historique` : stocke les derniers calculs
# - `afficher_historique()` : montre les derniers calculs
# - Le programme doit tourner en boucle jusqu'à ce que l'utilisateur quitte
# - Sauvegarde de l'historique dans un fichier
# - Fonctions trigonométriques (sin, cos, tan)
# - Gestion des erreurs pour toutes les opérations
print("*"*30)
print("*"*30)
print("Bienvenue dans votre calculatrice")
print("*"*30)
print("*"*30)
print("=="*3 , " Menu Principal", "=="*3)
print("1️⃣   Addition")
print("2️⃣   Soustraction")
print("3️⃣   Multiplication")
print("4️⃣   Division")
print("5️⃣   Puissance")
print("6️⃣   Racine carrée")
print("7️⃣   Factorielle")
print("8️⃣   Pourcentage")
print("9️⃣   Afficher l'historique")
print("0️⃣   Quitter")
def addition(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro impossible"
    return a / b
def puissance(base, exposant):
    return base ** exposant
def racine_carree(nombre):
    if nombre < 0:
        return "Erreur: Racine carrée d'un nombre négatif"
    return nombre ** 0.5
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)
def pourcentage(valeur, total):
    if total == 0:
        return "Erreur: Division par zéro impossible"
    return (valeur / total) * 100
    
historique = []
def afficher_historique():
    print("*" * 30)
    print("Historique des calculs:")
    print("*" * 30)
    for calcul in historique:
        print(calcul)
    print("*" * 30)

while True:
    choix = input("Choisissez une option: ")
    if choix == "1":
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
        resultat = addition(a, b)
        print(f"Résultat: {resultat}")
        historique.append(f"Addition: {a} + {b} = {resultat}")
    elif choix == "2":
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
        resultat = soustraction(a, b)
        print(f"Résultat: {resultat}")
        historique.append(f"Soustraction: {a} - {b} = {resultat}")
    elif choix == "3":
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
        resultat = multiplication(a, b)
        print(f"Résultat: {resultat}")
        historique.append(f"Multiplication: {a} * {b} = {resultat}")
    elif choix == "4":
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
        resultat = division(a, b)
        print(f"Résultat: {resultat}")
        historique.append(f"Division: {a} / {b} = {resultat}")
    elif choix == "5":
        base = float(input("Entrez la base: "))
        exposant = float(input("Entrez l'exposant: "))
        resultat = puissance(base, exposant)
        print(f"Résultat: {resultat}")
        historique.append(f"Puissance: {base} ^ {exposant} = {resultat}")
    elif choix == "6":
        nombre = float(input("Entrez un nombre: "))
        resultat = racine_carree(nombre)
        print(f"Résultat: {resultat}")
        historique.append(f"Racine carrée: √{nombre} = {resultat}")
    elif choix == "7":
        n = int(input("Entrez un nombre entier: "))
        resultat = factorielle(n)
        print(f"Résultat: {resultat}")
        historique.append(f"Factorielle: {n}! = {resultat}")
    elif choix == "8":
        valeur = float(input("Entrez la valeur: "))
        total = float(input("Entrez le total: "))
        resultat = pourcentage(valeur, total)
        print(f"Résultat: {resultat}")
        historique.append(f"Pourcentage: {valeur} / {total} = {resultat}")
    elif choix == "9":
        afficher_historique()
    elif choix == "0":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
