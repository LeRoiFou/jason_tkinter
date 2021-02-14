"""
Chapitre 24 : positionnement des widgets
Lien : https://www.youtube.com/watch?v=YGeRTVaBPoc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=24

Il existe 3 méthodes de positionnement de widgets :
    -> la méthode pack()
    -> la méthode grid()
    -> la méthode place() décrite ci-dessous
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

label.place(x=0, y=20)  # Affichage du label avec x = 0 pixel et y = 20 pixels
ent.place(x=200, y=100)  # Affichage du champ de saisies avec x = 200 pixels et y = 100 pixels
btn.place(x=100, y=50)  # Affichage du bouton avec x = 100 pixels et y = 50 pixels

app.mainloop()  # Arrêt du programme en fermant la fenêtre
