# Challenge Jour 6 - POO Avancée : Héritage et Polymorphisme
# Complétez tous les exercices ci-dessous

# =============================================================================
# PARTIE A - Héritage Simple (60min)
# =============================================================================

print("=== PARTIE A - Héritage Simple ===")


# Classe de base
class Animal:
    def __init__(self, nom, age, espece):
        """Constructeur de la classe Animal"""
        self.nom = nom
        self.age = age
        self.espece = espece
        self.sante = 100
        self.faim = 0

    def manger(self, quantite=10):
        """Nourrir l'animal"""
        self.faim = max(0, self.faim - quantite)
        self.sante = min(100, self.sante + 5)
        return f"{self.nom} a mangé et se sent mieux!"

    def dormir(self):
        """Faire dormir l'animal"""
        self.sante = min(100, self.sante + 10)
        self.faim = min(100, self.faim + 5)
        return f"{self.nom} a bien dormi!"

    def vieillir(self):
        """Faire vieillir l'animal"""
        self.age += 1
        self.sante = max(0, self.sante - 5)
        return f"{self.nom} a maintenant {self.age} ans"

    def etat(self):
        """Afficher l'état de l'animal"""
        return f"{self.nom} ({self.espece}, {self.age} ans) - Santé: {self.sante}% - Faim: {self.faim}%"

    def faire_bruit(self):
        """Méthode générique pour faire du bruit"""
        return f"{self.nom} fait du bruit"

    def __str__(self):
        return self.etat()


# Classes héritées
class Chien(Animal):
    def __init__(self, nom, age, race):
        """Constructeur du chien"""
        super().__init__(nom, age, "Chien")
        self.race = race
        self.obeissance = 50

    def faire_bruit(self):
        """Surcharge de la méthode faire_bruit"""
        return f"{self.nom} aboie: Wouf wouf!"

    def jouer(self):
        """Méthode spécifique au chien"""
        self.obeissance = min(100, self.obeissance + 10)
        self.faim = min(100, self.faim + 15)
        self.sante = min(100, self.sante + 5)
        return f"{self.nom} joue et apprend! Obéissance: {self.obeissance}%"

    def dresser(self):
        """Dresser le chien"""
        self.obeissance = min(100, self.obeissance + 20)
        return f"{self.nom} apprend de nouveaux tours! Obéissance: {self.obeissance}%"

    def etat(self):
        """État spécifique du chien"""
        return f"{super().etat()} - Race: {self.race} - Obéissance: {self.obeissance}%"


class Chat(Animal):
    def __init__(self, nom, age, couleur):
        """Constructeur du chat"""
        super().__init__(nom, age, "Chat")
        self.couleur = couleur
        self.independance = 80

    def faire_bruit(self):
        """Surcharge de la méthode faire_bruit"""
        return f"{self.nom} miaule: Miaou miaou!"

    def chasser(self):
        """Méthode spécifique au chat"""
        self.independance = min(100, self.independance + 10)
        self.faim = max(0, self.faim - 20)
        return f"{self.nom} a chassé et attrapé une proie! Indépendance: {self.independance}%"

    def faire_toilette(self):
        """Le chat fait sa toilette"""
        self.sante = min(100, self.sante + 5)
        return f"{self.nom} fait sa toilette et se sent propre!"

    def etat(self):
        """État spécifique du chat"""
        return f"{super().etat()} - Couleur: {self.couleur} - Indépendance: {self.independance}%"


class Oiseau(Animal):
    def __init__(self, nom, age, envergure):
        """Constructeur de l'oiseau"""
        super().__init__(nom, age, "Oiseau")
        self.envergure = envergure
        self.altitude = 0

    def faire_bruit(self):
        """Surcharge de la méthode faire_bruit"""
        return f"{self.nom} chante: Cui cui cui!"

    def voler(self, altitude):
        """Méthode spécifique à l'oiseau"""
        self.altitude = altitude
        self.faim = min(100, self.faim + 10)
        return f"{self.nom} vole à {altitude}m d'altitude!"

    def atterrir(self):
        """L'oiseau atterrit"""
        self.altitude = 0
        return f"{self.nom} a atterri en sécurité!"

    def construire_nid(self):
        """Construire un nid"""
        self.sante = min(100, self.sante + 15)
        return f"{self.nom} a construit un magnifique nid!"

    def etat(self):
        """État spécifique de l'oiseau"""
        return f"{super().etat()} - Envergure: {self.envergure}cm - Altitude: {self.altitude}m"


