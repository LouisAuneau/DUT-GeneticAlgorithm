from Carte import Carte
from Ville import Ville
from Chemin import Chemin
from Genetique import Genetique
from random import randint

# Creation d'une carte
carte = Carte()
ville1 = Ville(0, 0)
ville2 = Ville(100, 0)
ville3 = Ville(0, 100)
ville4 = Ville(50, 60)
ville5 = Ville(70, 75)
ville6 = Ville(25, 40)
ville7 = Ville(40, 80)
ville8 = Ville(90, 15)
carte.ajoutVille(ville1)
carte.ajoutVille(ville2)
carte.ajoutVille(ville3)
carte.ajoutVille(ville4)
carte.ajoutVille(ville5)
carte.ajoutVille(ville6)
carte.ajoutVille(ville7)
carte.ajoutVille(ville8)

# Generation de la population initiale scahant que l'on a n! chemins possibles.
algo = Genetique(carte)
population = algo.getpopulationInitiale()
i = 1

while True:
    # Crossover de la population initiale
    algo.crossovers(population)
    
    # Evaluation de la population
    algo.evaluation(population)
    
    # Passage a la generation suivante
    population = algo.generationSuivante(population)

    # Affichage du resultat
    couleur = "#%06x" % randint(0, 0xFFFFFF)
    Chemin.tracerChemins(carte, population, "graphs/etape"+str(i)+".png", couleur)
    
    i = i+1
    
    if i > 8:
        break

for chemin in population:
    print str(chemin.chemin) + " -> " + str(chemin.evaluation)
population[0].tracer(carte, "graphs/final.png", "b")

