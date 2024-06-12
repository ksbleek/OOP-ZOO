from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species) -> None:
        super.__init__(name, species)
    
    def give_birth(self):
        print(f"{self.name} the {self.species} has given birth")