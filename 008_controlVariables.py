"""
Chapitre 23 : variables de contrôle
Lien : https://www.youtube.com/watch?v=lUDF9bureH4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=23

Les variables de contrôle sont la connection entre deux widgets, ou un wigdet et la console PyCharm...
Pour les variables de contrôle, on utilise la méthode get pour accéder aux données de la variable et à la méthode set
pour modifier les données de la variable

Pour déclarer une variable de contrôle, il faut choisir l'un des types primitifs suivants :
StringVar() : les str
IntVar() : les entiers
DoubleVar() : les réels
BooleanVar() : les booleéns

Dans l'exemple ci-dessous dès qu'on saisit quelque chose dans le champ de saisies, ce sera copié dans le label.

Éditeur : Laurent REYNAUD
Date : 17-10-2020
"""

import tkinter

app = tkinter.Tk()  # déclaration du Widget parent


def update_label(*args):
    """La variable var_label_set va être modifiée (set) en récupérant (get) les données de la variable var_entry"""
    var_label.set(var_entry.get())


"""Configuration de la taille de la fenêtre et du titre"""
app.geometry("400x300")
app.title('Copié / copié !')

"""Les instructions ci-après permettent de copier ce qui est dans le champ de saisi dans le label"""

"""Instructions pour le champ de saisie"""
var_entry = tkinter.StringVar()  # déclaration de la variable du champ de saisies en StringVar()
entry = tkinter.Entry(app, textvariable=var_entry)  # textvariable à la place de text -> déclaration variable ci-avant
entry.pack()  # affichage du champ de saisies

"""Instructions pour le label"""
var_label = tkinter.StringVar()  # déclaration de la variable du label en String(var)
label = tkinter.Label(app, textvariable=var_label)  # textvariable à la place de text -> déclaration variable ci-avant
label.pack()  # affichage du label

"""Connexion entre le champ de saisies et le label avec le mode 'w' (écriture)"""
var_entry.trace('w', update_label)

app.mainloop()  # arrêt du programme en fermant la fenêtre
