# Challenge 3.1 - Lambda et fonctions d'ordre supérieur
# Votre code ici...

# challenge A:
# - Créez des lambda pour : carré, cube, pair/impair
lambda_carre = lambda x: x ** 2
print(lambda_carre(5))  
lambda_cube = lambda x: x ** 3
print(lambda_cube(3))
lambda_pair_impair = lambda x: "Pair" if x % 2 == 0 else "Impair"
print(lambda_pair_impair(4))
print(lambda_pair_impair(5))
# - Triez une liste de tuples par le 2ème élément
ma_liste = [(1, 2), (0, 1), (5, 0), (4, 3), (2, 4)]
ma_liste.sort(key=lambda x: x[1]) # Tri par le 2ème élément
print(ma_liste)
# - Trouvez le maximum avec une fonction custom
def trouver_maximum(liste):
    max_val = liste[0]
    for elem in liste:
        if elem > max_val:
            max_val = elem
    return max_val
print(trouver_maximum([1, 2, 3, 4, 5]))
# challenge B:
# - Convertissez des températures Celsius en Fahrenheit
convertir_c = lambda c: (c * 9/5) + 32
convertir_f = lambda f: (f - 32) * 5/9
print(convertir_c(0))
print(convertir_f(32))
print(convertir_c(100))
print(convertir_f(212))
# - Filtrez les mots de plus de 5 lettres
filter_mots = lambda mots: [m for m in mots if len(m) > 5]
print(filter_mots(["pomme", "banane", "cerise", "kiwi"]))
# - Extrayez les nombres d'un texte mixte
extraire_nombres = lambda texte: [int(s) for s in texte.split() if s.isdigit()]
print(extraire_nombres("Il y a 2 pommes et 3 bananes"))

# challenge C:
# - Calculez le produit de tous les éléments
produit = lambda lst: 1 if not lst else lst[0] * produit(lst[1:])
print(produit([1, 2, 3, 4, 5]))
# - Trouvez le mot le plus long
long_mot = lambda mots: max(mots, key=len)
print(long_mot(["pomme", "banane", "cerise", "kiwi"]))
# - Comptez les occurrences de chaque lettre
compter_occurrences = lambda texte: {c: texte.count(c) for c in set(texte)}
print(compter_occurrences("abracadabra"))
# - Calculez la moyenne d'une liste de nombres
moyenne = lambda lst: sum(lst) / len(lst) if lst else 0
print(moyenne([1, 2, 3, 4, 5]))
# challenge D:
# Analysez un dataset de ventes avec les fonctions :

# - Filtrage par critères multiples
ventes = [
    {'id': 1, 'montant': 150, 'categorie': 'A'},
    {'id': 2, 'montant': 80, 'categorie': 'B'},
    {'id': 3, 'montant': 200, 'categorie': 'A'},
]
filter_ventes = lambda ventes: [v for v in ventes if v['montant'] > 100 and v['categorie'] == 'A']
ventes = [
    {'id': 1, 'montant': 150, 'categorie': 'A'},
    {'id': 2, 'montant': 80, 'categorie': 'B'},
    {'id': 3, 'montant': 200, 'categorie': 'A'},
]
print(filter_ventes(ventes))
# - Calculs de statistiques
statistiques_ventes = lambda ventes: {
    'total': sum(v['montant'] for v in ventes),
    'moyenne': sum(v['montant'] for v in ventes) / len(ventes) if ventes else 0,
    'max': max(v['montant'] for v in ventes) if ventes else 0,
}
# - Transformations de données
transformer_ventes = lambda ventes: [{'id': v['id'], 'montant': v['montant'] * 1.2} for v in ventes]
print(transformer_ventes(ventes))   
# - Pipeline de traitement fonctionnel
pipeline_ventes = lambda ventes: (
    statistiques_ventes(
        transformer_ventes(
            filter_ventes(ventes)
        )
    )
)
print(pipeline_ventes(ventes))
