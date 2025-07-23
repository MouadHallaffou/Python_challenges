# Challenge 1.1 - Variables et Types de Données
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Déclaration de variables
# Votre code ici...
nom = "mouad"
age = 25
taille = 1.75
is_student = True
print(type(nom),type(age),type(taille),type(is_student))

# Challenge B - Calculs simples
# Votre code ici...
a = 10
b = 3
somme = a + b
difference = a - b
produit = a * b
quotient = a / b
div_entiere = a // b
div_reste = a % b
print("Somme:", somme, "Différence:", difference, "Produit:", produit, "Quotient:", quotient, "Division entière:", div_entiere, "Reste de la division:", div_reste)

# Challenge C - Manipulation de chaînes
# Votre code ici...
nom = "mouad"
prenom = "hallaffou"
nom_complete = nom + " " + prenom 
maj = nom_complete.upper()
mns = nom_complete.lower()
taille = len(nom_complete)
trois_char = nom_complete[:3]
print(nom_complete, maj, mns, taille, trois_char)

# Challenge D - Conversion de types
# Votre code ici...
# print("="*10, "saisir votre age:", "="*10)
# while True:
#     try:
#         age = int(input("saisir votre age : "))
#         annee_de_naissance = 2025 - age
#         print("vous tes  ne(e) en :", annee_de_naissance, "\ngood by")
#         break
#     except ValueError:
#         print("Entrez votre âge correctement sous forme d'un nombre ex: 10")

# Challenge E - Opérateurs de comparaison
# Votre code ici...
print("="*10, "saisir un numbre entre 1 et 10:", "="*10)
numbre_user = int(input("entre le numbre aleatoire ici :"))
numbre_secret = 5
if(numbre_user == numbre_secret and numbre_user%2 == 0) : 
    print("tres bien, votre number est pair")
elif(numbre_user == numbre_secret and numbre_user%2 != 0) : 
    print("tres bien, votre number est impair")
elif(numbre_user > numbre_secret and numbre_user%2 == 0):
    print("vous etes entre un numbre grande que le numbre de secret qui est :", numbre_secret, "votre number est pair")
elif(numbre_user > numbre_secret and numbre_user%2 != 0):
    print("vous etes entre un numbre grande que le numbre de secret qui est :", numbre_secret, "votre number est impair")
elif(numbre_user%2 == 0):
    print("vous etes entre un numbre petite que le numbre de secret qui est :", numbre_secret, "votre number est pair")
else:
    print("vous etes entre un numbre petite que le numbre de secret qui est :", numbre_secret, "votre number est impair")