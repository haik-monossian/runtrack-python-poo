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

class Professeur(Personne):
    def __init__(self, matiere):
        super().__init__()
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")


mon_eleve = Eleve()
mon_eleve.bonjour()       
mon_eleve.allerEnCours()   
mon_eleve.modifierAge(15) 
mon_eleve.afficherAge()    

print("-" * 10) 

mon_prof = Professeur("Mathématiques")
mon_prof.modifierAge(40) 
mon_prof.bonjour()         
mon_prof.enseigner()      