#Informe: https://docs.google.com/document/d/11NaIaZwYPun4qE8nseQSdyG-gVu_HgKF8nTu3j5SVgw/edit?usp=sharing 

#Importem les llibreries 

import matplotlib.pyplot as plt 

import numpy as np	

from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots()

#Definim les variables i llistes 

llistax = []

zerosx = []

zerosy = []

# La funció ts ens permet regular la intensitat 

Ts = 0.02



fig, ax = plt.subplots()

xdata, ydata = [], []

ln, = plt.plot([], [], 'ro')

           
#demanem que l'usuari entri les dades
	
x0 = float(input("x0: "))

y0 = float(input("y0: "))



gravetat_p = float(4.9)

gravetat_completa = float(9.8)

vx0 = float(input("vx0: "))

vy0 = float(input("vy0: "))



coordenada_x_t = {}

coordenada_x = []

temps = 0

coordenada_y_t = {}

coordenada_y_ = []



velocitat_x = []

velocitat_y = []



while True: #Creem un bucle per tal de generat tots els "punts de dades" 

	    

    temps += 0.15

    coordenades___y = float(y0 + vy0 * temps - gravetat_p * temps**2) 

    coordenades___x = float(x0 + vx0 * temps )

    coordenada_y_.append(coordenades___y)

    coordenada_x.append(coordenades___x)

    zerosx.append(0)

    zerosy.append(0)

    llistax.append(vx0)

    velocitat_y.append(float(vy0 - gravetat_completa ** temps)) 



    if coordenada_y_[-1] <= 0: #Trenquem el bucle quan l'objecte arriba a l'altura del terra 

    	break



print(coordenada_y_[-1]) #Imprimim els resultats de les operacions 

print(coordenada_x[-1])

print(temps)


ax.quiver(coordenada_x, coordenada_y_, velocitat_x, zerosy) #Creem vectors per tal de projectar-los posteriorment 



def init(): #Creem el gràfic i el presentem 

    ax.set_xlim(0, max(coordenada_x))

    ax.set_ylim(-1, max(coordenada_y_)+1)

    return ln,

    

def update(frame): 

	ln.set_data(coordenada_x[frame],coordenada_y_[frame])

	ax.quiver(coordenada_x[frame], coordenada_y_[frame], velocitat_x[frame], zerosy[frame]) 



	return ln, r							

	
ani = FuncAnimation(fig, update, frames=range(0,len(coordenada_x)), #Finalment, creem l'animació, i fem moure el punt

                    init_func=init,blit=True, interval = Ts*1000)


plt.show() 
