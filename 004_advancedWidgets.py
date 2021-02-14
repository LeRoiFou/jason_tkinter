"""
Chapitre 22 : widgets avancés
lien : https://www.youtube.com/watch?v=hfWE9dT6fgU&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=22

Autres widgets : case à cocher, case à sélectionner, barre de déroulement...

Éditeur : Laurent REYNAUD
Date : 17-10-2020
"""

import tkinter

app = tkinter.Tk()

"""Widget permettant de cocher une case"""
check_widget = tkinter.Checkbutton(app, text='Oui', width=10, height=5)  # Insertion case à cocher + positionnement
check_widget.pack()  # Affichage de la case à cocher

"""Widget permettant de sélectionner une case """
radio_widget1 = tkinter.Radiobutton(app, text='Homme', value=1)  # Insertion de la case non sélectionnée
radio_widget1.pack()  # Affichage de la 1ère case non sélectionnée
radio_widget2 = tkinter.Radiobutton(app, text='Femme', value=0)  # Insertion de la case sélectionnée
radio_widget2.pack()  # Affichage de la 2ème case sélectionnée

"""Widget pour une barre de déroulement"""
scale_widget = tkinter.Scale(app, from_=10, to=50, tickinterval=2)  # Insertion d'une barre de déroulement graduée
scale_widget.pack()  # Affichage de la barre de déroulement

"""Widget pour un champ de saisies déroulant"""
spin_widget = tkinter.Spinbox(app, from_=1, to=10)  # Insertion d'un champ de saisies déroulant gradué
spin_widget.pack()  # Affichage du champ de saisies déroulant

"""Widget pour un champ de saisies à compléter"""
lb_widget = tkinter.Listbox(app)  # Insertion d'un champ de saisie vide non saisissable
lb_widget.insert(1, 'Excel')  # Insertion à la 1ère ligne du mot Excel dans le champ de saisie
lb_widget.insert(2, 'Word')  # Insertion à la 2ème ligne du mot Word dans le champ de saisie
lb_widget.insert(3, 'PowerPoint')  # Insertion à la 3ème ligne du mot PowerPoint dans le champ de saisie
lb_widget.insert(4, 'Access')  # Insertion à la 4ème ligne du mot Access dans le champ de saisie
lb_widget.pack()  # Affichage du champ de saisies complété par les instructions ci-avant

app.mainloop()
