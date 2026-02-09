class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge

class Eleve(Personne):
    
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur:
    def __init__(self, matiere):
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")


une_personne = Personne()
un_eleve = Eleve()
un_eleve.afficherAge()