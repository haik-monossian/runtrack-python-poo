class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = 10
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts !")

    def est_vivant(self):
        return self.vie > 0

    def afficher_etat(self):
        print(f"{self.nom} : {self.vie} points de vie")


class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")

        choix = input("Votre choix : ")

        if choix == "1":
            self.niveau = "facile"
        elif choix == "2":
            self.niveau = "moyen"
        elif choix == "3":
            self.niveau = "difficile"
        else:
            print("Choix invalide, niveau facile sélectionné par défaut.")
            self.niveau = "facile"

    def lancerJeu(self):
        # Points de vie selon le niveau
        if self.niveau == "facile":
            vie_joueur = 120
            vie_ennemi = 80
        elif self.niveau == "moyen":
            vie_joueur = 100
            vie_ennemi = 100
        else:  # difficile
            vie_joueur = 80
            vie_ennemi = 120

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print("\n--- Début du combat ! ---")
        joueur.afficher_etat()
        ennemi.afficher_etat()
        print()

        # Boucle de combat
        while joueur.est_vivant() and ennemi.est_vivant():
            # Tour du joueur
            joueur.attaquer(ennemi)
            ennemi.afficher_etat()

            if not ennemi.est_vivant():
                break

            # Tour de l’ennemi
            ennemi.attaquer(joueur)
            joueur.afficher_etat()
            print()

        self.afficherGagnant(joueur, ennemi)

    def afficherGagnant(self, joueur, ennemi):
        print("\n--- Fin du combat ---")
        if joueur.est_vivant():
            print("Le joueur a gagné !")
        else:
            print("L’ennemi a gagné...")


jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
