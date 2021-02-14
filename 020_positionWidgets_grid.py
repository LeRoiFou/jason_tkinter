"""
Chapitre 24 : positionnement des widgets
Lien : https://www.youtube.com/watch?v=YGeRTVaBPoc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=24

Il existe 3 méthodes de positionnement de widgets :
    -> la méthode pack()
    -> la méthode grid() : chaque valeur est une case de la grille de la fenêtre -> dans l'exemple ci-dessous la
    fenêtre est une grille de 400 pixels x 300 pixels et la méthode columnspan et rowspan augmente la largeur / la
    longueur du widget
    -> la méthode place()
Note : utiliser une seule de ces méthodes pour un programme

Éditeur : Laurent REYNAUD
Date : 18-10-2020
"""

import tkinter

app = tkinter.Tk()

"""Dimension de la fenêtre et insertion d'un titre"""
app.geometry('400x300')  # Dimension de la fenêtre
app.title('Mon titre')  # Insertion d'un titre

"""Widgets"""
label = tkinter.Label(app, text='UN LABEL')  # Insertion d'un label
ent = tkinter.Entry(app)  # Insertion d'un champ de saisies
btn = tkinter.Button(app, text='UN BOUTON')  # Insertion d'un bouton

label.grid(row=0, column=0, columnspan=2)  # Affichage du label: 0 pixel en ligne et 0 pixel en colonne largeur 2 pixels
ent.grid(row=0, column=4)  # Affichage du champ de saisies à 0 pixel en ligne et 1 pixel en colonne
btn.grid(row=0, column=5, rowspan=5)  # Affichage du bouton: 0 pixel en ligne et 2 pixels en colonne hauteur 5 pixels

app.mainloop()  # Arrêt du programme en fermant la fenêtre
