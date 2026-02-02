import math

class Cercle:
    def __init__(self, r=0):
        self.r = r
    def changerRayon(self, r):
        self.r = r
        return self.r

    def afficherInfos(self):
        return f"rayon : {self.r}, circonférence : {self.circonference()}, aire : {self.aire()}, diametre : {self.diametre()}"

    def circonference(self):
        return 2 * math.pi * self.r
    def aire(self):
        return math.pi * self.r * self.r
    def diametre(self):
        return self.r*2

cercle = Cercle()

print(cercle.afficherInfos())

cercle.changerRayon(4)
print(cercle.afficherInfos())

cercle.changerRayon(7)
print(cercle.afficherInfos())

cercle2 = Cercle(8)
print(f"{cercle2.afficherInfos()} ------------- {cercle.afficherInfos()}")