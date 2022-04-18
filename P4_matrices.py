import tkinter as tk
import time

HEIGHT = 530
WIDTH = 600
ec = 15
obj = []
player = 0
liste_couleurs = []
a = WIDTH//7
variable_efface = []
l = []
lc = []

racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "blue")
canvas.grid()

for n in range(6):
    for i in range(7):
        l.append(canvas.create_oval((0+(70+ec)*i,20+(70+ec)*n),(70+(70+ec)*i,(70+20)+(70+ec)*n), fill = "white"))
        lc.append(0)
    obj.append(l)
    liste_couleurs.append(lc)
    l = []
    lc = []
print(obj)
print(liste_couleurs)


def couleur(x):
    global obj, liste_couleurs, player, variable_efface
    if player%2 == 0:
        col = "red"
        y = 1
    else:
        col = "yellow"
        y = 2
    b = 5
    while liste_couleurs[b][x] != 0:
        b -=1
    canvas.itemconfigure(obj[b][x], fill = col)
    variable_efface.append(x)
    liste_couleurs[b][x] = y

def efface():
    global variable_efface, obj
    canvas.itemconfigure(obj[variable_efface[-1]], fill = "white")
    liste_couleurs[variable_efface[-1]] = 0
    del variable_efface[-1]




def clic(event):
    global player
    player += 1
    if 0 < event.x < 70:
        couleur(0)
        gagnant()
    elif 85 < event.x < 155:
        couleur(1)
        gagnant()
    elif 170 < event.x < 240:
        couleur(2)
        gagnant()
    elif 255 < event.x < 325:
        couleur(3)
        gagnant()   
    elif 340 < event.x < 410:
        couleur(4)
        gagnant()
    elif 425 < event.x < 495:
        couleur(5)
        gagnant()
    elif 510 < event.x < 580:
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
                print("gagnant rougec lin")
            if cpt_j == 4:
                print("gagnant jaune, lin")
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
                print("gagnant rouge, col")
            if cpt_j == 4:
                print("gagnant jaune, col")
    
        


bouton1 = tk.Button(text = "effacer", command = efface)
bouton1.grid(column = 0, row = 1)
canvas.bind("<Button-1>", clic)
racine.mainloop()