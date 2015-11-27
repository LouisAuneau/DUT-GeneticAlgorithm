from math import ceil
from math import factorial
from math import floor
from random import sample
from Chemin import Chemin

class Genetique:
    def __init__(self, carte):
        self.carte = carte
        
    def getpopulationInitiale(self):
        # Calcul de la taille de la population initiale
        nbVilles = len(self.carte.villes)
        if(nbVilles > 5):
            taillePopInitiale = 150
        else:
            taillePopInitiale = int(ceil(0.5*factorial(nbVilles)))
            
        # Generation de la population initiale
        popInitiale = []
        for i in range(0, taillePopInitiale):
            chemin = Chemin()
            chemin.setChemin(sample(xrange(nbVilles), nbVilles))
            popInitiale.append(chemin)
        return popInitiale
        
    def evaluation(self, chemins):
        nbVilles = len(chemins[0].chemin)
        nbEvaluations = int(floor((nbVilles+5)/5))
        evaluations = sample(range(0, nbVilles), nbEvaluations)
        
        for chemin in chemins:
            chemin.setEvaluation(self.evaluationChemin(chemin, evaluations))
        
    def evaluationChemin(self, chemin, evaluations):
        distance = 0
        for evaluation in evaluations:
            if evaluation > 0:
                distance = distance + self.carte.getDistance(self.carte.villes[chemin.chemin[evaluation-1]], self.carte.villes[chemin.chemin[evaluation]])
            else:
                distance = distance + self.carte.getDistance(self.carte.villes[chemin.chemin[len(chemin.chemin)-1]], self.carte.villes[chemin.chemin[0]])
        #print str(chemin.chemin) + " - Evaluation de " + str(evaluations)
        
        return distance
    
    def crossovers(self, population):
        for i in range(0, len(population), 2):
            self.crossover(population[i], population[i+1])
            
                
    def crossover(self, chemin1, chemin2):
        # On genere les deux points de coupe
        nbVilles = len(chemin1.chemin)
        pointsCrossover = sample(range(0, nbVilles), 2)
        pointsCrossover.sort()
        
        # On echange les villes des deux chemins entre les deux points de coupe et on enleve si il y a un doublon
        villesManquantesChemin1 = []
        villesManquantesChemin2 = []
        for i in range(pointsCrossover[0], pointsCrossover[1]+1):
            chemin1.chemin[i], chemin2.chemin[i] = chemin2.chemin[i], chemin1.chemin[i]
            # Gestion des doublons hors de la zone de coupe
            for j in range(0, nbVilles):
                if j not in range(pointsCrossover[0], pointsCrossover[1]+1):
                    if chemin1.chemin[i] == chemin1.chemin[j]:
                        villesManquantesChemin2.append(chemin1.chemin[j])
                        chemin1.chemin[j] = -1
                    if chemin2.chemin[i] == chemin2.chemin[j]:
                        villesManquantesChemin1.append(chemin2.chemin[j])
                        chemin2.chemin[j] = -1
        
        # Ajout des villes manquantes
        for i in range(0, nbVilles):
            if chemin1.chemin[i] == -1:
                chemin1.chemin[i] = villesManquantesChemin1[0]
                villesManquantesChemin1.pop(0)
            if chemin2.chemin[i] == -1:
                chemin2.chemin[i] = villesManquantesChemin2[0]
                villesManquantesChemin2.pop(0)
    
    def generationSuivante(self, population):
        moitier = int(ceil((len(population)/2) / 2.) * 2)
        population = sorted(population, key=lambda chemin: chemin.evaluation)
        nouvellePopulation = []
        for i in range(0, moitier):
            nouvellePopulation.append(population[i])
        return nouvellePopulation
        
        
        
        