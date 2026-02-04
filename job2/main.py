class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = False

    def get_afficher(self):
        return(self.__numero, self.__nom, self.__prenom, self.__solde)

    def get_afficher_solde(self):
        return self.__solde

    def set_versement(self, montant):
        self.__solde += montant
        if self.__solde >= 0:
            self.__decouvert = False
    
    def set_retrait(self, montant: int):
        if (self.__solde - montant) >= 0:
            self.__solde -= montant
            print(f"vous avez maintenant {self.get_afficher_solde()} euros")
        else:
            self.__decouvert = True
            self.__solde -= montant
            self.agios()
            print(f"vous avez maintenant {self.get_afficher_solde()} euros")

    def agios(self):
        if self.__decouvert:
            self.__solde += self.__solde * 0.05 # += car on est en négatif

    def virement(self, CompteBancaire, montant: int):
        self.set_retrait(montant)
        CompteBancaire.set_versement(montant)


c = CompteBancaire(1, "A", "B", 200)
c2 = CompteBancaire(2, "C", "D", -100)

print(c.get_afficher())
print(c.get_afficher_solde())
c.set_versement(10)
print(c.get_afficher_solde())
c.set_retrait(20)
c.set_retrait(200)

print(c2.get_afficher_solde())
c.virement(c2, 100)
print(c2.get_afficher_solde())