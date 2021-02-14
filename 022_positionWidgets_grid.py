"""
Chapitre 24 : positionnement des widgets
Lien : https://www.youtube.com/watch?v=YGeRTVaBPoc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=24

Il existe 3 méthodes de positionnement de widgets :
    -> la méthode pack()
    -> la méthode grid() : chaque valeur est une case de la grille de la fenêtre -> dans l'exemple ci-dessous on utilise
    l'option sticky (avec n=nord, s=sud, est=e et ouest=w)
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

label.grid(sticky='n')  # Affichage du label
ent.grid(sticky='e')  # Affichage du champ de saisies
btn.grid(sticky='sw')  # Affichage du bouton

app.mainloop()  # Arrêt du programme en fermant la fenêtre
