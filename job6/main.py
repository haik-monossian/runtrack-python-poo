class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre proprement. Vroum !")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("La moto vrombit et s'élance !")


ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

print("-" * 15)

ma_moto = Moto("Yamaha", "MT-07", 2021, 7500)
ma_moto.informationsVehicule()
ma_moto.demarrer()