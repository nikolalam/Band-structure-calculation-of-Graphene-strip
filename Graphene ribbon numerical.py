import matplotlib.pyplot as plt
import numpy as np
from sympy.plotting import plot

D  = 70  #Dimension of the Hamiltonain
a = np.sqrt(3)
t = 1
#plt.style.use('ggplot')

def Initialise(H,kx):
    for i in range(0,D):
        for j in range(0+i ,D ):
            if i == j:
                H[i][j] = 0
            elif ( (i == j + 1) or ( i == j - 1 ) ) and (i % 2  == 0 ) :
                H[i][j] = 2 * t * ( np.cos(kx * a /2) )
                H[j][i] = 2* t * ( np.cos(kx * a /2) )
            elif ((i == j + 1) or (i == j - 1)) and (i % 2 == 1):
                H[i][j] = t
                H[j][i] = t
    return H

x_value = np.linspace(0, 2 * np.pi / a ,500)
y_val = []

for i in range(D):
    y_val.append([])

for i in range(len(x_value) ):
    H = np.zeros((D, D))
    He= Initialise(H,x_value[i])
    en = np.linalg.eigvals(He)
    en = np.sort(en)
    for j in range(D):
        y_val[j].append(en[j])
    print('We are working in ',i, 'of', len(x_value), 'step' )

plt.figure(1)
for i in range(D):
    plt.plot( x_value, y_val[i], color='black' )
plt.title( 'Energy spectrum of graphene ribbon with only nearest neighbor hopping vs 'r"$k_{x}$")
plt.xlabel(r"$k_{x}$")
plt.ylabel('Energy' r"$\quad E(k_{x})$")

plt.figure(2)
for i in range(D):
    plt.plot( x_value, y_val[i], color='black' )
plt.ylim(-1, 1)
plt.title( 'Energy spectrum of graphene ribbon with only nearest neighbor hopping vs 'r"$k_{x}$")
plt.xlabel(r"$k_{x}$")
plt.ylabel('Energy' r"$\quad E(k_{x})$")

