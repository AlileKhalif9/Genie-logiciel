from tkinter import messagebox
from naim.interface.inscription import Affiche_Inscription

# Classe qui permet d'afficher des messages d'erreur sur la page d'inscription
class Ex_inscri:
    @staticmethod
    def check_surname():
    # Fonction pour vérifier si le nom de famille est entré
        messagebox.showerror("Erreur : veuillez entrer votre nom")

    @staticmethod
    def check_name():
        messagebox.showerror("Erreur : veuillez entrer votre prénom")
    @staticmethod
    def check_email():
        messagebox.showerror("Erreur : veuillez entrer votre adresse mail")

    @staticmethod
    def check_adress():
        messagebox.showerror("Erreur : veuillez entrer votre adresse postale")
    
    @staticmethod
    def check_username():
        messagebox.showerror("Erreur : veuillez entrer votre nom d'utilisateur")

    @staticmethod
    def check_password():
        messagebox.showerror("Erreur : veuillez confirmer le meme mot de passe")

