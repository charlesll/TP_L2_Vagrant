#
# Import des bibliotheques pour utiliser les outils de Python
#

from pylab import *

#
# CHARGEMENT DES DONNEES
#

# On charge le fichier dans lequel sont rangees les valeurs experimentales

monfichier = 'data.txt' # variable qui porte le nom de notre fichier

# chargement des valeurs du fichier dans un tableau Python nommé data
data = loadtxt( monfichier, delimiter = ',')

# De ce tableau, on cree deux vecteurs, correspondant aux 2 premieres colonnes du tableau data
masse, allongement = data.T		# en g, mm

# On definit les incertitudes totales sur chacune des deux variables (a vous de remplir cette ligne...)
erreur_masse = 0.1 # En g
erreur_allongement =  0.1# En mm

#
# TRAITEMENT DES DONNEES
#

# Vous pouvez faire ici tous les calculs nécessaires

# dans notre cas : creation de la variable force,
# dans la bonne unite, en travaillant la variable masse
force = masse *1.e-3 *9.81 #en N
erreur_force = erreur_masse*1.e-3 *9.81 #en N

# On met la variable allongement en unite SI
allongement = allongement *1.e-3 #en m
erreur_allongement = erreur_allongement*1.e-3 #en m

#
# COURBE DE TENDANCE
#

# Nous allons creer une courbe de tendance affine
# passant par les points experimentaux grace a la fonction polyfit(x,y,n)
# du package numpy.

coefficients= polyfit(allongement,force,1)
a = coefficients[0] # en N/m
b = coefficients[1] # en N

#
# TRACES DES DONNEES
#

# Voir la documentation de matplotlib pour comprendre les fonctions ci-dessous.
# Le site suivant donne des informations utiles:
# https://courspython.com/introduction-courbes.html

# Ouvre une fenetre pour creer une figure, qui portera le numero 1
figure(1)

# on trace force en fonction d allongement, sous forme de points, avec les barres d erreur
errorbar(allongement, force, xerr=erreur_allongement,yerr=erreur_force,fmt='o',color='blue', label="Données")

# on trace la courbe de tendance, en pointilles rouge, avec une taille de line de 2pt...
plot(allongement, a*allongement+b, linestyle='--',linewidth=2,color='red', label = "ajustement linéaire")

# On donne un nom aux axes...
xlabel('Allongement $\Delta x$ (m)'  )
ylabel('Force (N)'  )

# ... et une légende à la figure
legend(loc='best')

# On laisse matplotlib rendre notre graphique plus beau
tight_layout()

# on enregistre la figure, au format .pdf, dans le dossier courant
savefig("notre_figure.pdf")
