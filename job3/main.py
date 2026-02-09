class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, valeur):
        self.__longueur = valeur

    def set_largeur(self, valeur):
        self.__largeur = valeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur



class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur


mon_rectangle = Rectangle(10, 5)

print(f"Longueur: {mon_rectangle.get_longueur()}")
print(f"Largeur: {mon_rectangle.get_largeur()}")
print(f"Périmètre: {mon_rectangle.perimetre()}")
print(f"Surface: {mon_rectangle.surface()}")

mon_rectangle.set_longueur(20)
print(f"Nouvelle longueur: {mon_rectangle.get_longueur()}")
print(f"Nouvelle surface: {mon_rectangle.surface()}")

mon_pave = Parallelepipede(10, 5, 2)
print(f"Volume du parallélépipède: {mon_pave.volume()}")