from math import sqrt
from math import pow

class Carte:
    def __init__(self):
        self.villes = []
        
    def ajoutVille(self, ville):
        self.villes.append(ville)
        
    def getVille(self, xVille, yVille):
        for ville in self.villes:
            if ville.x == xVille and ville.y == yVille:
                return ville
        return null
        
    def getDistance(self, ville1, ville2):
        ville1 = self.villes[self.villes.index(ville1)]
        ville2 = self.villes[self.villes.index(ville2)]
        return abs(sqrt(pow(ville2.x - ville1.x, 2) + pow(ville2.y - ville1.y, 2)))
            