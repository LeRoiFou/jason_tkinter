"""
Chapitre 24 : positionnement des widgets
Lien : https://www.youtube.com/watch?v=YGeRTVaBPoc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=24

Il existe 3 méthodes de positionnement de widgets :
    -> la méthode pack() décrite ci-dessous
    -> la méthode grid()
    -> la méthode place()

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

label.pack(side='top')  # Affichage du label en haut (par défaut le label est affiché en haut)
ent.pack(side='right')  # Affichage du champ de saisies à droite
btn.pack(side='bottom')  # Affichage du bouton en bas

app.mainloop()  # Arrêt du programme en fermant la fenêtre
