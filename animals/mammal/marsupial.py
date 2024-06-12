from mammal import Mammal

class Marsupial(Mammal):
    def __init__(self, name, species):
        super.__init__(name, species)

    def carry_baby(self):
        print(f"{self.name} the {self.species} is carrying its baby")