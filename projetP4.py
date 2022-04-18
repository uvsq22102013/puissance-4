import tkinter as tk
import time
from tracemalloc import stop

HEIGHT = 530
WIDTH = 600
ec = 15
obj = []

player = 0
liste_couleurs = []
a = WIDTH//7
variable_efface = []

racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "blue")
canvas.grid()

for n in range(6):
    obj_e=[]
    liste_couleurs_e=[]
    for i in range(7):
        obj_e.append(canvas.create_oval((0+(70+ec)*i,20+(70+ec)*n),(70+(70+ec)*i,(70+20)+(70+ec)*n), fill = "white"))
        liste_couleurs_e.append(0)
    obj.append(obj_e)
    liste_couleurs.append(liste_couleurs_e)

def couleur(x):
    global obj, liste_couleurs, player, variable_efface
    r=5
    if liste_couleurs[0][x]!=0:
        pass
        player -=1
    elif player%2 == 0:
        col = "red"
        y = 1
    else:
        col = "yellow"
        y = 2
    while liste_couleurs[r][x] != 0:
        r -=1
        
    canvas.itemconfigure(obj[r][x], fill = col)
    variable_efface.append([r,x])
    liste_couleurs[r][x] = y


def efface():
    global variable_efface, obj
    canvas.itemconfigure(obj[variable_efface[-1]], fill = "white")
    liste_couleurs[variable_efface[-1]] = 0
    del variable_efface[-1]

def animation(x):
    global obj, cercle
    cercle = canvas.create_oval((0,20),(70,90), fill = "yellow")
    bouge_cercle()

def bouge_cercle():
    global cercle
    canvas.move(cercle,0,5)
    canvas.after(20,bouge_cercle)


def clic(event):
    global player
    player += 1
    if 0 < event.x < 77:
        couleur(0)
        gagnant()
    elif 78 < event.x < 162:
        couleur(1)
        gagnant()
    elif 163 < event.x < 247:
        couleur(2)
        gagnant()
    elif 248 < event.x < 332:
        couleur(3)
        gagnant()
    elif 333 < event.x < 417:
        couleur(4)
        gagnant()
    elif 418 < event.x < 502:
        couleur(5)
        gagnant()
    elif 503 < event.x < 600:
        couleur(6)
        gagnant()

def gagnant():
    global liste_couleurs
    cpt_r = 0
    cpt_j = 0
    for i in range(6):
        for j in range(7):
            if liste_couleurs[i][j] == 1:
                cpt_r +=1
            else:
                cpt_r = 0
            if liste_couleurs[i][j] == 2:
                cpt_j +=1
            else:
                cpt_j = 0
            if cpt_r == 4:
                print("gagnant rouge")
            if cpt_j == 4:
                print("gagnant jaune")
    for i in range(7):
        for j in range(6):
            if liste_couleurs[j][i] == 1:
                cpt_r +=1
            else:
                cpt_r = 0
            if liste_couleurs[j][i] == 2:
                cpt_j +=1
            else:
                cpt_j = 0
            if cpt_r == 4:
                print("gagnant rouge")
                pass
            if cpt_j == 4:
                print("gagnant jaune")
                pass
        


bouton1 = tk.Button(text = "effacer", command = efface)
bouton1.grid(column = 0, row = 1)
canvas.bind("<Button-1>", clic)
racine.mainloop()