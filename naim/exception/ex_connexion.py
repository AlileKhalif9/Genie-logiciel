from tkinter import messagebox
from naim.interface.menu import Affiche_Acceuil

# Classe qui permet d'afficher un message d'erreur pour la connexion
class Ex_conn:
    @staticmethod
    def display():
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.\nVeuillez réessayer.")
