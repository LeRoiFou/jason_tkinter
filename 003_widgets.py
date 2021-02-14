"""
Chapitre 21 : premiers widgets
lien : https://www.youtube.com/watch?v=JdSqSKrPhSw&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=21

Les widgets sont tous les éléments qui sont dans une fenêtre : texte, bouton, champ de saisies, liste, menus, images...
Pour afficher un widget, il faut appliquer les étapes suivantes :

Étape 1
On importe le module tkinter : import tkinter

Étape 2
Déclaration d'une variable en tant que Widget parent : WidgetParent = tkinter.Tk()

Étape 3
Appel du Widget : NomVariable = tkinter.Widget(WidgetParent, argument supplémentaire)
Affichage du Widget : NomVariable.pack()

Étape 4
Arrêt du programme en fermant la fenêtre composant les Widgets : app.mainloop()

Éditeur : Laurent REYNAUD
Date : 16-10-2020
"""

import tkinter

app = tkinter.Tk()

"""Widget label"""
label_welcome = tkinter.Label(app, text='Salut !')  # Insertion d'un label
label_welcome.config(text='Bienvenue\ndans cette nouvelle fenêtre !')  # Modification du label
label_welcome.pack()  # Affichage du label

"""Widget message"""
message_welcome = tkinter.Message(app, text='Ceci est un test')  # Insertion d'un message
message_welcome.pack()  # Affichage du message

"""Widget champ de saisies"""
entry_name = tkinter.Entry(app, width=45)  # Insertion d'un champ de saisies avec une largeur
entry_name_bis = tkinter.Entry(app, show="*")  # Insertion d'un autre champ de saisies avec des caractères masqués (mdp)
entry_name.pack()  # Affichage du champ de saisies
entry_name_bis.pack()  # Affichage du deuxième champ de saisies

"""Widget bouton"""
button = tkinter.Button(app, text='Appuie !', width=30, height=5)  # Insertion d'un bouton avec une largeur et hauteur


def hello():
    """Cette fonction va s'implémeter dans l'instruction ci-après : à chaque fois qu'on appuyera sur le bouton affichant
    'Affichage console PyCharm' dans la console de PyCharm s'affichera 'Bonjour !'"""
    print('Bonjour !')


button_bis = tkinter.Button(app, text='Affichage console PyCharm', command=hello)
button.pack()  # Affichage du bouton
button_bis.pack()  # Affichage du deuxième bouton

app.mainloop()  # Arrêt du programme lors de la fermeture de la fenêtre
