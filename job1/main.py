class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def ajouter_habitant(self):
        self.__habitants += 1

    def get_ville(self):
        return (self.__nom, self.__habitants)

class Personne:
    def __init__(self, nom, age, ville: Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

        self.ajouter_population() # On ajoute ça pour incrémenter automatiquement 
        
    def ajouter_population(self):
        self.__ville.ajouter_habitant()

paris = Ville("Paris", 10000)
print(paris.get_ville())
marseille = Ville("Marseille", 2000)
print(marseille.get_ville())

a = Personne("John", 40, paris)
b = Personne("Crista", 30, marseille)
c = Personne("Joseph", 20, paris)


print(paris.get_ville())
print(marseille.get_ville())