# Tests des classes héritées
print("1. Test des classes héritées :")

# Création des animaux
chien = Chien("Rex", 3, "Berger Allemand")
chat = Chat("Minou", 2, "Tigré")
oiseau = Oiseau("Tweety", 1, 15)

# Test des méthodes communes
animaux = [chien, chat, oiseau]
for animal in animaux:
    print(animal.etat())
    print(animal.faire_bruit())
    print(animal.manger())
    print()

# Test des méthodes spécifiques
print("Méthodes spécifiques :")
print(chien.jouer())
print(chien.dresser())
print(chat.chasser())
print(chat.faire_toilette())
print(oiseau.voler(50))
print(oiseau.construire_nid())

# =============================================================================
# PARTIE B - Polymorphisme (45min)
# =============================================================================

print("\n=== PARTIE B - Polymorphisme ===")


class Vehicule:
    def __init__(self, marque, modele, annee):
        """Constructeur de base des véhicules"""
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = 0
        self.moteur_allume = False

    def demarrer(self):
        """Démarrer le véhicule"""
        if self.moteur_allume:
            return f"{self.marque} {self.modele} est déjà démarré"
        self.moteur_allume = True
        return f"{self.marque} {self.modele} démarre"

    def arreter(self):
        """Arrêter le véhicule"""
        self.moteur_allume = False
        self.vitesse = 0
        return f"{self.marque} {self.modele} s'arrête"

    def accelerer(self, vitesse):
        """Accélérer (méthode à surcharger)"""
        if not self.moteur_allume:
            return "Impossible d'accélérer, le moteur est éteint"
        self.vitesse = vitesse
        return f"{self.marque} {self.modele} roule à {self.vitesse} km/h"

    def klaxonner(self):
        """Klaxonner (méthode à surcharger)"""
        return "Bip bip!"

    def __str__(self):
        statut = "🟢 En marche" if self.moteur_allume else "🔴 Arrêté"
        return f"{self.marque} {self.modele} ({self.annee}) - {statut} - {self.vitesse} km/h"


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nombre_portes):
        """Constructeur de la voiture"""
        super().__init__(marque, modele, annee)
        self.nombre_portes = nombre_portes
        self.carburant = 50  # Litre

    def accelerer(self, vitesse):
        """Accélération spécifique à la voiture"""
        if not self.moteur_allume:
            return "Impossible d'accélérer, le moteur est éteint"

        if self.carburant <= 0:
            return "Impossible d'accélérer, plus de carburant!"

        vitesse_max = 180
        self.vitesse = min(vitesse, vitesse_max)
        self.carburant -= self.vitesse * 0.1  # Consommation
        self.carburant = max(0, self.carburant)

        return f"🚗 {self.marque} {self.modele} accélère à {self.vitesse} km/h (Carburant: {self.carburant:.1f}L)"

    def klaxonner(self):
        """Klaxon de voiture"""
        return "Tuut tuut!"

    def faire_plein(self):
        """Faire le plein de carburant"""
        self.carburant = 50
        return f"⛽ Plein fait! Carburant: {self.carburant}L"


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, cylindree):
        """Constructeur de la moto"""
        super().__init__(marque, modele, annee)
        self.cylindree = cylindree

    def accelerer(self, vitesse):
        """Accélération spécifique à la moto"""
        if not self.moteur_allume:
            return "Impossible d'accélérer, le moteur est éteint"

        vitesse_max = 250  # Les motos vont plus vite
        self.vitesse = min(vitesse, vitesse_max)

        return f"🏍️ {self.marque} {self.modele} fonce à {self.vitesse} km/h! Vrooom!"

    def klaxonner(self):
        """Klaxon de moto"""
        return "Beep beep!"

    def faire_wheelie(self):
        """Faire une roue arrière"""
        if self.vitesse > 20:
            return f"🏍️ {self.marque} {self.modele} fait une roue arrière spectaculaire!"
        return "Vitesse insuffisante pour faire une roue arrière"


