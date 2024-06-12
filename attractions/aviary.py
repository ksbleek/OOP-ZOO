from ..animals.bird import Bird

birds = []

class Aviary(Bird):
    
    def __init__(self, name, species, wingspan):
        super().__init__(name, species, wingspan)
    
        Aviary.birds.append(self)