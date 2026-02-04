class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes=0, jaunes=0, rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print(f"--- Statistiques de {self.nom} ---")
        print(f"Numéro : {self.numero}")
        print(f"Position : {self.position}")
        print(f"Buts : {self.buts}")
        print(f"Passes décisives : {self.passes}")
        print(f"Cartons jaunes : {self.jaunes}")
        print(f"Cartons rouges : {self.rouges}")
        print("----------------------------------")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur: Joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"\n=== Statistiques des joueurs de {self.nom} ===")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return
        print(f"Joueur {nom_joueur} introuvable dans l'équipe {self.nom}.")

# équipes
psg = Equipe("PSG")
om = Equipe("OM")

# joueurs
mbappe = Joueur("Mbappé", 7, "Attaquant")
hakimi = Joueur("Hakimi", 2, "Défenseur")
vitinha = Joueur("Vitinha", 17, "Milieu")

aubameyang = Joueur("Aubameyang", 10, "Attaquant")
clauss = Joueur("Clauss", 7, "Défenseur")

# Ajout des joueurs aux équipes
psg.ajouterJoueur(mbappe)
psg.ajouterJoueur(hakimi)
psg.ajouterJoueur(vitinha)

om.ajouterJoueur(aubameyang)
om.ajouterJoueur(clauss)

# Affichage initial
psg.afficherStatistiquesJoueurs()
om.afficherStatistiquesJoueurs()

# Simulation d'un match
psg.mettreAJourStatistiquesJoueur("Mbappé", "but")
psg.mettreAJourStatistiquesJoueur("Hakimi", "passe")
om.mettreAJourStatistiquesJoueur("Clauss", "jaune")
om.mettreAJourStatistiquesJoueur("Aubameyang", "rouge")

# Affichage après match
psg.afficherStatistiquesJoueurs()
om.afficherStatistiquesJoueurs()
