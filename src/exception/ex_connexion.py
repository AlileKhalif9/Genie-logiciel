from tkinter import messagebox
from src.interface.i18n import tr, get_langue


# Classe qui permet d'afficher un message d'erreur pour la connexion
class Ex_conn:
    @staticmethod
    def display():
        if get_langue() == "FR":
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.\nVeuillez réessayer.")
        else :
            messagebox.showerror("Login error", "Incorrect username or password.\nPlease try again.")

    @staticmethod
    def success(username):
        if get_langue() == "FR":
            messagebox.showinfo("Succès", f"Bonjour {username}")
        else :
            messagebox.showinfo("Success", f"Welcome {username}")

    @staticmethod
    def msg_english():
        messagebox.showinfo("Language", "You have switched in english.")

    @staticmethod
    def msg_french():
        messagebox.showinfo("Langue", "Vous êtes passé en français.")
