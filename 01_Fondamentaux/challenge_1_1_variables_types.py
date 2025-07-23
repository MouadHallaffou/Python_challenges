# Challenge 1.1 - Variables et Types de Données
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Déclaration de variables
# Votre code ici...
nom = "mouad"
age = 25
taille = 1.75
is_student = True
print(type(nom), type(age), type(taille), type(is_student))

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
puissance = a**b  # a élevé à la puissance b
print(
    "Somme:",
    somme,
    "Différence:",
    difference,
    "Produit:",
    produit,
    "Quotient:",
    quotient,
    "Division entière:",
    div_entiere,
    "Reste de la division:",
    div_reste,
    "Puissance:",
    puissance,
)

# Challenge C - Manipulation de chaînes
# Votre code ici...
prenom = "mouad"  # Correction: prenom au lieu de nom
nom_famille = "hallaffou"  # Correction: nom_famille au lieu de prenom
nom_complet = prenom + " " + nom_famille  # Correction: ordre logique
maj = nom_complet.upper()
mns = nom_complet.lower()
longueur = len(
    nom_complet
)  # Correction: éviter conflit avec variable taille du Challenge A
trois_char = nom_complet[:3]
print("Nom complet:", nom_complet)
print("Majuscules:", maj)
print("Minuscules:", mns)
print("Longueur:", longueur)
print("Trois premiers caractères:", trois_char)

# Challenge D - Conversion de types
# Votre code ici...
print("=" * 10, "Saisir votre âge:", "=" * 10)
while True:
    try:
        age_input = int(input("Saisir votre âge : "))
        annee_de_naissance = 2025 - age_input
        print(f"Vous êtes né(e) en : {annee_de_naissance}")
        break
    except ValueError:
        print("Entrez votre âge correctement sous forme d'un nombre (ex: 25)")

# Challenge E - Opérateurs de comparaison
# Votre code ici...
print("=" * 10, "Devinez un nombre entre 1 et 10:", "=" * 10)

try:
    nombre_user = int(input("Entrez le nombre ici : "))
    nombre_secret = 7  # Comme demandé dans l'énoncé

    # Comparaison avec le nombre secret
    if nombre_user == nombre_secret:
        print("🎉 Félicitations ! Vous avez trouvé le nombre secret !")
    elif nombre_user > nombre_secret:
        print(f"❌ Votre nombre ({nombre_user}) est plus grand que le nombre secret.")
    else:
        print(f"❌ Votre nombre ({nombre_user}) est plus petit que le nombre secret.")

    # Vérification pair/impair
    if nombre_user % 2 == 0:
        print(f"ℹ️  Votre nombre {nombre_user} est pair.")
    else:
        print(f"ℹ️  Votre nombre {nombre_user} est impair.")

    print(f"💡 Le nombre secret était : {nombre_secret}")

except ValueError:
    print("❌ Veuillez entrer un nombre valide !")
