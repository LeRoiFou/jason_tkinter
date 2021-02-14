"""
Chapitre 25 : création des menus
lien : https://www.youtube.com/watch?v=jGnGnro2vsk&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=25

Un menu est composé d'un titre et des données contenues dans le menu

Explications sur les instructions suivantes :
    -> tearoff=0 : permet de supprimer le séparateur présent entre le titre du menu et les sous-titres dans le menu
    déroulant
    -> command=WidgetParent.quit : permet de quitter le programme

Éditeur : Laurent REYNAUD
Date : 20-10-2020
"""

import tkinter


def hello():
    """Lorsqu'on clique sur 'option1' l'instruction suivante s'affiche dans la console"""
    print('Coucou !')


def show_about():
    """Création d'une sous-fenêtre"""
    about_window = tkinter.Toplevel(app)  # Insertion d'une fenêtre
    about_window.title('À propos')  # Titre de la sous-fenêtre
    lb = tkinter.Label(about_window, text='Bonjour !', width=20, height=10)  # Insertion d'un label dans la sous-fenêtre
    lb.pack()  # Affichage du label dans la sous-fenêtre


app = tkinter.Tk()

# Dimension de la fenêtre et ajout d'un titre
app.geometry('640x480')
app.title('Mon titre')

# Widgets
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label='Option1', command=hello)  # appel fonction : affichage dans la console
first_menu.add_command(label='Option2')
first_menu.add_command(label='Option3')
first_menu.add_separator()  # Séparateur entre les données ci-dessus et les données ci-après
first_menu.add_command(label='Quitter', command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label='Commande1')
second_menu.add_command(label='Commande2')
second_menu.add_command(label='À propos', command=show_about)  # appel fonction : création d'une sous-fenêtre

mainmenu.add_cascade(label='Premier', menu=first_menu)
mainmenu.add_cascade(label='Second', menu=second_menu)

# Boucle principale
app.config(menu=mainmenu)
app.mainloop()
