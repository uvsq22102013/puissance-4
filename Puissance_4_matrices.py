##################################
# groupe MI 3
# Edgar BAGHDASARYAN
# Ali HARGAS
# Hatim ZELAMTA
# Anis FETOUAB
# https://github.com/uvsq22102013/puissance-4.git
###################################

import tkinter as tk
from tkinter import*
import random
import copy

HEIGHT = 530
WIDTH = 600
ec = 15
obj = []
player = 0
player2 = 0
liste_couleurs = []
a = WIDTH//7
variable_efface = []
name_P1 = ""
name_P2 = ""
cond_start = False

racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "blue")
canvas.pack(side="left")

def create_oval():
    """fonction créant des ronds blancs représentant les emplacements des pions"""
    l = []
    lc = []
    for n in range(6):
        for i in range(7):
            l.append(canvas.create_oval((0+(70+ec)*i,20+(70+ec)*n),(70+(70+ec)*i,(70+20)+(70+ec)*n), fill = "white"))
            lc.append(0)
        obj.append(l)
        liste_couleurs.append(lc)
        l = []
        lc = []
create_oval()

def joueur():
    """fonction choisissant aléatoirement le joueur qui commence"""
    global player
    player = random.randint(1,2)
    if player%2 == 0:
        txt = name_P1
    else:
        txt = name_P2
    label3 = tk.Label(text = txt + " " + "commence")
    label3.pack(side = "top")

def clic(event):
    """fonction repérant la position du clic pour appeler la fonction servant à placer le pion
    et la fonction qui repère le gagnant (s'il y en a un)"""
    global player
    if cond_start == True:
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

def couleur(x):
    """fonction définissant la couleur du pion en alternant entre rouge et jaune,
    puis elle repère un emplacement vide dans la colonne afin d'y afficher le pion déposé par le joueur"""
    global obj, liste_couleurs, player, variable_efface
    if liste_couleurs[0][x]!=0:
        pass
        player -=1
    elif player%2 == 0:
        col = "red"
        y = 1
    else:
        col = "yellow"
        y = 2
    player += 1
    b = 5
    while liste_couleurs[b][x] != 0:
        b -=1
    canvas.itemconfigure(obj[b][x], fill = col)
    variable_efface.append([b,x])
    liste_couleurs[b][x] = y

def gagnant():
    """fonction compteur qui appelle la fonction gagnant s'il y a au moins 4 pions de la même couleur alignés"""
    global liste_couleurs
    cpt_r = 0
    cpt_j = 0
    ##compteur de gagnant en ligne
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
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    ##compteur de gagnant en colonne
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
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    ##compteur de gagant en diagonale allant de la gauche vers la droite
    for i in range(3):
        for j in range(6-i):
            if liste_couleurs[i+j][0+j] == 1:
                cpt_r += 1
            else :
                cpt_r = 0
            if liste_couleurs[i+j][0+j] == 2:
                cpt_j += 1
            else :
                cpt_j = 0
            if cpt_r == 4:
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    ##compteur de gagnant en diagonale allant de la gauche vers la droite
    for i in range(3):
        for j in range(6-i):
            if liste_couleurs[j][1+i+j] == 1:
                cpt_r += 1
            else :
                cpt_r = 0
            if liste_couleurs[j][1+i+j] == 2:
                cpt_j += 1
            else :
                cpt_j = 0
            if cpt_r == 4:
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    ##compteur de gagnant en diagonale allant de la droite vers la gauche
    for i in range(3):
        for j in range(6):
            if liste_couleurs[j][(5-i)-j] == 1:
                cpt_r += 1
            else :
                cpt_r = 0
            if liste_couleurs[j][(5-i)-j] == 2:
                cpt_j += 1
            else :
                cpt_j = 0
            if cpt_r == 4:
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    ##compteur de gagnant en diagonale allant de la droite vers la gauche
    for i in range(3):
        for j in range(6-i):
            if liste_couleurs[j+i][6-j] == 1:
                cpt_r += 1
            else :
                cpt_r = 0
            if liste_couleurs[j+i][6-j] == 2:
                cpt_j += 1
            else :
                cpt_j = 0
            if cpt_r == 4:
                gagnant_rouge()
            if cpt_j == 4:
                gagnant_jaune()
        cpt_r = 0
        cpt_j = 0
    
def sauvegarde():
    global liste_couleurs, player, player2
    player2 = player
    fic = open("f_texte", "w")
    for i in range(len(liste_couleurs)):
        for j in range(len(liste_couleurs[0])):
            fic.write(str(liste_couleurs[i][j])+ "\n")
    fic.close

def affiche_sauvegarde():
    global obj, liste_couleurs, player, cond_start, player2
    player = player2
    liste_couleurs2 = []
    s = 0
    fic= open("f_texte", "r")
    for l in fic:
        a = int(l)
        liste_couleurs2.append(a)
        if len(liste_couleurs2) == 7:
            liste_couleurs[s] = copy.deepcopy(liste_couleurs2)
            liste_couleurs2 = []
            s += 1
    for i in range(6):
        for j in range(7):
            if liste_couleurs[i][j] == 1:
                col = "red"
            elif liste_couleurs[i][j] == 2:
                col = "yellow"
            else:
                col = "white"
            canvas.itemconfigure(obj[i][j], fill = col)
    cond_start = True
                
def start():
    """enregistrement des noms des joueurs"""
    global name_P1,name_P2, cond_start
    name_P1 = (texte1.get(1.0, END))
    name_P2 = (texte2.get(1.0, END))
    cond_start = True
    joueur()

def efface():
    """fonction effaçant le dernier pion déposé"""
    global variable_efface, obj
    canvas.itemconfigure(obj[variable_efface[-1][0]][variable_efface[-1][1]], fill = "white")
    liste_couleurs[variable_efface[-1][0]][variable_efface[-1][1]] = 0
    del variable_efface[-1]

def new_game():
    """fonction remettant tout à 0 afin de pouvoir rejouer"""
    global liste_couleurs, obj, player
    player = 0
    liste_couleurs = []
    obj = []
    create_oval()
    start()

def gagnant_rouge():
    """affichage du nom du gagant ayant les pions rouges"""
    global cond_start
    cond_start = False
    label_gagnant = tk.Label(text = "Le gagnant est" + " " + name_P1)
    label_gagnant.pack(side = "top")

def gagnant_jaune():
    """affichage du nom du gagnant ayant les pions jaunes"""
    global cond_start
    cond_start = False
    label_gagnant = tk.Label(text = "Le gagnant est" + " " + name_P2)
    label_gagnant.pack(side = "top")

texte1 = Text(racine, height = 1, width = 15)
texte2 = Text(racine, height = 1, width = 15)
label1 = tk.Label(text = "Nom joueur 1")
label2 = tk.Label(text = "Nom joueur 2")
bouton_texte = tk.Button(racine, text = "START", command = start)
bouton1 = tk.Button(text = "DELETE LAST", command = efface)
bouton2 = tk.Button(text = "RESTART", command = new_game )
bouton3 = tk.Button(text = "SAVE", command = sauvegarde)
bouton4 = tk.Button(text = "LOAD SAVING", command = affiche_sauvegarde)

bouton_texte.pack(side = "top", pady = 30)
label1.pack(side = "top")
texte1.pack(side = "top")
label2.pack(side = "top")
texte2.pack(side = "top")
bouton1.pack(side = "bottom")
bouton2.pack(side = "top")
bouton3.pack(side = "bottom")
bouton4.pack(side = "bottom")

canvas.bind("<Button-1>", clic)
racine.mainloop()