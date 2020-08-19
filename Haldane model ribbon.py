import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import eigvalsh


t1 = 1
D = 100
a = np.sqrt(3)
t2 = 1/3
phi = np.pi/2
m = a * 3 * t2 * 0.5
#plt.style.use('ggplot')

def Initialise(k):
    H = np.zeros((D,D))
    for i in range(D):
        for j in range(0 + i,D):
            if (i == j) and i % 2 ==0:
                H[i][j] = -m + 2 * t2 * np.cos(k*a - phi)
            elif (i == j) and i % 2 != 0:
                H[i][j] = m + 2 * t2 * np.cos(k*a + phi)
            elif (i == j - 1 ) and (i % 2  ==  0 ):
                H[i][j] = t1 *  2 * np.cos(k*a/2)
                H[j][i] = t1 * 2 * np.cos(k*a/2)
            elif (i == j - 1 ) and (i % 2  ==  1 ):
                H[i][j] = t1
                H[j][i] = t1
            elif ( i == j - 2 ) and ( i % 2 == 0 ):
                H[i][j] = 2 * t2 * np.cos(k*a/2 + phi)
                H[j][i] = 2 * t2 * np.cos(k*a/2 + phi)
            elif ( i == j - 2 ) and ( i % 2 == 1 ):
                H[i][j] = 2 * t2 * np.cos(k*a/2 - phi)
                H[j][i] = 2 * t2 * np.cos(k*a/2 - phi)
    return H

x_val = np.linspace(0, 2 * np.pi/a, 1001)
y_val =[]
for i in range(D):
    y_val.append([])


for i in range( len(x_val) ):
    mat = Initialise(x_val[i])
    en = eigvalsh(mat)
    #en = np.sort(en)
    for j in range(D):
        y_val[j].append(en[j])
    print('We are working in ',i, 'of', len(x_val), 'step' )

plt.figure(1)
for i in range(D):
    plt.plot( x_val, y_val[i] , color='black')
#plt.ylim(-1, 1)
plt.title( 'Energy spectrum of Haldane graphene ribbon  vs ' r"$k_{x}$" 'with' r"$|M| < |3t_{2}\sqrt{3}sin\phi|$")
plt.xlabel(r"$k_{x}$")
plt.ylabel('Energy' r"$\quad E(k_{x})$")

###################################################################################################


m =  a * 3 * t2
y_val_2 =[]
for i in range(D):
    y_val_2.append([])


for i in range( len(x_val) ):
    mat = Initialise(x_val[i])
    en = eigvalsh(mat)
    #en = np.sort(en)
    for j in range(D):
        y_val_2[j].append(en[j])
    print('We are working in ',i, 'of', len(x_val), 'step' )
plt.figure(2)

for i in range(D):
    plt.plot( x_val, y_val_2[i] , color='black')
#plt.ylim(-2, 2)
plt.title( 'Energy spectrum of haldane graphene ribbon  vs 'r"$k_{x}$ t2 = 0.13" 'with' r"$|M| = |3t_{2}\sqrt{3}sin\phi|$")
plt.xlabel(r"$k_{x}$")
plt.ylabel('Energy' r"$\quad E(k_{x})$")

###################################################################################################

m =  a * 3 * t2 * 1.5
y_val_2 =[]
for i in range(D):
    y_val_2.append([])


for i in range( len(x_val) ):
    mat = Initialise(x_val[i])
    en = eigvalsh(mat)
    #en = np.sort(en)
    for j in range(D):
        y_val_2[j].append(en[j])
    print('We are working in ',i, 'of', len(x_val), 'step' )
plt.figure(3)

for i in range(D):
    plt.plot( x_val, y_val_2[i] , color='black')
#plt.ylim(-2, 2)
plt.title( 'Energy spectrum of haldane graphene ribbon  vs 'r"$k_{x}$ t2 = 0.13" 'with' r"$|M| > |3t_{2}\sqrt{3}sin\phi|$")
plt.xlabel(r"$k_{x}$")
plt.ylabel('Energy' r"$\quad E(k_{x})$")


