"""
Même exemple que le chapitre 23, mais cette fois-ci au lieu de recourir aux variables de contrôle, on utilise la
fonction lambda qui ne peut être utilisée dans une POO et l'action pour copier exige d'avoir

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Mon titre')


def copier():
    print(entry1.get())
    entry1.delete(0, 'end')


entry1 = Entry(root, justify='center')
entry1.pack()
button = Button(root, text='Copier', command=lambda: copier())
button.pack()

root.mainloop()