class Camion(Vehicule):
    def __init__(self, marque, modele, annee, charge_max):
        """Constructeur du camion"""
        super().__init__(marque, modele, annee)
        self.charge_max = charge_max
        self.charge_actuelle = 0

    def accelerer(self, vitesse):
        """Accélération spécifique au camion"""
        if not self.moteur_allume:
            return "Impossible d'accélérer, le moteur est éteint"

        # Vitesse limitée selon la charge
        vitesse_max = 90 - (self.charge_actuelle / self.charge_max * 30)
        self.vitesse = min(vitesse, vitesse_max)

        return f"🚛 {self.marque} {self.modele} roule à {self.vitesse:.0f} km/h (Charge: {self.charge_actuelle}t/{self.charge_max}t)"

    def klaxonner(self):
        """Klaxon de camion"""
        return "HONK HONK!"

    def charger(self, poids):
        """Charger des marchandises"""
        if self.charge_actuelle + poids <= self.charge_max:
            self.charge_actuelle += poids
            return f"📦 Chargement de {poids}t. Charge totale: {self.charge_actuelle}t"
        return f"❌ Impossible de charger {poids}t. Capacité dépassée!"

    def decharger(self, poids):
        """Décharger des marchandises"""
        if poids <= self.charge_actuelle:
            self.charge_actuelle -= poids
            return (
                f"📦 Déchargement de {poids}t. Charge restante: {self.charge_actuelle}t"
            )
        return f"❌ Impossible de décharger {poids}t. Pas assez de marchandises!"


# Tests du polymorphisme
print("2. Test du polymorphisme :")

# Création des véhicules
vehicules = [
    Voiture("Peugeot", "308", 2020, 5),
    Moto("Yamaha", "R1", 2021, 1000),
    Camion("Volvo", "FH", 2019, 25),
]

# Test des méthodes communes (polymorphisme)
print("Démarrage de tous les véhicules :")
for vehicule in vehicules:
    print(vehicule.demarrer())
    print(vehicule.klaxonner())
    print(vehicule.accelerer(100))
    print(vehicule)
    print()

# Test des méthodes spécifiques
print("Méthodes spécifiques :")
voiture = vehicules[0]
moto = vehicules[1]
camion = vehicules[2]

print(voiture.faire_plein())
print(moto.faire_wheelie())
print(camion.charger(15))
print(camion.accelerer(80))

# =============================================================================
# PARTIE C - Héritage Multiple (30min)
# =============================================================================

print("\n=== PARTIE C - Héritage Multiple ===")


class Volant:
    """Mixin pour les objets qui peuvent voler"""

    def __init__(self):
        self.en_vol = False
        self.altitude = 0

    def decoller(self):
        """Décoller"""
        if self.en_vol:
            return "Déjà en vol!"
        self.en_vol = True
        self.altitude = 100
        return "✈️ Décollage réussi!"

    def atterrir(self):
        """Atterrir"""
        if not self.en_vol:
            return "Déjà au sol!"
        self.en_vol = False
        self.altitude = 0
        return "✈️ Atterrissage réussi!"

    def monter(self, metres):
        """Monter en altitude"""
        if not self.en_vol:
            return "Impossible de monter, pas en vol!"
        self.altitude += metres
        return f"Montée à {self.altitude}m d'altitude"


