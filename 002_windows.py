"""
Chapitre 20 : introduction tkinter
lien : https://www.youtube.com/watch?v=H0BFsl2_St4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=20

Pour centrer une fenêtre, la formule est la suivante :
-> pour l'abscisse : (largeur écran // 2) - (largeur fenêtre // 2)
-> pour l'ordonnée : (hauteur écran // 2) - (hauteur fenêtre // 2)
Conseil : créer un module spécifique à ce programme...

Éditeur : Laurent REYNAUD
Date : 16-10-2020
"""

import tkinter

"""Centrer une fenêtre à l'écran"""
mainapp = tkinter.Tk()

largeur_ecran = int(mainapp.winfo_screenwidth())  # largeur de l'écran
hauteur_ecran = int(mainapp.winfo_screenheight())  # hauteur de l'écran
largeur_fenetre = 800  # largeur de la fenêtre
hauteur_fenetre = 600  # hauteur de la fenêtre

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)  # voir la formule ci-dessus dans DocStrings
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)  # voir la formule ci-dessus dans DocStrings

centrage = f"{largeur_fenetre}x{hauteur_fenetre}+{posX}+{posY}"

mainapp.geometry(centrage)

mainapp.mainloop()
