# -*- coding: utf-8 -*- 

"""BUT : 

Tracer l'image d'un point objet A par un dioptre plan séparant des milieux
d'indices n1. Le dioptre est l'axe des abscisses, le milieu 1 est en bas et le 
milieu 2 en haut. Le point A est pris sur l'axe des ordonnées avec une ordonnée
négative, on a donc : 
A (x_A = 0 , y_A < 0)

On oriente les angles positivement dans le sens trigonométrique.
Pour un angle d'incidence theta tel que -pi/2 < theta < 0 , on a : 

1 - Détermination du point B, intersection du rayon avec l'axe des abscisses :
angle entre l'axe des abscisses et le rayon incident : 
    a_B = pi/2 + theta
longueur du rayon qui annule l'ordonnée du point B :
    r_B = -y_A/sin(a_B)
coordonnées du point 
B(cos(a_B)*r_B , 0)

2 - Détermination du point C, point terminal du rayon réfracté, d'ordonnée y_C :
angle de réfraction : 
    theta_=arcsin(n1/n2*sin(theta))
angle entre l'axe des abscisses et le rayon réfracté : 
    a_C = pi/2+theta_
longueur du rayon réfracté qui impose l'ordonnée y_C > 0 :
    r_C = (y_C-y_B)/sin(a_C)
coordonnées du point C : 
C(cos(a_C)*r_C,y_C)

2 - Détermination du point D, point terminal du prolongement du rayon réfracté,
dans le milieu 1, d'ordonnée y_D < 0 :
angle entre l'axe des abscisses et le prolongement du rayon réfracté : 
    a_D = a_C
longueur du rayon réfracté qui impose l'ordonnée y_D :
    r_D = (y_D-y_B)/sin(a_D)
coordonnées du point D : 
D(cos(a_D)*r_D,y_D)

Attention : pour l'instant, le script ne tient pas compte du phénomène de 
réflexion totale...
"""

from pylab import *

close('all')

################################################################################
# Paramètres :
################################################################################
n1 = 1.
n2 = 1.03
x_A=0.
y_A = -1. # négatif !
theta=linspace(-1.2,-pi/2, 6,endpoint=False) # négatifs
y_B = 0.
y_C=0.5
y_D=-2.

# Si on veut demander les indices : 
#n1 = float(raw_input('Indice du milieu 1 ?\n'))
#n2 = float(raw_input('Indice du milieu 2 ?\n'))

################################################################################
# Initialisation du graph et :
################################################################################
fig=figure('image_dioptre_plan')
ax=fig.add_subplot(1,1,1)


################################################################################
# Points B et rayons incidents :
################################################################################
a_B = pi/2 + theta
r_B = -y_A/sin(a_B)
x_B=cos(a_B)*r_B

for x in x_B : 
    ax.plot([x_A,x],[y_A,y_B],color='red')

################################################################################
# Points C et rayons réfractés :
################################################################################
theta_=arcsin(n1/n2*sin(theta))
a_C = pi/2 + theta_
r_C = (y_C-y_B)/sin(a_C)
x_C=x_B+cos(a_C)*r_C

for x1,x2 in zip(x_B,x_C) : 
    ax.plot([x1,x2],[y_B,y_C],color='red')
    
################################################################################
# Points D et pronlongement des rayons réfractés :
################################################################################
a_D = a_C
r_D = (y_D-y_B)/sin(a_D)
x_D=x_B+cos(a_D)*r_D

for x1,x2 in zip(x_B,x_D) : 
    ax.plot([x1,x2],[y_B,y_D],color='red',linestyle='--')
    
################################################################################
# tracé du dioptre et élimination des ticks :
################################################################################
xticks([])
yticks([])
x_min=min([min(x) for x in [x_C,x_B,x_D]])
x_max=max([max(x) for x in [x_C,x_B,x_D]])
ax.plot([x_min,x_max],[0,0],color='k')
