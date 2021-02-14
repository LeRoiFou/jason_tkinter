"""
Chapitre 22 : widgets avancés
lien : https://www.youtube.com/watch?v=hfWE9dT6fgU&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=22

Recours à un cadre qui contient d'autres widgets

Éditeur : Laurent REYNAUD
Date : 18-10-2020
"""

import tkinter

app = tkinter.Tk()

"""Dimension de la fenêtre et insertion d'un titre"""
app.geometry('400x300')  # Dimension de la fenêtre
app.title('Mon titre')  # Insertion d'un titre

"""Widgets de cadre avec un titre cette fois-ci permettant de contenir d'autres widgets"""
mainframe = tkinter.LabelFrame(app, text='Titre', width=300, height=200)  # Insertion d'un cadre avec son titre
mainframe.pack()  # Affichage du cadre avec le titre saisi

app.mainloop()  # Arrêt du programme en fermant la fenêtre
