import matplotlib.pyplot as plt

import numpy as np

from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots()

xdata, ydata = [], []

ln, = plt.plot([], [], 'ro')

           

x0 = float(input("x0: "))

y0 = float(input("y0: "))



gravetat_p = float(4.9)



vx0 = float(input("vx0: "))

vy0 = float(input("vy0: "))



coordenada_x_t = {}

coordenada_x = []

temps = 0

coordenada_y_t = {}

coordenada_y_ = []



velocitat_x = []

velocitat_y = []



while True:

    

    temps += 0.15

    coordenades___y = float(y0 + vy0 * temps - gravetat_p * temps**2) 

    coordenades___x = float(x0 + vx0 * temps )

    coordenada_y_.append(coordenades___y)

    coordenada_x.append(coordenades___x)

    

    if coordenada_y_[-1] <= 0:

          break



print(coordenada_y_[-1])

print(coordenada_x[-1])

print(temps)





def init():

    ax.set_xlim(0, max(coordenada_x))

    ax.set_ylim(-1, max(coordenada_y_)+1)

    return ln,



def update(frame):

    ln.set_data(coordenada_x[frame],coordenada_y_[frame])

    return ln,	



ani = FuncAnimation(fig, update, frames=range(0,len(coordenada_x)),

                    init_func=init,blit=True)

                    

plt.show() 

