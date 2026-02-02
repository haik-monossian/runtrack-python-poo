class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        return f"coordonnée en x : {self.x} et en y : {self.y}"
    def afficherX(self):
        return f"coordonnée en x : {self.x}"
    def afficherY(self):
        return f"coordonnée en y : {self.y}"
    def changerX(self, x):
        self.old_x = self.x
        self.x = x
        return f"coordonnée changée de x : {self.old_x} en x : {self.x}"
    def changerY(self, y):
        self.old_y = self.y
        self.y = y
        return f"coordonnée changée de y : {self.old_y} en y : {self.y}"

point = Point(4, 2)
print(point.afficherLesPoints())
print(point.afficherX())
print(point.afficherY())
print(point.changerX(9))
print(point.changerY(30))