# Challenge 1.2 - Structures de Contrôle
# Écrivez votre code ici pour résoudre les challenges A, B, C, D et E

# Challenge A - Conditions simples
# Votre code ici...

print("="*10, "test de l'age:", "="*10)
while True :
    try : 
        age = int(input("entre votre age ici: "))
        if (age == 0) : 
            print("zero ce ni pas une corecte value!!")
        elif (age < 18 ) :
            print("vous etes Mineur")
        else : 
            print("vous etes Majeur")
        break
    except ValueError :
        print('il faut entre un age corecte , sous forme de numbre!!')

# Challenge B - Conditions multiples
# Votre code ici...
print("="*10, "test de la note:", "="*10)
while True:
    try:
        note = float(input("entre la note ici (entre 0 et 20): "))
        if note < 0 or note > 20:
            print("La note doit être entre 0 et 20.")
            continue
        if note >= 16:
            print("Très bien")
        elif note >= 14:
            print("Bien")
        elif note >= 12:
            print("Assez bien")
        elif note >= 10:
            print("Passable")
        else:
            print("Insuffisant")
        break
    except ValueError:
        print("La note doit être un nombre entre 0 et 20.")

# Challenge C - Opérateurs logiques
# Votre code ici...
print("="*10, "test du club:", "="*10)
while True : 
    try : 
        age = int(input("entre votre age ici : "))
        if age >=18 and age < 21:
            carte = str(input("entre la carte de votre numbre: "))
            if carte :
                print("Accès autorisé")
                break
            else : 
                print("entre une corete carte ")
                continue
        elif age >= 21 : 
            print("Accès autorisé")
            break
        else : 
            print("Accès refusé")
            break
    except ValueError :
        print("il faut respecte le type de l'age !!")

# Challenge D - Conditions imbriquées
# Votre code ici...
print("="*10, "test de l'IMC:", "="*10)
while True :
    try : 
        poids = float(input("entre votre poids: "))
        if poids :
            taille = float(input("entre votre taille : "))
            if taille :
                IMC = poids / taille
                if IMC < 18.5 :
                    print("Maigreur", IMC)
                    break
                elif 18.5 <= IMC or IMC < 25 :
                    print("Normal", IMC)
                    break
                elif 25 <= IMC or IMC < 30 :
                    print("Suspoids", IMC)
                    break
                else :
                    print("Obésité", IMC)
                    break
            else :
                print("entre une taille corecte!")
                continue 
        else : 
            print("entre un poids corecte!")
            continue
    except ValueError :
        print("tu n'a pas respecte les forme des valeurs !")
        continue 

# Challenge E - Logique complexe
# Votre code ici...
print("="*10, "vienvenus dans votre jeu", "="*10)

import random
nombre_secret = random.randint(1, 100)
tentatives = 3

for essai in range(1, tentatives + 1) :
    try :
        guess = int(input(f"Tentative {essai}/{tentatives} - Devinez le nombre (1-100): "))
        astuce = abs(nombre_secret - guess)
        if guess == nombre_secret:
            print("Bravo ! Vous avez trouvé le nombre secret qui est : ", nombre_secret)
            break
        elif guess < nombre_secret and astuce <= 5:
            print("Trop petit et Vous êtes très proche !")
        elif guess < nombre_secret and astuce >= 50:
            print("Trop petit et Vous êtes très loin !")
        elif guess > nombre_secret and astuce <= 5:
            print("Trop grand et Vous êtes très proche !")
        elif guess > nombre_secret and astuce >= 50:
            print("Trop grand et Vous êtes très loin !")
        else:
            print("Essayez encore !")
    except ValueError :
        print("Veuillez entrer un nombre valide.")
else :
    print(f"Dommage ! Le nombre secret était {nombre_secret}.")
