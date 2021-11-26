import matplotlib as plt

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


while True:
    
    temps += 0.0001 
    coordenades___y = float(y0 + vy0 * temps - gravetat_p * temps**2) 
    coordenades___x = float(x0 + vx0 * temps )
    coordenada_y_.append(coordenades___y)
    coordenada_x.append(coordenades___x)
    

    if coordenada_y_[-1] <= 0:
        break


print(coordenada_y_[-1])
print(coordenada_x[-1])
print(temps)

plt.style.use("bmh")
plt.scatter(coordenada_x, coordenada_y_)
plt.show() 

