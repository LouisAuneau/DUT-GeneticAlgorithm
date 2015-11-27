import random
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

class Chemin:
    def setChemin(self, chemin):
        self.chemin = chemin
        
    def setEvaluation(self, evaluation):
        self.evaluation = evaluation
        
    def tracer(self, carte, fichier, couleur):
        # On recupere les coordonnees du chemin
        xChemin = []
        yChemin = []
        for ville in self.chemin:
            xChemin.append(carte.villes[ville].x)
            yChemin.append(carte.villes[ville].y)
            
        # On recupere les coordonnes des villes
        xVilles = []
        yVilles = []
        for ville in carte.villes:
            xVilles.append(ville.x)
            yVilles.append(ville.y)
        
        # On genere l'image
        fig = plt.figure() # On creer la figure
        ax = fig.add_subplot(111)
        ax.plot(xVilles, yVilles, linestyle='', marker='o', color='black') # On ajoute les points des villes
        ax.plot(xChemin, yChemin, linestyle="--", color=couleur) # On ajoute le chemin
        ax.axis([-2, 102, -2, 102]) # On gradue les axes
        ax.axis('off') #On ne les affiche plus
        fig.savefig(fichier) # On genere l'image
        
    @staticmethod
    def tracerChemins(carte, chemins, fichier, couleur):
        # On recupere les coordonnes des villes
        xVilles = []
        yVilles = []
        for ville in carte.villes:
            xVilles.append(ville.x)
            yVilles.append(ville.y)
            
        # On genere l'image
        fig = plt.figure() # On creer la figure
        ax = fig.add_subplot(111)
        ax.plot(xVilles, yVilles, linestyle='', marker='o', color='black') # On ajoute les points des villes
        ax.axis([-2, 102, -2, 102]) # On gradue les axes
        ax.axis('off') #On ne les affiche plus
            
        # On ajoute les chemins
        for chemin in chemins:
            # On recupere les coordonnees du chemin
            xChemin = []
            yChemin = []
            for ville in chemin.chemin:
                xChemin.append(carte.villes[ville].x)
                yChemin.append(carte.villes[ville].y)
            ax.plot(xChemin, yChemin, linestyle="--", color=couleur) # On ajoute le chemin
            
        fig.savefig(fichier) # On genere l'image
        