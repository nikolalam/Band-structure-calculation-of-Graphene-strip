import matplotlib.pyplot as plt
import numpy as np
import cmath

D = 100
a = np.sqrt(3)
t1 = 1
t2 = 0.03
#plt.style.use('ggplot')

def Hamiltonian(k,phi,m):
    H = np.zeros( (D*2, D*2) )
    spin = -1
    for i in range(D):
        for j in range(0 + i, D):
            if (i == j) and i % 2 == 0:
                H[i][j] = -m + 2 * t2 * np.cos(2 * k - phi) * spin
            elif (i == j) and i % 2 != 0:
                H[i][j] = m + 2 * t2 * np.cos(2 * k + phi) * spin
            elif (i == j - 1) and (i % 2 == 0):
                H[i][j] = t1 * 2 * (np.cos(k))
                H[j][i] = t1 * 2 * (np.cos(k))
            elif (i == j - 1) and (i % 2 == 1):
                H[i][j] = t1
                H[j][i] = t1
            elif (i == j - 2) and (i % 2 == 0):
                H[i][j] = 2 * t2 * np.cos(k + phi) * spin
                H[j][i] = 2 * t2 * np.cos(k + phi) * spin
            elif (i == j - 2) and (i % 2 == 1):
                H[i][j] = 2 * t2 * np.cos(k - phi) * spin
                H[j][i] = 2 * t2 * np.cos(k - phi) * spin

    spin = 1
    for i in range(D,D*2):
        for j in range(0 + i, D*2):

            if (i == j) and i % 2 == 0:
                H[i][j] = -m + 2 * t2 * np.cos(-2 * k - phi) * spin
            elif (i == j) and i % 2 != 0:
                H[i][j] = m + 2 * t2 * np.cos(-2 * k + phi) * spin
            elif (i == j - 1) and (i % 2 == 0):
                H[i][j] = t1 * 2 * (np.cos(k))
                H[j][i] = t1 * 2 * (np.cos(k))
            elif (i == j - 1) and (i % 2 == 1):
                H[i][j] = t1
                H[j][i] = t1
            elif (i == j - 2) and (i % 2 == 0):
                H[i][j] = 2 * t2 * np.cos(-k + phi) * spin
                H[j][i] = 2 * t2 * np.cos(-k + phi) * spin
            elif (i == j - 2) and (i % 2 == 1):
                H[i][j] = 2 * t2 * np.cos(-k - phi) * spin
                H[j][i] = 2 * t2 * np.cos(-k - phi) * spin
    return H

x_val = np.linspace(0,2*np.pi/2,500)
y_val = []

for i in range(D*2):
    data = []
    y_val.append(data)

for i in range(len(x_val)):
    ma = Hamiltonian(x_val[i], phi = np.pi/2, m=0)
    en = np.linalg.eigvalsh(ma)
    for j in range(len(en)):
        y_val[j].append(en[j])
        print('We are working in ', i, 'of', len(x_val), 'step')



for i in range(D*2):
    plt.plot( x_val, y_val[i] , color='black')
plt.ylim(-1, 1)
plt.title('kane and mele model of zigzag Graphene' r"$\quad E(k_{x})$ vs $k_{x}$" )
plt.xlabel(r"$k_{x}$")
plt.ylabel(r"$E(k_{x})$")
