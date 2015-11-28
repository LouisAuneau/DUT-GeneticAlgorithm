# coding: utf8
from Carte import Carte
from Ville import Ville
from Chemin import Chemin
from Genetique import Genetique
from random import randint
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# Variables
results = []
carte = Carte()

# Creation d'une carte
ville1 = Ville(0, 0)
ville2 = Ville(100, 0)
ville3 = Ville(0, 100)
ville4 = Ville(50, 60)
ville5 = Ville(70, 75)
ville6 = Ville(25, 40)
ville7 = Ville(40, 80)
ville8 = Ville(90, 15)
ville9 = Ville(25, 80)
carte.ajoutVille(ville1)
carte.ajoutVille(ville2)
carte.ajoutVille(ville3)
carte.ajoutVille(ville4)
carte.ajoutVille(ville5)
carte.ajoutVille(ville6)
carte.ajoutVille(ville7)
carte.ajoutVille(ville8)
carte.ajoutVille(ville9)

# Generation de la population initiale scahant que l'on a n! chemins possibles.
algo = Genetique(carte)
population = algo.getpopulationInitiale()
i = 1

# Boucle de générations
while True:
    # Crossover de la population
    algo.crossovers(population)
    
    # Mutation de la population
    algo.mutation(population, carte)
    
    # Evaluation de la population
    algo.evaluation(population)
    
    # Passage a la generation suivante
    population = algo.generationSuivante(population, carte)

    # Enregistrement des resultats dans un graphe
    couleur = "#%06x" % randint(0, 0xFFFFFF)
    Chemin.tracerChemins(carte, population, "results/etape"+str(i)+".png", couleur)
    
    # Enregistrement des statistiques de la génération pour le graphe final (Moyenne de la longueur réelle des chemins dans la population)
    j= 0
    result = 0
    print "\nETAPE"
    for chemin in population:
        print chemin.calculDistanceReelle(carte)
        result = result + chemin.calculDistanceReelle(carte)
        j = j + 1
    results.append(result/j)

    # Passage à l'étape suivante
    i = i+1
    if i > 7:
        break



# Résultats finales
# -------------------------

# Tri de la population finale et choix du meilleur resultat
population[0].tracer(carte, "results/final.png", "black")
population = sorted(population, key=lambda chemin: chemin.evaluation)
results.append(population[0].calculDistanceReelle(carte))
print results

# Création du graphe de statistiques
fig = plt.figure() # On creer la figure
ax = fig.add_subplot(111)
ax.plot(range(1, len(results)+1), results, linestyle='-', marker='o', color='black') # On ajoute la moyenne des longueurs des chemins à chaque étape
fig.savefig("results/stats.png")