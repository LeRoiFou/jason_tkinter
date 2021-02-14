"""
Chapitre 22 : widgets avancés
lien : https://www.youtube.com/watch?v=hfWE9dT6fgU&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=22

Les fenêtres modales

Fenêtres modales en recourant au module messagebox intégré dans tkinter
-> Fenêtre affichant un message d'erreur :                  messagebox.showerror(Titre, Texte)
-> Fenêtre affichant un message d'avertissement :           messagebox.showwarning(Titre, Texte)
-> Fenêtre affichant un message d'information :             messagebox.showinfo(Titre, Texte)
-> Fenêtre affichant une commande OUI/NON:                  messagebox.askquestion(Titre, Texte)
-> Fenêtre affichant une commande OK/ANNULER :              messagebox.askokcancel(Titre, Texte)
-> Fenêtre affichant une commande RECOMMENCER/ANNULER :     messagebox.retrycancel(Titre, Texte)

Éditeur : Laurent REYNAUD
Date : 17-10-2020
"""

import tkinter
from tkinter import messagebox  # importution du module messagebox intégré dans tkinter


def show_modal_window_error():
    messagebox.showerror('ERREUR', 'Un problème est survenu !')


def show_modal_window_warning():
    messagebox.showwarning('AVERTISSEMENT', 'Un problème est survenu !')


def show_modal_window_info():
    messagebox.showinfo('INFORMATION', 'Un problème est survenu !')


def show_modal_window_ouinon():
    messagebox.askquestion('QUESTION', 'Tout va bien ?')


def show_modal_window_okannuler():
    messagebox.askokcancel('Validation', 'Ce message va être validé')


def show_modal_window_recomannuler():
    messagebox.askretrycancel('Option', 'Voulez-vous recommencer ?')


app = tkinter.Tk()

"""Message d'erreur : en déclenchant le bouton, une nouvelle fenêtre s'affiche avec un message d'erreur"""
btn_error = tkinter.Button(app, text='Déclencher une erreur', command=show_modal_window_error)
btn_error.pack()

"""Message d'avertissement : en déclenchant le bouton, une nouvelle fenêtre s'affiche avec un avertissement"""
btn_warning = tkinter.Button(app, text='Déclencher un avertissement', command=show_modal_window_warning)
btn_warning.pack()

"""Message d'information : en déclenchant le bouton, une nouvelle fenêtre s'affiche avec une information"""
btn_info = tkinter.Button(app, text='Déclencher une information', command=show_modal_window_info)
btn_info.pack()

"""Message de commande : en déclanchant le bouton, une nouvelle fenêtre s'affiche avec les boutons OUI et NON"""
btn_question = tkinter.Button(app, text='Poser une question', command=show_modal_window_ouinon)
btn_question.pack()

"""Message de commande : en déclanchant le bouton, une nouvelle fenêtre s'affiche avec les boutons OK et ANNULER"""
btn_ok = tkinter.Button(app, text='Valider', command=show_modal_window_okannuler)
btn_ok.pack()

"""Message de commande : en déclanchant le bouton, ... s'affiche avec les boutons RECOMMENCER et ANNULER"""
btn_cancel = tkinter.Button(app, text='Répéter', command=show_modal_window_recomannuler)
btn_cancel.pack()

app.mainloop()
