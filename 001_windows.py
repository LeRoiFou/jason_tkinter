"""
Chapitre 20 : introduction tkinter
lien : https://www.youtube.com/watch?v=H0BFsl2_St4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=20

Création d'une fenêtre en mentionnant un titre et en redimensionnant la fenêtre

Éditeur : Laurent REYNAUD
Date : 16-10-2020
"""

import tkinter

"""Création d'une fenêtre (widget)"""
mainapp = tkinter.Tk()
mainapp.title("Mon titre")  # titre de la fenêtre
mainapp.minsize(500, 200)  # taille minimale de la fenêtre : largeur x hauteur
mainapp.geometry('800x600+200+100')  # dimension de la fenêtre à l'affichage : largeur x hauteur x abscisse x ordonnée
mainapp.maxsize(900, 700)  # taille maximale de la fenêtre : largeur x hauteur
mainapp.resizable(width=False, height=True)  # width (largeur) : non modifiable / height (hauteur) : modifiable
mainapp.mainloop()  # boucle infinie : le programme s'arrête une fois qu'on a fermé la fenêtre
