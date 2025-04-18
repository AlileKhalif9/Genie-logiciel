from tkinter import messagebox
from naim.interface.inscription import Affiche_Inscription

# Classe qui permet d'afficher des messages d'erreur sur la page d'inscription
class Ex_inscri:
    @staticmethod
    def check_surname():
        messagebox.showerror("Erreur"  "Veuillez entrer votre nom.")

    @staticmethod
    def check_name():
        messagebox.showerror("Erreur"  "Veuillez entrer votre prénom.")

    @staticmethod
    def check_email():
        messagebox.showerror("Erreur"  "Veuillez entrer votre email.")

    @staticmethod
    def check_adress():
        messagebox.showerror("Erreur"  "Veuillez entrer votre adresse postale.")
    
    @staticmethod
    def check_username():
        messagebox.showerror("Erreur"  "Veuillez entrer votre nom d'utilisateur.")

    @staticmethod
    def check_password():
        messagebox.showerror("Erreur"  "Veuillez entrer votre mot de passe.")

    # Fonction qui envoie un message si le mot de passe n'est pas confirmé
    @staticmethod
    def confirm_password():
        messagebox.showerror("Erreur"  "Veuillez confirmer votre mot de passe.")

