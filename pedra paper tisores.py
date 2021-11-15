#pedra paper tisores 
"""
import random 
def probabilitat(llista):
    sum_tot = sum(llista)
    max = 0     
    for x in llista: 
        if x//sum_tot > max:
            max = x
        

"""
import random
from warnings import resetwarnings #Made By Roger Bajona

posicio = 1

entrada_respostes_usuaris = [1, 2, 3, 2, 3]

entrada_respostes_usuaris_text = []

outputs = []

player_wins = 0 

machine_wins = 0 

repostes_possibles = [1, 2, 3, 2, 3]

pedra = 0  
paper = 0 
tisores = 0 

choice = repostes_possibles[posicio]

def render_respotes():
    global entrada_respostes_usuaris
    num_div =  len(entrada_respostes_usuaris) / 5   #numero pel qual dividir, per trobar la mitjana de cada 5 

    suma_de_tots = 0 

    mitjana_de_cinc = suma_de_tots / num_div

    for x in entrada_respostes_usuaris:
        suma_de_tots += x
        del repostes_possibles[0:5]

    while sum(repostes_possibles) != round(mitjana_de_cinc):
        for x in range(5):
            random.randint(1, 3)

        if sum(repostes_possibles) == round(mitjana_de_cinc):
            break 
        else: 
            del repostes_possibles[0:5]




while True:
    five_times = 0  #determina si han pasat cinc cops per tornat a executar el render de les respostes quant arribi a 5 s'executa
    resposta = 1 #definim aquesta resposta perquè és pugui determinar si s'ha guanyat o no 
    in_put = input("Pedra, paper o tisores? ")
    entrada_respostes_usuaris_text.append(in_put)
    if in_put == "pedra":
        pedra += 1
        resposta = 1
        entrada_respostes_usuaris.append(1)
    elif in_put == "paper":
        paper += 1
        resposta = 2
        entrada_respostes_usuaris.append(2)
    elif in_put == "tisores": 
        tisores += 1
        resposta = 3 
        entrada_respostes_usuaris.append(3)
    
    five_times += 1 
    
    if resposta == 1 or 2 and resposta == 3: 
        print("Molt bé!")
        player_wins += 1 
        #in_put += 1 
    elif resposta != choice:
        print("Has perdut =(")
        #input += 1 
        machine_wins += 1 
        posicio += 1 
    posicio += 1 
    if five_times == 5: 
        render_respotes()
        five_times = 0 
        posicio = 1     #resetejem posició del choice


