"""
Chapitre 23 : variables de contrôle

Dans le programme ci-après, à chaque fois qu'on case la case, un message s'affiche dans la console PyCharm

Éditeur : Laurent REYNAUD
Date : 17-10-2020
"""

import tkinter


def observateur(*args):
    if var_case.get() == 'Vrai':
        pass
    else:
        print("C'est vrai !")


app = tkinter.Tk()

app.geometry('300x200')
app.title('Mon titre')

var_case = tkinter.IntVar()
case = tkinter.Checkbutton(app, text='Vrai', variable=var_case)
case.pack()

var_case.trace('w', observateur)

app.mainloop()
