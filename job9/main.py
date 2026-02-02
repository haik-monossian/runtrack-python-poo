# La nomenclature des méthodes est basée sur le pdf exercices, le snake case est préférable pour les méthodes

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA # en 0. quelquechose 
    def CalculerPrixTTC(self):
        return f"{self.prixHT - (self.prixHT * self.TVA)} €"
    
    def afficher(self):
        return f"nom : {self.nom}, prixHT : {self.prixHT} €, TVA : {self.TVA*100} %"

    def modifier_nom(self, nom):
        self.nom = nom

    def modifier_prix (self, prixHT):
        self.prixHT = prixHT

    def modifier_nom_et_prix(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT


#Initialiser les produits
produit1 = Produit("Table", 20, 0.2)
produit2 = Produit("chaise", 10, 0.4)
produit3 = Produit("tapis", 40, 0.05)
produit4 = Produit("gourde", 1, 0.2)

#Afficher les produits
print(produit1.afficher())
print(produit1.CalculerPrixTTC())
print(produit2.afficher())
print(produit2.CalculerPrixTTC())
print(produit3.afficher())
print(produit3.CalculerPrixTTC())
print(produit4.afficher())
print(produit4.CalculerPrixTTC())


print("changement de nom et de prix")
produit1.modifier_nom_et_prix("Bureau", 15)
print(produit1.afficher())
print(produit1.CalculerPrixTTC())

print("changement de nom")
produit1.modifier_nom("Nom")
print(produit1.afficher())

print("changement de prix")
produit1.modifier_prix(44)
print(produit1.afficher())