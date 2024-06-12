from mammal import Mammal

class Primate(Mammal):
    def __init__(self, name, species):
        super.__init__(name, species)
    
    def climb_trees(self):
        print(f"{self.name} the {self.species} is climbing trees")