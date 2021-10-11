import random 

nombre_repeticions = 0 
llargada_llista = int(input("Llargada llista: "))
llista = []
llista_ordenada = []
llista_unica = []

for i in range(1, llargada_llista):
    llista=llista+[random.randint(1,llargada_llista)]
print("Llista original:", llista)

num_trobats = {}
for x in llista:
    if x in num_trobats:
        num_trobats[x] += 1
    else: 
        num_trobats[x] = 1 
print("Cada numero de la llista i quants cops és repeteix", num_trobats)

def ordenar_llista(): 
    while llista:
        minim = llista[0]
        for x in llista:
            if x < minim:
                minim = x
        llista_ordenada.append(minim)
        llista.remove(minim)

def valors_duplicats():
    global nombre_repeticions
    for x in llista_ordenada:
        if x in llista_unica:
            nombre_repeticions += 1
        else: 
            llista_unica.append(x) 
        

ordenar_llista()
valors_duplicats()

print("Nombre total de repeticions: ", nombre_repeticions)

print("La llista ordenada: ", llista_ordenada)
print("Lista ordenada i sense repeticions: ", llista_unica)
