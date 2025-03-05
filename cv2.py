class Equipment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Equipment Name: {self.name}, ID: {self.id}"

class Furniture(Equipment):
    def __init__(self, id, name, legs):
        super().__init__(id, name)
        self.legs = legs

    def __str__(self):
        return f"Equipment Name: {self.name}, ID: {self.id}, Legs: {self.legs}"

class Electronics(Equipment):
    def __init__(self, id, name, power):
        super().__init__(id, name)
        self.power = power

    def __str__(self):
        return f"Equipment Name: {self.name}, ID: {self.id}, Power: {self.power}"

class WashingMachine(Electronics):
    def __init__(self,id, name, power, weight):
        super().__init__(id, name, power)
        self.weight = weight

    def __str__(self):
        return f"Equipment Name: {self.name}, ID: {self.id}, Power: {self.power}, Weight: {self.weight}"

class Household:
    def __init__(self):
        self.items = {}

    def add(self, eq:Equipment):
        self.items[eq, id] = eq

    def __str__(self):
        result = ""
        for id, eq in self.items.items():
            result += str(eq) + "\n"
        return result

a = Furniture(104, "Židle", 4)
b = Electronics(108,"pracka", 220)
c = WashingMachine(200,"machine", 220, 40)

house = Household()
house.add(a)
house.add(b)

print(house)