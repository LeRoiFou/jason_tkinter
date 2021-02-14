"""
Chapitre 24 : positionnement des widgets
Lien : https://www.youtube.com/watch?v=YGeRTVaBPoc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=24

Il existe 3 méthodes de positionnement de widgets :
    -> la méthode pack() décrite ci-dessous avec l'instruction fill='x' (axe abscisses) et fill='y' (axe ordonnées)
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

label.pack()  # Affichage du label en haut (soit rien mentionné entre parenthèses)
ent.pack(side='right', fill='x')  # Affichage du champ de saisies à droite sur tout l'axe x (axe des abscisses)
btn.pack(side='left', fill='y')  # Affichage du bouton à gauche sur tout l'axe y (axe des ordonnées)

app.mainloop()  # Arrêt du programme en fermant la fenêtre
