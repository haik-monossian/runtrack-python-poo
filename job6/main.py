class Animal:
    def __init__(self, age=0, prenom=None):
        self.age = age
        self.prenom = prenom
    def veillir(self):
        self.age += 1
        return self.age
    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom
        
animal = Animal()
print(animal.prenom)

print(f"l'age de l'animal est de {animal.age} ans")
print(f"l'age de l'animal est de {animal.veillir()} ans")
print(f"l'age de l'animal est de {animal.veillir()} ans")
print(f"l'age de l'animal est de {animal.veillir()} ans")

animal.nommer("Robert")
print(f"l'animal se nomme {animal.prenom}")
print(f"l'animal se nomme {animal.nommer("Albert")}")