class Flottant:
    """Mixin pour les objets qui peuvent flotter"""

    def __init__(self):
        self.flotte = False

    def mettre_a_eau(self):
        """Mettre à l'eau"""
        if self.flotte:
            return "Déjà à l'eau!"
        self.flotte = True
        return "🚤 Mise à l'eau réussie!"

    def sortir_eau(self):
        """Sortir de l'eau"""
        if not self.flotte:
            return "Déjà hors de l'eau!"
        self.flotte = False
        return "🚤 Sorti de l'eau!"


class VehiculeAmphibie(Vehicule, Volant, Flottant):
    """Véhicule qui peut rouler, voler et flotter"""

    def __init__(self, marque, modele, annee):
        Vehicule.__init__(self, marque, modele, annee)
        Volant.__init__(self)
        Flottant.__init__(self)
        self.mode = "terrestre"

    def changer_mode(self, nouveau_mode):
        """Changer le mode de transport"""
        modes_valides = ["terrestre", "aerien", "maritime"]
        if nouveau_mode not in modes_valides:
            return f"Mode invalide. Modes disponibles: {', '.join(modes_valides)}"

        if nouveau_mode == self.mode:
            return f"Déjà en mode {nouveau_mode}"

        # Arrêter le mode actuel
        if self.mode == "aerien" and self.en_vol:
            self.atterrir()
        elif self.mode == "maritime" and self.flotte:
            self.sortir_eau()

        self.mode = nouveau_mode
        return f"🔄 Mode changé vers: {nouveau_mode}"

    def accelerer(self, vitesse):
        """Accélération selon le mode"""
        if not self.moteur_allume:
            return "Moteur éteint!"

        if self.mode == "terrestre":
            self.vitesse = min(vitesse, 120)
            return f"🚗 Roulage à {self.vitesse} km/h"
        elif self.mode == "aerien":
            if not self.en_vol:
                return "Décollage requis pour voler!"
            self.vitesse = min(vitesse, 200)
            return f"✈️ Vol à {self.vitesse} km/h à {self.altitude}m"
        elif self.mode == "maritime":
            if not self.flotte:
                return "Mise à l'eau requise pour naviguer!"
            self.vitesse = min(vitesse, 60)
            return f"🚤 Navigation à {self.vitesse} km/h"

    def statut_complet(self):
        """Afficher le statut complet du véhicule"""
        statut = f"{self} - Mode: {self.mode}"
        if self.en_vol:
            statut += f" - En vol à {self.altitude}m"
        if self.flotte:
            statut += " - À l'eau"
        return statut


# Test du véhicule amphibie
print("3. Test véhicule amphibie :")
amphibie = VehiculeAmphibie("AquaCar", "Splash", 2023)

print(amphibie.demarrer())
print(amphibie.accelerer(80))
print(amphibie.statut_complet())

print("\nMode aérien :")
print(amphibie.changer_mode("aerien"))
print(amphibie.decoller())
print(amphibie.monter(500))
print(amphibie.accelerer(150))
print(amphibie.statut_complet())

print("\nMode maritime :")
print(amphibie.changer_mode("maritime"))
print(amphibie.mettre_a_eau())
print(amphibie.accelerer(40))
print(amphibie.statut_complet())

# =============================================================================
# PARTIE D - Classes Abstraites (30min)
# =============================================================================

print("\n=== PARTIE D - Classes Abstraites ===")

from abc import ABC, abstractmethod


class Forme(ABC):
    """Classe abstraite pour les formes géométriques"""

    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def calculer_aire(self):
        """Méthode abstraite pour calculer l'aire"""
        pass

    @abstractmethod
    def calculer_perimetre(self):
        """Méthode abstraite pour calculer le périmètre"""
        pass

    def afficher_info(self):
        """Méthode concrète commune"""
        return f"{self.nom} - Aire: {self.calculer_aire():.2f} - Périmètre: {self.calculer_perimetre():.2f}"


class Rectangle(Forme):
    """Rectangle héritant de Forme"""

    def __init__(self, longueur, largeur):
        super().__init__("Rectangle")
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        """Implémentation concrète du calcul d'aire"""
        return self.longueur * self.largeur

    def calculer_perimetre(self):
        """Implémentation concrète du calcul de périmètre"""
        return 2 * (self.longueur + self.largeur)

    def est_carre(self):
        """Méthode spécifique au rectangle"""
        return self.longueur == self.largeur


