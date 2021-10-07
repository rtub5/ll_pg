import random
import datetime


llargada_llista = int(input("De quina llargada vols que sigui la llista? "))
numero_buscar = int(input("Quin numero vols buscar? "))

temps1 = datetime.datetime.now()

numeros_cercats = 0 

posicions = []

llista=[]

for i in range(1, llargada_llista):
    llista=llista+[random.randint(1,1000)]

while True:
    if numero_buscar in llista:
        while numeros_cercats != len(llista):
            if llista[numeros_cercats] == numero_buscar:
                numeros_cercats += 1
                posicions.append(numeros_cercats)
            else:
                numeros_cercats += 1
        break
    else:
        print("El nombre no es troba a llista.")
        break



temps2 = datetime.datetime.now()

temps = temps2 - temps1

print("Posicions del nombre", numero_buscar, "son: ", posicions)
print("Ha trigat: ", temps)