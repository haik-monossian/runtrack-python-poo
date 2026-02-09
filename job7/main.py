import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.main_joueur = []
        self.main_croupier = []

    def calculer_score(self, main):
        score = 0
        as_count = 0
        valeurs_speciales = {"Valet": 10, "Dame": 10, "Roi": 10, "As": 11}

        for carte in main:
            if carte.valeur.isdigit():
                score += int(carte.valeur)
            else:
                score += valeurs_speciales[carte.valeur]
                if carte.valeur == "As":
                    as_count += 1

        while score > 21 and as_count > 0:
            score -= 10
            as_count -= 1
        return score

    def afficher_main(self, main, nom):
        print(f"Main de {nom}:", [str(c) for c in main], f"| Score: {self.calculer_score(main)}")

    def jouer(self):
        self.main_joueur.append(self.jeu.tirer_carte())
        self.main_joueur.append(self.jeu.tirer_carte())
        self.main_croupier.append(self.jeu.tirer_carte())
        self.main_croupier.append(self.jeu.tirer_carte())

        while True:
            self.afficher_main(self.main_joueur, "Joueur")
            if self.calculer_score(self.main_joueur) > 21:
                print("Vous avez dépassé 21 ! Perdu.")
                return

            choix = input("Voulez-vous 'prendre' une carte ou 'passer' ? ").lower()
            if choix == "prendre":
                self.main_joueur.append(self.jeu.tirer_carte())
            else:
                break

        while self.calculer_score(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.tirer_carte())

        self.afficher_main(self.main_croupier, "Croupier")
        
        score_j = self.calculer_score(self.main_joueur)
        score_c = self.calculer_score(self.main_croupier)

        if score_c > 21:
            print("Le croupier a dépassé 21 ! Vous gagnez.")
        elif score_j > score_c:
            print("Vous gagnez !")
        elif score_j == score_c:
            print("Égalité !")
        else:
            print("Le croupier gagne.")

partie = Blackjack()
partie.jouer()