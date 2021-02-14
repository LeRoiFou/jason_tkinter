"""
Même exemple que le chapitre 23, mais cette fois-ci au lieu de recourir aux variables de contrôle, on utilise la
fonction lambda : dans ce cas on ne peut pas recourir à la POO et on a besoin d'un bouton engager l'action à copier le
texte saisi dans le champ concerné

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Copié / Collé !')


def copier():
    entry2.delete(0, 'end')
    entry2.insert(0, entry1.get())


entry1 = Entry(root, justify='center')
entry1.pack()
button = Button(root, text='Copier', command=lambda: copier())
button.pack()
entry2 = Entry(root, justify='center', bd=0, bg='#EFEFEF')
entry2.pack()

root.mainloop()