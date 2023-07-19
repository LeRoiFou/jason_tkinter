"""
Lien : https://www.youtube.com/watch?v=W1gKlpXE2hs

Vous allez coder un petit éditeur dans une interface graphique selon ces critères :
    -> prendre en charge des fichiers .txt
    -> fournir des commandes standard (nouveau, ouvrir, enregistrer, quitter)
    
Indications :
    -> travailler en utf-8
    -> l'éditeur utilisera un champ de saisie avec le widget -> tkt.Text
    -> Ouverture / enregistrement de fichiers à utiliser -> tkt.filedialog

... mes débuts en informatique 😁

Date : 19-07-23
"""

import tkinter as tk
from tkinter import filedialog

class Gui:
    
    def __init__(self, root):
        
        self.root = root
        self.root.title('Bloc-notes')
        self.root.geometry('1000x650')
        
        self.widgets()
    
    # Configuration des widgets    
    def widgets(self):
        
        # Barre de menu
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Nouveau', command=self.new_file)
        file_menu.add_command(label='Ouvrir', command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Enregistrer', command=self.save_file)
        file_menu.add_command(label='Quitter', command=self.root.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        root.config(menu=menu_bar)
        
        # Zone de texte
        self.my_text = tk.Text(self.root)
        self.my_text.pack(fill=tk.BOTH, expand=True)

    # Menu Fichier -> Nouveau
    def new_file(self):
        
        # Réinitialisation du texte
        self.my_text.delete('1.0', tk.END)
    
    # Menu Fichier -> Ouvrir
    def open_file(self):
        
        # Ouverture de la boîte de dialogue
        file_path = filedialog.askopenfilename(
            filetypes=[("Fichier texte", ".txt")])
        
        # Si un fichier a été récupéré...
        if file_path:
            # Toujours la fonction "with" pour charger un fichier
            with open(file_path, "r", encoding='utf-8') as f:
                # Réinitialisation du texte
                self.my_text.delete('1.0', tk.END)
                # Insertion du texte récupéré dans la zone de texte
                self.my_text.insert(tk.END, f.read())
                
    
    # Menu Fichier -> Enregistrer
    def save_file(self):
        
        # Ouverture de la boîte de dialogue
        file_path = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[("Fichier texte", ".txt")])
        
        # Si un fichier a été récupéré...
        if file_path:
            # Toujours la fonction "with" pour sauvegarder un fichier
            with open(file_path, "w", encoding='utf-8') as f:
                # Récupération du texte saisi dans la zone de texte
                f.write(self.my_text.get('1.0', tk.END))

    
if __name__ == '__main__':
    
    root = tk.Tk()
    gui = Gui(root)
    root.mainloop()
    