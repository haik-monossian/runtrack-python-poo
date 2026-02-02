class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y
    def gauche(self):
        self.x -= 1
        return self.x
    def droite(self):
        self.x += 1
        return self.x
    def haut(self):
        self.y += 1
        return self.y
    def bas(self):
        self.y -= 1
        return self.y
    def position(self):
        return (self.x, self.y)

personnage = Personnage()
print(personnage.position())

personnage.gauche()
print(personnage.position())

personnage.droite()
personnage.droite()

print(personnage.position())

personnage.bas()
print(personnage.position())

personnage.haut()
personnage.haut()

print(personnage.position())