class Cercle(Forme):
    """Cercle héritant de Forme"""

    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def calculer_aire(self):
        """Implémentation concrète du calcul d'aire"""
        import math

        return math.pi * self.rayon**2

    def calculer_perimetre(self):
        """Implémentation concrète du calcul de périmètre"""
        import math

        return 2 * math.pi * self.rayon

    def calculer_diametre(self):
        """Méthode spécifique au cercle"""
        return 2 * self.rayon


class Triangle(Forme):
    """Triangle héritant de Forme"""

    def __init__(self, cote1, cote2, cote3):
        super().__init__("Triangle")
        self.cote1 = cote1
        self.cote2 = cote2
        self.cote3 = cote3

    def calculer_aire(self):
        """Implémentation avec la formule de Héron"""
        s = self.calculer_perimetre() / 2
        import math

        return math.sqrt(s * (s - self.cote1) * (s - self.cote2) * (s - self.cote3))

    def calculer_perimetre(self):
        """Implémentation concrète du calcul de périmètre"""
        return self.cote1 + self.cote2 + self.cote3

    def est_equilateral(self):
        """Méthode spécifique au triangle"""
        return self.cote1 == self.cote2 == self.cote3


# Test des classes abstraites
print("4. Test classes abstraites :")

# Création des formes
formes = [Rectangle(5, 3), Cercle(4), Triangle(3, 4, 5)]

# Test du polymorphisme avec les méthodes abstraites
for forme in formes:
    print(forme.afficher_info())

# Test des méthodes spécifiques
rect = formes[0]
cercle = formes[1]
triangle = formes[2]

print(f"Le rectangle est-il un carré ? {rect.est_carre()}")
print(f"Diamètre du cercle: {cercle.calculer_diametre():.2f}")
print(f"Le triangle est-il équilatéral ? {triangle.est_equilateral()}")

# =============================================================================
# PROJET FINAL - Système de Gestion d'École (45min)
# =============================================================================

print("\n=== PROJET FINAL - Système de Gestion d'École ===")


