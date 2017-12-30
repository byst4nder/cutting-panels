#!/usr/bin/env python
# -*- coding: utf-8 -*-
from packages.backboard import Backboard
from packages.cut_backboard import Cut_backboard
from tkinter import *
fenetre = Tk()
backboard = ""


def recupere_mesure():
    if valueLargeur.get() != "" and valueLongueur != "":
        test = "largeur " + valueLongueur.get() + " cm " + " longueur " + valueLargeur.get() + " cm "
        listbox.insert(END, test)

def taille_panneau():
    backboard = Backboard(TaillePanneauvalueLongueur.get(), TaillePanneauvalueLargeur.get())
    affichageTailleDuPanneau.config(text=backboard.taille_panneau)

def tester():
    print("tester")
    for i in listbox.get(0,END):
        print(i)

def calcul_reste(calcul):
    longueur = (int(TaillePanneauvalueLongueur.get()) % int(longueur))

## taille panneau
taillePanneau = LabelFrame(fenetre, text="taille du panneau", padx=2, pady=2)
taillePanneau.pack(fill="both", expand="yes")
test = ""
affichageTailleDuPanneau = Label(taillePanneau, text=test)
affichageTailleDuPanneau.pack(side=TOP)
canvas = Canvas(taillePanneau, width=400, height=200, background='brown')

canvas.pack()

taillePanneauLongueurFrame = LabelFrame(taillePanneau, text="longueur", padx=2, pady=2)
taillePanneauLongueurFrame.pack()
taillePanneauLargeurFrame = LabelFrame(taillePanneau, text="largeur", padx=2, pady=2)
taillePanneauLargeurFrame.pack()

TaillePanneauvalueLongueur = StringVar()
TaillePanneauvalueLargeur = StringVar()
TaillePanneauentree = Entry(taillePanneauLongueurFrame, textvariable=TaillePanneauvalueLongueur, width=30)
TaillePanneauentree.pack()
TaillePanneauentree = Entry(taillePanneauLargeurFrame, textvariable=TaillePanneauvalueLargeur, width=30)
TaillePanneauentree.pack()

bouton = Button(taillePanneau, text="Valider", command=taille_panneau)

bouton.pack()

## Taille coupe

cutBackBoard = Cut_backboard(backboard)

tailleCoupe = LabelFrame(fenetre, text="taille des coupes", padx=2, pady=2)
tailleCoupe.pack(fill="both", expand="yes")
longueurFrame = LabelFrame(tailleCoupe, text="longueur", padx=2, pady=2)
longueurFrame.pack()
largeurFrame = LabelFrame(tailleCoupe, text="largeur", padx=2, pady=2)
largeurFrame.pack()

valueLongueur = StringVar()

valueLargeur = StringVar()

entree = Entry(longueurFrame, textvariable=valueLongueur, width=30)
entree.pack()
entree = Entry(largeurFrame, textvariable=valueLargeur, width=30)
entree.pack()
bouton = Button(tailleCoupe, text="Ajouter", command=recupere_mesure)
bouton.pack()
listbox = Listbox(tailleCoupe)
listbox.pack(fill="both", expand="yes")
boutonn = Button(tailleCoupe, text="Valider", command=recupere_mesure)
boutonn.pack()

coupePossible = LabelFrame(fenetre, text="coupe possible", padx=20, pady=20)
coupePossible.pack(fill="both", expand="yes")
listboxx = Listbox(coupePossible)
listboxx.pack(fill="both", expand="yes")



fenetre.mainloop()
