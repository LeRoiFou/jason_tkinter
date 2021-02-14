"""
Chapitre 23 : variables de contrôle
Lien : https://www.youtube.com/watch?v=lUDF9bureH4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=23

Dans le programme ci-après, à chaque fois que l'utilisateur appuye sur la case, la console PyCharm affiche le texte lié
à la case sélectionnée

On utilise comme type primitif IntVar(), car dans la méthode RadioButtuton(), on utilise pour l'argument 'value' un
entier

Éditeur : Laurent REYNAUD
Date : 17-10-2020
"""

import tkinter


def observateur(*args):
    """Si la variable var_radio a une valeur de 1 alors la variable varl_label aura pour valeur 'C'est un homme'...
    On accède à la variable var_radio (get) afin de modifier les valeurs de la variable var_label (set)"""
    if var_radio.get() == 1:
        var_label.set("C'est un homme")
    else:
        var_label.set("C'est une femme")


"""Déclaration du Widget parent"""
app = tkinter.Tk()

"""Configuration de la taille de la fenêtre et du titre de la fenêtre"""
app.geometry("400x300")
app.title('Mon titre')

"""Configuration des cases à sélectionner"""
var_radio = tkinter.IntVar()  # Déclaration de la variable var_radio de type IntVar()
radio_man = tkinter.Radiobutton(app, text='Homme', variable=var_radio, value=1)  # Arguments de la case 1
radio_man.pack()  # Affichage de la case 1
radio_woman = tkinter.Radiobutton(app, text='Femme', variable=var_radio, value=0)  # Arguments de la case 2
radio_woman.pack()  # Affichage de la case 1

"""Traceur de la variable var_radio en mode écriture (w)"""
var_radio.trace('w', observateur)

"""Configuration du label"""
var_label = tkinter.StringVar()  # Déclaration de la variable var_label de type StringVar()
label = tkinter.Label(app, textvariable=var_label)  # Arguments du label
label.pack()  # Affichage du label

app.mainloop()  # Arrêt du programme à la fermeture de la fenêtre