class Personne:
    """Classe de base pour toutes les personnes de l'école"""

    def __init__(self, nom, prenom, age, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.identifiant = identifiant

    @property
    def nom_complet(self):
        """Propriété pour le nom complet"""
        return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"{self.nom_complet} (ID: {self.identifiant})"


class Etudiant(Personne):
    """Classe pour les étudiants"""

    def __init__(self, nom, prenom, age, numero_etudiant, classe):
        super().__init__(nom, prenom, age, f"ETU{numero_etudiant}")
        self.numero_etudiant = numero_etudiant
        self.classe = classe
        self.notes = {}  # {matiere: [notes]}
        self.absences = 0

    def ajouter_note(self, matiere, note):
        """Ajouter une note dans une matière"""
        if not 0 <= note <= 20:
            return "❌ Note invalide (doit être entre 0 et 20)"

        if matiere not in self.notes:
            self.notes[matiere] = []

        self.notes[matiere].append(note)
        return f"✅ Note ajoutée: {note}/20 en {matiere}"

    def calculer_moyenne_matiere(self, matiere):
        """Calculer la moyenne dans une matière"""
        if matiere not in self.notes or not self.notes[matiere]:
            return 0
        return sum(self.notes[matiere]) / len(self.notes[matiere])

    def calculer_moyenne_generale(self):
        """Calculer la moyenne générale"""
        if not self.notes:
            return 0

        total_notes = 0
        nombre_notes = 0

        for notes_matiere in self.notes.values():
            total_notes += sum(notes_matiere)
            nombre_notes += len(notes_matiere)

        return total_notes / nombre_notes if nombre_notes > 0 else 0

    def obtenir_mention(self):
        """Obtenir la mention selon la moyenne"""
        moyenne = self.calculer_moyenne_generale()
        if moyenne >= 16:
            return "Très bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez bien"
        elif moyenne >= 10:
            return "Passable"
        else:
            return "Insuffisant"

    def ajouter_absence(self):
        """Ajouter une absence"""
        self.absences += 1
        return f"Absence ajoutée. Total: {self.absences}"

    def bulletin(self):
        """Générer le bulletin de notes"""
        print(f"\n📊 BULLETIN DE {self.nom_complet.upper()}")
        print(f"Classe: {self.classe} | Absences: {self.absences}")
        print("-" * 50)

        if not self.notes:
            print("Aucune note enregistrée")
            return

        for matiere, notes in self.notes.items():
            moyenne = self.calculer_moyenne_matiere(matiere)
            print(f"{matiere:15} | Notes: {notes} | Moyenne: {moyenne:.2f}")

        print("-" * 50)
        print(f"Moyenne générale: {self.calculer_moyenne_generale():.2f}/20")
        print(f"Mention: {self.obtenir_mention()}")


class Professeur(Personne):
    """Classe pour les professeurs"""

    def __init__(self, nom, prenom, age, numero_employe, matiere, salaire):
        super().__init__(nom, prenom, age, f"PROF{numero_employe}")
        self.numero_employe = numero_employe
        self.matiere = matiere
        self.salaire = salaire
        self.classes = []
        self.heures_enseignees = 0

    def ajouter_classe(self, classe):
        """Ajouter une classe à enseigner"""
        if classe not in self.classes:
            self.classes.append(classe)
            return f"✅ Classe {classe} ajoutée"
        return f"❌ Classe {classe} déjà assignée"

    def enseigner(self, heures):
        """Enregistrer des heures d'enseignement"""
        self.heures_enseignees += heures
        return f"📚 {heures}h enseignées. Total: {self.heures_enseignees}h"

    def calculer_salaire_mensuel(self):
        """Calculer le salaire mensuel avec heures supplémentaires"""
        heures_normales = min(self.heures_enseignees, 120)  # 120h par mois max normal
        heures_sup = max(0, self.heures_enseignees - 120)

        salaire_base = self.salaire
        salaire_sup = heures_sup * (self.salaire / 120) * 1.25  # 25% de majoration

        return salaire_base + salaire_sup

    def __str__(self):
        return f"{super().__str__()} - {self.matiere} - Classes: {', '.join(self.classes) if self.classes else 'Aucune'}"


class Cours:
    """Classe pour représenter un cours"""

    def __init__(self, nom, professeur, classe, horaire):
        self.nom = nom
        self.professeur = professeur
        self.classe = classe
        self.horaire = horaire
        self.etudiants_presents = []

    def marquer_presence(self, etudiant):
        """Marquer la présence d'un étudiant"""
        if etudiant not in self.etudiants_presents:
            self.etudiants_presents.append(etudiant)
            return f"✅ {etudiant.nom_complet} marqué présent"
        return f"❌ {etudiant.nom_complet} déjà marqué présent"

    def __str__(self):
        return f"{self.nom} - {self.professeur.nom_complet} - {self.classe} - {self.horaire}"


class Ecole:
    """Classe principale pour gérer l'école"""

    def __init__(self, nom):
        self.nom = nom
        self.etudiants = {}  # {numero: etudiant}
        self.professeurs = {}  # {numero: professeur}
        self.cours = []
        self.classes = set()

    def ajouter_etudiant(self, etudiant):
        """Ajouter un étudiant à l'école"""
        if etudiant.numero_etudiant in self.etudiants:
            return f"❌ Étudiant {etudiant.numero_etudiant} déjà inscrit"

        self.etudiants[etudiant.numero_etudiant] = etudiant
        self.classes.add(etudiant.classe)
        return f"✅ Étudiant {etudiant.nom_complet} inscrit"

    def ajouter_professeur(self, professeur):
        """Ajouter un professeur à l'école"""
        if professeur.numero_employe in self.professeurs:
            return f"❌ Professeur {professeur.numero_employe} déjà employé"

        self.professeurs[professeur.numero_employe] = professeur
        return f"✅ Professeur {professeur.nom_complet} embauché"

    def creer_cours(self, nom, numero_prof, classe, horaire):
        """Créer un nouveau cours"""
        if numero_prof not in self.professeurs:
            return f"❌ Professeur {numero_prof} non trouvé"

        professeur = self.professeurs[numero_prof]
        cours = Cours(nom, professeur, classe, horaire)
        self.cours.append(cours)
        professeur.ajouter_classe(classe)

        return f"✅ Cours '{nom}' créé"

    def afficher_statistiques(self):
        """Afficher les statistiques de l'école"""
        print(f"\n📊 STATISTIQUES - {self.nom}")
        print("=" * 40)
        print(f"Étudiants inscrits: {len(self.etudiants)}")
        print(f"Professeurs employés: {len(self.professeurs)}")
        print(f"Cours programmés: {len(self.cours)}")
        print(f"Classes: {', '.join(sorted(self.classes))}")

        if self.etudiants:
            moyennes = [
                etudiant.calculer_moyenne_generale()
                for etudiant in self.etudiants.values()
            ]
            moyenne_ecole = sum(moyennes) / len(moyennes)
            print(f"Moyenne générale de l'école: {moyenne_ecole:.2f}/20")

    def lister_etudiants_classe(self, classe):
        """Lister les étudiants d'une classe"""
        etudiants_classe = [e for e in self.etudiants.values() if e.classe == classe]
        if not etudiants_classe:
            return f"Aucun étudiant en {classe}"

        print(f"\n👥 ÉTUDIANTS DE LA CLASSE {classe}")
        print("-" * 40)
        for etudiant in sorted(etudiants_classe, key=lambda e: e.nom):
            moyenne = etudiant.calculer_moyenne_generale()
            print(
                f"{etudiant.nom_complet:25} | Moyenne: {moyenne:5.2f} | Mention: {etudiant.obtenir_mention()}"
            )


# Test du système complet
print("5. Test du système d'école :")

# Création de l'école
ecole = Ecole("Lycée Python")

# Ajout d'étudiants
etudiants = [
    Etudiant("Dubois", "Alice", 16, 1001, "1èreS"),
    Etudiant("Martin", "Bob", 17, 1002, "1èreS"),
    Etudiant("Durand", "Charlie", 16, 1003, "1èreS"),
    Etudiant("Bernard", "Diana", 18, 2001, "TermS"),
]

for etudiant in etudiants:
    print(ecole.ajouter_etudiant(etudiant))

# Ajout de professeurs
professeurs = [
    Professeur("Leroy", "Jean", 45, 101, "Mathématiques", 3000),
    Professeur("Moreau", "Marie", 38, 102, "Physique", 2800),
    Professeur("Simon", "Paul", 52, 103, "Français", 2900),
]

for professeur in professeurs:
    print(ecole.ajouter_professeur(professeur))

# Création de cours
print(ecole.creer_cours("Algèbre", 101, "1èreS", "Lundi 8h-10h"))
print(ecole.creer_cours("Mécanique", 102, "1èreS", "Mardi 10h-12h"))
print(ecole.creer_cours("Littérature", 103, "TermS", "Mercredi 14h-16h"))

# Ajout de notes
alice = etudiants[0]
bob = etudiants[1]

print(alice.ajouter_note("Mathématiques", 16))
print(alice.ajouter_note("Mathématiques", 14))
print(alice.ajouter_note("Physique", 18))
print(alice.ajouter_note("Français", 15))

print(bob.ajouter_note("Mathématiques", 12))
print(bob.ajouter_note("Physique", 13))
print(bob.ajouter_note("Français", 16))

# Affichage des bulletins
alice.bulletin()
bob.bulletin()

# Statistiques de l'école
ecole.afficher_statistiques()
ecole.lister_etudiants_classe("1èreS")

print("\n🎉 Système d'école POO terminé !")
print("⏭️ Passez maintenant aux Jour 7-8 : Gestion d'erreurs et fichiers !")
