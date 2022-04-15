import tkinter as tk
import time

HEIGHT = 530
WIDTH = 600
ec = 15
obj = [1]
player = 0
liste_couleurs = [0]
a = WIDTH//7
variable_efface = []

racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "blue")
canvas.grid()

for n in range(6):
    for i in range(7):
        obj.append(canvas.create_oval((0+(70+ec)*i,20+(70+ec)*n),(70+(70+ec)*i,(70+20)+(70+ec)*n), fill = "white"))
        liste_couleurs.append(0)

def couleur(x):
    global obj, liste_couleurs, player, variable_efface
    if player%2 == 0:
        col = "red"
        y = 1
    else:
        col = "yellow"
        y = 2
    while liste_couleurs[x] != 0:
        x -=7
    canvas.itemconfigure(obj[x], fill = col)
    variable_efface.append(x)
    liste_couleurs[x] = y

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
    if 0 < event.x < 70:
        couleur(36)
        gagnant()
    elif 85 < event.x < 155:
        couleur(37)
        gagnant()
    elif 170 < event.x < 240:
        couleur(38)
        gagnant()
    elif 255 < event.x < 325:
        couleur(39)
        gagnant()   
    elif 340 < event.x < 410:
        couleur(40)
        gagnant()
    elif 425 < event.x < 495:
        couleur(41)
        gagnant()
    elif 510 < event.x < 580:
        couleur(42)
        gagnant()

def gagnant():
    global liste_couleurs
    cpt = 0
    for i in range(5):
        if liste_couleurs[1+i] == liste_couleurs[2+i] and liste_couleurs[1] != 0:
            cpt += 1
            print(cpt)
        else:
            cpt = 0
        if cpt == 4 :
            print("gagnant")
        


bouton1 = tk.Button(text = "effacer", command = efface)
bouton1.grid(column = 0, row = 1)
canvas.bind("<Button-1>", clic)
racine.mainloop()