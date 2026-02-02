class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

operation1 = Operation(12,3)
operation2 = Operation(2,3)

print(operation1.addition(), operation2.addition())