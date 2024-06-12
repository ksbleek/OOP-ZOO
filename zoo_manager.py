class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Animal sound")

class Mammal:
    def __init__(self, name, species) -> None:
        super.__init__(name, species)
    
    def give_birth(self):
        print(f"{self.name} the {self.species} has given birth")

class bird:
    def __init__(self, name, species, wingspan):
        super.__init__(name, species)
        self.wingspan = wingspan

class reptile:
    def __init__(self, name, species):
        super.__init__(name, species)

    def bask_in_sun(self):
        print(f"{self.name} the {self.species} is basking in the sun")

class Primate:
    def __init__(self, name, species):
        super.__init__(name, species)
    
    def climb_trees(self):
        print(f"{self.name} the {self.species} is climbing trees")

class Marsupial:
    def __init__(self, name, species):
        super.__init__(name, species)

    def carry_baby(self):
        print(f"{self.name} the {self.species} is carrying its baby")

